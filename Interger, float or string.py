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

def numberstring(number):

 if number.isalpha():
    print("this input is a string")
    return
 else:
        number = float(number)
        print(abs(number))
        return


value = input("Enter a value:")
numberstring(value)

