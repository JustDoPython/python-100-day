from flask import Flask, session, render_template, url_for, redirect
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = '!secret'

oauth = OAuth(app)


app.config["GITHUB_CLIENT_ID"] = '55ffa..<省略>...9e1fb3a'
app.config["GITHUB_CLIENT_SECRET"] = '692317a38d0..<省略>...d63f2d9f8c'
app.config["GITHUB_AUTHORIZE_URL"] = 'https://github.com/login/oauth/authorize'
app.config["GITHUB_ACCESS_TOKEN_URL"] = 'https://github.com/login/oauth/access_token'
app.config["GITHUB_API_BASE_URL"] = 'https://api.github.com'
app.config["GITHUB_AUTHORIZE_PARAMS"] = {
    'scope': 'user repo'
}
oauth.register('Github')

github = oauth.Github

@app.route('/')
def homepage():
    user = session.get('user')
    print('auth user:', user)
    return render_template('home.html', user=user)


@app.route('/login')
def login():
    redirect_uri = url_for('auth', _external=True)
    return github.authorize_redirect(redirect_uri)

@app.route('/auth/redirect')
def auth():
    token = github.authorize_access_token()
    print('auth token:', token)
    user = github.get('user').json()
    print('auth user:', user)
    session['user'] = user
    return redirect('/')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')

if __name__ == '__main__':
    app.run()