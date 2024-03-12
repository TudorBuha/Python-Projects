def add_phone(phones: list):
    try:
        manufacturer = input("Enter manufacturer: ")
        model = input("Enter model: ")
        price = int(input("Enter price: "))

        if len(manufacturer) < 3 or len(model) < 3 or price < 0:
            raise ValueError("Input too short, it has to be at least 3 characters long")

        phones.append({"manufacturer": manufacturer, "model": model, "price": price})
        print("Phone added successfully!")
    except ValueError as ve:
        print(ve)


def display_phones(phones: list):
    index = 1
    print("Phones:")
    for phone in phones:
        print(f"{index}.{phone['manufacturer']}, {phone['model']}, {phone['price']}")
        index += 1


def display_phones_by_manufacturer(phones: list):
    search_manufacturer = input("Enter manufacturer(partial matching): ")
    matching_phones = []
    for phone in phones:
        if search_manufacturer.lower() in phone["manufacturer"].lower():
            matching_phones.append(phone)

    if matching_phones:  # if matching_phones list is not empty
        print("\nMatching phones:")
        index = 1
        for phone in matching_phones:
            print(f"{index}.Manufacturer: {phone['manufacturer']}, Model: {phone['model']}, Price: {phone['price']}")
            index += 1
    else:
        print("No matching phones")


def increase_price(phones: list):
    try:
        manufacturer = input("Enter the manufacturer: ")
        model = input("Enter the model: ")
        amount = int(input("Enter the amount to increase the price: "))

        for phone in phones:
            if phone["manufacturer"].lower() == manufacturer.lower() and phone["model"].lower() == model.lower():
                phone["price"] += amount
                print(f"Price increased succesfully. New price: {phone['price']}")
                return
        raise ValueError("Phone or model not found.")
    except ValueError as ve:
        print(ve)


def increase_all_prices(phones: list):
    try:
        percent = int(input("Enter a percent to increase all plices (between -50 and 100): "))

        if percent < -50 or percent > 100:
            raise ValueError("Invalid percentage. Must be between -50 and 100.")

        for phone in phones:
            phone["price"] = int(phone["price"] * (1 + percent / 100))

        print(f"All phones increased by {percent}%")
    except ValueError as ve:
        print(ve)


def main():
    phones = []
    while True:
        print(" Menu:")
        print("1. Display all phones")
        print("2. Add a phone")
        print("3. Display phones by manufacturer")
        print("4. Increase the price of a phone")
        print("5. Increase all prices by percent")
        print("6. Exit")

        option = input("Enter option: ")

        if option == "1":
            display_phones(phones)
        elif option == "2":
            add_phone(phones)
        elif option == "3":
            display_phones_by_manufacturer(phones)
        elif option == "4":
            increase_price(phones)
        elif option == "5":
            increase_all_prices(phones)
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
