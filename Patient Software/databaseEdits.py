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

# #Test Add Data
# ptFName = "Alice"
# ptLName = "McClean"
# ptDOB = "1993, 04, 20"
# ptMCP = "234-235-134"
# ptStAddress = "3 Block St"
# ptCity = "Mile City"
# ptPostalCode = "A3F 4F3"
# ptProvince = "ON"
# ptFamDoc = "Dr. Tree"

# cur.execute("INSERT INTO PATIENT (FNAME, LNAME, ptDOB, ptMCP, ptStAddress, ptCity, ptPostalCode, ptProvince, ptFamDoc) VALUES (?,?,?,?,?,?,?,?,?);",(ptFName, ptLName, ptDOB, ptMCP, ptStAddress, ptCity, ptPostalCode, ptProvince, ptFamDoc))

#Add Table to Database

#Delete Data

#Rename 

con.commit()
con.close()
print("--------------------------------------------")
print("******* SQLite Connection Closed *******")
