#
# Functions section
#

def get_flights():
    return [
        {"code": "0B3001", "duration": 70, "departure_city": "Cluj", "destination_city": "Zanzibar"},
        {"code": "0B3002", "duration": 30, "departure_city": "Cluj", "destination_city": "Oradea"},
        {"code": "0B3003", "duration": 50, "departure_city": "Cluj", "destination_city": "Albania"},
    ]


def show_all_flights_from_departure_city(initial_flight_list, departure_city, list_of_flights_from_departure):
    list_of_flights_from_departure = []
    found = False

    try:
        for flight in initial_flight_list:
            if flight["departure_city"].lower() == departure_city.lower():
                list_of_flights_from_departure.append(flight)
                found = True
        if not found:
            raise ValueError("Error: No flights found departing from that city!")
    except ValueError as ve:
        print(ve)

    list_of_flights_from_departure.sort(key=lambda x: x["destination_city"])
    show_all_flights(list_of_flights_from_departure)

def delete_a_given_flight(initial_flight_list, code, new_flights_list_without_deleted_one):
    """
    User should add a code and this function add in a new list all flights without the one that has the code provided by user
    and overwrite the initial flight list with the one wothout the specified flight
    :param initial_flight_list:
    :param code:
    :param flights_list_without_deleted_one:
    :return:
    """
    for flight in initial_flight_list:
        if flight["code"] != code:
            new_flights_list_without_deleted_one.append(flight)

def add_flight(flights_list, code, duration, departure, destination):
    # code = input("Enter the flight's code: ")
    # duration = int(input("Enter the flight's duration: "))
    # departure = input("Enter the flight's departure city: ")
    # destination = input("Enter the flight's destination city: ")
    ok = True
    try:
        if len(code) < 3:
            ok = False
            raise ValueError("Error: Code is too short!")
        if len(departure) < 3:
            ok = False
            raise ValueError("Error: Departure city name is too short!")
        if len(destination) < 3:
            ok = False
            raise ValueError("Error: Destination city name is too short!")
        if duration < 20:
            ok = False
            raise ValueError("Error: Duration of the flight is too short!")

        if ok == True:
            flights_list.append({"code": code, "duration": duration, "departure_city": departure, "destination_city": destination})

    except ValueError as ve:
        print(ve)
    # if ok == True:
    #     flights_list.append({"code": code, "duration": duration, "departure_city": departure, "destination_city": destination})


def duration_increase(flight_list, departure_city, new_duration):
    try:

        if new_duration < 10 or new_duration > 60:
            raise ValueError("Invalid duration")
        for flight in flight_list:
            if flight["departure_city"] == departure_city:
                flight["duration"] = int(flight["duration"]) + new_duration

    except ValueError as ve:
        print(ve)



#
# User interface section
#



def show_all_flights(flights):
    index = 1
    for flight in flights:
        print(
            f"{index}.Code: {flight['code']}, Duration: {flight['duration']}, Departure from: {flight['departure_city']}, Destination: {flight['destination_city']}")
        index += 1



#Menu

def main():
    flights_dict = get_flights()

    menu_show = "1"
    menu_add = "2"
    menu_delete = "3"
    menu_departure = "4"
    menu_modify = "5"
    menu_exit = "6"

    while True:
        print("Menu:")
        print(f"{menu_show}. Show all flights")
        print(f"{menu_add}. Add a flight")
        print(f"{menu_delete}. Delete a flight")
        print(f"{menu_departure}. Show flights with given departure")
        print(f"{menu_modify}. Modify flight duration for a departure city")
        print(f"{menu_exit}. Exit")

        user_choice = input(">")

        if user_choice == menu_show:
            print("Flights:")
            show_all_flights(flights_dict)
        elif user_choice == menu_add:
            code = input("Add flight's code: ")
            duration = int(input("Add flight's duration: "))
            departure = input("Add flight's departure city: ")
            destination = input("Add flight's destination: ")
            add_flight(flights_dict, code, duration, departure, destination)
            #add_flight(flights_dict)
        elif user_choice == menu_delete:
            code = input("Add flight's code to be deleted: ")
            flights_list_without_deleted_one = []
            delete_a_given_flight(flights_dict, code, flights_list_without_deleted_one)
            flights_dict = flights_list_without_deleted_one
            show_all_flights(flights_dict)
        elif user_choice == menu_departure:
            departure_city = input("Add a departure city: ")
            list_of_flights_from_departure = []
            show_all_flights_from_departure_city(flights_dict, departure_city, list_of_flights_from_departure)
        elif user_choice == menu_modify:
            departure_city = input("Provide departure city: ")
            new_duration = int(input("Add a number of minutes(10-60): "))
            duration_increase(flights_dict, departure_city, new_duration)
        elif user_choice == menu_exit:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()


