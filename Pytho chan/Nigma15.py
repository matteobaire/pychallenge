__author__ = 'Matteo'

import calendar
'''mozart'''
print [i for i in range(1006, 2006, 10) if calendar.weekday(i, 1, 26) == 0][-3]
