from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager

from models import db
from config import Config

from views.home import home
from views.auth import auth

app = Flask(__name__)

app.config.from_object(Config())

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')

migrate = Migrate(app)
login = LoginManager(app)

db.init_app(app)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
