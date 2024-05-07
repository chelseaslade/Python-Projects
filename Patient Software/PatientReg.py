#Patient Registration Software Dev
#Start Date: February 16
#Author: Chelsea Slade
#Python Projects V1.

#Import Libraries
import sqlite3
from sqlite3 import Error
import patientRegFunctions as PF
import PySimpleGUI as sg


#Welcome to the Program Message
print()
print("Welcome to the Patient Registration Program.")
print()
print("--------------------------------------------")


#SQL Lite 3 Database
#SQL in main program possibly redunant? Use only in functions as needed?
try: 
   con = sqlite3.connect("/Users/student/Documents/GitHub - Stored Projects/Python-Projects/Patient Software/patientRecords.db")
   cur = con.cursor()
   print("Program has connected to the Patient Records database.")
   query = "select sqlite_version();"
   cur.execute(query)

   result = cur.fetchall()
   print("SQLite version is {}".format(result))
   print("--------------------------------------------")
   print()


   def mainMenu():
      while True:
         optionSelect = input("Please select a menu option (1-4): ")
         if optionSelect == "1":
            #Menu Option One: Add Patient
            PF.addPatient()
         # elif optionSelect == "2":
         #    #Menu Option Two: Search Patients
         # elif optionSelect == "3":
         #    #Menu Option Three: View Doctor List
         # elif optionSelect == "4":
         #    #Menu Option Four: Add New Doctor
         elif optionSelect == "5":
            PF.addDoctor()
         #    print("Exiting Patient Software program.")
         #    break
         else:
            print("Invalid menu selection, please re-select.")
            continue


#Menu
   mainMenu()

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