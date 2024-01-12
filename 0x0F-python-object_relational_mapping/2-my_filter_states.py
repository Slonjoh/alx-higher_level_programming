#!/usr/bin/python3
"""Select States Script to extract states from database table"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    states = db.cursor()
    states.execute("""SELECT * FROM states
                   WHERE BINARY `name` = '{}'
                   ORDER BY 'states.id' ASC""".format(sys.argv[4]))
    for state in states:
        print("({}, '{}')".format(state[0], state[1]))
    states.close()
    db.close()
