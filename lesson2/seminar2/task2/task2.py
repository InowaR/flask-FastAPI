# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.
import os.path

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')
def photo_upload():
    message = request.args.get("message")
    if message is None:
        return render_template('image-input.html')
    return render_template('image-input.html', message=message)


@app.route('/output', methods=['POST'])
def show_photo():
    if not os.path.exists('static'):
        os.mkdir('static')
    if not os.path.exists('static/img'):
        os.mkdir('static/img')
    image = request.files['image']
    filename = secure_filename(image.filename)
    if filename is not '':
        image.save(os.path.join('static/img', filename))
        print(os.path.join('static/img', filename))
        return render_template('image-output.html', image_path=os.path.join('static/img', filename))
    return redirect(url_for('photo_upload', message='Изображение не загружено'))


if __name__ == '__main__':
    app.run()
