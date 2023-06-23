class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Create instances of different classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Polymorphic behavior
animals = [dog, cat]

# Iterate through the list and call the make_sound() method
for animal in animals:
    print(animal.name + " says " + animal.make_sound())
