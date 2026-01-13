# LinkedIn Learning Python course by Joe Marini
# Example file for working with loops


x = 0

# define a while loop
# Executes WHILE a particular condition evaluates to true
# while x < 5:
#   print(x)
#   x = x + 1

# answer = input("Should I stop?")
# while answer != "yes":
#   print(answer)
#   answer = input("Should I stop?")

# define a for loop
# For loops good to use when you have a fairly good idea how many items
# there are in a particular set of data
days = ["Mon","Tue","Wed","Thurs","Fri","Sat","Sun"]
# for d in days:
#   print(d)

# use a for loop over a collection


# use the break and continue statements
# for d in days:
#   if (d == "Wed"):
#     break # Used to stop execution of a loop
#   print(d)

# for d in days:
#   if (d == "Thurs"):
#     continue # skips the rest of the code in the loop
#   print(d)

# using the enumerate() function to get an index and an item
# i means index
# Note that (i, d) is a tuple
for i,d in enumerate(days):
  print(i, d)
  