from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, TextField
from wtforms.validators import DataRequired

class TextForm(Form):
	text = TextField('text', validators=[DataRequired()])
