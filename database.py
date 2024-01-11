import sqlite3
from collections import defaultdict

QUERIES_LIST = {
    'cars_query': """
        SELECT
            m.id as brand_id,
            m.name as brand,
            m2.id as model_id,
            m2.name as model_name
        FROM marki as m
            INNER JOIN main.models as m2 on m.id = m2.marki_id
        ORDER BY m.name, m2.id
    """,

    'transmissions_query': 'SELECT id, name FROM transmissions',

    'insert_advertisement_query': """
                            INSERT INTO advertisement (brand, model, transmission, year, phone, comment, photos) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)
                        """,

    'all_advertisements_query': """
        SELECT * FROM advertisement
    """
}

DB_NAME = 'auto.db'


def select_all(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()


def insert_all(cursor, query):
    cursor.execute(query)
    cursor.connection.commit()
    return cursor.lastrowid


def delete(cursor, query):
    cursor.execute(query)


def get_data_from_form():
    response = {
        'cars': {},
        'transmissions': {},
        'errors': ''
    }

    try:
        with (sqlite3.connect(DB_NAME) as conn):
            cursor = conn.cursor()

            for row in select_all(cursor, QUERIES_LIST['cars_query']):
                if row[1] not in response['cars']:
                    response['cars'][row[1]] = []
                else:
                    response['cars'][row[1]].append({'id': row[2], 'model': row[3]})

            response['transmissions'] = [{'id': item[0], 'title': item[1]} for item in
                                         select_all(cursor, QUERIES_LIST['transmissions_query'])]
    except Exception as e:
        response['errors'] = 'Ошибка при обращении к базе данных'

    return response


def add_new_advertisement(params: dict):
    with (sqlite3.connect(DB_NAME) as conn):
        cursor = conn.cursor()
        cursor.execute(QUERIES_LIST['insert_advertisement_query'], tuple(params.values()))


def all_advertisements():
    with (sqlite3.connect(DB_NAME) as conn):
        cursor = conn.cursor()
        return [{'ID': item[0], 'Марка': item[1], 'Модель': item[2], 'Трансмиссия': item[3], 'Год': item[4],
                 'Телефон': item[5], 'Комментарий': item[6], 'images': item[7]} for item in
                select_all(cursor, QUERIES_LIST['all_advertisements_query'])]