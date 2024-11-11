#Exercise 5: Days of the Month.
"""Write a program that tells a user how many days there are in a specific month.
Use a dictionary to map the month numbers (1-12) to the number of days in
each month."""
#Instructions:
"""1. Create a Dictionary: Define a dictionary where the keys are month num-
bers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid
and print the number of days in the corresponding month."""

#Creating a dictionary with month numbers as key and the number of months as value.
D={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

#Asking the user for the input.
month=int(input("Enter a month number: "))

#Using the if condition to check whether the entered month number exists in the dicctionary.
if month in D:
    #Prints the output
    print(f"The number of days in the corresponding month {month} is {D[month]}")
else:
    print("The month number you have entered in invalid.")
