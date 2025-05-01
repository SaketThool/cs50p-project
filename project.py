import pyfiglet
from db import db_setup, get_all_routes
from pprint import pprint
from datetime import date

def main():

    con = db_setup()

    figlet = pyfiglet.Figlet(font='slant')
    art = figlet.renderText("WELCOME")
    print(art)

    print("1. Book Your Train Ticket")
    print("2. Quit")

    while True:
        option = input("Enter the number you want choose\n")
        match (option.lower()):
            case "1":
                print("Welcome to our website")
                book_a_train(con)
                break

            case "2":
                print("Thank for visiting our website")
                break

def book_a_train(con):
    routes = get_all_routes(con)
    
    print("Here are all the arrival stations available")

    departure_stations = set()
    for route in routes:
        departure_stations.add(route.dep_station)
    departure_stations = sorted(departure_stations)
    pprint(departure_stations) # TODO proper print

    while True:
        chosen_dep_station = input("Enter the Departure Station: ").strip()
        if chosen_dep_station in departure_stations :
            break
        else:
            print("Invalid Station code")

    arrival_stations = set()
    for route in routes:
        if chosen_dep_station == route.dep_station:
            arrival_stations.add(route.arri_station)
    arri_stations = sorted(arrival_stations)
    pprint(arrival_stations) # TODO proper print

    while True:
        chosen_arri_station = input("Enter the Arrival Station: ").strip()
        if chosen_arri_station in arrival_stations :
            break
        else:
            print("Invalid Station code")

    while True:
        chosen_date_string = input("Enter your date for journey(YYYY-MM-DD): ").strip()

        try:
            chosen_date = date.fromisoformat(chosen_date_string)
            break
        except ValueError:
            print("Invalid date")
            continue
           
if __name__ == "__main__":
    main()