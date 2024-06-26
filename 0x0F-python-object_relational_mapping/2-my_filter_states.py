#!/usr/bin/python3
""" print states starting with capital N"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                         user=argv[1], passwd=argv[2], db=argv[3])
    mycursor = db.cursor()
    query = """ SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY
        states.id ASC"""
    mycursor.execute(query.format(argv[4]))
    query_rows = mycursor.fetchall()
    for row in query_rows:
        print(row)
    mycursor.close()
    db.close()
