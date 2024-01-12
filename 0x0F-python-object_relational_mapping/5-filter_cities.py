#!/usr/bin/python3
"""Py script to list all cities in database by certain state name"""
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
    retstr = ""
    cities = db.cursor()
    num = cities.execute("SELECT * FROM `cities`\
                   INNER JOIN `states`\
                   ON states.id = cities.state_id\
                   WHERE states.name = %s\
                   ORDER BY cities.id\
                   ASC", (sys.argv[4],))
    for city in cities:
        retstr += str(city[2]) + ", "
    pstr = retstr.strip(" ,")
    print(pstr)
    cities.close()
    db.close()
