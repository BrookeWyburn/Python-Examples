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

print("1: Add")
print("2: Subtract")
print("3: Muiltiply")
print("4: Divide")

Choice = input("Enter the number of the function you want (1/2/3/4) :")

num1 = float (input("Please Enter First Number:"))
num2 = float (input("Please Enter Second Number:"))

if Choice == '1':
    print(num1, "+", num2, "=", num1+num2)
if Choice == '2':
    print(num1, "-", num2, "=", num1-num2)
if Choice == '3':
    print(num1, "x", num2, "=", num1*num2)
if Choice == '4':
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Invaild Input")