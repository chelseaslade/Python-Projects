#Functions for Patient Reg Project
#Author: Chelsea Slade
#Date: April 17, 2024 -

#Menu Option One: Add Patient
def addPatient():
    allowed_characters = set("abcdefghijklmnopqrstuvwxyz ABCEDFGHIJKLMNOPQRSTUVWXYZ ,.-'")
    allowed_num_only = set("1234567890")
    allowed_num= set("1234567890-., ")

    print("To exit the program, type END in first name input.")
    print("Enter patient information as indicated below: ")
    print()

    continueProg = True
    while continueProg == True: 

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
            if ptLastName == "":
                print("Data entry error: Patient last name cannot be blank. Please re-enter.")
                continue
            else: 
                break
            
        while True:
            ptDOB = input("Enter the patients date of birth (YEAR/MONTH/DAY, ex. 2000/01/30): ")
            if ptDOB == "":
                print("Data entry error: Patient date of birth cannot be blank. Please re-enter.")
                continue
            else:
                break

        while True:
            ptMCP = input("Enter the patients MCP number: ")
            if ptMCP == "":
                print("Data entry error: Patient MCP cannot be blank. Please re-enter.")
                continue
            else:
                break
            

        while True:
            ptStAddress = input("Enter the patients street address: (Ex. 99 Hospital Road) ").title()
            if ptStAddress == "":
                print("Data entry error: Patient street address cannot be blank. Please re-enter.")
                continue
            else:
                break

        while True: 
            ptCity = input("Enter the patients city: ").title()
            if ptCity == "":
                print("Data entry error: Patient city cannot be blank. Please re-enter.")
                continue
            else:
                break

        while True:
            ptPostalCode = input("Enter the patients postal code: ").upper()
            if ptPostalCode == "":
                print("Data entry error: Patient postal code cannot be blank. Please re-enter.")
                continue
            else:
                break

        while True:
            provLst = ["AB", "BC", "NB", "NS", "NL", "QC", "ON", "YT", "NT", "NU", "MB", "SK", "PE"]
            ptProvince = input("Enter the patients province: (ie. XX) ").upper()
            if ptProvince == "":
                print("Data entry error: Patient postal code cannot be blank. Please re-enter.")
                continue
            else:
                break

        while True:
            ptFamDoc = input("Enter the patients family doctor: ").title()
            if ptFamDoc == "":
                print("Data entry error: Patient family doctor cannot be blank. Please re-enter. If the patient has no family doctor at this time, please enter 'none'.")
                continue
            else:
                break

    if continueProg == True:
        print("--------------------------------------------")
        print()
        print("PATIENT INFORMATION SUMMARY")
        print()
        print(f"Patient Name: {ptFirstName} {ptLastName} ")
        print(f"Patient Date of Birth: {ptDOB} ")
        print(f"Patient Address: {ptStAddress} {ptCity} {ptPostalCode} ")
        print(f"Patient MCP #: {ptMCP} ")
        print(f"Patient Family Doctor: {ptFamDoc} ")
        print()
        print("--------------------------------------------")

# def searchPatient():
#     continueProg = True
#     while continueProg == True: 