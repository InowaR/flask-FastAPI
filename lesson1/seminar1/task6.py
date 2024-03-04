# Написать функцию, которая будет выводить на экран HTML страницу с блоками новостей.
# Каждый блок должен содержать заголовок новости, краткое описание и дату публикации.
# Данные о новостях должны быть переданы в шаблон через контекст.

from flask import Flask, render_template

from datetime import datetime

app = Flask(__name__)

_news = [{'title': 'Футбол',
          'description': 'Кубок мира',
          'date': datetime.now().strftime("%d, %m, %Y")
          },
         {'title': 'Политика',
          'description': 'Новости',
          'date': datetime.now().strftime("%d, %m, %Y")
          },]


@app.route('/')
def page():
    return render_template('news.html', news=_news)


if __name__ == '__main__':
    app.run()
