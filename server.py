from flask import Flask, render_template


#
app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


# debug=True this will let the server to auto refresh new changes.
if __name__ == "__main__":
    app.run(debug=True)
