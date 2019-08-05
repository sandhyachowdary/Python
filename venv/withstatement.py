#using with statement
#In real life scenerious we should try to use with statement. It will take care of closing the file for you
#>> with open('setup.py') as fobj:
#       for line in fobj: print(line)

#Date and Time:
#       Python is providing ib built module i.e "datetime",which is used for date & time operations


#ex:

import datetime as dt
print("Date and time :",dt.datetime.now())
print("Date:",dt.date.today())
print("Today Weekday :", dt.date.weekday(dt.date.today()))


#ex:
import datetime as dt
today = dt.datetime.today()
print(today)
print(today.year)
print(today.month)
print(today.day)


#ex:To display entire CALENDAR for month

import calendar as cal
year = 2019
month = 8
print(cal.month(year,month))



#one year calendar
import calendar as cal
year = 2019
print(cal.calendar(year))

#creating object to text calendar class and passing sunday as parameter

#import calendar as cal
#cal.TextCalendar(cal.SUNDAY)

#ex
import calendar as cal
tc = cal.TextCalendar(cal.SUNDAY)
s1 = tc.formatmonth(2019,8)
print(s1)


tc = cal.TextCalendar(cal.THURSDAY)
s1 = tc.formatmonth(2019,8)
print(s1)

hc = cal.HTMLCalendar(cal.SUNDAY)
s1 = tc.formatmonth(2019,8)
print(s1) # After getting output paste it by creating a sample Html file and after that click on browser to see output


#<------------- After these refer to Nested function fike ----------------->