import pymysql
import psycopg2

def insert_cities():
    con = pymysql.connect(host='83.220.175.75', port=3306, user='edwica_root', password="b00m5gQ40WB1", database="edwica")

    cities = []
    with con.cursor() as cur:
        query = "SELECT id_hh, id_edwica, name, id_rabota_ru FROM h_city"
        cur.execute(query)
        cities = [i for i in cur.fetchall()]

    con.close()

    conn = psycopg2.connect(database="resumes", user="postgres", password="admin", host="127.0.0.1", port=5432)
    cur = conn.cursor()
    cur.executemany("INSERT INTO city(id_hh, id_edwica, name, id_rabota_ru) VALUES (%s, %s, %s, %s)", [i for i in cities])
    conn.commit()
    conn.close()


def insert_postions():
    con = pymysql.connect(host='83.220.175.75', port=3306, user='edwica_root', password="b00m5gQ40WB1", database="edwica")

    positions = []
    with con.cursor() as cur:
        query = """SELECT position_id, parent_id, level, h_position.name, professional_area.name, other_names FROM h_position
        LEFT JOIN professional_area ON professional_area.id=area_id  """
        cur.execute(query)
        positions = [i for i in cur.fetchall()]

    con.close()

    conn = psycopg2.connect(database="resumes", user="postgres", password="admin", host="127.0.0.1", port=5432)
    cur = conn.cursor()
    print(positions[0])
    cur.executemany("INSERT INTO position(id, parent_id, level, title, prof_area, other_names) VALUES (%s, %s, %s, %s, %s, %s)", [i for i in positions])
    conn.commit()
    conn.close()


if __name__ == "__main__":
    insert_postions()
    insert_cities()
