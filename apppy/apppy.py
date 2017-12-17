from flask import Flask, render_template, url_for , request,redirect,flash
from datetime import datetime
#from logging import DEBUG
from forms import BookmarkForm

app = Flask(__name__)
#app.logger.setLevel(DEBUG)
app.config['SECRET_KEY'] = '+\xaeOm\xa7D["\xff\x1b-\x83\xd7\x87\xd4\x8a\x8730\xa0\x00\x1fe\xe9'


bookmark = []
def store_bookmark(obj,description):
	bookmark.append(dict(
		obj = obj,
		user = "erik",
		date = 	datetime.utcnow(),
		description = description
		))

def new_bookmark(num):
	return sorted(bookmark,key=lambda bm: bm['date'] , reverse=True)[:num]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',new_bookmark=new_bookmark(5))


@app.route('/add',methods=['GET','POST'])
def add():
	form = BookmarkForm()
	if form.validate_on_submit():
		obj = form.obj.data
		description = form.description.data
		store_bookmark(obj,description)
		flash("Bookmark Stored: {}".format(description))
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
