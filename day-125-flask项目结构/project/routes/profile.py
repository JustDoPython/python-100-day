from flask import Blueprint, render_template, redirect, url_for
from ..models.profile import Profile
from ..forms.myform import MyForm
from ..models import db

profile_bp = Blueprint('profile_bp', __name__)

@profile_bp.route('/myprofile/<id>/')
def myprofile(id):
    profile = Profile.query.get(id)  # 利用参数 id 读取数据库记录
    return render_template('profile.html', profile=profile)  # 将结果送给模板做展示

@profile_bp.route('/createprofile/', methods=('GET', 'POST'))
def createprofile():
    form = MyForm()
    if form.validate_on_submit():  # 如果表单提交了 用表单数据创建 Profile 对象
        profile = Profile()
        profile.name = form.name.data
        profile.birthday = form.birthday.data
        profile.about = form.about.data or ""

        db.session.add(profile)
        db.session.commit()
        return redirect(url_for('.myprofile', id=profile.id))  # 跳转到展示页面
    else:
        return render_template('createprofile.html', form=form)  # 显示创建页面