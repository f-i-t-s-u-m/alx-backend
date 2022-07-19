#!/usr/bin/env python3
""" flask app file """

from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """ app config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """ get user data function """
    arg = request.args.get('login_as')
    if arg:
        return users.get(int(arg))
    return None


@app.before_request
def before_request():
    """ get user data """
    user = get_user()
    if user:
        g.user = user


@babel.localeselector
def get_locale():
    """ return best match language """
    loc = request.args.get('locale')
    if loc and loc in app.config['LANGUAGES']:
        return str(loc)
    elif g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    elif request.headers.get('locale') in app.config['LANGUAGES']:
        return request.headers.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ index route """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
