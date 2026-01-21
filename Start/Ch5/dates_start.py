#
# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime # class datetime imported

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
# today = date.today()
# print("Today's date is", today)

# print out the date's individual components
# print("Date Components:", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
# weekday() is a method within date
# print("Today's Weekday #:", today.weekday())

# If I had some list and I wanted to provide an index variable for that list,
# which depended on the weekday, I could use the weekday property to
# index into a list of, say, abbreviated names
# days = ["mon", "tues", "wed", "thu", "fri", "sat", "sun"]
# print("Which is a", days[today.weekday()])

## DATETIME OBJECTS
# Get today's date from the datetime class
today = datetime.now()
# print("The current date and time is", today)

# Get the current time
# Call datetime class and call time function,
# whose argument is the datetime object
t = datetime.time(datetime.now())
print("The current time is", t)