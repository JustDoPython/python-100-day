from flask import Flask  # 引入Flask模块
from flask import request

app = Flask(__name__) # 创建一个应用

@app.route('/') 
def index():    # 定义根目录处理器
    return '<h1>Hello World!</h1>'

@app.route('/user/<name>/<age>')
def user(name, age):
    return '<h1> Hello, %s, you\'re %s years old' % (name, age)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    return request.url

@app.route('/job/')
@app.route('/work/')
def show_works():
    return 'This is works page'

@app.before_first_request
def first_quest():
    print("run before first request")

if __name__ == '__main__':
    app.run() # 启动服务