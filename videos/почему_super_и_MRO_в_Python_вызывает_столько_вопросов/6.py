
class New:
    def speak(self):
        print("New")

class Animal:
    def speak(self):
        print("Animal speaks")

class Mammal(Animal, New):
    def speak(self):
        print("Mammal speaks")
        super().speak()

class Dog(Mammal):
    def speak(self):
        print("Dog barks")
        super().speak()

dog = Dog()
dog.speak()

print()
mammal = Mammal()
super(Animal, mammal).speak()

print(Mammal.__mro__)
