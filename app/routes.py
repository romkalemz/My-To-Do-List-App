from flask import render_template, request, make_response
from flask_restful import Resource, fields, marshal_with
from app import api, db
from app.models import TaskModel

# Handling requests to root URL
class Index(Resource):
    def get(self):
        tasks = TaskModel.query.all() # Call database for the list of tasks
        tasksDict = [task.to_dict() for task in tasks] # Convert database object to dictionary
        # wrap rendered html file to proper HTTP response
        # set content-type to HTML (with make_repsonse) since Flask_restful wraps in JSON-like reponse by default
        return make_response(render_template('index.html', tasks=tasksDict), 200) # Return HTML template with tasks

# Handling requests to the full list of tasks
class TaskList(Resource):
    # Get list of tasks
    def get(self):
        tasks = TaskModel.query.all()
        tasksDict = [task.to_dict() for task in tasks]
        return {'tasks': tasksDict}, 200 # Return JSON response with status code *OK*
    # Add a task to the list of tasks
    def post(self):
        task = request.json.get('task').strip() # Parse incoming request, return as Python dict (then into string)
        if task and len(task) <= 100: # Check if task is empty or if input too long
            new_task = TaskModel(task=task)
            db.session.add(new_task)
            db.session.commit()
            return {'task': new_task.to_dict()}, 201 # Return JSON response with status code *Created*
        return {'error': 'Task cannot be empty'}, 400 # Return JSON response with status code *Bad Request*

# Handling requests to an individual task
class Task(Resource):
    # Update status of task (done or not done)
    def put(self, id):
        task = TaskModel.query.get(id) # Grab the task at the [id] position
        if task:
            task.status = not task.status # Flip the status
            db.session.commit()
            return {'message': 'Task status updated', 'task': task.to_dict()}, 200
        return {'error': 'Task not found'}, 404 # Return JSON response with status code *Not found*

    def delete(self, id):
        task = TaskModel.query.get(id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return {'message': 'Task successfully delete', 'id': id}, 200
        return {'error': 'Task not found'}, 404

api.add_resource(Index, '/')
api.add_resource(TaskList, '/tasks')
api.add_resource(Task, '/task/<int:id>')