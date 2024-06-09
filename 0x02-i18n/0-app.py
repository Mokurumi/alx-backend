#!/usr/bin/env python3
"""
i18n
"""


from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index"""
    return render_template('0-index.html')
