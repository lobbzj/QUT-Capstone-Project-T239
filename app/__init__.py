from flask import Flask 
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()

def create_app():
    
    print(__name__)
    app = Flask(__name__)  
    app.debug = True
    app.secret_key = 'asecret'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
    db.init_app(app)

    Bootstrap5(app)

    from . import views
    app.register_blueprint(views.mainbp)
    from . import register
    app.register_blueprint(register.registerbp)
    from . import login
    app.register_blueprint(login.loginbp)
    from . import create
    app.register_blueprint(create.createbp)
    return app