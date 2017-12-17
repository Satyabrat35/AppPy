from flask_wtf import Form 
from wtforms import StringField,validators
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired , url 

class BookmarkForm(Form):
	obj = URLField('url',validators=[DataRequired(),url()])
	description = StringField('description')
