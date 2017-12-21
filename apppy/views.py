from flask import render_template, flash, redirect, url_for, abort , request

from apppy import app, db , login_manager
from forms import BookmarkForm , LoginForm
from models import User, Bookmark
from flask_login import login_required , login_user



@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

#def logged_in_user():
 #   return models.User.query.filter_by(username="Erik").first() #fake login :(

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',new_bookmark=Bookmark.new(2))


@app.route('/add',methods=['GET','POST'])
@login_required
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

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            login_user(user,form.remember_me.data)
            flash("Logged In Successful as {}".format(user.username))
            return redirect(request.args.get('next') or url_for('index')) #next makes sure that after logging in the user can then visit any other page
        flash("Incorrect password or username")
    return render_template("login.html",form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


