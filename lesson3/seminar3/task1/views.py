from flask import render_template

from lesson3.seminar3.task1.app import Student, Faculty, app


@app.route("/")
def index():
    students_data = Student.query.all()
    faculties_data = Faculty.query.all()
    return render_template("students.html", students=students_data, faculties=faculties_data)


if __name__ == '__main__':
    app.run(debug=True)
