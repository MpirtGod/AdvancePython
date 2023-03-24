import itertools
import json
import operator
import os
import re
from collections import Counter


def read_book(filename) -> list[dict]:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)
    with open(BOOK_FILE) as book:
        logs = book.readlines()
        logs = [json.loads(log) for log in logs]
    return logs


logs = read_book('skillbox_json_messages.log')


def group_by_level_and_print(logs):
    for level, logs_list in itertools.groupby(logs,key=lambda d: d['level']):
        print(f'{level}: {len(list(logs_list))}')

def group_by_time_and_print_max_logs(logs):
    logs_by_hours = {}
    for time, logs_list in itertools.groupby(logs, key=lambda d: d['time'][:2]):
        logs_by_hours[time] = len(list(logs_list))
    max_hour = max(logs_by_hours.items(), key=operator.itemgetter(1))[0]
    print(f'Больше всего логов было в {max_hour} часов')


def print_level_logs_in_period(logs, level):
    result = [log for log in logs if log['level'] == level and bool(re.search('05:[0-1]', log['time']))]
    print(f'Логов уровня {level} в период с 05:00:00 по 05:20:00 было: {len(result)}')


def print_count_logs_contains_word(logs, word):
    result = [log for log in logs if word in str(log)]
    print(f'Cообщений, которые содержат слово "{word}": {len(result)}')


def print_most_common_word_in_level(logs, search_level):
    filtered_logs = [log for log in logs if log['level'] == search_level]
    words_list = [log['message'].split() for log in filtered_logs]
    counter = Counter([item for sublist in words_list for item in sublist]).most_common()[0]
    print(f'Самое частовстречаемое слово в сообщениях уровня {search_level}: "{counter[0]}", встречалось {counter[1]} раз')



if __name__ == '__main__':
    print('Подзадача 1:')
    group_by_level_and_print(logs)
    print('Подзадача 2:')
    group_by_time_and_print_max_logs(logs)
    print('Подзадача 3:')
    print_level_logs_in_period(logs, 'CRITICAL')
    print('Подзадача 4:')
    print_count_logs_contains_word(logs, 'dog')
    print('Подзадача 5:')
    print_most_common_word_in_level(logs, "WARNING")

