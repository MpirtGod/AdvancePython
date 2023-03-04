import datetime
import os
import re
from flask import Flask
import random

app = Flask(__name__)
cars_names = ['Chevrolet', 'Renault', 'Ford', 'Lada']
cats_names = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
count = 0

def read_txt(filename):
    global war_and_peace
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)

    with open(BOOK_FILE) as book:
        war_and_peace = book.read()
        war_and_peace = re.findall('[a-zа-яё]+', war_and_peace, flags=re.IGNORECASE)
    return war_and_peace

war_and_peace = read_txt('war_and_peace.txt')

@app.route('/hello_world')
def hello_world():  # put application's code here
    return 'Привет, мир!'

@app.route('/cars')
def cars():  # put application's code here
    global cars_names
    return ', '.join(cars_names)

@app.route('/cats')
def cats():  # put application's code here
    global cats_names
    return random.choice(cats_names)

@app.route('/get_time/now')
def now():
    current_time = datetime.datetime.now()
    return f'Точное время: {current_time}'

@app.route('/get_time/future')
def future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(seconds=3600)
    return f'Точное время через час будет {current_time_after_hour}'

@app.route('/get_random_word')
def get_random_word():
    global war_and_peace
    return random.choice(war_and_peace)

@app.route('/counter')
def counter():
    global count
    count += 1
    return str(count)

if __name__ == '__main__':
    app.run()
