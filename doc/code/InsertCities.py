import json

import pymysql


def load_data():
    with open('./data/cities.json', 'r') as cities_json_file:
        cities_json_str = cities_json_file.read()
        cities_json = json.loads(cities_json_str)

    return cities_json


def insert_cities(cities_json):
    cities = cities_json.get("returnValue")

    keys = cities.keys()

    db = pymysql.Connect(host='localhost', port=3306, user='root', password='rock1204', database='GP1FlaskTpp', charset='utf8')

    cursor = db.cursor()

    for key in keys:
        # print(key)

        cursor.execute("INSERT INTO letter(letter) VALUES ('%s');" % key)

        db.commit()

        cursor.execute("SELECT letter.id FROM letter WHERE letter='%s'" % key)

        letter_id = cursor.fetchone()[0]

        print(letter_id)

        cities_letter = cities.get(key)

        for city in cities_letter:
            print(city)

            c_id = city.get('id')
            c_parent_id = city.get('parentId')
            c_region_name = city.get('regionName')
            c_city_code = city.get('cityCode')
            c_pinyin = city.get('pinYin')

            cursor.execute("INSERT INTO city(letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin) VALUES (%d, %d, %d, '%s', %d, '%s');" % (letter_id, c_id, c_parent_id, c_region_name, c_city_code, c_pinyin))

            db.commit()


if __name__ == '__main__':
    cities_json = load_data()
    insert_cities(cities_json)

