# Создать страницу, на которой будет форма для ввода имени
# и электронной почты
# При отправке которой будет создан cookie файл с данными
# пользователя
# Также будет произведено перенаправление на страницу
# приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка "Выйти"
# При нажатии на кнопку будет удален cookie файл с данными
# пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.


from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/welcome')
def welcome():
    name = request.cookies.get('name')
    if name is None:
        return redirect('/')
    return render_template('welcome.html', name=name)


@app.route('/set_cookie', methods=['POST'])
def set_cookie():
    name = request.form['name']
    email = request.form['email']
    resp = make_response(redirect(url_for('welcome')))
    resp.set_cookie('name', name)
    resp.set_cookie('email', email)
    return resp


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.delete_cookie('name')
    resp.delete_cookie('email')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
