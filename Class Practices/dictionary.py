#Creating dictionary.
dict={}
print(dict)

#Checking the type of dictionary.
dict={}
print(dict, type(dict))

#To print the dictionary.
d={'color':'blue','fruit':'orange','place':'UAE'}
print (d)

# Testing dictionary 
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict["Name"])

#to check whether the key exists in the dictionary.
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict.get("student"))

# to test .items methods   
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict.items())

# To check keys in our dictionary 
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict.keys())

# Delete method 
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
del dict["Age"]
print(dict.items())

# Deleting
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
del dict["Age"]
print(dict.items())
print(dict.keys())
print(dict.values())

#Pop Method -to remove 
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict.pop("Name"))
print(dict.keys())
print(dict.values())

#pop items.
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
print(dict.popitem())
print(dict.keys())
print(dict.values())

#to iterate through the dictionary and print the keys one by one.
dict={'Name':'Anaswara','Age':'18','Fathers name':'Anish'} 
for x in dict:
    print(x)
#to iterate through the dictionary and print the values one by one.
for x in dict:
    print(dict[x])
