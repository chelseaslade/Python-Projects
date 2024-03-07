#Patient Registration Software Dev
#Start Date: February 16
#Author: Chelsea Slade


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
  con = sqlite3.connect("/Users/student/Documents/GitHub - Stored Projects/Python-Projects/Patient Software/patientRecords.db")
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
    
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz ABCEDFGHIJKLMNOPQRSTUVWXYZ ,.-'")
    allowed_num_only = set("1234567890")
    allowed_num= set("1234567890-., ")

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
    
    while True:   
      ptLastName = input("Enter patients last name: ").title()
      if ptLastName.upper() == "END":
         continueProg == False
         break
      elif ptLastName == "":
         print("Data entry error: Patient last name cannot be blank. Please re-enter.")
         continue
      else: break

    if continueProg == False:
       break
        
    while True:
      ptDOB = input("Enter the patients date of birth (YEAR/MONTH/DAY, ex. 2000/01/30): ")
      if ptDOB.upper() == "END":
         continueProg == False
         break
      elif ptDOB == "":
         print("Data entry error: Patient date of birth cannot be blank. Please re-enter.")
         continue
      else:
         break

    if continueProg == False:
       break

    while True:
      ptMCP = input("Enter the patients MCP number: ")
      if ptMCP.upper() == "END": 
         continueProg == False
         break
      elif ptMCP == "":
         print("Data entry error: Patient MCP cannot be blank. Please re-enter.")
         continue
      else:
         break
      
    if continueProg == False:
      break

    while True:
      ptStAddress = input("Enter the patients street address: (Ex. 99 Hospital Road) ").title()
      if ptStAddress.upper() == "END":
         continueProg == False
         break
      elif ptStAddress == "":
         print("Data entry error: Patient street address cannot be blank. Please re-enter.")
         continue
      else:
         break
      
    if continueProg == False:
      break

    while True: 
      ptCity = input("Enter the patients city: ").title()
      if ptCity.upper() == "END":
         continueProg == False
         break
      elif ptCity == "":
         print("Data entry error: Patient city cannot be blank. Please re-enter.")
         continue
      else:
         break
      
    if continueProg == False:
       break
    
    while True:
      ptPostalCode = input("Enter the patients postal code: ").upper()
      if ptPostalCode.upper() == "END":
         continueProg == False
         break
      elif ptPostalCode == "":
         print("Data entry error: Patient postal code cannot be blank. Please re-enter.")
         continue
      else:
         break
      
    if continueProg == False:
      break

    while True:
      ptFamDoc = input("Enter the patients family doctor: ").title()
      if ptFamDoc.upper() == "END":
         continueProg == False
         break
      else:
         break
      
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

print("Thank you for using the Patient Registration Program!")
print("--------------------------------------------")