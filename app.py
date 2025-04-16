from flask import Flask , request , jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)

# ------------------------------------------------
# Configuration for the database:
# ------------------------------------------------
# Here we configure Flask to use a SQLite database file named "app.db".
# SQLite is a lightweight file-based database; for production, you might choose
# something like PostgreSQL or MySQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
# Disable the SQLAlchemy event system which is not needed and uses extra memory.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -----------------------------------------------
# Initialize the SQLAlchemy extension
# -----------------------------------------------
db = SQLAlchemy(app)


# -----------------------------------------------------------------------------
# Define the Task model for the to-do app:
# -----------------------------------------------------------------------------
# This model represents a task with an ID, title, and description.
# In a full to-do app, you can expand the model to include additional fields like
# "completed" status, due dates, priority, etc.

class Task(db.Model):

    # Unique identifier for each task, auto-incremented by the database.
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.String(200), nullable= False) 
    description = db.Column(db.Text, nullable= True)
    completed = db.Column(db.Boolean, default= False)

    # date and time fields

    created_at = db.Column(db.DateTime, default= datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable= True)

# Special method to return a string representation of a Task object.
    def __repr__(self):
        return f'<Task {self.title}>'
    

#  method to convert a task object to a dictionary.

    def to_dict(self):
        return{
            'id': self.id,
            'title' : self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at,
            'due_date' : self.due_date
        }
 # Create the database tables:   
with app.app_context():
    db.create_all()


@app.route('/')

def home():
    return "TIDE NOW"

# creat Task.
#  endpoint to create a new task using POst and Json input.
@app.route('/api/tasks', methods = ['POST'])
def create_task():
    # Get Json data from the incoming request.
    data = request.get_json()
    # validate that the required field 'title' is provided.
    if not data or not data.get('title'):
        return jsonify({'error': 'Title is required'}), 400

    # create a new Task instance with data from the request.
    new_task = Task(
        title = data['title'],
        description= data.get('description'),
        completed= data.get('completed', False)
    )
    # add the new task to the database session.
    db.session.add(new_task)
    db.session.commit()

    return jsonify({'message': 'Task created', 'task': new_task.to_dict()}), 201

#  list Tasks
# Endpoint to list all tasks. uses GET and returns JSON data.

@app.route('/api/tasks', methods= ['GET'])
def list_tasks():
    # Query all tasks from the database.
    tasks = Task.query.all()
    #  Convert all task to a list of dictionaries.
    tasks_list = [task.to_dict() for task in tasks]
    return jsonify(tasks_list), 200


# -----------------------------------------------------------------------------
# GET Single Task
# -----------------------------------------------------------------------------
# This endpoint retrieves a single task based on the provided task ID.
@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Query the task by ID; if not found, Flask will return a 404 error.
    task = Task.query.get_or_404(task_id)
    # Return the task as a JSON response.
    return jsonify(task.to_dict()), 200

# -----------------------------------------------------------------------------
# For testing purposes, here's an endpoint that adds a sample task:
# -----------------------------------------------------------------------------
@app.route('/add-task', methods=['GET'])
def add_task():
    # Create a new task instance with sample data.
    new_task = Task(
        title="Learn Flask",
        description="Understand how to build a web app with Flask and SQLAlchemy"
    )
    # Add the new task to the database session.
    db.session.add(new_task)
    # Commit the session to save the task in the database.
    db.session.commit()
    return "New Task Added", 201

# update Task
#  Endpoint to update an existing task.

@app.route('/api/tasks/<int:task_id>', methods= ['PUT'])
def update_task(task_id):
    # get the task from the database by ID.
    task = Task.query.get_or_404(task_id)

    # Get json data from the request
    data = request.get_json()

    # update task fields if provided in the request
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.completed = data.get('completed', task.completed)

    # Commit the Update to the database
    db.session.commit()
    return jsonify({'message': 'Task updated', 'task': task.to_dict()}), 200   

# delete Task
@app.route('/api/tasks/<int:task_id>', methods= ['DELETE'])
def delete_task(task_id):
    # get the task by id or return a 404 error
    task = Task.query.get_or_404(task_id)

    # delete the task from the session
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted'}), 200


if __name__ == '__main__':
    app.run(debug=True)