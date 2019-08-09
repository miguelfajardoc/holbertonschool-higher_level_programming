#!/usr/bin/python3
""" select states with python MySQLdb where coincide with the arg
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    course = db.cursor()
    course.execute(""" SELECT (cities.id), (cities.name), (states.name)
                   FROM states JOIN cities ON states.id = cities.state_id """)
    rows = course.fetchall()
    for i in rows:
        print(i)

    course.close()
    db.close()
