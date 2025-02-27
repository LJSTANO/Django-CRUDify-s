# class Animal:
#
#
#     def __init__(self, employee, organization):
#         self.employee = employee
#         self.organization = organization
#
#
# animal = Animal(employee="Stanley",organization="churcharmyafrica")
#
#
# # print("-------------------------")
# #
# # dog = Animal(name="Osama", age=6)
#
# def move(self):
#        return "i run very fast"
#
# print(f"Age:{animal.employee}")
#
# print("-------------------------")
#
# print(f"Name:{animal.organization}")

#


# we use def to define a function in python

class Animal:
    def __init__(self):
        self.name = input("What is your name? ")
        self.age = input("What is your age? ")
        self.sound = input("What is your sound? ")
        self.move = input("What is your move? ")

    def get_sound(self):
        return f"I am {self.name}, and I produce {self.sound} sound"

    def get_move(self):
        return f"I {self.move} very fast"

class Dog(Animal):
    pass  # Dog inherits from Animal

animal = Animal()
print(animal.get_sound())
print(animal.get_move())

print("-------------------------")

dog = Dog()
print(dog.get_sound())  # Output will be the same as for the animal object
print(dog.get_move())  # Output will be the same as for the animal object


