import sys

t = (3, 30, 2019, 9, 25)
day = ''
month = ''
year = ''
hour = ''
minute = ''
if (t[3] < 10):
    month = '0'
month += str(t[3])
if (t[4] < 10):
    day = '0'
day += str(t[4])
if (t[1] < 10):
    minute = '0'
minute += str(t[1])
if (t[0] < 10):
    hour = '0'
hour += str(t[0])
year = str(t[2])
print(month + '/' + day + '/' + year, hour + ':' + minute)
