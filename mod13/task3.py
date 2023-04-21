import datetime
import sqlite3

sql_request_create_table_if_not_exist = """
CREATE TABLE IF NOT EXISTS table_with_birds(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       bird_name TEXT NOT NULL,
       date_when_added TEXT NOT NULL);
"""

sql_request_add_new_bird = """
INSERT INTO table_with_birds (bird_name, date_when_added) VALUES (?, ?);
"""

sql_request_check_if_exist = """
SELECT EXISTS(SELECT 1 
                FROM table_with_birds 
                WHERE bird_name = ? 
                LIMIT 1)
"""


def log_bird(cursor: sqlite3.Cursor, bird_name: str, date_time: str) -> None:
    cursor.execute(sql_request_add_new_bird, (bird_name, date_time))


def check_if_such_bird_already_seen(cursor: sqlite3.Cursor, bird_name: str) -> bool:
    result = cursor.execute(sql_request_check_if_exist, (bird_name, )).fetchone()[0]
    return bool(result)


if __name__ == "__main__":
    print("Программа помощи ЮНатам v0.1")
    name = input("Пожалуйста введите имя птицы\n> ")
    count_str = input("Сколько птиц вы увидели?\n> ")
    count = int(count_str)
    right_now = datetime.datetime.utcnow().isoformat()

    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        cursor.execute(sql_request_create_table_if_not_exist)
        if check_if_such_bird_already_seen(cursor, name):
            print("Такую птицу мы уже наблюдали!")
        else:
            log_bird(cursor, name, right_now)
            print("Мы записали вашу птицу!")
