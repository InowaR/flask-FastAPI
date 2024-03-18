from flask import redirect, url_for, render_template
from werkzeug.security import generate_password_hash
from lesson3.homework3.task8.app import RegistrationForm, User, app, db


@app.route('/')
def main():
    return 'awdawd'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # hashed_password = generate_password_hash(form.password.data, method='bcrypt')
        new_user = User(name=form.name.data,
                        surname=form.surname.data,
                        email=form.email.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('main'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
