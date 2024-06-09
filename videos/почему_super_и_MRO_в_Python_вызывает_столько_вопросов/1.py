class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(self)
        return f"{self.name} makes a noise"

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        print(f"Cat: {self.name} | Breed: {self.breed}")
        return super().speak() + " and meows"

cat = Cat("Buddy", "Golden Retriever")
print(cat.speak())
