#Patient Registration Software Dev
#Start Date: February 16
#Author: Chelsea Slade
#Python Projects V1.

#Import Libraries
import datetime
import sqlite3
from sqlite3 import Error

#Constants


#Welcome to the Program Message
print()
print("Welcome to the Patient Registration Program.")
print()
print("--------------------------------------------")

#SQL Lite 3 Database
try: 
  con = sqlite3.connect("/Users/student/Documents/GitHub/Python-Projects/Patient Software/patientRecords.db")
  cur = con.cursor()
  print("Program has connected to the Patient Records database.")
  query = "select sqlite_version();"
  cur.execute(query)

  result = cur.fetchall()
  print("SQLite version is {}".format(result))
  print("--------------------------------------------")


  #Main Program Loop
  continueProg = True
  while continueProg == True: 

  #User Inputs
    print("To exit the program, type END in any user input.")
    print("Enter patient information as indicated below: ")
    print()

    while True:
      ptFirstName = input("Enter patients first name: ").title()
      if ptFirstName.upper() == "END":
         continueProg = False
         break
      elif ptFirstName == "":
         print("Data entry error: Patient first name cannot be blank. Please re-enter.") 
         continue
      else:
         break
      
    if continueProg == False:
       break
    
    ptLastName = input("Enter patients last name: ").title()
    ptDOB = input("Enter the patients date of birth (YEAR/MONTH/DAY, ex. 2000/01/30): ")
    ptMCP = input("Enter the patients MCP number: ")
    ptStAddress = input("Enter the patients street address: (Ex. 99 Hospital Road) ").title()
    ptCity = input("Enter the patients city: ").title()
    ptPostalCode = input("Enter the patients postal code: ").upper()
    ptFamDoc = input("Enter the patients family doctor: ").title()
    
    if continueProg == False:
       break
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
  
except sqlite3.Error as error:
   print("Error occured -", error)

finally: 
   if con:
      con.commit()
      con.close()
      print("--------------------------------------------")
      print("******* SQLite Connection Closed *******")

print("Thank you for using the Patient Registration Program!")
print("--------------------------------------------")