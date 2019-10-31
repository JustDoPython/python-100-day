from flask import Flask, url_for, redirect, abort  # 引入Flask模块
from flask import request
from flask_restful import Resource, Api, reqparse, fields, marshal_with


app = Flask(__name__) # 创建一个应用

api = Api(app)

class HelloRESTful(Resource):
    def get(self):
        return {'greet': 'Hello Flask RESTful!'}

api.add_resource(HelloRESTful, '/')


todos = {}

def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in todos:
        abort(404, "Todo {} doesn't exist".format(todo_id))

class TodoSample(Resource):
    def get(self, todo_id):
        # parser = reqparse.RequestParser()
        # parser.add_argument('rate', type=int, help='Rate to charge for this resource')
        # args = parser.parse_args()
        # print(args)
        abort_if_todo_doesnt_exist(todo_id)
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

class Todo3(Resource):
    def get(self):
        # Set the response code to 201 and return custom headers
        
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

class Todo(Resource):
    def get(self, todo_id):
        # Set the response code to 201 and return custom headers
        return {'task': 'Hello world'}, 201, {'Etag': 'some-opaque-string'}

api.add_resource(Todo, '/todo/<int:todo_id>/', endpoint='todo_ep2')

api.add_resource(TodoSample, '/api/todo/<string:todo_id>/')
api.add_resource(Todo3, '/api/todo3/', endpoint='todo_ep')

resource_fields = {
    'task':   fields.String,
    'uri':    fields.Url('todo_ep')
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task

        # This field will not be sent in the response
        self.status = 'active'

class Todo2(Resource):
    @marshal_with(resource_fields)
    def get(self, **kwargs):
        return TodoDao(todo_id='my_todo', task='Remember the milk')

api.add_resource(Todo2, '/api/todo_2/')

@app.route('/tep/')
def todoTest():
    print(url_for('todo_ep', todo_id=1))
    return redirect(url_for('todosample', todo_id=1))

if __name__ == '__main__':
    app.run(debug=True)

