#Exercise 3: Biography 

""" In this exercise, you’ll create a program that stores and prints your name, home-
town, and age to the console using a Python dictionary. """

#Steps:
"""
1. Store the information (name, hometown, and age) as key-value pairs in a
dictionary.
2. Print the values on separate lines using a single print() statement.
3. Use variables with appropriate data types for each piece of information. 
"""

#Storing the values in their respective keys.
dict={'Name':'Anaswara',
      'Home-town':'Kerala',
      'Age':18}
      
#printing only the values.
#Using \n to print all the values in separate lines.
print(dict['Name'],dict['Home-town'],dict['Age'],sep='\n')
