#!/usr/bin/python3
"""
list all states
"""

import MySQLdb
import sys

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password, db=database, port=3306)

    mycursor = db.cursor()
    Q1 = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    mycursor.execute(Q1)
    table = mycursor.fetchall()
    for l in table:
        print(l)

    mycursor.close()
    db.close()
