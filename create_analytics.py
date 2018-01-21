import pandas, sqlite3

con = sqlite3.connect("session_history.db")
query = """SELECT
               session_id, created_at, summary_status
           FROM
               session_history
           WHERE
               summary_status IS 'failed'
           ORDER BY
               created_at
           """
data = pandas.read_sql(query, con)

with sqlite3.connect("session_history.db") as connection:
    conn = connection.cursor()
    conn.execute(
            """SELECT
                   session_id, created_at, summary_status
               FROM
                   session_history
               WHERE
                   summary_status IS 'failed'
               ORDER BY
                   created_at""")
    rows_failed = conn.fetchall()

with sqlite3.connect("session_history.db") as connection:
    conn = connection.cursor()
    conn.execute(
            """SELECT
                   session_id, created_at, summary_status
               FROM
                   session_history
               WHERE
                   summary_status IS 'stopped'
               ORDER BY
                    created_at""")
    rows_stopped = conn.fetchall()

with sqlite3.connect("session_history.db") as connection:
    conn = connection.cursor()
    conn.execute(
            """SELECT
                   session_id, created_at, summary_status
               FROM
                   session_history
               WHERE
                   summary_status IS 'error'
               ORDER BY
                   created_at""")
    rows_error = conn.fetchall()

with sqlite3.connect("session_history.db") as connection:
    conn = connection.cursor()
    conn.execute(
            """SELECT
               summary_status, COUNT(summary_status) As Count
           FROM
               session_history
           GROUP BY 
               summary_status""")
    data_count = conn.fetchall()
