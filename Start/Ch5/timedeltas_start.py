#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
# print(timedelta(days=365,hours=5,minutes=1))

# print today's date
now = datetime.now()
# print("Today is", now)

# print today's date one year from now
# print("In one year it will be:", now + timedelta(days=365))

# create a timedelta that uses more than one argument
# print("In two weeks and 3 days it will be:", now + timedelta(weeks=2, days=3))

# calculate the date 1 week ago, formatted as a string
# t = datetime.now() - timedelta(weeks=1)

# %A = full weekday name, %B = full month name, %d = day of month,
# %Y = year with century (4-digit format)
# s = t.strftime("%A %B %d, %Y")
# print("One week ago it was", s)

### How many days until April Fools' Day?
today = date.today()
# afd = date(today.year, 4, 1)
# if afd < today:
#   print(f"April Fool's Day already went by {(today-afd).days} days ago.")
#   # If April Fool's Day already gone, get date for next one
#   afd = afd.replace(year=today.year+1)

# time_to_afd = afd-today
# print(f"It's just {time_to_afd.days} days to April Fool's Day.")

# Alt result with fake date
today = date(today.year, 11, 10)
afd = date(today.year, 4, 1)
if afd < today:
  print(f"April Fool's Day already went by {(today-afd).days} days ago.")
  # If April Fool's Day already gone, get date for next one
  afd = afd.replace(year=today.year+1)

time_to_afd = afd-today
print(f"It's just {time_to_afd.days} days to April Fool's Day.")