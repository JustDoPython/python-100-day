from . import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    birthday = db.Column(db.Date())
    createtime = db.Column(db.DateTime())
    about = db.Column(db.Text())