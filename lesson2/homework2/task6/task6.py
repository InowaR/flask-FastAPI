# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int(request.form['age'])

    if age < 18:
        return render_template('error.html', name=name)
    else:
        return render_template('success.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
