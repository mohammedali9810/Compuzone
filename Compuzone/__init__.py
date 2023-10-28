from flask import Flask
from Compuzone.models import db
from Compuzone.config import projectConfig as AppConfig
from flask_migrate import Migrate

def cr_app(mode='dev'):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = AppConfig[mode]
    app.config[' UPLOAD_FOLDER'] = AppConfig[mode]
    app.config.from_object(AppConfig[mode])

    db.init_app(app)
    migrate = Migrate(app, db,render_as_batch=True)

    from Pos.views import compos_blueprint
    app.register_blueprint(compos_blueprint)

    from catgs.views import catgs_blueprint
    app.register_blueprint(catgs_blueprint)


    return app