#!/usr/bin/env python3
""" flask app file """

import locale
from flask import (
    Flask,
    render_template,
    request,
    g
)
from flask_babel import Babel
from datetime import timezone as tmzn
from datetime import datetime
from pytz import timezone
import pytz.exceptions

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
    g.user = get_user()
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    fmt = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(fmt)


@babel.localeselector
def get_locale():
    """ return best match language """
    loc = request.args.get('locale')
    if loc and loc in app.config['LANGUAGES']:
        return str(loc)
    elif g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    elif request.accept_languages:
        return request.accept_languages.best_match(app.config['LANGUAGES'])
    return babel.default_locale


@babel.timezoneselector
def get_timezone():
    """determines correct time_zone"""
    tzone = request.args.get('timezone', None)
    if tzone:
        try:
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    if g.user:
        try:
            tzone = g.user.get('timezone')
            return timezone(tzone).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    dflt = app.config['BABEL_DEFAULT_TIMEZONE']
    return dflt


@app.route('/', strict_slashes=False)
def index():
    """ index route """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
