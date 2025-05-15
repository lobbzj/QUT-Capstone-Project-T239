from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import datetime


db = SQLAlchemy()


def create_app():


    print(__name__)
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'asecret'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sitedata.sqlite'
    db.init_app(app)

    Bootstrap5(app)

    Bcrypt(app)

    UPLOAD_FOLDER = 'app/static/img'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

     #create a user loader function takes userid and returns User
    from .models import User  # importing here to avoid circular references
    @login_manager.user_loader
    def load_user(user_id):
      return User.query.get(int(user_id))

    from . import views
    app.register_blueprint(views.mainbp)
    from . import auth
    app.register_blueprint(auth.authbp)
    from . import confirmation
    app.register_blueprint(confirmation.confirmationbp)
    from . import checkout
    app.register_blueprint(checkout.checkoutbp)
    from . import products
    app.register_blueprint(products.productsbp)
    from . import cart
    app.register_blueprint(cart.cartbp)
    from . import contact  
    app.register_blueprint(contact.contactbp)
    from . import wishlist
    app.register_blueprint(wishlist.wishlist_bp, url_prefix='/wishlist')
    from .api import productsAPI
    app.register_blueprint(productsAPI.api_products_bp)
    from .api import usersAPI
    app.register_blueprint(usersAPI.api_users_bp)
    from .api import commentsAPI
    app.register_blueprint(commentsAPI.api_comments_bp)

    

    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)
    
    #this creates a dictionary of variables that are available to all templates
    @app.context_processor
    def get_context():
      year = datetime.datetime.today().year
      return dict(year=year)
    
    @app.after_request
    def add_header(response):
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'
        return response

    
    with app.app_context():
      db.create_all()
    
    return app
