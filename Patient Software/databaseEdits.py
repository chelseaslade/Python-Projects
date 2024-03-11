import sqlite3

con = sqlite3.connect("/Users/student/Documents/GitHub - Stored Projects/Python-Projects/Patient Software/patientRecords.db")
cur = con.cursor()
print("Program has connected to the Patient Records database.")
query = "select sqlite_version();"
cur.execute(query)

result = cur.fetchall()
print("SQLite version is {}".format(result))
print("--------------------------------------------")

#DATABASE EDITS

addColumn = "ALTER TABLE patient ADD COLUMN ptFamDoc varchar(32)"
cur.execute(addColumn)

con.commit()
con.close()
print("--------------------------------------------")
print("******* SQLite Connection Closed *******")
