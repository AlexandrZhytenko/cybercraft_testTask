# import sqlite3
#
#
# con = sqlite3.connect("session_history.db")
# cur = con.cursor()
# cur.execute(
#     "SELECT created_at, summary_status FROM session_history LIMIT 3"
# )
# results = cur.fetchall()
# print results
#
#
# cur.close()
# con.close()


# passing and failing builds per day, stacked-chart.
#  Use columns created_at and summary status
# import pandas
# import sqlite3
#
# con = sqlite3.connect("session_history.db")
# query = """SELECT
#                session_id, created_at, summary_status
#            FROM
#                session_history
#            """
#
# data = pandas.read_sql(query, con)
# print data
# from matplotlib import pyplot as plt
#
# plt.plot(data["created_at"], data["summary_status"])
# plt.grid()
# plt.title("passing and failing builds per day")
# plt.ylabel("summary_status")
# plt.xlabel("created_at")
# plt.xticks(rotation=90)
# plt.show()

# build duration vs. time.
# Use columns duration and created_at
# import pandas
# import sqlite3
#
# con = sqlite3.connect("session_history.db")
# query = """SELECT
#                session_id, created_at, duration
#            FROM
#                session_history
#            """
#
# data = pandas.read_sql(query, con)
# print data
#
# from matplotlib import pyplot as plt
#
# plt.plot(data["created_at"], data["duration"])
# plt.grid()
# plt.title("duration vs. time")
# plt.ylabel("duration")
# plt.xlabel("created_at")
# plt.xticks(rotation=90)
# plt.show()

