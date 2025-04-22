from flask import Flask , request , jsonify , render_template, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS 
from waitress import serve
from dotenv import load_dotenv
import os


app= Flask(__name__)


CORS(app)
# ------------------------------------------------
# Configuration for the database:
# ------------------------------------------------
# Here we configure Flask to use a SQLite database file named "app.db".
# SQLite is a lightweight file-based database; for production, you might choose
# something like PostgreSQL or MySQL.
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set!")
# Disable the SQLAlchemy event system which is not needed and uses extra memory.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# -----------------------------------------------
# Initialize the SQLAlchemy extension
# -----------------------------------------------
db = SQLAlchemy(app)

# Test the database connection
with app.app_context():
    try:
        db.engine.connect()
        print("Database connection successful!")
    except Exception as e:
        print(f"Error connecting to database: {e}")
        raise

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
            'created_at': self.created_at.strftime("%Y-%m-%d %H:%M:%S") if self.created_at else None,
            'due_date': self.due_date.strftime("%Y-%m-%d %H:%M:%S") if self.due_date else None
        }
    
# Create the database tables if they don't already exist
with app.app_context():
    db.create_all()
# 👇 This is the route you need
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")

        new_task = Task(title=title, description=description)
        db.session.add(new_task)
        db.session.commit()

        return redirect("/")
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return render_template("index.html", tasks=tasks)
  


# creat Task.
#  endpoint to create a new task using POst and Json input.
@app.route('/api/tasks', methods=['GET', 'POST'])
def create_task():
    if request.method == 'POST':
        try:
            if request.is_json:  # Check if it's a JSON request
                data = request.get_json()
                title = data.get('title')
                description = data.get('description')
            else:  # For regular form data
                title = request.form.get('title')
                description = request.form.get('description')

            # Debug logging
            print(f"Title: {title}, Description: {description}")

            # Validate that the required field 'title' is provided
            if title:
                new_task = Task(
                    title=title,
                    description=description,
                    completed=False,
                    created_at=datetime.utcnow()
                )
                db.session.add(new_task)
                db.session.commit()

                # Return JSON for Postman or redirect to homepage for form submission
                if request.is_json:
                    return jsonify({'message': 'Task created', 'task': new_task.to_dict()}), 201
                else:
                    return redirect(url_for('home'))
            else:
                # Title is required
                return jsonify({'error': 'Title is required'}), 400
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'error': 'Something went wrong'}), 500
    
    # Handle GET request
    if request.is_json:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return jsonify([task.to_dict() for task in tasks])
    else:
        tasks = Task.query.order_by(Task.created_at.desc()).all()
        return render_template('index.html', tasks=tasks)

@app.route('/edit-task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description')
        task.completed = True if request.form.get('completed') else False

        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit_task.html', task=task)

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
    port = int(os.getenv('PORT', 5000))
    serve(app, host= '0.0.0.0', port=5000)