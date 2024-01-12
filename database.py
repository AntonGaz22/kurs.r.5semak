import sqlite3
from collections import defaultdict

QUERIES_LIST = {
    '''словарь запросов'''
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
'''Эта переменная определяет имя файла базы данных SQLite (auto.db) '''


def select_all(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()
'''создаем функцию, которая выполняет запрос SELECT с помощью предоставленного курсора и возвращает все результаты, извлеченные из базы данных'''


def insert_all(cursor, query):
    cursor.execute(query)
    cursor.connection.commit()
    return cursor.lastrowid
'''cоздаем функцию, которая выполняет запрос INSERT с использованием предоставленного курсора, фиксирует изменения в базе данных и возвращает идентификатор последней вставленной строки'''


def delete(cursor, query):
    cursor.execute(query)
'''создаем функцию, которая выполняет запрос на удаление с помощью предоставленного курсора'''


def get_data_from_form():
    '''создаем функцию для извлечения данных из базы данных'''
    response = {
        'cars': {},
        'transmissions': {},
        'errors': ''
        '''создаем словарь для хранения извлеченных данных'''
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
    '''Внутри блока try-except функция подключается к базе данных SQLite (DB_NAME), создает курсор и выполняет запросы для извлечения данных об автомобиле и трансмиссии'''

    return response
'''создаем функцию для возврата заполненного словаря'''


def add_new_advertisement(params: dict):
    with (sqlite3.connect(DB_NAME) as conn):
        cursor = conn.cursor()
        cursor.execute(QUERIES_LIST['insert_advertisement_query'], tuple(params.values()))
'''создаем функцию add_new_advertisement, которая принимает параметры словаря в качестве входных данных '''


def all_advertisements():
    with (sqlite3.connect(DB_NAME) as conn):
        cursor = conn.cursor()
        return [{'ID': item[0], 'Марка': item[1], 'Модель': item[2], 'Трансмиссия': item[3], 'Год': item[4],
                 'Телефон': item[5], 'Комментарий': item[6], 'images': item[7]} for item in
                select_all(cursor, QUERIES_LIST['all_advertisements_query'])]
'''создаем функцию all_advertisements, которая заполняет данные в базу данных'''