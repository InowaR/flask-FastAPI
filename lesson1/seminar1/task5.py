# Написать функцию, которая будет выводить на экран HTML страницу с таблицей,
# содержащей информацию о студентах. Таблица должна содержать следующие поля:
# "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст.


from flask import Flask, render_template

app = Flask(__name__)


_users = [{'name': 'Ivan',
           'last_name': 'Ivanov',
           'age': '34',
           'average_mark': '4.8',
           },
          {'name': 'Sergey',
           'last_name': 'Chernov',
           'age': '24',
           'average_mark': '4.2',
           },]


@app.route('/')
def page():
    return render_template('students.html', users=_users)


if __name__ == '__main__':
    app.run()
