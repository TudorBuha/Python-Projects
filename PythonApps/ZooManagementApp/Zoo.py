def get_animals():
    return [
        {"code": "Z01", "name": "Alex", "type": "herbivore", "species": "zebra"},
        {"code": "L02", "name": "Leo", "type": "carnivore", "species": "lion"},
        {"code": "G03", "name": "Gina", "type": "herbivore", "species": "giraffe"},
        {"code": "E04", "name": "Ellie", "type": "herbivore", "species": "elephant"},
        {"code": "M05", "name": "Max", "type": "carnivore", "species": "monkey"},
        {"code": "M05", "name": "Max", "type": "herbivore", "species": "lion"}
    ]


def display_all_animals(animals):

    index = 1
    for animal in animals:
        print(f"{index}.Code: {animal['code']}, Name: {animal['name']}, Type: {animal['type']}, Species: {animal['species']}")
        index += 1

def add_an_animal(animals):
    try:
        code = input("Enter the animal's code: ")
        name = input("Enter the animal's name: ")
        type = input("Enter the animal's type: ")
        species = input("Enter the animal's species: ")

        if not code or not name or not type or not species:
            raise ValueError("Error:All fields must be filled!")
            return

        for animal in animals:
            if animal["code"] == code:
                raise ValueError("Error: Code already exists!")
                return
        new_animal = {"code": code, "name": name, "type": type, "species": species}

        animals.append(new_animal)
        print("Animal added succesfully!")
    except ValueError as ve:
        print(ve)

def modify_the_type(animals):

    try:
        code = input("Enter the animal's code: ")
        new_type = input("Enter the animal's new type: ")

        for animal in animals:
            if animal["code"] ==  code:
                animal["type"] = new_type
                print("Animal type modified succesfully!")
                return
        raise ValueError("Error: Animal not found!")
    except ValueError as ve:
        print(ve)




def change_a_species_type(animals):
    species = input("Enter the species to change the types for: ")
    new_type = input("Enter the new type: ")

    try:
        if not new_type: #if the new_type is void
            raise ValueError("Error: New type cannot be empty.")
            return
    except ValueError as ve:
        print(ve)

    for animal in animals:
        if animal["species"] == species:
            animal["type"] = new_type


def show_all_animals_with_a_given_type(animals, new_animal_list: list):
    new_animal_list = []
    type = input("Type: ")
    try:
        for animal in animals:
            if animal["type"] == type:
                new_animal_list.append(animal)

        new_animal_list.sort(key = lambda x: x["name"])

        if not new_animal_list:
            raise ValueError("Error: This species does not exists!")
            return
    except ValueError as ve:
        print(ve)


    display_all_animals(new_animal_list)



def main():
    animals = get_animals()
    same_type_animals = []
    while True:
        print("\nMenu:")
        print("1.Display all the animals")
        print("2.Add an animal")
        print("3.Modify the type of an animal")
        print("4.Change a species type")
        print("5.Show all animals with a given type")
        print("6.Exit")

        users_choice = input(">")

        if users_choice == "1":
            display_all_animals(animals)
        elif users_choice == "2":
            add_an_animal(animals)
        elif users_choice == "3":
            modify_the_type(animals)
        elif users_choice == "4":
            change_a_species_type(animals)
            print("Types changed succesfully!")
        elif users_choice == "5":
            show_all_animals_with_a_given_type(animals, same_type_animals)
        elif users_choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select one of (1-6)")


if __name__ == "__main__":
    main()
