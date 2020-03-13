from flask import Flask  # 引入Flask模块
from flask import render_template # 引入Jinja2模板

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello.html', name=(1,2,3,4))

@app.route('/template/')
def template():
    name = 'Jinja2 模板引擎'
    myindex = 1
    mylist = [1,2,3,4]
    mydict = {
       'key': 'age',
       'value': '25'
    }
    mytuple = (1,2,3,4)
    return render_template('template.html', name=name, myindex=myindex, mylist=mylist, mydict=mydict, mytuple=mytuple)


if __name__ == "__main__":
    app.run()