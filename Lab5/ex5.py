class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        pass

    def move(self):
        pass

    def get_info(self):
        return f"{self.name} is a {self.species}"


class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def births(self):
        return "Gives birth to a fully developed offspring"

    def get_info(self):
        return f"{super().get_info()}. {self.births()}"


class Bird(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def births(self):
        return "Lays eggs"

    def get_info(self):
        return f"{super().get_info()}. {self.births()}"


class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def births(self):
        return "Gives birth by bearing live young or by laying eggs"

    def get_info(self):
        return f"{super().get_info()}. {self.births()}"


mammal = Mammal("Lion", "Mammal")
bird = Bird("Eagle", "Bird")
fish = Fish("Clownfish", "Fish")

print(mammal.get_info())
print(bird.get_info())
print(fish.get_info())

