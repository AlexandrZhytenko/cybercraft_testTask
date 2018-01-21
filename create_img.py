import pandas, sqlite3
from matplotlib import pyplot as plt

con = sqlite3.connect("session_history.db")
query = """SELECT
               created_at, summary_status, duration
           FROM
               session_history
           ORDER BY
               created_at
           """
data = pandas.read_sql(query, con)

 # passing and failing builds per day, stacked-chart.
#  Use columns created_at and summary status
plt.plot(pandas.to_datetime(data["created_at"], utc=True), data["summary_status"], 'b.-')
plt.grid(True)
plt.title("passing and failing builds per day")
plt.ylabel("summary_status")
plt.xlabel("created_at")
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.11, right=0.95, bottom=0.25, top=0.93)
plt.savefig('passing_failing')
plt.show()
plt.close()

# build duration vs. time.
# Use columns duration and created_at
plt.plot_date(pandas.to_datetime(data["created_at"], utc=True), data["duration"], 'b.-')
plt.grid(True)
plt.title("duration vs. time")
plt.ylabel("duration")
plt.xlabel("created_at")
plt.xticks(rotation=90)
plt.subplots_adjust(left=0.11, right=0.95, bottom=0.25, top=0.93)
plt.savefig('duration_time')
plt.show()
plt.close()