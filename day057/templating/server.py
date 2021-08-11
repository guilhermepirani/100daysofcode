import random
import requests
import datetime as dt
from flask import Flask, render_template


app = Flask(__name__)

# Makes the return avaiable to all templates in the application
@app.context_processor
def inject_year():
    year = dt.datetime.now().year

    # Returned as a dict, but acessed as variable inside the templates
    return dict(year=year)


@app.route('/')
def home():
    num = random.randint(1, 10)

    return render_template('index.html', num=num)

@app.route('/guess/<name>')
def guess(name):
    gender = requests.get(f'https://api.genderize.io?name={name}').json()['gender']
    age = requests.get(f'https://api.agify.io?name={name}').json()['age']

    return render_template('guess.html', name=name.capitalize(), gender=gender, age=age)

@app.route('/blog')
def blog():
    posts = requests.get('https://api.npoint.io/ed99320662742443cc5b').json()

    return render_template('blog.html', posts=posts)


if __name__ == '__main__':
    app.run(debug=True)