import os
from flask import Flask, render_template, url_for , request,redirect,flash
from datetime import datetime
#from logging import DEBUG

from flask_sqlalchemy import SQLAlchemy
#from models import Bookmark //for the time being we can get away with circular import situations



base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '+\xaeOm\xa7D["\xff\x1b-\x83\xd7\x87\xd4\x8a\x8730\xa0\x00\x1fe\xe9'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir ,'apppy.db')
db = SQLAlchemy(app)

from forms import BookmarkForm
import models
# moved below db due to circular import in manage.py



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',new_bookmark=models.Bookmark.new(2))


@app.route('/add',methods=['GET','POST'])
def add():
    form = BookmarkForm()
    if form.validate_on_submit():
        db.session.add(models.Bookmark(url=form.obj.data,description=form.description.data))
        db.session.commit()
        flash("Stored description {}".format(form.description.data))
        return redirect(url_for('index'))
    return render_template('add.html',form=form)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
