
from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.moment import Moment
from flask.ext.mail import Mail
from config import config
import os
import logging


bootstrap = Bootstrap()
moment = Moment()
mail = Mail()


def create_app(config=None):
    app = Flask(__name__)
    
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)


    if config is None:
        config = os.path.join(app.root_path, 'default.cfg')
    
    app.config.from_pyfile(config)
    
    return app
