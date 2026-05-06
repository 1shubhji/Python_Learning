# class Person:
#     def __init__(self,age,name):
#         self.age = age
#         self.name = name

class Animal:
    def sound(self):
        print("Some Sound")


class Dog(Animal):
    def sound(self):
        print("Bark")

newAnimal = Dog()

Animal.sound()
        