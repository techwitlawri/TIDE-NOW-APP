# TIDE NOW APP

TIDE-NOW-APP is a simple web application that provides **real-time tide data** based on user location. Built using **Flask** and **SQLite**, 
it fetches and displays tidal information using an external API, making it useful for beachgoers, sailors, and marine enthusiasts.A to-do app,that allows users to manage tasks. 
Users can add, view, update, and delete tasks, as well as mark tasks as complete

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)


live demo: https://tide-now-app.onrender.com/

 ![WhatsApp Image 2025-05-22 at 18 46 32_c56b4225](https://github.com/user-attachments/assets/d6316929-4502-43cb-84a2-7dc80eb1c418)


##  📋  Features

- 🌍 Get tide info based on your selected location
  
- 📡 Uses an external public API to fetch real-time tide data
  
- Add Tasks: Create new tasks by filling in a title and description.

- Edit Tasks: Modify the title, description, and completion status of tasks.

- Mark Tasks as Completed: Toggle a task's completion status.

- Delete Tasks: Remove tasks from the to-do list.

- 🧭Responsive UI: Optimized for mobile and desktop(Simple and clean user interface).
  
- 🔒 Lightweight and fast Flask backend
  


---

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, Bootstrap
- SQLite: Lightweight relational database for storing tasks.
- **API**: (Include the tide API you used here, e.g. [WorldTides](https://www.worldtides.info/))
- **Deployment**: (Optional – Render, Replit, etc.)

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/techwitlawri/TIDE-NOW-APP.git
   cd TIDE-NOW-APP

 2. **Create and activate a virtual environment**:
      ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

 
4. **Install dependencies**:
      ```bash
    pip install -r requirements.txt
   
5. **Run the app**:
     ```bash
   flask run

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




```
## 🧠 Lessons Learned
While building this project, I improved my understanding of:

.Consuming APIs with Python

.Rendering dynamic data using Flask and Jinja2

.Structuring a small Flask web app

## 📫 Contact
Have questions or feedback?

Email: mihenetugeoffrey@gmail.com

LinkedIn: Mmachi Ezeh https://www.linkedin.com/in/mmachilawri/

## 🌟 Support
If you found this project helpful, please consider giving it a ⭐!
