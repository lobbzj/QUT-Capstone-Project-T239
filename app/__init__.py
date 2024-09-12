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
    return app