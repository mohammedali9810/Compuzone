from flask_sqlalchemy import SQLAlchemy
from flask import url_for
db = SQLAlchemy()



class Pos_Mod(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    image = db.Column(db.String, nullable=False)
    desc = db.Column(db.String, nullable=False)
    creat_dat = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    upd_dat = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
    category = db.Column(db.Integer, db.ForeignKey('categ.id'), nullable=True)
    @property
    def get_image_url(self):
        return url_for('static', filename=f'images/pim/{self.image}')

    def get_category_name(self):
        categoryname = Categ.query.get_or_404(self.category)
        return categoryname

class Categ(db.Model):
        id = db.Column(db.Integer, primary_key=True, autoincrement=True)
        name = db.Column(db.String[30], nullable=False)
        created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
        description = db.Column(db.String, nullable=True)
        updated_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now(), onupdate=db.func.now())
        posts = db.relationship('Pos_Mod', backref='categid', lazy=True)

        def __str__(self):
            return self.name

        @classmethod
        def get_all_categories(cls):
            return cls.query.all()