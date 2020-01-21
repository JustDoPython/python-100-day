from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, InputRequired

class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[InputRequired()])
    birthday = DateField(label='Birthday', format="%Y-%m-%d", validators=[DataRequired('Invalided Date'),InputRequired()])
    about = TextAreaField(label='About')