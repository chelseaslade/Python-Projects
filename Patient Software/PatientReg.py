#Patient Registration Software Dev
#Start Date: February 16
#Author: Chelsea Slade
#Python Projects V1.

#Import Libraries
import datetime
import sqlite3
from sqlite3 import Error

#SQL Lite 3 Database


def create_connection(patientRecords):
  # connection = sqlite3.connect("patientRecords.db")
  conn = None
  try:
    conn = sqlite3.connect(patientRecords)
    return conn
  except Error as x: 
    print(x)
  # finally:
  #   if conn:
  #     conn.close()

  return conn

def create_table(conn, create_table_sql):
  try:
    c = conn.cursor()
    c.execute(create_table_sql)
  except Error as x:
    print(x)

def main():
  
  database = "patientRecords.db"

  sql_create_projects_table = """ CREATE TABLE projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

  sql_create_tasks_table = """ CREATE TABLE tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                              ); """

  conn = create_connection("patientRecord=")
  if conn is not None: 
    create_table(conn, sql_create_projects_table)
    create_table(conn, sql_create_tasks_table)
    print("Success, tables created")

  else:
    print("Error! Cannot create database connection.")
               
if __name__ == '__main__':
    main()

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