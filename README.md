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
- Persistence with Database from SQLite

# Setup

0. Make sure to have python and GIT installed!

1. CLONE REPOSITORY
   git clone https://github.com/romkalemz/My-To-Do-List-App.git

2. CREATE VIRTUAL ENVIRONMENT (optional - to maintain dependency isolation)

- Mac & Windows command: (on Windows I used Git Bash instead of PowerShell)
  python -m venv .venv

3. ACTIVATE VM (optional - to maintain dependency isolation)

- Mac command:
  source .venv/bin/activate
- Windows command:
  source .venv/Scripts/activate

4. INSTALL DEPENDENCIES
   pip install -r requirements.txt

5. INITIALIZE DATABASE
   python init_db.py

6. RUN APP
   python run.py

7. VISIT WEB-PAGE
   http://127.0.0.1:5000
   OR if that doesnt work try
   http://localhost:5000

# Aha Moments

1. Adding a validation to the front end ON TOP of the back-end is beneficial because if the front end catches a bad input before sending a request to the API, it reduces server load.
2. Flask RESTful API Resource class expects the return value to be JSON by default, so I need to wrap the rendered HTML file to proper HTTP response before returning it.
3. Adding an external library like DOMPurify allowed me to further increase security for malicious user input.
