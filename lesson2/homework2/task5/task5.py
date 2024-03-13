# Создать страницу, на которой будет форма для ввода двух
# чисел и выбор операции (сложение, вычитание, умножение
# или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление
# результата выбранной операции и переход на страницу с
# результатом.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']
    res = 0
    if operation == '+':
        res = num1 + num2
    elif operation == '-':
        res = num1 - num2
    elif operation == '*':
        res = num1 * num2
    elif operation == '/':
        try:
            res = num1 / num2
        except ZeroDivisionError:
            res = 0

    return render_template('result.html', operation=operation, result=res)


if __name__ == '__main__':
    app.run(debug=True)
