from counter import Counter
from animal import Animal


def determine_animal_class(animal_type):
    class Dog(Animal):
        pass

    class Cat(Animal):
        pass

    class Hamster(Animal):
        pass

    class Horse(Animal):
        pass

    class Camel(Animal):
        pass

    class Donkey(Animal):
        pass
    animal_classes = {
        "dog": Dog,
        "cat": Cat,
        "hamster": Hamster,
        "horse": Horse,
        "camel": Camel,
        "donkey": Donkey
    }

    if animal_type in animal_classes:
        return animal_classes[animal_type]
    else:
        return None


class AnimalRegistry:
    def __init__(self):
        self.animals = []
        self.counter = Counter()

    def add_animal(self, animal):
        self.animals.append(animal)
        self.counter.add()

    def show_animal_commands(self, name):
        for animal in self.animals:
            if animal.name == name:
                print(f"Commands for {name}: {animal.commands}")
                return
        print(f"{name} not found in the registry.")

    def train_animal(self, name, new_command):
        for animal in self.animals:
            if animal.name == name:
                animal.add_command(new_command)
                print(f"{name} has learned a new command: {new_command}")
                return
        print(f"{name} not found in the registry.")
