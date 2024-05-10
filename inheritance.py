class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} speaks a sound")


class Cat(Animal):
    def meow(self):
        print(f"{self.name}meows")


my_cat = Cat("Buddy")

my_cat.speak()
my_cat.meow()
