from flask import Flask 
from config import config_options
from flask_mail import Mail
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import IMAGES, UploadSet,configure_uploads
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
mail = Mail()
bootstap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos',IMAGES)



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    app.config['SECRET_KEY'] = 'secret'

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from .users.routes import users as users_blueprint
    from .posts.routes import posts as posts_blueprint
    from .main.routes import main as main_blueprint
    from .errors.handlers import errors as errors_blueprint
    app.register_blueprint(users_blueprint)
    app.register_blueprint(posts_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(errors_blueprint)
   
    return app
