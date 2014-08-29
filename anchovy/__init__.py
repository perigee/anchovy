from anchovy.oauth import oauth 
from flask import Flask
import os

def create_app(config=None):
    app = Flask(__name__)
    if config is None:
        config = os.path.join(app.root_path, 'default.cfg')
    
    app.config.from_pyfile(config)
    
    return app
