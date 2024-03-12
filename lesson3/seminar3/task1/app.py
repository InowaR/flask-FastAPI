from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/georgiy/PycharmProjects/flask-FastAPI/university.db'
db = SQLAlchemy(app)


class Student(db.Model):
    __tablename__ = "Students"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(1))
    group = db.Column(db.String(255))
    faculty_id = db.Column(db.Integer, db.ForeignKey("Faculties.id"))
    faculty = db.relationship("Faculty", foreign_keys=[faculty_id])


class Faculty(db.Model):
    __tablename__ = "Faculties"

    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(255))


@app.cli.command('init-db')
def init_db_command():
    db.create_all()
    print('Database tables created successfully!')


@app.cli.command('add-student')
def add_student_command():
    new_student = Student(
        name='Alex',
        surname='Black',
        age=30,
        gender='m',
        group='group1',
        faculty_id='1'
    )
    new_faculty = Faculty(
        faculty_name='engineer'
    )

    db.session.add(new_student)
    db.session.add(new_faculty)
    db.session.commit()
    print("Student added successfully!")
