class Animal:
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

