import csv
import sqlite3

sql_request = """
    DELETE FROM table_fees
        WHERE truck_number = ? AND timestamp = ?
"""


def delete_wrong_fees(cursor: sqlite3.Cursor, wrong_fees_file: str) -> None:
    with open(wrong_fees_file, 'r') as f:
        reader = csv.reader(f)
        wrong_fees = list(reader)[1:]
        for fee in wrong_fees:
            cursor.execute(sql_request, (fee[0], fee[1]))


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        delete_wrong_fees(cursor, "wrong_fees.csv")
