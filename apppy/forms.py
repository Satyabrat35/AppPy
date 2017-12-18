from flask_wtf import Form 
from wtforms import StringField,validators
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired , url 



class BookmarkForm(Form):
    obj = URLField('The URL for your bookmark:', validators=[DataRequired(),url()])
    description = StringField('Optional description:')

    def validate(self):
        
        if not self.obj.data.startswith("http://") or\
            self.obj.data.startswith("https://"):
            self.obj.data = "http://" + self.obj.data

        if not Form.validate(self):
            return False

        if not self.description.data:
            self.description.data = self.obj.data + " is the URL"

        return True


