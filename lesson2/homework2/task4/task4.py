# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.


from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('templates.html')


@app.route('/result', methods=['POST'])
def result():
    text = request.form['text']
    word_count = len(text.split())
    return render_template('result.html', word_count=word_count)


if __name__ == '__main__':
    app.run(debug=True)
