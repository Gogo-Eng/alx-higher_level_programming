#!/usr/bin/python3

"""
script that lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3], port=3306)

    mycursor = db.cursor()

    mycursor.execute(
        "SELECT cities.id, cities.name, states.name FROM cities\
              JOIN states ON cities.state_id = states.id ORDER BY\
                  cities.id ASC")
    rows = mycursor.fetchall()
    for row in rows:
        print(row)

    mycursor.close()
    db.close()
