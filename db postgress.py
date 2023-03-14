import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
try:
    # Подключение к существующей базе данных
    connection = psycopg2.connect(host='127.0.0.1',
                            user='postgres',
                            password='dfgzxcqwe45',
                            port="5432",
                            database='test')
    cursor = connection.cursor()

    # Выполнение SQL-запроса для вставки данных в таблицу
    insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 1100)"""
    cursor.execute(insert_query)
    connection.commit()
    print("1 запись успешно вставлена")
    # Получить результат
    cursor.execute("SELECT * from mobile")
    record = cursor.fetchall()
    print("Результат", record)

    print("Запрос успешно создан в PostgreSQL")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")