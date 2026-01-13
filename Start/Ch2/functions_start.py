# LinkedIn Learning Python course by Joe Marini
# Example file for working with functions


# define a basic function
# def hello_func():
#   print("hello world!")
#   name = input("What is your name? ")
#   print("Nice to meet you,", name)

# hello_func() # This is a function call

# function that takes parameters
# def hello_func(greeting):
#   print("hello world!")
#   name = input("What is your name? ")
#   print(greeting, name)

# hello_func("How are you doing ")
# hello_func("Hey, what's up ")

# function that returns a value
# def cube(x):
#   return x*x*x

# result = cube(4)
# print(result)

# function with default value for an parameter
# def hello_func(greeting, name=None):
#    print("hello world!")
#    if name == None:
#       name = input("What is your name? ")
#    print(greeting, name)

# hello_func("Nice to meet you", "Victoria")

# Alt if value not provided for name parameter
# def hello_func(greeting, name=None):
#    print("hello world!")
#    if name == None:
#       name = input("What is your name? ")
#    print(greeting, name)

# hello_func("Nice to meet you")

# function with variable number of parameters
# *args means that there are going to be a variable number of parameters,
# but you don't know how many there are in advance
# def multi_add(*args):
#   result = 0
#   for x in args:
#     result = result + x
#   return result

# print(multi_add(4, 5, 10, 4, 10))

# Variable parameter ALWAYS comes last
# This example has a starting value argument
def multi_add(start, *args):
  result = start
  for x in args:
    result = result + x
  return result

print(multi_add(0, 4, 5, 10, 4, 10))