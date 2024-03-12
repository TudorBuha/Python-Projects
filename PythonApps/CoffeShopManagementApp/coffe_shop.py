#Non UI
def get_coffees():
    return [
        {"name": "Capucinno", "country_of_origin": "France", "price": 69.99},
        {"name": "Latte", "country_of_origin": "Romania", "price": 31.50},
        {"name": "Espresso", "country_of_origin": "Albania", "price": 12.10},
        {"name": "Frappe", "country_of_origin": "Albania", "price": 21.00},
        {"name": "Ciocolata", "country_of_origin": "Israel", "price": 34.21}
    ]

def show_sorted_by_country(coffe_list):
    coffe_list.sort(key = lambda coffe: (coffe["country_of_origin"], coffe["price"]))
    show_coffes(coffe_list)


def add_coffe(coffe_list, name, country_orig, price):
    try:
        if price <= 0:
            raise ValueError("Price is to low!")


        for coffe in coffe_list:
            if coffe["name"] == name:
                raise ValueError("Coffe with same name already exists!")
        coffe_list.append({"name": name, "country_of_origin": country_orig, "price": price})

    except ValueError as ve:
        print(ve)

def filter_coffees(initial_coffe_list, filtred_coffe_list, country_orig, price):

    #TODO nu merge daca nu pun pret , tre facut ceva float din string

    found = False
    try:

        if not price:
            for coffe in initial_coffe_list:
                if coffe["country_of_origin"] == country_orig:
                    filtred_coffe_list.append(coffe)
                    found = True
        elif not country_orig:
            for coffe in initial_coffe_list:
                if coffe["price"] <= price:
                    filtred_coffe_list.append(coffe)
                    found = True
        else:
            for coffe in initial_coffe_list:
                if coffe["country_of_origin"] == country_orig and coffe["price"] <= price:
                    filtred_coffe_list.append(coffe)
                    found = True
        if not found:
            raise ValueError("No such coffees!")

    except ValueError as ve:
        print(ve)

    show_coffes(filtred_coffe_list)

#UI

def show_coffes(coffe_list):

    index = 1
    for coffe in coffe_list:
        print(f"{index}.Name: {coffe['name']}, Country of origin: {coffe['country_of_origin']}, Price: {coffe['price']}")
        index += 1



def main():

    coffe_list = get_coffees()
    filtred_coffe_list = []
    while True:
        print(" Menu:")
        print("1. Show all coffees")
        print("2. Add a coffe")
        print("3. Dysplay all coffees sorted by country of origin")
        print("4. Filter coffes based on origin and price")
        print("5. Exit")

        users_choice = input(">")

        if users_choice == "1":
            show_coffes(coffe_list)
        elif users_choice == "2":
            name = input("Enter coffee's name: ")
            country_orig = input("Enter coffee's origin: ")
            price = float(input("Enter coffee's price: "))
            add_coffe(coffe_list, name, country_orig, price)
        elif users_choice == "3":
            show_sorted_by_country(coffe_list)
        elif users_choice == "4":
            country_orig = input("Enter coffee's origin: ")
            price = int(input("Enter coffee's price: "))
            filter_coffees(coffe_list, filtred_coffe_list, country_orig, price)
        elif users_choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()