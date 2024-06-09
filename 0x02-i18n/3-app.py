#!/usr/bin/env python3
"""
i18n
"""


from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """get_locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index"""
    g.locale = get_locale()
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template("3-index.html", home_title=home_title,
                           home_header=home_header, get_locale=get_locale)
