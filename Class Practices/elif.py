#practice
#asks the user to input the score
score=int(input("Enter the score"))
#checks if the score is above or equal to 90
if score>=90:
    print("your grade is A")
#checks if the score is above or equal to 80
elif score>=80:
    print("your grade is B")
#checks if the score is above or equal to 70
elif score>=70:
    print("your grade is C")
#checks if the score is above or equal to 60
elif score>=60:
    print("your grade is D")
#comes out of the loop if the score is less than 60
else:
    print("your grade is F")

#Elif statement (checking whether the value is bigger)
val1=530
val2=200
if val2>val1:
    print("val2 is greater than val1")
elif val1==val2:
    print("val1 and val2 are equal")
else:
    print("val1 is greater than val2")
