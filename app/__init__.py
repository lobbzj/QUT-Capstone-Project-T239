from flask import Flask 

def create_app():
    print(__name__)  
    app = Flask(__name__)  
    app.debug = True
    app.secret_key = 'asecret'
    from . import views
    app.register_blueprint(views.mainbp)
    from . import register
    app.register_blueprint(register.registerbp)
    from . import login
    app.register_blueprint(login.loginbp)
    from . import checkout
    app.register_blueprint(checkout.checkoutbp)
    from . import confirmation
    app.register_blueprint(confirmation.confirmationbp)
    return app