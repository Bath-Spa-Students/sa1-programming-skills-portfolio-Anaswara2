#Exercise 8: Simple Search.
""" Write a program that searches for a specific string within a list of strings. The list
is initialized with specific names (“Jake” “Zac”, “Ian”, “Ron”, “Sam”, “Dave”).
, and your task is to search for “Sam”. """

#List of strings
names_6=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]

#Initializing Sam in variable 's'
s="Sam"

#Checking if the entered name is found in the list.
if s in names_6: 
    print("The entered input exists in the list")
else:
    print("The entered input does not exist in the list")
