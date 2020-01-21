from flask import Blueprint
from flask import render_template

home_bp = Blueprint('home_bp', __name__)
print("routes/home.py __name__ is :", __name__)
@home_bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')