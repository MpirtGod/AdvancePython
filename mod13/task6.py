from datetime import datetime, timedelta
import sqlite3
import random

working_days_count = 366
employees_on_one_day = 10
employees_count = 366
days_everyone_should_work = working_days_count * employees_on_one_day // employees_count


week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
sports = ['футбол', "хоккей", "шахматы","SUP сёрфинг", "бокс", "Dota2", "шах-бокс"]


sql_request_insert_employee = """
INSERT INTO table_friendship_schedule (employee_id, date)
    VALUES (?,?)
"""


def update_work_schedule(cursor: sqlite3.Cursor) -> None:

    cursor.execute("DELETE FROM table_friendship_schedule")
    employees = cursor.execute("SELECT id, preferable_sport FROM table_friendship_employees").fetchall()
    worker_days = {employee[0]:0 for employee in employees}
    curr_day = datetime.strptime("2020-01-01", "%Y-%m-%d")
    workers_on_day = {curr_day + timedelta(days=i): 0 for i in range(366)}
    for day, emp in workers_on_day.items():
        week_day = week_days[day.weekday()]
        for id, sport in employees:
            if week_day == week_days[sports.index(sport)]:
                continue
            if worker_days[id] != days_everyone_should_work + 1:
                cursor.execute(sql_request_insert_employee, (id, str(day)[:10]))
                worker_days[id] += 1
                workers_on_day[day] += 1
                if workers_on_day[day] == 10:
                    break


if __name__=="__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        update_work_schedule(cursor)