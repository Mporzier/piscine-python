import sys

t = (0, 4, 132.42222, 10000, 12345.67)
day = ''
ex = ''
if t[0] < 10:
    day = '0'
day = day + str(t[0])
if t[1] < 10:
    ex = '0'
ex = ex + str(t[1])

print("day_" + day + ',', "ex_" + ex, ':', "%.2f" %
      t[2] + ',', "{:.2e}".format(t[3]) + ',', "{:.2e}".format(t[4]))
