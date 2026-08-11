#inheritance
class Animal: #parent class

    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")


class Dog(Animal): #child class
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

class Cat(Animal): #child class
    def eat(self):
        print("Eating")

    def sleep(self):
        print("Sleeping")

dog = Dog() #function call
cat = Cat()

dog.eat()
dog.sleep()

cat.eat()
cat.sleep()




# # The child can have its own methods too
class Animal:
    def eat(self):
        print("Animal is Eating")

class Dog(Animal):
    def eat(self):
        print("Dog is Eating")

    def bark(self):
        print("Dog is Barking")

dog = Dog()
dog.eat()
dog.bark()




# inheritance with __init__()
class Animal:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name: {self.name}")


class Dog(Animal): #child calss with __inti__()
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


dog = Dog("Tommy","buld dog")

print(dog.name)
print(dog.breed)





#super() method
class Animal:

    def __init__(self, name):
        self.name = name


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Tommy","buld dw dog")

print(dog.name)
print(dog.breed)