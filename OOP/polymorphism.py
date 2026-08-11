# class Dog:
#     def speak(self):
#         print("woof!")

# class Cat:
#     def speak(self):
#         print("meow")

# dog = Dog()
# cat = Cat()

# dog.speak()
# cat.speak()

# #speak()--behaves differentlly thats polymorphism


# class Animal:
#     def speak(self):
#         return "some sound"

# class Dog(Animal):
#     def speak(self):
#         return"woof!"

# # class Cat(Animal):
# #     def speak(self):
# #         return"meow"

# for animal in [Dog()]:
#     print(animal.speak())


class Animal:

    def speak(self):
        print("Animal sound")


class Dog(Animal):

    def speak(self):
        print("Woof!")

# animal = Animal()
dog = Dog()

# animal.speak()
dog.speak()
