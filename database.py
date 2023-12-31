import sqlite3

def get_marki():
    """
    берет список марок машин из базы данных
    :return: список строк марок машин
    """
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('auto.db')

    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

# Выполняем SQL-запрос для выборки значений из таблицы
    select_query = "SELECT name FROM marki"
    cursor.execute(select_query)

# Получаем результат выполнения запроса
    result = cursor.fetchall()

        # Закрываем соединение с базой данных
    conn.close()
    return result

def get_models():
    """
    берет список моделей марок машин из базы данных
    :return: список строк моделей марок машин
    """
    # Устанавливаем соединение с базой данных
    conn = sqlite3.connect('auto.db')

    # Создаем курсор для выполнения SQL-запросов
    cursor = conn.cursor()

# Выполняем SQL-запрос для выборки значений из таблицы
    select_query = "SELECT name FROM models"
    cursor.execute(select_query)

# Получаем результат выполнения запроса
    result = cursor.fetchall()

        # Закрываем соединение с базой данных
    conn.close()
    return result

