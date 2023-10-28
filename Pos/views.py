from flask import render_template, redirect, url_for,request
from Pos import compos_blueprint
from Compuzone import db
from Compuzone.models import Pos_Mod
from werkzeug.utils import secure_filename
import os
from datetime import datetime
from uuid import uuid4



@compos_blueprint.route('/', endpoint='all')
def get_all_posts():
    pos_comps = Pos_Mod.query.all()
    return render_template('index.html', posts=pos_comps)

@compos_blueprint.route('/contactus')
def get_contact():
    return render_template('contact.html')

@compos_blueprint.route('/newpost', methods=['GET', 'POST'])
def create_post():
    if request.method == 'POST':
        image = request.files['image']
        imageurl = generate_filename(secure_filename(image.filename))
        image.save(os.path.join('static/images/pim', imageurl))
        post = Pos_Mod(name=request.form['name'], desc=request.form['desc'], image=imageurl)
        db.session.add(post)
        db.session.commit()
        return redirect((url_for('compos.all')))
    return render_template('newp.html')

@compos_blueprint.route('/post/<int:id>')
def showpost(id):
    pos_comps = Pos_Mod.query.get_or_404(id)
    return render_template('det.html', post=pos_comps)

@compos_blueprint.route('/post/<int:id>/delete')
def deletepost(id):
    pos_comps = Pos_Mod.query.get_or_404(id)
    imageurl = pos_comps.image
    os.remove(os.path.join('static/images/pim', imageurl))
    db.session.delete(pos_comps)
    db.session.commit()
    return redirect((url_for('index')))

@compos_blueprint.route('/edpos/<int:id>', methods=['POST', 'GET'])
def edpos(id):
    pos_comps = Pos_Mod.query.get_or_404(id)
    if request.method == 'POST':
        if request.files['image']:
            image = request.files['image']
            pre_imageurl = pos_comps.image
            os.remove(os.path.join('static/images/pim', pre_imageurl))
            imageurl = generate_filename(secure_filename(image.filename))
            image.save(os.path.join('static/images/pim', imageurl))

        pos_comps.image = image.filename
        pos_comps.name = request.form['name']
        pos_comps.desc = request.form['desc']
        db.session.commit()
        return redirect((url_for('compos.all')))
    return render_template('edpos.html',post=pos_comps)


def generate_filename(filename):
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
    random_uuid = str(uuid4().hex)
    _, extension = os.path.splitext(filename)
    new_filename = f"{timestamp}_{random_uuid}{extension}"
    return new_filename