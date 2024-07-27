class Animal:
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Derived Class Must Implement This Function")
    
class Cat(Animal):
    def talk(self):
        return "meow"

class Dog(Animal):
    def talk(self):
        return "woof"

animals = [Cat("Billa"), Cat("Billu"), Dog("Choco"), Dog("Daku"), Cat("Lemma")]
for animal in animals:
    print(animal.name, "-" , animal.talk())
                