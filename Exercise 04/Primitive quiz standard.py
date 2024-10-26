#Exercise 4: Primitive Quiz standard
"""In this exercise, you’ll create a simple program that asks the user a question,
evaluates their answer, and provides feedback.
Steps:
1. Write a program that asks the user “What is the capital of France?” and
waits for their response.
2. If the user’s answer is correct (i.e., “Paris”), the program should print a
message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the
answer is wrong."""

#Asking the user for the input
cap=input("What is the capital of France: ") #cap(variable)= capital
if cap=="Paris":
#The code will print correct answer if the given answer is exactly "Paris".
    print("The answer is correct")
else:
    print("The answer is incorrect")
