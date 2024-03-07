# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.
import os.path

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def page1():
    return render_template('page1.html')


@app.route('/output', methods=['POST'])
def output():
    image = request.files['image']
    filename = secure_filename(image.filename)
    image.save(os.path.join('uploads', filename))
    return render_template('page2.html', image=filename)


if __name__ == '__main__':
    app.run()