#!/usr/bin/python3
""" select citites acording to an imput argument
"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    course = db.cursor()
    course.execute(""" SELECT (cities.name) FROM states JOIN cities
                   ON states.id = cities.state_id WHERE states.name = %s ;""",
                   (argv[4], ))
    rows = course.fetchall()
    leng = len(rows)
    for i in range(leng):
        print(str(rows[i][0]), end="")
        if i + 1 != leng:
            print(", ", end="")
    print("")
    course.close()
    db.close()
