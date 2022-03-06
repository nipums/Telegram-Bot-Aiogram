import sqlite3


def start(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS user_id(
        id INTEGER,
        name TEXT,
        last_name TEXT
    )""")

    connect.commit()
    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM user_id WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_list = message.chat.id
        user_list2 = message.chat.first_name
        user_list3 = message.chat.last_name
        cursor.execute(f"INSERT INTO user_id VALUES(?, ?, ?)", (user_list, user_list2, user_list3))
        connect.commit()
    else:
        pass


def delete(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM user_id WHERE id = {people_id}")
    connect.commit()


def show(message):
    connect = sqlite3.connect('users.db')
    cursor = connect.cursor()
    people_id_2 = message.chat.id
    cursor.execute(f"SELECT id FROM user_id WHERE id = {people_id_2}")
    data = cursor.fetchone()


