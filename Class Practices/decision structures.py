#Nested if statements.
sal=int(input("Enter your salary:")) #sal=salary
#using if statement to check whether the salary is mor than or equal to 45000
if sal>=45000:
    job_experience_years=float(input("Enter the years of experience"))
    if job_experience_years>=2:
        print("You qualify for your job")
    else:
        print("experience is less than 2")
else:
    print("you've to earn atleast 45k to qualify")
