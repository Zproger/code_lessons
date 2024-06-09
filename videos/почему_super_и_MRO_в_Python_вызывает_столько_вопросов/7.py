class Animal:
    def speak(self):
        print("Animal speaks")

class Flyer:
    def speak(self):
        print(Flyer)

class Swimmer:
    def speak(self):
        print("Swimmer")

class Bird(Animal, Flyer):
    def speak(self):
        super().speak()
        print("Bird chirps")

class Fish(Animal, Swimmer):
    def speak(self):
        print("Fish")

class Penguin(Bird, Swimmer):
    def speak(self):
        super().speak()
        print("Penguin squawks")

penguin = Penguin()
penguin.speak()

print(Penguin.__mro__)
