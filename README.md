# TIDE NOW APP

A simple to-do app built with Flask and SQLite.

## 📁 Project Structure

```bash
TIDE-NOW-APP/
│
├── app.py              # Main application file
├── app.db              # SQLite database
├── templates/
│   ├── index.html      # Home page
│   └── edit_task.html  # Task edit form
├── static/
│   └── style.css       # Custom CSS styling
├── requirements.txt    # Python dependencies
└── README.md           # This file!

## 🚀 Installation

To get started with the TIDE NOW app, follow the steps below.

### 1. Clone the repository


git clone https://github.com/techwitlawri/TIDE-NOW-APP.git


2. Navigate to the project directory
bash

cd TIDE-NOW-APP

3. Set up a virtual environment
If you don't have a virtual environment set up, run the following commands:



python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate
On macOS/Linux:



source venv/bin/activate

4. Install dependencies
Once the virtual environment is active, install the necessary Python dependencies:



pip install -r requirements.txt

5. Create the database
Run the following command to create the database tables:



python app.py

6. Run the application
To start the application, run:



python app.py
The app should be available at http://127.0.0.1:5000.
______________________________________________________________
📋 Features
Add Tasks: Create new tasks by filling in a title and description.

Edit Tasks: Modify the title, description, and completion status of tasks.

Mark Tasks as Completed: Toggle a task's completion status.

Delete Tasks: Remove tasks from the to-do list.

Responsive UI: Optimized for mobile and desktop.
______________________________________________________________
🛠️ Technologies Used
Flask: Python web framework used for backend development.

SQLite: Lightweight relational database for storing tasks.

HTML/CSS: Used for the frontend layout and styling.

JavaScript: Used for AJAX calls to handle API requests.
______________________________________________________________
⚙️ Setup for Development
To contribute to the development of this app:

Fork the repository to your own GitHub account.

Clone your fork to your local machine.

Create a new branch for the feature or fix you are working on.

After making changes, commit and push your changes.

Submit a Pull Request for review.
____________________________________________________________
🤝 Contributing
Fork this repository.

Create a branch (git checkout -b feature-name).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-name).

Create a new Pull Request.
______________________________________________________________
📝 License
This project is open-source and available under the MIT License.

