from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def task():
    from create_analytics import data, rows_failed, rows_stopped, rows_error, data_count
    return render_template("index.html",
                           data=data,
                           rows_failed=rows_failed,
                           rows_stopped=rows_stopped,
                           rows_error=rows_error,
                           data_count=data_count)

if __name__ == "__main__":
    app.run(debug=True)