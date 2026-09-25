class Animal:
    def speak(self):
        print("animal is speaking")

class Dog(Animal):
    def speak(self):
        print("woof")

class Cat(Animal):
    def speak(self):
        print("meow")

class Cow(Animal):
    def speak(self):
        print("moo")

animals = [Dog(), Cat(), Cow()]
for animal in animals:
    animal.speak()