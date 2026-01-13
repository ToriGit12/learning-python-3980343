# LinkedIn Learning Python course by Joe Marini
# Example file for variables and basic types


# Basic data types in Python: Numbers, Strings, Booleans 
# Variable names must start with a letter or _, and can have numbers. They are case sensitive. 
myint = 10
myfloat = 13.2576
mystr = "This is a string"
mybool = True

# We can display the content of a variable using the print() function
#print(myint)
#print(mystr)

# Operators are used to perform operations on variables
# print(myint + myfloat)
# print(myint * myfloat)
# print(myint / myfloat)
# print(myint % 3)  remainder should be 1

# another_str = "This is another string"
# print(mystr + another_str)
# print("nom " * 3)
# print(mystr + 1)  you cannot add two fundamentally different data types

# Logical and comparison operators 
# print(myint == 10)  '==' is for comparing, '=' is for assigning; answer True
# print(myfloat != 20)
# print(myint > 20)
# print(myfloat < 10)

# AND True: Both statements are true
# AND False: One statement true, the other false, or both are false
# print(myint > 5 and myfloat < 25.0)

# True because in the case of OR operator,
# only one of the results has to be true for the result to be "True"
# print(myint < 5 or myfloat < 25.0)

# NOT changes the result to its opposite
# print(not (myint < 5 or myfloat < 25.0))

# re-declaring a variable works
myint = "abc"
print(myint)