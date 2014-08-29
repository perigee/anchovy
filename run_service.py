import os
from anchovy import create_app
from flask.ext.script import Manager, Shell

app = create_app(os.getenv('CONFIG') or 'default')
manager = Manager(app)


if __name__ == '__main__':
    manager.run()
