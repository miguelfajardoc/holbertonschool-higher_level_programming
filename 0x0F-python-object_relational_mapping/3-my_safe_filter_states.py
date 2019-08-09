#!/usr/bin/python3
""" select states with python MySQLdb where coincide with the arg
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    course = db.cursor()
    course.execute(""" SELECT * FROM states WHERE name=%s ORDER BY
                   id ASC ;""", (argv[4], ))
    rows = course.fetchall()
    for i in rows:
        print(i)
