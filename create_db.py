import csv, sqlite3

con = sqlite3.connect("session_history.db")
cur = con.cursor()
cur. execute(
    """CREATE TABLE session_history (
    session_id INTEGER,
    started_by TEXT,
    created_at TEXT,
    summary_status TEXT,
    duration REAL,
    worker_time REAL,
    bundle_time INTEGER,
    num_workers INTEGER,
    branch TEXT,
    commit_id TEXT,
    started_tests_count INTEGER,
    passed_tests_count INTEGER,
    failed_tests_count INTEGER,
    pending_tests_count INTEGER,
    skipped_tests_count INTEGER,
    error_tests_count INTEGER)"""
)

with open("session_history.csv", "r") as session_history:
    dataRow = csv.DictReader(session_history)
    to_db = [
        (
            item["session_id"],
            item["started_by"],
            item["created_at"],
            item["summary_status"],
            item["duration"],
            item["worker_time"],
            item["bundle_time"],
            item["num_workers"],
            item["branch"],
            item["commit_id"],
            item["started_tests_count"],
            item["passed_tests_count"],
            item["failed_tests_count"],
            item["pending_tests_count"],
            item["skipped_tests_count"],
            item["error_tests_count"]
        ) for item in dataRow
    ]

cur.executemany(
    "INSERT INTO session_history VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db
)
con.commit()






