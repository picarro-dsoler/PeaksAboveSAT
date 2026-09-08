import pandas as pd

SCFH_TO_G_PER_HOUR = 19.1
SCFH_TO_SLPM_FACTOR = 0.471947

@pd.api.extensions.register_dataframe_accessor("emissionrates")
class EmissionRateAccessor:
    def __init__(self, pandas_obj):
        self._obj = pandas_obj

    def convert(self, SCFH_TO_SLPM_FACTOR=SCFH_TO_SLPM_FACTOR, SCFH_TO_G_PER_HOUR=SCFH_TO_G_PER_HOUR):
        """
        Convert emission rates to SLPM and grams per hour
        Modifies the DataFrame in place.
        """

        # Track new columns added
        new_cols = []

        # --- EmissionRate conversions ---
        if "EmissionRate" in self._obj.columns:
            self._obj["EmissionRateGramsPerHour"] = self._obj["EmissionRate"] * SCFH_TO_G_PER_HOUR
            self._obj["EmissionRateLPM"] = self._obj["EmissionRate"] * SCFH_TO_SLPM_FACTOR
            new_cols += ["EmissionRateGramsPerHour", "EmissionRateLPM"]

        # --- RepresentativeEmissionRate conversions ---
        if "RepresentativeEmissionRate" in self._obj.columns:
            self._obj["RepresentativeEmissionRateGramsPerHour"] = (
                self._obj["RepresentativeEmissionRate"] * SCFH_TO_G_PER_HOUR
            )
            self._obj["RepresentativeEmissionRateLPM"] = (
                self._obj["RepresentativeEmissionRate"] * SCFH_TO_SLPM_FACTOR
            )
            new_cols += ["RepresentativeEmissionRateGramsPerHour", "RepresentativeEmissionRateLPM"]

        # If columns were added, reorder them
        if len(new_cols) > 0:
            # --- Reordering ---
            cols = self._obj.columns.tolist()

            def insert_after(base_col, new_cols_to_insert, cols):
                if base_col in cols:
                    base_idx = cols.index(base_col)
                    # Remove new_cols if already present somewhere
                    for nc in new_cols_to_insert:
                        if nc in cols:
                            cols.remove(nc)
                    # Insert right after base_col
                    for offset, nc in enumerate(new_cols_to_insert, 1):
                        cols.insert(base_idx + offset, nc)
                return cols

            # Order for EmissionRate
            cols = insert_after("EmissionRate",
                                ["EmissionRateGramsPerHour", "EmissionRateLPM"],
                                cols)

            # Order for RepresentativeEmissionRate
            cols = insert_after("RepresentativeEmissionRate",
                                ["RepresentativeEmissionRateGramsPerHour", "RepresentativeEmissionRateLPM"],
                                cols)
            
            # Reorder columns in place by updating the DataFrame's column order
            temp_data = {}
            for col in cols:
                temp_data[col] = self._obj[col]
            
            # Clear existing columns and add them back in the correct order
            for col in list(self._obj.columns):
                del self._obj[col]
            
            for col in cols:
                self._obj[col] = temp_data[col]

        return self._obj