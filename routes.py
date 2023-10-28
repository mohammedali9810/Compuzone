# from flask import render_template, redirect, url_for,request
# from Compuzone import app, db
# from Compuzone.models import Pos_Mod
# from werkzeug.utils import secure_filename
# import os
#
#
#
# @app.route('/', endpoint='index')
# def get_all_posts():
#     pos_comps = Pos_Mod.query.all()
#     return render_template('index.html', posts=pos_comps)
#
# @app.route('/contactus')
# def get_contact():
#     return render_template('Contact.html')
#
# @app.route('/newpost', methods=['GET', 'POST'])
# def create_post():
#     if request.method == 'POST':
#         image = request.files['image']
#         imageurl = secure_filename(image.filename)
#         image.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/pim', imageurl))
#         post = Pos_Mod(name=request.form['name'], desc=request.form['body'], image=imageurl)
#         db.session.add(post)
#         db.session.commit()
#         return redirect((url_for('index')))
#     return render_template('newp.html')
#
# @app.route('/post/<int:id>')
# def showpost(id):
#     pos_comps = Pos_Mod.query.get_or_404(id)
#     return render_template('det.html', post=pos_comps)
#
# @app.route('/post/<int:id>/delete')
# def deletepost(id):
#     pos_comps = Pos_Mod.query.get_or_404(id)
#     imageurl = pos_comps.image
#     os.remove(app.config['UPLOAD_FOLDER']+'/pim/'+imageurl)
#     db.session.delete(pos_comps)
#     db.session.commit()
#     return redirect((url_for('index')))
#
# @app.route('/edpos/<int:id>', methods=['POST', 'GET'])
# def editpost(id):
#     pos_comps = Pos_Mod.query.get_or_404(id)
#     if request.method == 'POST':
#         if request.files['image']:
#             image = request.files['image']
#             old_image_url = pos_comps.image
#             os.remove(app.config['UPLOAD_FOLDER']+'/pim/'+old_image_url)
#             image.save(os.path.join(app.config['UPLOAD_FOLDER'] + '/pim', image.filename))
#
#         pos_comps.image = image.filename
#         pos_comps.name = request.form['name']
#         pos_comps.desc = request.form['body']
#         db.session.commit()
#         return redirect((url_for('index')))
#     return render_template('edpos.html',post=pos_comps)
