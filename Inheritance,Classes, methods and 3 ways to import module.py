#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      brooke.wyburn
#
# Created:     26/05/2021
# Copyright:   (c) brooke.wyburn 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#Explain Inheriatence with code example
#Parent class
class Dog:
    def __init__(self):
        print("Dog is ready")

    def whoIsThis(self):
        print("Dog")

    def run(self):
        print("Run faster!")
#Child class
class Husky:
    def __init__(self):
      #the super function
      super().__init__()
      print("Husky is ready")
    def whoIsThis(self):
        print("Husky")
    def pull(self):
        print("Pull Faster!")
#we have two classes Dog(the parent class) and Husky(the child class)
# The super functiuon allows the child class to inhert from the parent
# We see this from the run method
# The pull mehtod is extentsion of the parent class
#The Child class modifys the parents behaviour as seen in whoIsThis

#Class example
class Student:
    def __init__(self, student_name, student_id):
        self.name = student_name
        self.id = student_id
        self.age = None
        self.marks = None
    def setAge(self, age):
        self.age = age
    def setMarks(self, marks):
        self.marks = marks
    def display_student_info(self):
        print(self.name)
        print(self.id)
        print(self.age)
        print(self.marks)

Brooke = Student ("Brooke", "2200026")
Brooke.setAge(20)
Brooke.setMarks ("B")
Brooke.display_student_info()
#Three methods of importing modules
#1.
import random
#2
from random import randrange
#3
import add as #local name for module


