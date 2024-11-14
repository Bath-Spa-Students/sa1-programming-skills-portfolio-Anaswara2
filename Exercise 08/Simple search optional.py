#Exercise 08 - Simple search
#Optional Requirements:
""" 1. Allow the user to input the search term instead of using a predefined value.
    2. Implement the search functionality based on user input. """

#List of strings
names_6=["Jake","Zac", "Ian", "Ron", "Sam", "Dave"]

#Asking the user for the input
s=input("Enter a name to search in the list: ")

#Checking if the entered name is found in the list.
if s in names_6:
    print("The entered input exists in the list")
else:
    print("The entered input does not exist in the list")
