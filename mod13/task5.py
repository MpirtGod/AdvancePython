import random
import sqlite3

countries = ['Испания', 'Франция', 'Германия', 'Италия', 'Англия', 'Нидерланды', 'Португалия', 'Бельгия', 'Аргентина', 'Бразилия', 'Россия']

sql_request_insert_teams = """
INSERT INTO uefa_commands (command_number, command_name, command_country, command_level)
    VALUES (?, ?, ?, ?)
"""

sql_request_insert_draw = """
INSERT INTO uefa_draw (command_number, group_number)
    VALUES (?, ?)
"""

def generate_test_data(cursor: sqlite3.Cursor, number_of_groups: int) -> None:
    teams = []
    for i in range(number_of_groups * 4):
        name = f'Team {i + 1}'
        country = random.choice(countries)
        if i%4 == 0:
            strength = "Сильная"
        elif i%4 == 1 or i%4 == 2:
            strength = "Средняя"
        else: strength = "Слабая"
        teams.append((i+1, name, country, strength))
    random.shuffle(teams)

    cursor.execute("DELETE FROM uefa_commands")
    cursor.executemany(sql_request_insert_teams, teams)

    groups = [[] for x in range(number_of_groups)]
    strong_teams = [team for team in teams if team[3] == "Сильная"]
    medium_teams = [team for team in teams if team[3] == "Средняя"]
    weak_teams = [team for team in teams if team[3] == "Слабая"]
    for i in range(number_of_groups):
        groups[i].append(random.choice(strong_teams))
        strong_teams.remove(groups[i][-1])
        groups[i].extend(random.sample(medium_teams, 2))
        medium_teams.remove(groups[i][-1])
        medium_teams.remove(groups[i][-2])
        groups[i].append(random.choice(weak_teams))
        weak_teams.remove(groups[i][-1])
        random.shuffle(groups[i])

    draw = [(team[0], i + 1) for i, group in enumerate(groups) for team in group]
    cursor.execute("DELETE FROM uefa_draw")
    cursor.executemany(sql_request_insert_draw, draw)


if __name__ == "__main__":
    with sqlite3.connect("hw.db") as conn:
        cursor = conn.cursor()
        groups_count = int(input('Введите количество групп (от 4 до 16): '))
        generate_test_data(cursor, groups_count)
