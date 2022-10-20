#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost", port=3306, user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], charset="utf8"
    )

    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities INNER JOIN"
        " states ON cities.state_id = states.id"
        " WHERE states.name = %s ORDER BY cities.id",
        (sys.argv[4], )
    )
    end = 0
    for row in cur.fetchall():
        if end == 1:
            print(", ", end="")
        end = 1
        print(row[0], end="")
    print()
    cur.close()
    db.close()
