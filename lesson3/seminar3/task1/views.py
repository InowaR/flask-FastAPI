from flask import render_template

from lesson3.seminar3.task1.models import Student, app


@app.route('/')
def students_list():
    students = Student.query.all()
    print(students)
    return render_template('students.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
