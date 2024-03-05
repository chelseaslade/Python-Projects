#Patient Registration Software Dev
#Start Date: February 16
#Author: Chelsea Slade
#Python Projects V1.

#Import Libraries
import datetime
import sqlite3
from sqlite3 import Error

#SQL Lite 3 Database


try: 
  con = sqlite3.connect("patientRecords.db")
  cur = con.cursor()
  print()
  print("Database connection complete")
  print()

  query = "select sqlite_version();"
  cur.execute(query)

  result = cur.fetchall()
  print("SQLite version is {}".format(result))
  print()

  patientTable = '''CREATE TABLE PATIENT(FNAME VARCHAR(255), LNAME VARCHAR(255)) ;'''
  cur.execute(patientTable)

  cur.execute('''INSERT INTO PATIENT (FNAME, LNAME) VALUES ("John", "Smith")''')
  print("Data inserted in the table: ")
  data=cur.execute('''SELECT * FROM PATIENT''')
  for row in data:
     print(row)


except sqlite3.Error as error:
   print("Error occured -", error)

finally: 
   if con:
      con.commit()
      con.close()
      print("SQLite Connection Closed!")


#Constants

#Main Program Loop
continueProg = True
while continueProg == True: 

#User Inputs
  ptFirstName = input("Enter patients first name: ").title()
  ptLastName = input("Enter patients last name: ").title()
  ptDOB = input("Enter the patients date of birth (YEAR/MONTH/DAY, ex. 2000/01/30): ")
  ptMCP = input("Enter the patients MCP number: ")
  ptStAddress = input("Enter the patients street address: (Ex. 99 Hospital Road) ").title()
  ptCity = input("Enter the patients city: ").title()
  ptPostalCode = input("Enter the patients postal code: ").upper()
  ptFamDoc = input("Enter the patients family doctor: ").title()
  

#Calculations

#Patient ID #: 

#Output
  print()
  print(f"Patient Name: {ptFirstName} {ptLastName} ")
  print(f"Patient Date of Birth: {ptDOB} ")
  print(f"Patient Address: {ptStAddress} {ptCity} {ptPostalCode} ")
  print(f"Patient MCP #: {ptMCP} ")
  print(f"Patient Family Doctor: {ptFamDoc} ")
  print()


#Housekeeping