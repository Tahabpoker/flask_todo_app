# flask_todo_app

A simple Todo application built with Flask.
Setup Instructions

use bash\cmd\shell for the commands below

## Clone the Repository:
```bash
git clone https://github.com/Tahabpoker/flask_todo_app.git
cd flask_todo_app
```

## Create and Activate a Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install Dependencies:

```bash 
pip install -r requirements.txt
```
## Initialize the Database:
Run the create_db.py script to create the database tables using db.create_all():python create_db.py
```bash
python3 create_db.py
```

## Run the Application:
```bash
python app.py
```

## The app will be available at http://127.0.0.1:5000.
