import psycopg2
from confi import BASE


def start(message):
    connect = psycopg2.connect(BASE, sslmode="require")
    cursor = connect.cursor()

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
    connect = psycopg2.connect(BASE, sslmode="require")
    cursor = connect.cursor()
    people_id = message.chat.id
    cursor.execute(f"DELETE FROM user_id WHERE id = {people_id}")
    connect.commit()


def show(message):
    connect = psycopg2.connect(BASE, sslmode="require")
    cursor = connect.cursor()
    people_id_2 = message.chat.id
    cursor.execute(f"SELECT id FROM user_id WHERE id = {people_id_2}")
    data = cursor.fetchone()
