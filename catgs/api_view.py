from flask_restful import marshal_with, Resource,fields
from flask_restful.reqparse import RequestParser
from Compuzone.models import db, Categ
# from flask_restx import Api, Resource, fields


# api = Api()
#
# categ_model = api.model('Category', {
#     'id': fields.Integer,
#     'name': fields.String,
#     'created_at': fields.DateTime,
#     'description': fields.String,
#     'updated_at': fields.DateTime,
# })
#
# @api.route('/categories')
# class CategList(Resource):
#     @api.marshal_with(categ_model)
#     def get(self):
#         categ = Categ.query.all()
#         return categ
#
#     @api.expect(categ_model)
#     @api.marshal_with(categ_model)
#     def post(self):
#         categargs = api.payload
#         categs = Categ(name=categargs['name'], description=categargs['description'])
#         db.session.add(categs)
#         db.session.commit()
#         return categs
#
# @api.route('/category/<int:id>')
# class CategDetail(Resource):
#     @api.marshal_with(categ_model)
#     def get(self, id):
#         categs = Categ.query.get_or_404(id)
#         return categs
#
#     @api.expect(categ_model)
#     @api.marshal_with(categ_model)
#     def put(self, id):
#         category = Categ.query.get_or_404(id)
#         categargs = api.payload
#         category.name = categargs['name']
#         category.description = categargs['description']
#         db.session.commit()
#         return category
#
#     @api.response(204, 'Category deleted')
#     def delete(self, id):
#         compcateg = Categ.query.get_or_404(id)
#         db.session.delete(compcateg)
#         db.session.commit()
#         return "deleted"
#






categ_serializer = {
    "id" : fields.Integer,
    "name" : fields.String,
    "created_at" : fields.DateTime,
    "description" : fields.String,
    "updated_at" : fields.DateTime,
}

CategoryParser = RequestParser()
CategoryParser.add_argument('name',type=str,required=True,help="Category name name is required")
CategoryParser.add_argument('description',type=str,required=True,help="Student image is required")


class Categlis(Resource):
    @marshal_with(categ_serializer)
    def get(self):
        categ = Categ.query.all()
        return categ

    @marshal_with(categ_serializer)
    def post(self):
        categargs = CategoryParser.parse_args()
        categs = Categ(name=categargs['name'],description=categargs['description'])
        db.session.add(categs)
        db.session.commit()
        return categs

class CategDat(Resource):
    @marshal_with(categ_serializer)
    def get(self,id):
        categs = Categ.query.get_or_404(id)
        return categs
    @marshal_with(categ_serializer)
    def put(self,id):
        category = Categ.query.get_or_404(id)
        categargs = CategoryParser.parse_args()
        category.name = categargs['name']
        category.description = categargs['description']
        db.session.commit()
        return category

    @marshal_with(categ_serializer)
    def delete(self, id):
        compcateg = Categ.query.get_or_404(id)
        db.session.delete(compcateg)
        db.session.commit()
        return "deleted"