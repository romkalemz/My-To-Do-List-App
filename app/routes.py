from flask import render_template, request, make_response
from flask_restful import Resource
from app import app, api

# Our dictionary of tasks
tasks = []

# Handling requests to root URL
class Index(Resource):
    def get(self):
        return make_response(render_template('index.html', tasks=tasks), 200)

api.add_resource(Index, '/')