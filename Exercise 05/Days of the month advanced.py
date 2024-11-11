#Exercise 5: Days of the Month
#Advanced Requirement:
"""Leap Year Adjustment: Modify the program to account for leap years. For
February, ask the user if the year is a leap year and adjust the number of days
accordingly."""

#Creating a dictionary with month numbers as key and the number of months as value.
D={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#Asking the user for the input.
month=int(input("Enter a month number: "))

#Using the if condition to check whether the entered month number exists in the dicctionary.
if month in D:
    #Checking if the entered month number is 2.
    if month==2:
        #Asking the user if that year is a leap year.
        Leapyear=input("Is the year a leap year?(yes/no)").lower()
        #Checking if the input is "yes".
        if Leapyear=="yes":
            #Prints the output
            print("There are 29 days in this month")
        else:
            print("There are 28 days in this month")
    else:
        #Prints the corresponding number of days if the entered month is not 2
        print(f"The number of days in the corresponding month {month} is {D[month]}")
else:
    #Prints that the number is invalid.
    print("The month number you have entered in invalid.")
