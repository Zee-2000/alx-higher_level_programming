#!usr /bin/python3
"""
Lists an argument and displays all values in the states table 
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user = sys.argv[1], passwd = sys.argv[2], 
                         db = sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * \
        FROM states \
            WHERE CONVERT(name USING LATIN1) \
                COLLATE LATIN1_General_CS = '{};'".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)