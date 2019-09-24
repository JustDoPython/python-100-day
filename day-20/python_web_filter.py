from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', 
    name=" taiyangxue ",
    html='<b>Bob</b>')

@app.route('/filter')
def filter():
    return render_template('filter.html', data={
        'name': 'Bob',
        'age': 23,
        'city': 'Beijing'
    }, data1=False, name=None,
    list=[1,2,3,4])


# 定义过滤器函数
def mylen(arg):# 实现一个可以求长度的函数
    return len(arg)
def interval(test_str, start, end): # 返回字符串中指定区间的内容
    return test_str[int(start):int(end)]

# 注册过滤器
env = app.jinja_env
env.filters['mylen'] = mylen
env.filters['interval'] = interval

# 视图函数
@app.route('/myfilter')
def myfilter():
    return render_template('myfilter.html', phone='13300000000')

# 控制结构 if-else
@app.route('/hello2/<name>/<gender>')
def hello2(name, gender):
    return render_template('hello2.html', name=name, gender=gender)

# 控制结构 for
@app.route('/names')
def names():
    return render_template('for.html', names=['Lily', 'Bob', 'Tom', 'Jan'])

# 宏
@app.route('/marco')
def marco():
    return render_template('mymarco.html', names=['Lily', 'Bob', 'Tom', 'Jan'])

# 继承
@app.route('/hello3')
def hello3():
    return render_template('hello3.html')
    
if __name__ == '__main__':
    app.run(debug=True) 