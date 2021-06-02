#Interger, float or string by Brooke Wyburn

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

