#!/usr/bin/env python3
""" flask app file """

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config(object):
    """ app config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ return best match language """
    loc = request.args.get('locale')
    if loc and loc in app.config['LANGUAGES']:
        return str(loc)
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ index route """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
