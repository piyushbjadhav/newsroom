#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host=,    # your host, usually localhost
                     user=,         # your username
                     passwd=,  # your password
                     db="newsroom")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM TAB")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row[0]