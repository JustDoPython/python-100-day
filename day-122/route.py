from flask import Blueprint, request
from model import User, db

route_bp = Blueprint('route_bp', __name__)

@route_bp.route('/')
def index():
    return "Hello world!"

@route_bp.route('/login/', methods=['POST'])
def login():
    username = request.form['username']
    user = User.query.filter_by(name=username).first()
    if user is not None:
        return {
            'success': True,
            'username': user.name,
            'userid': user.id
        }
    else:
        return {
            'success': False,
            'emsg': 'No Found User'
        }

@route_bp.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = User()
        user.name = request.form['username']
        db.session.add(user)
        db.session.commit()

        return {
            'success': True
        }
    else:
        return {
            'success': False,
            'emsg': 'Method Not Allowed'
        }
