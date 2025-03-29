from flask import render_template, request, make_response
from flask_restful import Resource
from app import app, api

# Our dictionary of tasks
tasks = [
    { "task": "Get rid of this temperary task!", "status": False }
]

# Handling requests to root URL
class Index(Resource):
    def get(self):
        # wrap rendered html file to proper HTTP response
        # set content-type to HTML (with make_repsonse) since Flask_restful wraps in JSON-like reponse by default
        return make_response(render_template('index.html', tasks=tasks), 200)

# Handling requests to the full list of tasks
class TaskList(Resource):
    # Get list of tasks
    def get(self):
        return {'tasks': tasks}, 200 # Return JSON response with status code *OK*
    # Add a task to the list of tasks
    def post(self):
        task = request.json.get('task').strip() # Parse incoming request, return as Python dict
        if task and len(task) <= 100: # Check if task is empty or if input too long
            tasks.append({'task': task, 'status': False})
            return {'tasks': tasks}, 201 # Return JSON response with status code *Created*
        return {'error': 'Task cannot be empty'}, 400 # Return JSON response with status code *Bad Request*

# Handling requests to an individual task
class Task(Resource):
    # Update status of task (done or not done)
    def put(self, id):
        if 0 <= id < len(tasks):
            task = tasks[id]
            task['status'] = not task ['status'] # Flip the status
            return {'message': 'Task status updated', 'task': task}, 200
        return {'error': 'Task not found'}, 404 # Return JSON response with status code *Not found*


api.add_resource(Index, '/')
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/task/<int:id>')