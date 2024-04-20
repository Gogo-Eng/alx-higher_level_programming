#!/usr/bin/python3

import MySQLdb
from sys import argv
state_name_search = argv[4]

db = MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2], database=argv[3], prt=3306)
mycursor = db.cursor()

list = mycursor.fetchall()
for l in list:
    