import os
import re

t9 = {'2': 'abc',
     '3': 'def',
     '4': 'ghi',
     '5': 'jkl',
     '6': 'mno',
     '7': 'pqrs',
     '8': 'tuv',
     '9': 'wxyz'}

def read_book(filename):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    BOOK_FILE = os.path.join(BASE_DIR, filename)
    with open(BOOK_FILE) as book:
        engwords = book.read()
        engwords = re.findall('[a-z]+', engwords, flags=re.IGNORECASE)
    return engwords

def my_t9(string_t9):
    result = []
    book = read_book('engwords.txt')
    for word in book:
        if len(word) >= len(string_t9) and \
                all(w.lower() in t9[c] for w, c in zip(word, string_t9)):
            result.append(word)
    return result

if __name__ == '__main__':
    words = my_t9(input())
    print(words)