# To Do List App
A basic to-do list app with a front-end interface (using HTML, CSS, and JS) and a solid back-end API (using Python and Flask RESTful API).

# Features
- Responsive Web page
    - Check out tasks
    - Add new tasks
    - Mark tasks as "done"
    - Delete tasks
    - Animated loading spinner
- RESTful API
    - GET /tasks
    - POST /tasks
    - PUT /task/:id
    - DELETE /task/:id

# Setup
1. Clone repository:
    git clone https://github.com/romkalemz/My-To-Do-List-App.git

2. Create virtual environment (optional - to maintain dependency isolation)
- Mac & Windows command:
    python -m venv .venv

3. Activate virtual environment (optional - to maintain dependency isolation)
- Mac command:
    source .venv/bin/activate
- Windows command:
    .venv/Scripts/activate

4. Install dependencies
    pip install -r requirements.txt

5. Run Application
    python run.py

6. Visit web application on local server on any browser
    http://127.0.0.1:5000

# Aha Moments
1. Adding a validation to the front end ON TOP of the back-end is beneficial because if the front end catches a bad input before sending a request to the API, it reduces server load.
2. Flask RESTful API Resource class expects the return value to be JSON by default, so I need to wrap the rendered HTML file to proper HTTP response before returning it.
3. Adding an external library like DOMPurify allowed me to further increase security for malicious user input.

Sample API requests (using curl):
╰─± curl -X GET http://127.0.0.1:5000/tasks
{"tasks": [{"task": "Get rid of this temporary task!", "status": false}]}

╰─± curl -X POST http://127.0.0.1:5000/tasks \
-H "Content-Type: application/json" \
-d '{"task": "Walk the dog"}' 
{"tasks": [{"task": "Get rid of this temporary task!", "status": false}, {"task": "Walk the dog", "status": false}]}

╰─± curl -X PUT http://127.0.0.1:5000/task/1
{"message": "Task status updated", "task": {"task": "Walk the dog", "status": true}}

╰─± curl -X DELETE http://127.0.0.1:5000/task/0
{"message": "Task successfully delete"}

╰─± curl -X GET http://127.0.0.1:5000/tasks
{"tasks": [{"task": "Walk the dog", "status": true}]}