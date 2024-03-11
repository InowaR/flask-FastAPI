# Создать страницу, на которой будет форма для ввода логина и пароля,
# при нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля
# и переход на страницу приветствия пользователя или страницу с ошибкой.


import secrets
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()


@app.route('/')
def login_password():
    _login = session.get('_login')
    print(_login)
    return render_template('login_password.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    _login = request.form['login']
    _password = request.form['password']
    if _login == 'admin' and _password == '12345':
        flash('Вы успешно зарегистрировались!', category='success')
        return render_template('profile.html', _login=_login)
    else:
        flash('Неверный логин или пароль', category='error')
        return redirect(url_for('login_password'))


if __name__ == '__main__':
    app.run()
