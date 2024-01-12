#!/usr/bin/python3
"""Py script to list all cities in database"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cities = db.cursor()
    cities.execute("SELECT * FROM `cities`\
                   INNER JOIN `states`\
                   ON states.id = cities.state_id\
                   ORDER BY cities.id\
                   ASC")
    for city in cities:
        print("({}, '{}', '{}')".format(city[0], city[2], city[4]))
    cities.close()
    db.close()
