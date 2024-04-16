#!/usr/bin/python3
"""
list all states
"""
import MySQLdb
import sys

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    cursor = db.cursor()

    query = "SELECT * FROM states ORDER BY id ASC"

    cursor.execute(query)
    table_row = cursor.fetchall()

    for row in table_row:
        print(row)
    cursor.close()
    db.close()
