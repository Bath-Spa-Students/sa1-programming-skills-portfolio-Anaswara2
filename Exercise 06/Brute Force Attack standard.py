#Exercise 6: Brute Force Attack.
""" Write a program that simulates a password entry system. The correct password
is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.
Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the
correct one is entered.
3. Output an appropriate message when the correct password is entered. """

#Defining the password under the variable 'crt_password'.
crt_pass=12345

#Checking if the password is correct through the while loop.
while True:
    #Asking the user to input the password.
    password=int(input("Enter the password: "))

    if password==crt_pass:
        #Outputs the given statement if the password is correct.
        print("THE PASSWORD YOU'VE ENTERED IS CORRECT")
        break
    else:
        #Outputs the given statement if the password is incorrect.
        print("THE PASSWORD YOU'VE ENTERED IS INCORRECT")
