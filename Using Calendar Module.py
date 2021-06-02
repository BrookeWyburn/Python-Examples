#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brook
#
# Created:     25/04/2021
# Copyright:   (c) brook 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import calendar

c = calendar.TextCalendar(calendar.SUNDAY)

str = c.formatmonth(2021, 4)
#change 2021 ,4 for the year and month you want#
print(str)

#this program doesn't work in pyscripter but work in python#
