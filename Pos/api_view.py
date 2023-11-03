from flask_restful import Resource, fields, marshal_with
from Compuzone.models import Pos_Mod  # Make sure to import Pos_Mod
from flask_restful.reqparse import RequestParser
from Compuzone.models import db
from werkzeug.datastructures import FileStorage
from flask import request
import json


import os
from werkzeug.utils import secure_filename

compos_serializer = {
    "id": fields.Integer,
    "name": fields.String,
    "image": fields.String,
    "desc": fields.String,
    "creat_dat": fields.DateTime,
    "upd_dat": fields.DateTime,
    "category": fields.Integer,
}

CompParser = RequestParser()
CompParser.add_argument('name', type=str, required=True, help="Post name is required")
CompParser.add_argument('image', type=FileStorage, required=True, help="Post image is required")
CompParser.add_argument('desc', type=str)
CompParser.add_argument('category', type=int)

def save_uploaded_file(file):
    if isinstance(file, FileStorage):
        # If the file is a FileStorage object, save it to the destination folder
        filename = secure_filename(file.filename)
        upload_folder = 'static/images/pim'
        os.makedirs(upload_folder, exist_ok=True)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        return f'/static/images/pim/{filename}'
    elif isinstance(file, str):
        # If the file is already a path, return it as is
        return file
    else:
        # Handle other cases if needed
        raise ValueError("Invalid file type")


class Compapi(Resource):
    @marshal_with(compos_serializer)
    def get(self):
        posts = Pos_Mod.query.all()
        return posts, 200

    @marshal_with(compos_serializer)
    def post(self):
        raw_data = request.data.decode('utf-8')
        postargs = json.loads(raw_data)
        image_file = postargs.get('image')
        image_url = save_uploaded_file(image_file)

        comps = Pos_Mod(
            name=postargs.get('name'),
            image=image_url,
            desc=postargs.get('desc'),
            category=postargs.get('category')
        )

        db.session.add(comps)
        db.session.commit()
        return comps


class Compdat(Resource):
    @marshal_with(compos_serializer)
    def put(self, id):
        compos = Pos_Mod.query.get_or_404(id)
        postargs = CompParser.parse_args()

        if 'image' in request.files:
            # If a new image is provided, save it and update the image URL
            new_image = request.files['image']
            new_image_url = save_uploaded_file(new_image)
            compos.image = new_image_url

        # Update other fields
        compos.name = postargs['name']
        compos.desc = postargs['desc']
        compos.category = postargs['category']

        db.session.commit()
        return compos

    @marshal_with(compos_serializer)
    def delete(self, id):
        comps = Pos_Mod.query.get_or_404(id)
        db.session.delete(comps)
        db.session.commit()
        return "deleted"

    @marshal_with(compos_serializer)
    def get(self, id):
        comps = Pos_Mod.query.get_or_404(id)
        return comps
