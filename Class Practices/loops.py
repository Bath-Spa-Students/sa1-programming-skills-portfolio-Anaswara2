#Loops
a = 1
while a < 5:
  print(a)
  a+= 1

#Infinite Loop With Break 
c = 1
while c < 5:
  print(c)
  if c == 2:
    break
  c+= 1  

#For loop 
fruit=["strawberry","apple","avacado"]
for x in fruit:
  print(x)

#Using the range Function with for Loop
for x in range(0,10):
    print (x)

#To improve readibility 
for x in range(0,10):
      print (x, end=",")
  
#step count (1 increment ) 
for x in range (0,10,2):
   print(x ,end=",")

# 5 increment
for x in range (0,30,5):
      print(x,end=",")

#input from user 
N=int(input("Enter max number for range: "))
for i in range (0,N):
      print(i,end=",")
