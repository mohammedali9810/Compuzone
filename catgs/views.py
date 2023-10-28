from . import catgs_blueprint
from Compuzone.models import db,Categ,Pos_Mod
from flask import redirect, render_template, url_for, request

@catgs_blueprint.route('/allcat',endpoint='allcategories')
def all_catg():
    categories = Categ.query.all()
    return render_template('allcat.html', categories=categories)

@catgs_blueprint.route('/crcat',methods=['POST','GET'])
def cr_catg():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        category = Categ(name=name, description=description)
        db.session.add(category)
        db.session.commit()
        return redirect(url_for('compos.all'))
    return render_template('addcat.html')


@catgs_blueprint.route('/edcat/<int:id>',methods=['POST','GET'])
def edcatg(id):
    print(id)
    catgs = Categ.query.get(id)
    if request.method =='POST':
        catgs.name = request.form['name']
        catgs.description = request.form['description']
        db.session.commit()
        return redirect(url_for('posts.all'))
    return render_template('edcat.html',category=catgs)

@catgs_blueprint.route('/delcat/<int:id>')
def delcatg(id):
    catgs = Categ.query.get(id)
    db.session.delete(catgs)
    db.session.commit()
    return redirect(url_for('posts.all'))

@catgs_blueprint.route('/catg/<int:id>/posts', endpoint='category_posts')
def category_posts(id):
    category = Categ.query.get_or_404(id)
    posts = Pos_Mod.query.filter_by(category_id=id).all()
    return render_template('index.html', category=category, posts=posts)




