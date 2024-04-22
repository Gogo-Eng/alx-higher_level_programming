#!/usr/bin/python3

"""list all states corresponding to the argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    state_name_search = argv[4]

    db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         database=argv[3], port=3306)
    mycursor = db.cursor()

    mycursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                     (state_name_search,))
    list = mycursor.fetchall()
    for l in list:
        print(l)

    mycursor.close()
    db.close()
