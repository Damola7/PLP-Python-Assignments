# Base Class: Animal
class Animal:
    def move(self):
        pass  # lets the specific animals decide how to move, it makes the move possible to be overidden


# Derived Classes
class Fish(Animal):
    def move(self):
        return "The fish is Swimming 🐟"


class Bird(Animal):
    def move(self):
        return "This bird is Flying 🦅"


class Snake(Animal):
    def move(self):
        return "There's a snake Slithering 🐍"


# Objects
animals = [Fish(), Bird(), Snake()]

# Demonstration
for animal in animals:
    print(animal.move())
