
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def login_password():
    return render_template('login_password.html')


@app.route('/profile', methods=['POST'])
def profile():
    _login = request.form['login']
    _password = request.form['password']
    if _login == 'admin' and _password == '12345':
        return render_template('profile.html', _login=_login, _password=_password)
    else:
        return redirect(url_for('login_password'))


if __name__ == '__main__':
    app.run()
