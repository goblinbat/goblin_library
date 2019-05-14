"""
OOP = Object-Orientated Programming

APIE:
    "The four pillars of OOP"

A - Abstraction
    The goal of abstraction is to make your classes (or functions, etc) easy to reuse
    You want to hide the logic of how it works
P - Polymorphism
    Polymorphism helps us achieve abstraction
    Make a program that can be used interchangeably
I - Inheritance
    allows for another method of polymorphism. derived classes inherit code from base classes
    (see example below)
E - Encapsulation
    Simple objects: hide inside the workings of that object
"""


class Animal():                                 # This can be considered a base class
    def speak(self):
        print('an animal is speaking')

    def sleep(self):
        print('an animal is sleeping')


class Human(Animal):            # human inherits animal's code
    def speak(self):
        print("I am a human!")      # method overwriting
        super().speak()             # This line allows animal's version to run in addition to human's


Jack = Human()
Jack.sleep()                    # since 'human' (jack's class) is an instance of 'animal', it inherits animal's code
Jack.speak()
