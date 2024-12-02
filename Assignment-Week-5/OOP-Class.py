# Base Class: Superhero
class Superhero:
    def __init__(self, name, alias, superpower):
        self.name = name
        self.alias = alias
        self.superpower = superpower

    def reveal_identity(self):
        return f"My name is {self.name}, but you know me as {self.alias}."

    def use_superpower(self):
        return f"{self.alias} uses {self.superpower}! 💥"


# Derived Class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, alias, superpower, flight_speed):
        super().__init__(name, alias, superpower)
        self.flight_speed = flight_speed  # Measured in km/h

    def fly(self):
        return f"{self.alias} is flying at {self.flight_speed} km/h! 🚀"


# Objects
hero1 = Superhero("Bruce Wayne", "Batman", "Martial Arts Mastery")
hero2 = FlyingSuperhero("Clark Kent", "Superman", "Super Strength", 1000)

# Demonstration
print(hero1.reveal_identity())  # My name is Bruce Wayne, but you know me as Batman.
print(hero1.use_superpower())  # Batman uses Martial Arts Mastery! 💥
print(hero2.reveal_identity())  # My name is Clark Kent, but you know me as Superman.
print(hero2.fly())  # Superman is flying at 1000 km/h! 🚀
