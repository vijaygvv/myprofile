from flask import Flask

# app = Flask(__name__)
from app import app

# @app.route('/')
# def home():
#     return "<h1> this is HOME page <h1>"

if __name__ == '__main__':
    app.run(debug=True)


