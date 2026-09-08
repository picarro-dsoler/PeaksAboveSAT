import pandas as pd
import numpy as np

class CustomBinnedRER:
    def __init__(self,A,B,bin_floors):
        self.A = A
        self.B = B
        self.bin_floors = bin_floors
        #Set the bin labels       
        self.A_inv = list(reversed(self.A))

        #Set the posterior probability matrix
        self.posterior_PAB = pd.DataFrame(columns=self.A, index=self.B)

        #Set the actual leak distribution
        self.actual_leak_distribution = pd.DataFrame(columns =['Probability', 'AverageFlow'], index = self.A)
        self.posterior_leak_distribution = pd.DataFrame(columns =['Probability', 'AverageFlow'], index = self.B)

        #Set the experiments variabl
        self.experiments = None

    def get_system_PBA(self):
        return self.system_PBA

    def set_system_PBA(self, system_PBA):
        self.system_PBA = system_PBA
        

    #Set the experimental data and calculate the actual leak distribution
    def set_experiments(self, experiments):
        self.experiments = experiments
        self.set_actual_leak_distribution()


    def set_actual_leak_distribution(self, actual_leak_distribution = None):
        if actual_leak_distribution is not None:
            self.actual_leak_distribution = actual_leak_distribution
        else:
            if self.experiments is None:
                raise ValueError("Neither experimental data nor actual leak distribution is set")
            else:
                #Aggregate the data into bins
                df = pd.DataFrame(self.experiments, columns=['A'])
                df["Bin"] = pd.cut(df["A"], bins=self.bin_floors, labels=self.A)
                out = df.groupby('Bin').agg({'A': ['count', 'mean', 'std']})
                out['Prob'] = out['A']['count']/out['A']['count'].sum()
                self.actual_leak_distribution['Probability'] = out['Prob']
                self.actual_leak_distribution['AverageFlow'] = out['A']['mean']
        return self.actual_leak_distribution

    def get_actual_leak_distribution(self):
        return self.actual_leak_distribution

    def get_posterior_probability_matrix(self):
        for b in self.B:
            for a in self.A:
                self.posterior_PAB.loc[b][a] = (self.system_PBA.loc[a][b]*self.actual_leak_distribution.loc[a]['Probability'])/self.system_PBA[b].dot(self.actual_leak_distribution['Probability'])
        return self.posterior_PAB

    def get_posterior_leak_distribution(self):
        for b in self.B:
            self.posterior_leak_distribution.loc[b]['Probability'] = self.system_PBA[b].dot(self.actual_leak_distribution['Probability'])
            self.posterior_leak_distribution.loc[b]['AverageFlow'] = self.posterior_PAB.loc[b].dot(self.actual_leak_distribution['AverageFlow'])
        return self.posterior_leak_distribution


class BinnedDistribution():
    def __init__(self,experiments = None,bin_labels = ['A-2','A-1','A0','A1'],bin_floors = [1E-5,0.1,1,10,1E5]):
        self.experiments = experiments
        self.bin_labels = bin_labels
        self.bin_floors = bin_floors
        self.binned_distribution = pd.DataFrame()

    def set_binned_distribution(self):
        if self.experiments is None:
            raise ValueError("Experiments are not set")
        else:
            #Aggregate the data into bins
            df = pd.DataFrame(self.experiments, columns=['A'])
            df["Bin"] = pd.cut(df["A"], bins=self.bin_floors, labels=self.bin_labels)
            out = df.groupby('Bin').agg({'A': ['count', 'mean', 'std']})
            out['Prob'] = out['A']['count']/out['A']['count'].sum()
            self.binned_distribution['Probability'] = out['Prob']
            self.binned_distribution['AverageFlow'] = out['A']['mean']
            self.binned_distribution['Count'] = out['A']['count']
        return self.binned_distribution

class BinnedRER(CustomBinnedRER):
    def __init__(self):
        B = ['B-2','B-1','B0','B1']
        A = ['A-2','A-1','A0','A1']
        bin_floors = [1E-5,0.1,1,10,1E5]
        #Set the system PBA matrix
        self.system_PBA =  pd.DataFrame(np.array([[0,0,0.16,0.84],[0,0.17,0.66,0.17],[0.17,0.66,0.17,0],[0.84,0.16,0,0]]),columns = B)
        self.system_PBA.index = A[::-1]
        super().__init__(A,B,bin_floors)

class System_Matrix:
    def __init__(self,prior_mu = -1.36, prior_sigma = 1.77, trials = 1000000, error_mu = 0, error_sigma = 0.95, bin_floors = [1e-5, 0.1,1,10,1e5], b_labels = ["B-2", "B-1","B0","B1"], a_labels = ["A-2", "A-1","A0","A1"]):
        self.prior_mu = prior_mu
        self.prior_sigma = prior_sigma
        self.trials = trials
        self.error_mu = error_mu
        self.error_sigma = error_sigma
        self.bin_floors = bin_floors
        self.b_labels = b_labels
        self.a_labels = a_labels

        self._system_performance_counts()

    def _system_performance_counts(self):
            # Perform Monte Carlo to get the relationship between A and B given an error
        # of np.random.lognormal(0.0,0.95)
        self.experiments = np.random.lognormal(self.prior_mu, self.prior_sigma, self.trials)
        self.random_errors = np.random.lognormal(mean=self.error_mu, sigma=self.error_sigma, size=self.trials)
        self.measurements = self.experiments * self.random_errors

        df = pd.DataFrame()
        df["ActualLeak"] = self.experiments
        df["MeasuredLeak"] = self.measurements
        df["B"] = pd.cut(df["MeasuredLeak"], bins=self.bin_floors, labels=self.b_labels)
        df["A"] = pd.cut(df["ActualLeak"], bins=self.bin_floors, labels=self.a_labels)
        # System performance for A given B and the inverse (Tables 1 and 3)
        # Convert to probability of B given A by normalizing rows to sum to 1
        self.system_performance_counts = pd.crosstab(df["A"], df["B"])
        return self.system_performance_counts

    def get_PBA_matrix(self):
        return self.system_performance_counts.div(self.system_performance_counts.sum(axis=1), axis=0)

    def get_PAB_matrix(self):
        return self.system_performance_counts.div(self.system_performance_counts.sum(axis=0), axis=1)
    
    def get_counts_matrix(self):
        return self.system_performance_counts

class SymmetricSystem_Matrix(System_Matrix):
    def __init__(self,prior_mu = -1.36, prior_sigma = 1.77, trials = 10000000, error_mu = 0, error_sigma = 0.95, bin_floors = [1e-5, 0.1,1,10,1e5], b_labels = ["B-2", "B-1","B0","B1"], a_labels = ["A-2", "A-1","A0","A1"]):
        super().__init__(prior_mu, prior_sigma, trials, error_mu, error_sigma, bin_floors, b_labels, a_labels)


    def _system_performance_counts(self):
        LOG_START = -2
        LOG_STOP = 3
        np.random.seed(42)
        #Actual leak rate distribution
        A = np.logspace(LOG_START, LOG_STOP, num=100_000)
        #Measured leak rate distribution
        B = A * np.random.lognormal(self.error_mu, self.error_sigma, size=len(A))

        df = pd.DataFrame({'A_val': A, 'B_val': B})
        df['A'] = pd.cut(df['A_val'], bins=self.bin_floors, labels=self.a_labels)
        df['B'] = pd.cut(df['B_val'], bins=self.bin_floors, labels=self.b_labels)
        df.dropna(subset=['A', 'B'], inplace=True)
        self.system_performance_counts = pd.crosstab(df['A'], df['B'])
        return self.system_performance_counts
