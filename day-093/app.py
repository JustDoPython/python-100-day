from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

# User 类，用于模拟用户实体
class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

# User 实体集合，用于模拟用户对象的缓存
users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

# 获取认证的回调函数，从 request 中得到登录凭证，返回凭证所代表的 用户实体
def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

# 通过 token 获得认证主体的回调函数
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)  # 用 JWT 初始化应用

@app.route('/protected', methods= ["GET", "POST"])  # 定义一个 endpoint
@jwt_required()  # 声明需要 token 才能访问
def protected():
    return '%s' % current_identity  # 验证通过返回 认证主体

if __name__ == '__main__':
    app.run()


"""
命令行代码
>>> from authlib.jose import jwt
>>> header = {'alg': 'HS256'}
>>> payload = {'iss': 'Authlib', 'sub': '123', 'name': 'bob'}
>>> secret = '123abc.'
>>> token = jwt.encode(header, payload, secret)
>>> print(token)
b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
eyJpc3MiOiJBdXRobGliIiwic3ViIjoiMTIzIiwibmFtZSI6ImJvYiJ9.
cBo6e7Uss5__16mlqZECjHJSKJDdyisevDP5cUGvJms'

>>> claims = jwt.decode(token, secret)
>>> print(claims)
{'iss': 'Authlib', 'sub': '123', 'name': 'bob'}
>>> print(claims.header)
{'alg': 'HS256', 'typ': 'JWT'}
>>> claims.validate()
"""