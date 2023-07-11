# ToDo-List App

A simple and easy-to-use ToDo App built with Django. This application allows users to create, update, and delete tasks, helping them stay organized and manage their daily tasks efficiently.

## Features

- Create new tasks with a title and description
- Update existing tasks with new information
- Delete tasks when they are completed or no longer needed
- View all tasks in a list

## Installation


1. Clone the repository:

```
git clone https://github.com/younesveisi1374/todo_app.git
```

2. Change to the project directory:

```
cd todo_project
```

3. Create a virtual environment:

```
python -m venv env
```

4. Activate the virtual environment:

- On Windows:

```
env\Scripts\activate
```

- On Linux/Mac:

```
source venv/bin/activate
```

5. Install the required packages:

```
pip install -r requirements.txt
```

## Before Running:
1. First, make sure that MYSQL is installed on your system.
2. Then install the MySQL Shell for VS Code plugin in the vscode program and connect to Data Base.
3. To create the database, you must enter the following command:
```
CREATE DATABASE todo_app
```
## Remember that in order to run the program correctly, you must enter your database information in the todo_project folder in the settings.py file in the DATABASES section, which includes the database name and password.
## Running the Application

1. Run the migrations:

```
python manage.py migrate
```

2. Start the development server:

```
python manage.py runserver
```

3. Open your browser and navigate to `http://127.0.0.1:8000/` to start using the ToDo App.
