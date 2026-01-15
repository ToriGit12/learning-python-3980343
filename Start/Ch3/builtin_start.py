# LinkedIn Learning Python course by Joe Marini
# Example file for using built-in functions
#

mystring = "The quick, brown fox jumped over the lazy dog!"
mynumbers = [1,3,5,6,9,12,14,17,20,30]

# the len() function calculates the length of a sequence
# print(len(mystring))
# print(len(mynumbers))

# the max() and min() functions will find the largest and smallest value in a sequence
# print(max(mystring))
# print(min(mynumbers))

# the str() function will return a string version of an object
# prefix = "result: "
# result = 5
# print(prefix + result) # this is wrong because string and int cannot concatenate
# print(prefix + str(result))

# Can do str() on almost any object
# print(prefix + str(3.1415))

# range(start, stop, step) will create a range of numbers 
# You can use ranges along with loops
# for i in range(5, 15): # 15 is not included in the range
#   print(i)

# Example using optional step value
# for i in range(5, 15, 2):
#   print(i)

# Can use ranges as a way to index into a sequence of values
# for i in range(5, len(mystring), 2):
#   print(mystring[i]) # using an index; starting @ index 5, which is "q"

# the print function itself is pretty flexible - you can embed variables directly in it
greeting = "Hello!"
count = 10

# the f inside makes it an interpolated string
# can use {} to refer to (I should say embed) variables within print()
print(f"{greeting} you are visitor number {count}")