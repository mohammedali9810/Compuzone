# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# import os
#
#
# app = Flask(__name__)
#
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mali9810:M123456@localhost/compos'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#
# app.config['UPLOAD_FOLDER'] = 'static/images'
# os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)