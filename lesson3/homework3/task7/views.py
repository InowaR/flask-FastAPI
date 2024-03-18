from flask import render_template
from werkzeug.security import generate_password_hash
from lesson3.homework3.task7.app import app, db, User, RegistrationForm


@app.route('/', methods=['GET', 'POST'])
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
        return 'success'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)