from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)