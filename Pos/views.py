from flask import render_template, redirect, url_for,request
from Pos import compos_blueprint
from Compuzone import db
from Compuzone.models import Pos_Mod, Categ
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
        # upload_folder = os.path.join(os.getcwd(), 'static', 'images', 'pim')
        # print("Absolute Path:", os.path.join(upload_folder, image.filename))
        image.save(os.path.join('static', 'images', 'pim', imageurl))
        post = Pos_Mod(name=request.form['name'], desc=request.form['desc'], image=imageurl)
        db.session.add(post)
        db.session.commit()
        return redirect((url_for('compos.all')))
    return render_template('newp.html')

@compos_blueprint.route('/post/<int:id>')
def showpost(id):
    pos_comps = Pos_Mod.query.get_or_404(id) # Assuming there is a one-to-many relationship
    category = pos_comps.category
    return render_template('det.html', post=pos_comps, category=category)



@compos_blueprint.route('/post/<int:id>/delete')
def deletepost(id):
    pos_comps = Pos_Mod.query.get_or_404(id)
    imageurl = pos_comps.image
    os.remove(os.path.join('static/images/pim', imageurl))
    db.session.delete(pos_comps)
    db.session.commit()
    return redirect((url_for('compos.all')))





@compos_blueprint.route('/edpos/<int:id>', methods=['POST', 'GET'])
def edpos(id):
    pos_comps = Pos_Mod.query.get_or_404(id)
    categs = Categ.get_all_categories()
    img_dir = os.path.join('static', 'images', 'pim')
    old_category = pos_comps.category
    if request.method == 'POST':
        if 'image' in request.files and request.files['image']:
            image = request.files['image']

            old_image_path = os.path.join(img_dir, pos_comps.image)
            if os.path.exists(old_image_path):
                os.remove(old_image_path)

            imageurl = generate_filename(secure_filename(image.filename))
            image.save(os.path.join(img_dir, imageurl))
            pos_comps.image = imageurl

        pos_comps.name = request.form['name']
        pos_comps.desc = request.form['desc']
        category_id = request.form.get('category')
        if category_id and category_id.isdigit():
            pos_comps.category = int(category_id)
        else:
            pos_comps.category = old_category

        db.session.commit()

        return redirect(url_for('compos.all'))

    return render_template('edpos.html', post=pos_comps,categories=categs)


def generate_filename(filename):
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')[:-3]
    random_uuid = str(uuid4().hex)
    _, extension = os.path.splitext(filename)
    new_filename = f"{timestamp}_{random_uuid}{extension}"
    return new_filename

@compos_blueprint.route('/search', methods=['GET', 'POST'])
def search_posts():
    if request.method == 'POST':
        search_term = request.form['search_term']
        results = search_in_posts(search_term)
        return render_template('seares.html', results=results, search_term=search_term)

    return render_template('index.html')

def search_in_posts(search_term):
    results_by_name = Pos_Mod.query.filter(Pos_Mod.name.ilike(f"%{search_term}%")).all()
    results_by_category = Pos_Mod.query.join(Categ).filter(Categ.name.ilike(f"%{search_term}%")).all()
    results = list(set(results_by_name + results_by_category))

    return results

@compos_blueprint.route('/category/<int:category_id>/posts')
def posts_by_category(category_id):
    category = Categ.query.get_or_404(category_id)
    posts_in_category = Pos_Mod.query.filter_by(category=category.id).all()
    return render_template('allcatpos.html', category=category, posts=posts_in_category)