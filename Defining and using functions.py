#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brooke.wyburn
#
# Created:     07/05/2021
# Copyright:   (c) brooke.wyburn 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def hotelcost(nights):
   global cost1
   daycost = 140
   cost1 = nights* daycost
   return
def planecost(location):
   global cost2
   if location.isalpha():
     location = location.lower()
     if location =="napier":
         cost2 = 150
     elif location =="auckland":
         cost2 = 220
     elif location =="christchurch":
          cost2 = 250
     elif location =="dunedin":
         cost2 = 476
     else:
         print ("Location not on list. standard costs apply")
         cost2 = 750
   else:
         print("invaild input")

def carcost(dayshired):
    global cost3
    cost3 = dayshired * 40
    if dayshired >=7:
     cost3 = cost3-50
    elif dayshired>=3:
     cost3=cost3-20
    else:
     return






no_nights = int(input("How many nights did you stay"))
destination = str(input("Where did you travel to? :"))
carhire = int(input("How many days did you hire the car?"))
moneyspent = float(input("How much did you spend? :"))

hotelcost(no_nights)
print(cost1)
planecost(destination)
print(cost2)
carcost(carhire)
print(cost3)
totalcost = float(cost1)+float(cost2)+float(cost3)+moneyspent
print(totalcost)