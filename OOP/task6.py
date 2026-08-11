class Animal:
    def eat(self):
        print("Animal Eating")

    def sleep(self):
        print("Animal is sleeping")

class Dog(Animal):
    def bark(self):
        print("woff!")

animal = Animal()
dog = Dog()

animal.eat()
animal.sleep()
dog.bark()
