class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

  


class Warrior(Character):

    def attack(self):
        print(f"{self.name} → hammer attack")


class Mage(Character):

    def attack(self):
        print(f"{self.name} → Magic attack")


class Archer(Character):

    def attack(self):
        print(f"{self.name} → Arrow attack")


# Create characters
characters = [
    Warrior("Thor", 100),
    Mage("Doctor Strange", 80),
    Archer("Hawkeye", 90)
]


# Polymorphism
for character in characters:
    character.attack()