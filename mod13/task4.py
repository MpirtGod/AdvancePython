import sqlite3

sql_request_return_ivan_sovins_salary = """
SELECT salary
    FROM table_effective_manager
    WHERE name = 'Иван Совин'
"""

sql_request_get_employee = """
SELECT * 
    FROM table_effective_manager
    WHERE name=?
"""

sql_request_delete_employee = """
DELETE 
    FROM table_effective_manager 
    WHERE name=?
"""

sql_request_update_salary_by_name = """
UPDATE table_effective_manager 
    SET salary = ? 
    WHERE name = ?
"""


def ivan_sovin_the_most_effective(cursor: sqlite3.Cursor, name: str) -> None:
    ivan_sovin_salary = cursor.execute(sql_request_return_ivan_sovins_salary).fetchone()[0]
    employee = cursor.execute(sql_request_get_employee, (name, )).fetchone()
    if name == 'Иван Совин':
        print("Нельзя изменять з/п у эффективного менеджера!")
    elif not employee:
        print(f"Сотрудник {name} не найден в базе данных!")
    else:
        new_salary = int(employee[2] * 1.1)
        if new_salary > ivan_sovin_salary:
            cursor.execute(sql_request_delete_employee, (name,))
            print(f"Сотрудник {name} уволен!")
        else:
            cursor.execute(sql_request_update_salary_by_name, (new_salary, name))
            print(f"Зарплата сотрудника {name} была повышена до {new_salary} рублей!")


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        employee_name = input("Введите ФИО сотрудника в формате (Иванов И.И.): ")
        ivan_sovin_the_most_effective(cursor, employee_name)
