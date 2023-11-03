from flask import Flask
from Compuzone.models import db
from Compuzone.config import projectConfig as AppConfig
from flask_migrate import Migrate
from flask_restful import Api
# from flask_restx import Api, Resource, fields
from Pos.api_view import Compapi, Compdat
from catgs.api_view import Categlis, CategDat

def cr_app(mode='dev'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = AppConfig[mode]
    app.config['UPLOAD_FOLDER'] = AppConfig[mode]
    app.config.from_object(AppConfig[mode])
    db.init_app(app)
    migrate = Migrate(app, db,render_as_batch=True)
    from Pos.views import compos_blueprint
    app.register_blueprint(compos_blueprint)
    from catgs.views import catgs_blueprint
    app.register_blueprint(catgs_blueprint)
    api = Api(app)
    api.add_resource(Compapi, "/api/allpos")
    api.add_resource(Compdat, "/api/allpos/<int:id>")
    api.add_resource(Categlis, "/api/categ")
    api.add_resource(CategDat, "/api/categ/<int:id>")
    # api.init_app(app, version='1.0', title='Your API', description='API documentation', doc='/swagger')


    return app