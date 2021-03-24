import random
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        name_1 = request.form["name1"]
        name_2 = request.form["name2"]

        percentage = random.randint(0, 100)

        result = name_1 + " and " + name_2 + " like each other " + str(percentage) + "%"

        return render_template("index.html", content=result)

    else:
        return render_template("index.html")