import os
from flask import Flask

app = Flask(__name__)
storage = {}

@app.route('/add/<int:date>/<int:number>')
def add(date, number):
    if len(str(date)) == 8:
        date = str(date)
        storage.setdefault(date[:4], {}).setdefault(date[4:6], 0)
        storage[date[:4]][date[4:6]] += number
        return f'Сохранено!'

@app.route('/calculate/<int:year>')
def calculate_year(year):
    months = storage[str(year)]
    summ = sum([number for key, number in months.items()])
    return f'Суммарные траты за указанный год: {summ}'

@app.route('/calculate/<int:year>/<int:month>')
def calculate_month(year, month):
    return f'Суммарные траты за указанные год и месяц: {storage[str(year)][str(month)]}'

if __name__ == '__main__':
    app.run(debug=True)
