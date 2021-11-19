# From https://wiki.postgresql.org/wiki/Psycopg2_Tutorial

import psycopg2

# https://docs.python.org/3/tutorial/errors.html
try:
    conn = psycopg2.connect("dbname='vpdbitest' user='virtuepoker' host='localhost' password='virtuepoker'")

    cur = conn.cursor()

    cur.execute("""SELECT * from vp_user limit 1""")

    # This is now an array of arrays
    #[
    # [row1value1, row1value2, ...]
    # row2....
    #]
    rows = cur.fetchall()

    myRows = []

    for row in rows:
        myDict = {}
        myRows.append(myDict)
        for index in range(len(row)):
            # for each value of the row, we take its column name and add an entry
            # on the dictionary where the key is column name, and the value is the value from the row
            myDict[cur.description[index].name] = row[index]
        print()


    for row in myRows:
        print row


except Exception:
    print("I am unable to connect to the database")
finally:
  if (conn):
      cur.close()
      conn.close()
