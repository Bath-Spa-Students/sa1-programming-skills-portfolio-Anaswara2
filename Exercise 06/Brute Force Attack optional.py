#Exercise 6: Brute Force Attack
""" Optional Requirements:
Modify the program to include a maximum of 5 password attempts. If the
user enters the wrong password, inform them of the remaining attempts. If the
maximum number of attempts is reached, inform the user that the authorities
have been alerted. """

#Defining the password under the variable 'crt_password'.
crtpass=12345

#initializing maximum number of attempts as 5.
max_i=5

#Initializing 0 in variable 'i'.
i=0

#Using the while loop to allow the number of attempts to try.
while i<max_i:
    password=int(input("Enter the password:")) #Asking the user for the input
    if password==crtpass:
        print("Correct Password.")
        break
    else:
        i+=1
    if i<max_i:
        print("You have",max_i-i,"attempts left")
    else:
        print("You can't attempt as you have reached the maximum number of attempts")
