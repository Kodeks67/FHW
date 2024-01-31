from animal_registry import AnimalRegistry
from animal import Animal


if __name__ == "__main__":
    registry = AnimalRegistry()

    try:
        with registry.counter:
            while True:
                print("1. Add a new animal")
                print("2. Show animal commands")
                print("3. Train animal with new command")
                print("4. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                    name = input("Enter the name of the animal: ")
                    animal_type = input("Enter the type of the animal: ")
                    animal = Animal(name, animal_type)
                    registry.add_animal(animal)
                    print(f"{name} has been added to the registry.")

                elif choice == "2":
                    name = input("Enter the name of the animal: ")
                    registry.show_animal_commands(name)

                elif choice == "3":
                    name = input("Enter the name of the animal: ")
                    new_command = input("Enter the new command: ")
                    registry.train_animal(name, new_command)

                elif choice == "4":
                    break

    except TypeError:
        print("Exception: TypeError")
