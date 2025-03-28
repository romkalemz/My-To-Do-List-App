from flask import render_template, request, make_response
from flask_restful import Resource
from app import app, api

# Our dictionary of tasks
tasks = []

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
        if task: # Check if task is empty or an invalid input
            tasks.append({'task': task, 'status': False})
            return {'tasks': tasks}, 201 # Return JSON response with status code *Created*
        return {'error': 'Task cannot be empty'}, 400 # Return JSON response with status code *Bad Request*
    
api.add_resource(Index, '/')
api.add_resource(TaskList, '/tasks')