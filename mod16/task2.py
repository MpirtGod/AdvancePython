import sqlite3


if __name__ == "__main__":
    with open('task2_1.sql', 'r') as sql_file:
        sql_script: str = sql_file.read()

    with sqlite3.connect('hw.db') as conn:
        cursor: sqlite3.Cursor = conn.cursor()
        result = cursor.executescript(sql_script).fetchall()
        print(result)
        conn.commit()