#Loops-Pizza Toppings
"""
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you’ll add that topping to their pizza.
"""

#Using the while loop 
while True:
    #asking the user for the input
    top=input("Enter a pizza topping and enter 'quit' to finish: ")
    
    #using if statement to check whether the user has entered 'quit'
    if top.lower()=='quit':
        break
    else:
        print(top,"is added to their pizza")
