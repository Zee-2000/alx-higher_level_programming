#!usr/bin/python3
"""_
    Lists all the states that starts with upper N_
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.agrv[2], 
                         db = sys.argv[3], port = 3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM STATES \
        WHERE CONVERT(`name USING LATIN1)\
            COLLATE LATIN1_General_CS\
                LIKE N%;")
    states = cur.fetchall()
    for state in states:
        print(state)