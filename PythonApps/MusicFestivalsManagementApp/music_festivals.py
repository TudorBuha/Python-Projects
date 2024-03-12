
def get_festivals():
    return [
        {"name": "Untold", "month": 1, "ticket_cost": 123, "artists": ["Puya", "Salam"]},
        {"name": "Neversea", "month": 2, "ticket_cost": 321, "artists": ["Cerebel", "VladCenuse"]},
        {"name": "Electric Castle", "month": 3, "ticket_cost": 456, "artists": ["Tudor", "Mihaita"]},
        {"name": "Summer Well", "month": 4, "ticket_cost": 789, "artists": ["Mihnea", "Tudor"]},
        {"name": "Jazz in the Park", "month": 5, "ticket_cost": 987, "artists": ["Mara", "Eduarda"]},
        {"name": "Rockstadt Extreme Fest", "month": 6, "ticket_cost": 654, "artists": ["Andrei", "Alex"]},
        {"name": "Awake", "month": 7, "ticket_cost": 321, "artists": ["Chisu", "Robert"]},
        {"name": "Summer Well", "month": 8, "ticket_cost": 123, "artists": ["Cora", "Ionut"]},
        {"name": "X", "month": 9, "ticket_cost": 456, "artists": ["Voievod", "Paul"]},
        {"name": "Y", "month": 10, "ticket_cost": 789, "artists": ["Ovidiu", "Marius"]},
        {"name": "K", "month": 12, "ticket_cost": 789, "artists": ["Ovidiu", "Marius"]},
        {"name": "Z", "month": 11, "ticket_cost": 987, "artists": ["Cristina", "Cristinel"]},
        {"name": "E", "month": 12, "ticket_cost": 654, "artists": ["Cartof", "Tudor"]},
        {"name": "D", "month": 12, "ticket_cost": 654, "artists": ["Cartof", "Tudor"]},
        {"name": "C", "month": 12, "ticket_cost": 654, "artists": ["Cartof", "Tudor"]}
    ]


def display_festivals(festivals_to_display):
    index = 1
    for festival in festivals_to_display:
        print(f"{index}.{festival['name']} (Month: {festival['month']}), "
              f"Ticket Cost: {festival['ticket_cost']}, Artists: {', '.join(festival['artists'])}")
        index += 1

def add_festival(festivals: list):
    try:
        name = input("Enter festival name: ")
        month = int(input("Enter month (1-12): "))
        if month < 1 or month > 12:
            raise ValueError("Month should be in the interval [1,12]")

        # check for duplicate festival names
        for festival in festivals:
            if festival["name"] == name:
                raise ValueError("Festival with the same name already exists")

        ticket_cost = int(input("Enter ticket cost: "))
        artists = input("Enter artists (comma-separated): ").split(',')

        festivals.append({"name": name, "month": month, "ticket_cost": ticket_cost, "artists": artists})
        print("Festival added successfully!")
    except ValueError as ve:
        print(ve)

def show_season_festivals(season: list, festivals: list):

    festivals_in_season = []
    months_in_season = {"winter":[12, 1, 2], "spring": [3, 4, 5], "summer": [6, 7, 8], "autumn": [9, 10, 11]}
    for festival in festivals:
        if festival["month"] in months_in_season[season]:
            festivals_in_season.append(festival)
    festivals_in_season.sort(key=lambda festival: (festival["month"], festival["name"])) #lambda poate fi folosit cu mai multe key


    display_festivals(festivals_in_season)

def show_artist_festivals(artist_name, festivals: list):
    artists_festival = []
    for festival in festivals:
        if artist_name in festival["artists"]:
            artists_festival.append(festival)

    artists_festival.sort(key=lambda festival: festival["month"])

    display_festivals(artists_festival)




def main():
    festivals = get_festivals()
    while True:
            print("\n")
            print(" Menu:")
            print("1. Display all festivals")
            print("2. Add a music festival")
            print("3. Show festivals in a season")
            print("4. Show festivals with a given artist")
            print("5. Exit")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                display_festivals(festivals)
            elif choice == "2":
                add_festival()
            elif choice == "3":
                season = input("Enter season (winter/spring/summer/autumn): ")
                show_season_festivals(season, festivals)
            elif choice == "4":
                artist_name = input("Enter artist name: ")
                show_artist_festivals(artist_name, festivals)
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()