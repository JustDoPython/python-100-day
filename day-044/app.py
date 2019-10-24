from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from wtforms import StringField, DateField, RadioField, SelectMultipleField
from wtforms.validators import DataRequired, InputRequired, Length
from werkzeug import secure_filename
import os
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.secret_key = 'abc'
app.config['UPLOAD_FOLDER'] = './upload'

class MyForm(FlaskForm):
    name = StringField(label='姓名', validators=[InputRequired()])
    city = StringField('城市', validators=[Length(min=4, max=25, message='输入的长度不符合要求')])
    birthday = DateField(label='生日', format="%Y-%m-%d", validators=[DataRequired('日期格式不正确')])
    gender = RadioField(label='性别', choices=[(1, 'male'), (2, 'female')])
    interest = SelectMultipleField(label='兴趣', choices=[(1, 'Football'), (2, 'Movies'), (3, 'Reading')])

class PhotoForm(FlaskForm):
    photo = FileField('上传照片')

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    form = PhotoForm()
    filepath = None
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        file = form.photo.data
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save( filepath )
    else:
        filename = None
    return render_template('upload.html', form=form, filename= filename)

@app.route('/success/')
def success():
    return "Welcome"

@app.route('/bootstrap/')
def bootstrap():
    form = MyForm()
    return render_template('bootstrap.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)