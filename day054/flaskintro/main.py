'''First contact with flask'''

from flask import Flask

# Initialize Flask
app = Flask(__name__)


@app.route('/') # Decorator to run code below when route is /
def hello_world():
    return 'Hello, World!'

@app.route("/bye") # Decorator to run code below when route is /bye
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()
