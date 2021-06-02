#Inheritance and 3 ways to import module by Brooke Wyburn
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

#Three methods of importing modules
#1.
import random
#2
from random import randrange
#3
import add as #local name for module


