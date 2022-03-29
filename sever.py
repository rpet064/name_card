from flask import Flask, render_template
import random

app = Flask(__name__)

number = random.randint(1, 10)

@app.route("/")
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

