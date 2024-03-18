from flask import redirect, url_for, render_template, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from lesson3.homework3.task8.app import RegistrationForm, User, app, db, LoginForm, csrf


@app.route('/')
def profile():
    if 'email' not in session or 'password' not in session:
        return redirect(url_for('login'))
    email = session.get('email')
    return render_template('profile.html', email=email)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user.name)
        if user and check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data
            session['password'] = form.password.data
            return redirect(url_for('profile'))
        flash('Неверный логин или пароль.', category='error')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        new_user = User(name=form.name.data,
                        surname=form.surname.data,
                        email=form.email.data,
                        password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('profile'))
    return render_template('register.html', form=form)


@app.route('/logout', methods=['POST'])
@csrf.exempt
def logout():
    session.clear()
    return redirect(url_for('profile'))


if __name__ == '__main__':
    app.run(debug=True)
