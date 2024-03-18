import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields.simple import StringField, PasswordField, SubmitField, EmailField

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/georgiy/PycharmProjects/flask-FastAPI/reg.db'
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))


class RegistrationForm(FlaskForm):
    name = StringField('Имя', validators=[validators.DataRequired()])
    surname = StringField('Фамилия', validators=[validators.DataRequired()])
    email = EmailField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Пароль', validators=[validators.DataRequired(), validators.Length(min=8, message='Пароль должен содержать не менее 8 символов'), validators.Regexp(r'[A-Za-z0-9]+', message='Пароль должен содержать хотя бы одну букву и одну цифру')])
    password_confirm = PasswordField('Подтверждение пароля', validators=[validators.DataRequired(), validators.EqualTo('password', message='Пароли не совпадают')])
    submit = SubmitField('Зарегистрироваться')




@app.cli.command('init-db')
def init_db_command():
    db.create_all()
    print('Database tables created successfully!')
