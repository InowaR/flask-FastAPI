# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('templates.html')


@app.route('/result', methods=['POST'])
def result():
    number = int(request.form['number'])
    square = number ** 2
    return render_template('result.html', number=number, square=square)


if __name__ == '__main__':
    app.run(debug=True)
