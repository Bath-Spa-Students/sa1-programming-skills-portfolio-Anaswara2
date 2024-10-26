#Exercise 4: Primitive Quiz advanced
"""Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of
the capitalization (e.g., “paris”, “Paris”, and “PaRis” should all be considered
correct). Multiple Questions: Extend the program into a quiz that asks for the
capitals of 10 European countries. Provide feedback for each question."""

#Countries
ctry=["France","Greece","Ireland","Netherlands","Spain","United Kingdom","Italy","Austria","Belgium","Hungary"]
#Capitals of the respective countries
cap=["Paris","Athens","Dublin","Amsterdam","Madrid","London","Rome","Vienna","Brussels","Budapest"]
#Looping every line
for i in range(len(ctry)):
    #Asking the user for the answer
    ans=input(f"What is the capital of {ctry[i]}: ").lower()
    if ans==cap[i].lower():
        #Prints the statement according to the answer
        print("The answer is correct")
    else:
        print("The answer is incorrect")
