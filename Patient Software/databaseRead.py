import sqlite3


con = sqlite3.connect("/Users/student/Documents/GitHub/Python-Projects/Patient Software/patientRecords.db")
cur = con.cursor()
print()
print("Database connection complete")
print()

query = "select sqlite_version();"
cur.execute(query)

result = cur.fetchall()
print("SQLite version is {}".format(result))
print()

statement = '''SELECT * FROM PATIENT'''
cur.execute(statement)

print("Patient records data: ")
output = cur.fetchall()
for row in output:
    print(row)
    con.commit()
    con.close()
    print("SQLite Connection Closed!")