import sqlite3

#Create Menu for Selection (TBD)

con = sqlite3.connect("/Users/student/Documents/GitHub - Stored Projects/Python-Projects/Patient Software/patientRecords.db")
cur = con.cursor()
print("Program has connected to the Patient Records database.")
query = "select sqlite_version();"
cur.execute(query)

result = cur.fetchall()
print("SQLite version is {}".format(result))
print("--------------------------------------------")

#Add Column to Table

# addColumn = "ALTER TABLE patient ADD COLUMN ptFamDoc varchar(32)"
# cur.execute(addColumn)

#Add Table to Database

#Delete Data

#Rename 

con.commit()
con.close()
print("--------------------------------------------")
print("******* SQLite Connection Closed *******")
