from flask import *
import random

application = Flask(__name__)


@application('/', method=['GET', 'POST'])
def home():
   if request.method== "POST":
       friendship_percent = random.randint(1, 101)
       friendship_percent = str(friendship_percent)
       return render_template('home.html', friendship=(friendship_percent+"4"))
   else:
       return render_template('home.html')


if __name__ == '__main__':
    application.run(debug=True)
