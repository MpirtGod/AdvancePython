import datetime
import os
from flask import Flask

app = Flask(__name__)
weekdays_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресения')
weekdays_ends = ('его', 'его', 'ей', 'его', 'ей', 'ей', 'его')

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = weekdays_tuple[datetime.datetime.today().weekday()]
    end = 'ей' if weekday[-1] == 'ы' else 'его'
    return f'Привет, {name}. Хорош{end} {weekday}!'

@app.route('/max_number/<path:numbers>')
def max_number(numbers):
    numbers = numbers.split('/')
    valid_numbers = []
    for number in numbers:
        if number.isdigit():
            valid_numbers.append(int(number))
        else: return 'Передано неожиданное значение'
    number = max(valid_numbers)
    return f'Максимальное переданное число: <i>{number}</i>'

@app.route('/file_previev/<int:size>/<path:relative_path>')
def file_previev(size, relative_path):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    abs_path = os.path.join(BASE_DIR, relative_path)
    with open(abs_path) as book:
        result_text = book.read(size)
    result_size = len(result_text)
    return f'<b>{abs_path}</b> {result_size}<br>{result_text}'

if __name__ == '__main__':
    app.run(Debug=True)
