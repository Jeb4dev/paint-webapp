from flask import Flask
from flask_migrate import Migrate

from models import db
from config import Config
from login import login_manager

from views.home import home
from views.auth import auth
from views.artworks import artworks

app = Flask(__name__)

app.config.from_object(Config())

app.register_blueprint(home, url_prefix='/')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(artworks, url_prefix='/artworks')

db.init_app(app)
login_manager.init_app(app)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
