#
# Example file for working with Calendars
# LinkedIn Learning Python course by Joe Marini
#


import calendar

# create a plain text calendar
# c = calendar.TextCalendar(calendar.SUNDAY)
c = calendar.TextCalendar(calendar.MONDAY)

# formatmonth() method lets you format a particular month
# into a text string
# thestr = c.formatmonth(2026,1,0,0)
# print(thestr)

# create an HTML formatted calendar
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# thestr = hc.formatmonth(2026, 1)
# print(thestr)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
# This will return numbers that represent each day in the month
# for i in c.itermonthdays(2026, 8):
#   print(i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
# for name in calendar.month_name:
#   print(name)

# for day in calendar.day_name:
#   print(day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.
# To figure out what days that would be for each month,
# we can use this script:
print("Team meetings will be on:")
for m in range(1,13): # There is no 13th month, but need to include 12
  # Get array of weeks that represent each of the months
  cal = calendar.monthcalendar(2026, m)
  # First Friday will occur within first two weeks;
  # if weekone doesn't have it, weektwo will
  weekone = cal[0]
  weektwo = cal[1]
  # Use calendar's Friday constant to index into each of the arrays
  if weekone[calendar.FRIDAY] != 0:
    meetday = weekone[calendar.FRIDAY]
  else:
    meetday = weektwo[calendar.FRIDAY]

  print(f"{calendar.month_name[m]}: {meetday}")