import datetime
from flask import Flask

app = Flask(__name__)
weekdays_tuple = ('Понедельника', 'Вторника', 'Среды', 'Четверга', 'Пятницы', 'Субботы', 'Воскресения')
weekdays_ends = ('его', 'его', 'ей', 'его', 'ей', 'ей', 'его')

@app.route('/hello-world/<name>')
def hello_world(name):
    weekday = weekdays_tuple[datetime.datetime.today().weekday()]
    end = 'ей' if weekday[-1] == 'ы' else 'его'
    return f'Привет, {name}. Хорош{end} {weekday}!'


if __name__ == '__main__':
    app.run(Debug=True)
