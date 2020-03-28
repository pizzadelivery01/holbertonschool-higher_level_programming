#!/usr/bin/python3
"""
lists all states with uppercase letter N form db
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute(SELECT * from states WHERE name like "N%" ORDER BY id ASC)
    rows = cursor.fetchall()
    for each in rows:
        print(each)
    cursor.close()
    db.close()
