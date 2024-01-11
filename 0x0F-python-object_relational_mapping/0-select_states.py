#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Check if the correct number of arguments is provided
    """
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    """
    Extracting MySQL connection details from command line arguments
    """
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    """
    Establish a MySQL connection
    """
    try:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database,
            charset="utf8"
        )
        cursor = conn.cursor()

        # Execute the SELECT query and fetch results
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cursor.fetchall()

        # Display results
        for row in query_rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error connecting to MySQL: {}".format(e))
    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if conn:
            conn.close()
