from flask import Flask, redirect, url_for
from flask_migrate import Migrate
from flask_login import LoginManager

from models import db
from config import Config
from sockets.socketio import socketio

login_manager = LoginManager()


def create_app():
    _app = Flask(__name__)

    _app.config.from_object(Config())

    # init plugins
    db.init_app(_app)
    login_manager.init_app(_app)
    socketio.init_app(_app)

    from views.home import home
    from views.auth import auth
    from views.artworks import artworks

    # register blueprints
    _app.register_blueprint(home, url_prefix='/')
    _app.register_blueprint(auth, url_prefix='/auth')
    _app.register_blueprint(artworks, url_prefix='/artworks')

    migrate = Migrate(_app, db)

    from models.user import User

    @login_manager.user_loader
    def load_user(identifier):
        return User.query.get(int(identifier))

    # Error Management
    @_app.errorhandler(404)
    def page_not_found(error):
        return redirect(url_for('index.index'))

    db.create_all(app=_app)

    return _app


app = create_app()

if __name__ == '__main__':
    socketio.run(app, port=8000, debug=True)
