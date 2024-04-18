#Functions Library
#Author: Chelsea Slade (Mayne)
#Start Date: March 2024
import datetime
     
def firstOfMonth():
    #First Day of Next Month Date Function
    #Date: March 17, 2024

    TODAY = datetime.datetime.now()

    todayStr = (TODAY.strftime("%d-%m-%Y"))
    todayFormat = ("%d-%m-%Y")

    todayDt = datetime.datetime.strptime(todayStr, todayFormat)

    #replace day number with 1
    todayDt = todayDt.replace(day=1)

    #add 32 days to the date
    todayDt = todayDt + datetime.timedelta(days=32)

    #replace day number with 1
    firstOfMonth = todayDt.replace(day =1)
    firstOfMonthDsp = firstOfMonth.strftime("%d-%m-%Y")

    return firstOfMonthDsp


def validateProvince():
    #Validate Province Name (by initial)
    #Date: March 19, 2024

    while True:
         custProv = input("Enter customer province: ").upper()
         provLst = ["AB", "BC", "NB", "NS", "NL", "QC", "ON", "YT", "NT", "NU", "MB", "SK", "PE"]
         if custProv == "":
            print("Data entry error: Province cannot be blank. Please enter a valid value.")
            continue
         if custProv in provLst:
            break
         else: 
            print("Data entry error: Province is not valid. Please re-enter.")
            continue
 
    return custProv

def dollarFormat(unformattedCost):
    #Format float output to dollar value (two decimals)
    #Date: March 23, 2024

    formattedCost = "${:,.2f}".format(unformattedCost)

    return formattedCost