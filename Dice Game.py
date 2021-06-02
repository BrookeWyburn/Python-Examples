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
import random, time

computer_score = 0
human_score = 0
rollagain = None
while rollagain != "exit":
    print("You are rolling now")
    human_roll = random.randint(1, 6)
    if human_roll == 1:
        print("-------")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("-------")
    if human_roll == 2:
        print("-------")
        print("|0    |")
        print("|     |")
        print("|    0|")
        print("-------")
    if human_roll == 3:
        print("-------")
        print("|0    |")
        print("|  0  |")
        print("|    0|")
        print("-------")
    if human_roll == 4:
        print("-------")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("-------")
    if human_roll == 5:
        print("-------")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("-------")
    if human_roll == 6:
        print("-------")
        print("|0 0 0|")
        print("|     |")
        print("|0 0 0|")
        print("-------")
    print("computer will roll after a delay of 5 seconds")
    time.sleep(5)
    print("computer is rolling now")
    computer_roll = random.randint(1, 6)
    if computer_roll == 1:
        print("-------")
        print("|     |")
        print("|  0  |")
        print("|     |")
        print("-------")
    if computer_roll == 2:
        print("-------")
        print("|0    |")
        print("|     |")
        print("|    0|")
        print("-------")
    if computer_roll == 3:
        print("-------")
        print("|0    |")
        print("|  0  |")
        print("|    0|")
        print("-------")
    if computer_roll == 4:
        print("-------")
        print("|0   0|")
        print("|     |")
        print("|0   0|")
        print("-------")
    if computer_roll == 5:
        print("-------")
        print("|0   0|")
        print("|  0  |")
        print("|0   0|")
        print("-------")
    if computer_score == 6:
        print("-------")
        print("|0 0 0|")
        print("|     |")
        print("|0 0 0|")
        print("-------")
    if human_roll > computer_roll:
        print("You win")
        human_score = human_score + 1
    if human_roll < computer_roll:
        print("Computer wins")
        computer_score = computer_score + 1
    if human_roll == computer_roll:
        print("Its A draw!")

    rollagain= input("Would you like to roll again or exit")

print("Thank you for playing")
print("Your score:", human_score)
print("Computer score:", computer_score)
exit



