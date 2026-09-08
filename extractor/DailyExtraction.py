import logging
import os
import sys
from datetime import datetime
from pathlib import Path

import pandas as pd
from slack_bolt import App


def _find_project_root() -> Path:
    extractor_dir = Path(__file__).resolve().parent
    root = extractor_dir.parent
    if (root / "locallib").is_dir() and (root / "lib" / "tables").is_dir():
        return root
    raise FileNotFoundError(
        f"Could not find PeakAboveSAT root (locallib + lib/tables). cwd={Path.cwd()!r}"
    )


PROJECT_ROOT = _find_project_root()
EXTRACTOR_DIR = Path(__file__).resolve().parent
LOG_DIR = PROJECT_ROOT / "logs"
LOG_FILE = LOG_DIR / "extractor.log"

# Ensure project locallib wins over any copy installed in the venv.
_project_root_str = str(PROJECT_ROOT)
sys.path = [_project_root_str] + [p for p in sys.path if p != _project_root_str]
os.chdir(PROJECT_ROOT)

from locallib.picarrodb import *
from locallib.box import *
from locallib.pandas import *
from locallib.query import *

import lib.custom_pandas
from lib.query import *
from lib.input_output import *
from lib.msapi import *
from lib.config import *
from lib.tables.IngesterTables import *
from lib.KPIHubConnection import *

OUT_COLS = [
    "CustomerName",
    "PeakName",
    "PeakId",
    "Date",
    "WeekNumber",
    "Disposition",
    "LocalTime",
    "BoundaryName",
    "Region",
    "SubRegion",
    "Plant",
    "EmissionRate",
    "PeakGpsLatitude",
    "PeakGpsLongitude",
    "Easting",
    "Northing",
    "UserName",
    "SurveyorUnit",
    "AnalyzerSerialNumber",
    "Hyperlink",
    "LastUpdated",
]
DB_COLS = [
    "CustomerId",
    "PeakName",
    "PeakId",
    "Date",
    "WeekNumber",
    "Disposition",
    "LocalTime",
    "BoundaryName",
    "Region",
    "SubRegion",
    "Plant",
    "EmissionRate",
    "PeakGpsLatitude",
    "PeakGpsLongitude",
    "Easting",
    "Northing",
    "UserName",
    "SurveyorUnit",
    "AnalyzerSerialNumber",
    "Hyperlink",
    "LastUpdated",
]


NOISY_LOGGER_NAMES = (
    "slack_sdk",
    "slack_sdk.web",
    "slack_sdk.web.base_client",
    "slack_bolt",
    "urllib3",
    "boxsdk",
    "boxsdk.network",
    "gasanalytics",
)


class _TeeStream:
    def __init__(self, stream, log):
        self.stream = stream
        self.log = log
        self._buffer = ""

    def _should_log_line(self, line: str) -> bool:
        stripped = line.strip()
        if not stripped:
            return False
        lowered = stripped.lower()
        if stripped.startswith(("\x1b[", "POST ", "GET ", '"POST ', '"GET ')):
            return False
        if any(
            token in lowered
            for token in (
                "api.box.com",
                "upload.box.com",
                "slack.com/api",
                "chat.postmessage",
                "chat_postmessage",
            )
        ):
            return False
        return True

    def write(self, data):
        if not data:
            return 0
        self.stream.write(data)
        self._buffer += data
        while "\n" in self._buffer:
            line, self._buffer = self._buffer.split("\n", 1)
            if self._should_log_line(line):
                self.log.info(line)
        return len(data)

    def flush(self):
        self.stream.flush()
        if self._buffer and self._should_log_line(self._buffer):
            self.log.info(self._buffer)
            self._buffer = ""
        elif self._buffer:
            self._buffer = ""


def setup_logging() -> logging.Logger:
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.FileHandler(LOG_FILE, mode="a")],
        force=True,
    )
    for logger_name in NOISY_LOGGER_NAMES:
        logging.getLogger(logger_name).setLevel(logging.WARNING)

    logger = logging.getLogger("extractor")
    sys.stdout = _TeeStream(sys.__stdout__, logger)
    print(f"Logging to {LOG_FILE}")
    return logger


def process_customer(
    customer_info: pd.Series,
    start_date: str,
    end_date: str,
    send_email: bool,
    app: App,
) -> None:
    customer_name = customer_info["Name"]
    print(f"-----{customer_name}")
    customer_id = customer_info["CustomerId"]
    threshold = float(customer_info["ThresholdSCFH"])
    connection = CONN_DICT[customer_info["DBLocation"]]
    box_folder_id = customer_info["BoxFolderId"]
    xchange_location = customer_info["XchangeLocation"]
    
    filename = f"{customer_name}_{SUFFIX}_{end_date}.xlsx"
    output_path = EXTRACTOR_DIR / filename

    recipients = PeakAboveSATRecipients.query_table(arguments={"db_path": DB_PATH})
    recipients = recipients[
        (recipients["Active"] == True) & (recipients["CustomerId"] == customer_id)
    ]

    output_log = "=" * 20 + "\n"
    output_log = f"Starting the process for {customer_name}  \n "
    output_log += f'Process started at: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n'
    output_log += "=" * 20 + "\n"

    a = get_users(customer_name, "#UserList")
    b = get_surveys("#UserList", "#SurveyList", start_date, end_date)
    b.set_child(get_peak_table("#SurveyList", "#UserList", threshold))
    a.set_child(b)
    current_data = a.execute(connection)
    db_records = len(current_data)
    print("Number of peaks in the P-Cubed Database:", db_records)

    local_data = Query(
        f"SELECT * FROM PeakAboveSAT WHERE CustomerId =  '{customer_id}'"
    ).execute(KPIHub_Conn)

    if len(current_data) > 0:
        if local_data is not None:
            process_data = current_data[~current_data["PeakName"].isin(local_data["PeakName"])]
        else:
            process_data = current_data
        new_peaks = len(process_data)
        print("There are", len(process_data), "new peaks")
        output_log += f"There are {len(process_data)} new peaks\n"
    else:
        print("There are no SAT peaks between", start_date, "and", end_date)
        process_data = pd.DataFrame()
        new_peaks = 0

    if len(process_data) > 0:
        process_data.DA3540.add_easting_northing()
        process_data.DA3540.epoch_to_local_time()

        boundaries = pd.DataFrame(process_data["BoundaryName"].unique(), columns=["BoundaryName"])
        query = (
            f"SELECT externalid as BoundaryName, region as Region, subregion as SubRegion, "
            f"plant as plant FROM xchange.{xchange_location} "
            f"WHERE externalid IN (SELECT BoundaryName FROM temp_boundaries)"
        )
        boundaries.db.set_query(query)
        regions = boundaries.db.execute(
            DATAHUB_Conn,
            temp_table_name="temp_boundaries",
            source_col="BoundaryName",
        )
        process_data["Region"] = process_data["BoundaryName"].map(
            regions.set_index("boundaryname")["region"]
        )
        process_data["SubRegion"] = process_data["BoundaryName"].map(
            regions.set_index("boundaryname")["subregion"]
        )
        process_data["Plant"] = process_data["BoundaryName"].map(
            regions.set_index("boundaryname")["plant"]
        )
        process_data["Date"] = pd.to_datetime(process_data["Date"], errors="coerce")
        process_data["WeekNumber"] = process_data["Date"].dt.isocalendar().week
        process_data["LastUpdated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        daily_report = process_data.copy()
        daily_report["Hyperlink"] = daily_report["SurveyId"].apply(
            lambda x: f"https://pcubed2.eu.picarro.com/Live/Survey/{x.lower()}"
            if pd.notna(x)
            else ""
        )
        daily_report.sort_values(by=["Date", "LocalTime"], inplace=True, ascending=False)
        daily_report["CustomerId"] = customer_id

        PeakAboveSAT.update_table(
            arguments={
                "db_path": DB_PATH,
                "DataFrame": daily_report[DB_COLS],
                "PrimaryKey": "PeakId",
            }
        )

    local_data = Query(
        f"SELECT * FROM PeakAboveSAT WHERE CustomerId =  '{customer_id}'"
    ).execute(KPIHub_Conn)
    num_local_data = len(local_data)
    output_log += f"Number of peaks in the local database: {num_local_data}\n"
    print("Number of peaks in the local database:", num_local_data)
    output_log += f"Number of peaks in the P-Cubed database: {db_records}\n"
    print("Number of peaks in the P-Cubed database:", db_records)
    output_log += "=" * 20 + "\n"

    if len(process_data) > 0:
        local_data.drop(columns=["CustomerId"], inplace=True)
        local_data["CustomerName"] = customer_name
        local_data.sort_values(by=["Date", "LocalTime"], inplace=True, ascending=False)
        local_data[OUT_COLS].to_excel(output_path, index=False)
        auto_adjust_excel_columns(str(output_path))

        box_file = BoxFile(str(output_path), str(box_folder_id))
        box_file.upload()

    if send_email and len(process_data) > 0:
        for rcpt in recipients["Email"]:
            try:
                send_email_via_outlook_api(
                    subject=f"{customer_name} - Peaks above SAT - New {new_peaks} peaks found",
                    body=f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}.',
                    recipient=rcpt,
                    attachments=[str(output_path)],
                )
                print(f"Email sent successfully to {rcpt}")
            except Exception as e:
                print(f"Failed to send email to {rcpt}: {e}")
    else:
        print("No new peaks to process")
        output_log += "No new peaks to process\n"

    #Send the log to the slack channel
    app.client.chat_postMessage(
            channel='C0C0F3XA8NQ',
            text="Data Extractions Uploaded",
            emoji=True,
            blocks=[
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": output_log
                    }
                }
            ]
        )


def main() -> None:
    _ = setup_logging()

    customers = PeakAboveSATCustomer.query_table(arguments={"db_path": DB_PATH})
    start_date = STARTING_DATE.strftime("%Y-%m-%d")
    end_date = datetime.now().strftime("%Y-%m-%d")
    send_email = True

    slack_bot_token = os.getenv("SLACKBOTTOKEN")
    app = App(token=slack_bot_token)

    for _, customer_info in customers.iterrows():
        process_customer(customer_info, start_date, end_date, send_email, app)


if __name__ == "__main__":
    main()
