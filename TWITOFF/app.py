"""
Main application for twitoff
"""

from flask import Flask, render_template
from .models import DB


def create_app():
    """
    Creates and configures an instance of a flask application
    """
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    DB.init_app(app)

    @app.route('/')
    def root():
        return render_template('home.html')

    @app.route('/about')
    def nfl():
        return render_template('about.html')

    return app
