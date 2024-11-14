#Exercise 10: Is it even?
""" Write a program that tests if a value is even or odd. Follow the instructions
outlined below:"""
#Instructions:
"""
• The program should ask the user for a number from within the main
function.
• The entered number should be passed to a function that determines if the
value is even or odd.
• The function should return a message indicating whether the number is
even or odd.
• The message returned by the function should be printed from within the
main function. """

#Function definition
def check():
    #Checks whether the entered number is divisible by 2.
    if num%2==0:
        #Outputs the corresponding answer.
        print("The entered digit is an even number")
    else:
        print("The entered digit is an odd number")

#Asking the user for the input.
num=int(input("Enter a digit: "))
#Calling the function.
check()
