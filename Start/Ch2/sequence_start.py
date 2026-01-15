# LinkedIn Learning Python course by Joe Marini
# Example file for complex types

# Sequences: Lists and Tuples
# These are -- surprise -- sequences of values
mylist = [0, 1, "two", 3.2, False] # contents do not have to be of same type
# print(len(mylist))

# to access a member of a sequence type, use []
# Python lists are zero-based, so the first item in a list is 0
# print(mylist[2]) starts from beginning of a list
# print(mylist[-1]) starts from the end of a list
# mylist[0] = 10 changes value of an index in a list
# print(mylist)

# add a list to another list
# another_list = [6,7,8]
# mylist = mylist + another_list
# print(mylist)

# Strings are also sequences
# mystr = "This is a string"
# print(mystr[2])  <- this is a sequence indexer

# Strings are also immutable, meaning you can't change the value once created
# mystr[2] = "Z"

# use slices to get parts of a sequence
# 1st number is index to start (if empty, will start at 0)
# 2nd number is index to stop (not inclusive. If empty, will go to end)
# 3rd number is step amount
# print(mylist[1:4:2])
# print(mylist[::2])

# Can do this with negative values
# print(mylist[-4:-1:2]) # this will start at -4 index, which is 1
# print(mylist[-5:-2:2]) # this will start at -5 index, which is 0

# you can use slices to reverse a sequence
# print(mylist[::-1])

# Tuples are like lists, but they are immutable
# Tuples good for holding data that isn't going to change
mytuple = (0,1,2,"three")
# print(mytuple[1])

# Sets are also sequences, but they contain unique values
myset = {1, 2, 3, 2, 4, "hey"}
# Upon printing, the other '2' will disappear
# You can only have one instance of each value
#print(myset)

# Set, however, can not be indexed like lists or tuples
# print(myset[0]) # this will cause an error

# Test for membership
print(1 in mylist)
print(3 in mytuple)
print(5 in myset)
print(3 not in mytuple)