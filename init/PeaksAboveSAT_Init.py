import os
import sys
from pathlib import Path

import pandas as pd


def _find_project_root() -> Path:
    init_dir = Path(__file__).resolve().parent
    root = init_dir.parent
    if (root / "locallib").is_dir() and (root / "lib" / "tables").is_dir():
        return root
    raise FileNotFoundError(
        f"Could not find PeakAboveSAT root (locallib + lib/tables). cwd={Path.cwd()!r}"
    )


PROJECT_ROOT = _find_project_root()
INIT_DIR = Path(__file__).resolve().parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))
os.chdir(PROJECT_ROOT)

from locallib.picarrodb import *
from locallib.query import *
from locallib.box import *
from locallib.pandas import *

from lib.tables.IngesterTables import *
from lib.config import *
from lib.KPIHubConnection import *


def init_customers() -> pd.DataFrame:
    customer_list = pd.read_csv(INIT_DIR / "PeaksAboveSAT_Customer.csv")
    customer_ids = []

    for _, customer in customer_list.iterrows():
        result = Query(
            query=(
                "SELECT C.Id as CustomerId, C.Name FROM Customer C "
                f"WHERE LOWER(C.Name) = LOWER('{customer['Name']}')"
            )
        ).execute(CONN_DICT[customer["DBLocation"]])

        if not result.empty:
            customer_ids.append(result.iloc[0]["CustomerId"])
        else:
            customer_ids.append(None)

    customer_list["CustomerId"] = customer_ids
    customer_list["LastUpdated"] = pd.Timestamp.now()
    PeakAboveSATCustomer.update_table(
        arguments={"db_path": DB_PATH, "DataFrame": customer_list, "PrimaryKey": "CustomerId"}
    )
    return PeakAboveSATCustomer.query_table(arguments={"db_path": DB_PATH})


def init_mailing_list(customer_list: pd.DataFrame) -> pd.DataFrame:
    mailing_list = pd.read_csv(INIT_DIR / "PeaksAboveSAT_MailList.csv")
    mailing_list = pd.merge(
        mailing_list,
        customer_list[["Name", "CustomerId"]],
        left_on="Customer",
        right_on="Name",
        how="left",
    )
    mailing_list.drop(columns=["Name", "Customer"], inplace=True)
    mailing_list["LastUpdated"] = pd.Timestamp.now()
    PeakAboveSATRecipients.update_table(
        arguments={
            "db_path": DB_PATH,
            "DataFrame": mailing_list,
            "PrimaryKey": ["CustomerId", "Email"],
        }
    )
    return PeakAboveSATRecipients.query_table(arguments={"db_path": DB_PATH})


def main() -> None:
    print("Initializing PeakAboveSAT customers...")
    customers = init_customers()
    print(customers)

    print("\nInitializing PeakAboveSAT mailing list...")
    recipients = init_mailing_list(customers)
    print(recipients)


if __name__ == "__main__":
    main()
