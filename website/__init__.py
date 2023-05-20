from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'nhasdp9ihb12-938gs018b081cgvbdwiu8vboa'

    from .views import views
    from .ratings import ratings

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(ratings, url_prefix='/')

    return app

