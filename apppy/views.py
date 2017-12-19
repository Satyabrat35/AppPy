from flask import render_template, flash, redirect, url_for, abort

from apppy import app, db
from forms import BookmarkForm
from models import User, Bookmark


def logged_in_user():
    return models.User.query.filter_by(username="Erik").first() #fake login :(

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',new_bookmark=Bookmark.new(2))


@app.route('/add',methods=['GET','POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        db.session.add(Bookmark(user=logged_in_user(),url=form.obj.data,description=form.description.data))
        db.session.commit()
        flash("Stored description {}".format(form.description.data))
        return redirect(url_for('index'))
    return render_template('add.html',form=form)

@app.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html',user=user)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


