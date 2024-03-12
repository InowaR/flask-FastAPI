from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university.db'
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.String(10), nullable=False)


@app.cli.command('init-db')
def init_db_command():
    """
    Creates the database tables.
    """
    db.create_all()
    print('Database tables created successfully!')


@app.cli.command('add-student')
def add_student_command():
    new_student = Student(
        name='Peter',
        surname='Grey',
        age=30,
        gender='m',
        group='group1'
    )
    db.session.add(new_student)
    db.session.commit()
    print("Student added successfully!")
