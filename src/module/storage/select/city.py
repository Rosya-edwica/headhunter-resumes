import os

from storage.config import connect, TABLE_CITY
from models import City

LIMIT = os.getenv("CITY_LIMIT")
if LIMIT:
    print(f"Ограничение на количество городов: {LIMIT}")
else:
    print(f"Ограничения на количество городов НЕТ")
    
def GetCities() -> list[City]:
    cities: list[City] = []
    connection = connect()
    cursor = connection.cursor()
    query = f"SELECT * FROM {TABLE_CITY} WHERE id_hh != 0 ORDER BY id_hh LIMIT {LIMIT} "
    try:
        cursor.execute(query)
        cities = [City(*i) for i in cursor.fetchall()]
    except BaseException as err:
        print(f"Ошибка при получении городов: {err}")
    finally:
        connection.close()
    return cities
