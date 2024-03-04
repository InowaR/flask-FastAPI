# Добавьте две дополнительные страницы в ваше веб-приложение:
# страницу "about" и страницу "contact".
#
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму


from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello'


@app.route('/about/')
def about():
    return 'about.html'


@app.route('/contact/')
def contact():
    return 'contact.html'


@app.route('/<int:num1>/<int:num2>/')
def return_number(num1, num2):
    return str(num1 + num2)


if __name__ == '__main__':
    app.run()
