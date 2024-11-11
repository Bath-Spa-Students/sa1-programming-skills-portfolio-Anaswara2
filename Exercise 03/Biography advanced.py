#Exercise 3: Biography.
"""
Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the
values. Try giving both your first and second name when asked for your name.
What happens? How can you handle multiple words in Python? Test the
program by entering a string value for age (e.g., “twenty”). What happens?
How can you prevent this issue? """

#Asking the user to input their name.
Name=input("Enter your name: ")

#Asking the user to input their Home-town.
Hometown=input("Enter your Home-town: ")

#Asking the user to input their Age.
while True:
    Age1=input("Enter your age: ")
    if Age1.isdigit():  
        Age=int(Age1) 
        break
    else:
        print("Invalid input. Please enter a numeric age.")

#Making a dictionary to store the values from the user.
d={"Name":Name,"Hometown":Hometown,"Age":Age1}

#printing the values of the dictionary
print(f"\nName:{d['Name']}\nHometown:{d['Hometown']}\nAge:{d['Age']}")
