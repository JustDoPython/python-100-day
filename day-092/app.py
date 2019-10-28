from flask import Flask, render_template, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length
from flask_sqlalchemy import SQLAlchemy
import os
import datetime

from flask import Flask

app = Flask(__name__)
# Linux 系统中 将 sqlite:/// 改为 sqlite:////
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.secret_key = 'abc'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique= True, index= True)

class T1(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64), unique= True, index= True)
    father_id = db.Column(db.Integer)
    flag = db.Column(db.Enum)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True) # 主键
    name = db.Column(db.String(20))
    birthday = db.Column(db.Date())
    createtime = db.Column(db.DateTime())
    about = db.Column(db.Text())

class MyForm(FlaskForm):
    name = StringField(label='Name', validators=[InputRequired()])
    birthday = DateField(label='Birthday', format="%Y-%m-%d", validators=[DataRequired('Invalided Date'),InputRequired()])
    about = TextAreaField(label='About')

@app.route('/myprofile/<id>/')
def myprofile(id):
    profile = Profile.query.get(id)  # 利用参数 id 读取数据库记录
    return render_template('profile.html', profile=profile)  # 将结果送给模板做展示

@app.route('/createprofile/', methods=('GET', 'POST'))
def createprofile():
    form = MyForm()
    if form.validate_on_submit():  # 如果表单提交了 用表单数据创建 Profile 对象
        profile = Profile()
        profile.name = form.name.data
        profile.birthday = form.birthday.data
        profile.about = form.about.data or ""

        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('myprofile', id=profile.id))  # 跳转到展示页面
    else:
        return render_template('createprofile.html', form=form)  # 显示创建页面

if __name__ == '__main__':

    # 如果数据库为空时 初始化一条记录
    if Profile.query.count() == 0:
        profile = Profile()
        profile.name = "Tiger"
        # Date 和 DateTime 类型属性，必须接受 Python datetime 对象
        profile.birthday = datetime.datetime(2001, 10, 1)
        profile.createtime = datetime.datetime.now()
        profile.about = 'My name is Tiger, come from Beijing China.'
        db.session.add(profile)
        db.session.commit()

    app.run(debug=True)
    

"""
Flask Shell 中的代码

from app import Profile # Profile 是在应用中定义的模型
from app import db
import datetime

# 新增
# 创建一个 Profile 实例
profile = Profile()
profile.name = "Tiger"
# Date 和 DateTime 类型属性，必须接受 Python datetime 对象
profile.birthday = datetime.datetime(2001, 10, 1)
profile.createtime = datetime.datetime.now()
profile.about = 'My name is Tiger, come from Beijing China.'

db.session.add(profile)  # 将变化添加
db.session.commit() # 将变化提交

# 查询
profile = Profile.query.first()  # 查询出 profile 表中第一条记录
profile.name  # Tiger
profile.birthday # 2001-10-01 00:00:00
profile.about  # My name is Tiger, come from Beijing China.
profiles = Profile.query.all()  # 查询出所有记录，返回 Profile 实例列表
profile_count = Profile.query.count()  # 记录条数
profile = Profile.query.get(1)  # 获取主键为 1 的记录
profile = Profile.filter_by(name='Tiger').first()  # 查询 name 等于 Tiger 的记录集中第一条记录
profiles = Profile.filter(Profile.name != 'Tiger').all()  # 查询 name 不等于 Tiger 的所有记录

# 更新
profile = Profile.query.get(1)  # 查询出ID为 1 的记录
profile.about = profile.about + ' I like coding~'  # 在简介中添加些内容
db.session.commit()  # 必须调用提交，否则将不会被更新到数据库

# 删除
profile = Profile.query.get(1)  # 查询出ID为 1 的记录
db.session.delete(profile)  # 删除记录
db.session.commit()  # 提交变更
"""
