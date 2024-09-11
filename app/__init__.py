from flask import Flask


def create_app():
    print(__name__)
    app = Flask(__name__)
    app.debug = True
    app.secret_key = 'asecret'
    from . import views, products
    app.register_blueprint(views.mainbp)
    app.register_blueprint(products.productsbp)
    return app
