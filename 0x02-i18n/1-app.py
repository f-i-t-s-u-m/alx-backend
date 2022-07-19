#!/usr/bin/env python3
""" flask app file """

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ app config class """
    LANGUAGES = ['en', 'fr']
    local = 'en'
    timezone = 'UTC'


@app.route('/')
def index():
    """ index route """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
