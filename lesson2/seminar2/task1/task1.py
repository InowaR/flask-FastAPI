# Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def page1():
    return render_template('page1.html')


@app.route('/page2', methods=['POST'])
def page2():
    name = request.form['form1']
    return render_template('page2.html', name=name)


if __name__ == '__main__':
    app.run()
