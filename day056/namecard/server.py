'''A name card simple website

This day's objective was to understand the importance of placing
files in their correponding directories when dealing with frameworks, so
most of the code isn't mine, just reorganized to fit in a flask app.
'''

from flask import Flask, render_template


app = Flask(__name__)

# Home
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)