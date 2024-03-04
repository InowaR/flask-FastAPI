# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.

from flask import Flask

app = Flask(__name__)


@app.route('/<text>/')
def return_number(text):
    return str(len(text))


if __name__ == '__main__':
    app.run()
