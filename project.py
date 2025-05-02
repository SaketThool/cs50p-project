import pyfiglet
import sys
from db import db_setup, get_all_routes
from pprint import pprint
from datetime import date


WEEKDAYS = {0:"mon",
            1:"tue",
            2:"wed",
            3:"thu",
            4:"fri",
            5:"sat",
            6:"sun"
}


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
        chosen_dep_station = input("Enter the DEPARTURE STATION: ").strip()
        if chosen_dep_station in departure_stations :
            break
        else:
            print("Invalid Station code")

    arrival_stations = set()
    for route in routes:
        if chosen_dep_station == route.dep_station:
            arrival_stations.add(route.arri_station)
    arri_stations = sorted(arrival_stations)
    pprint(arrival_stations) # TODO proper print , print full station name , use survey package

    while True:
        chosen_arri_station = input("Enter the ARRIVAL STATION: ").strip()
        if chosen_arri_station in arrival_stations :
            break
        else:
            print("Invalid Station code")

    while True:
        chosen_date_string = input("Enter your DATE for journey(YYYY-MM-DD): ").strip()

        try:
            chosen_date = date.fromisoformat(chosen_date_string)
            break
        except ValueError:
            print("Invalid date")
            continue

    chosen_weekday = WEEKDAYS[chosen_date.weekday()]


    available_routes = []# TODO check the available seats
    for route in routes:
        if chosen_dep_station == route.dep_station and chosen_arri_station == route.arri_station and chosen_weekday in route.days_running:
            available_routes.append(route)
    if len(available_routes) == 0:
        sys.exit("Trains are not available")
    # TODO to print it nicely like pizza.py , print all information of train
    for i,route in enumerate(available_routes):
        print(f"{i}: {route}") # TODO print number of seats free

    while True:
    
        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (chosen_route_number >= 0 and chosen_route_number < len(available_routes)):
            #if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    print(chosen_route_number)## TODO name, age, gender, ph. number
    chosen_route = available_routes[chosen_route_number]


    # NAME
    username = []
    while True:
    
        try:
            passanger_name = int(input("Enter your NAME: "))
            if not (passanger_name >= 0 and passanger_name < len(username)):
            #if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    print(passanger_name)

    #AGE
    while True:
    
        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (chosen_route_number >= 0 and chosen_route_number < len(available_routes)):
            #if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    print(chosen_route_number)

    #GENDER
    while True:
    
        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (chosen_route_number >= 0 and chosen_route_number < len(available_routes)):
            #if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    print(chosen_route_number)

    #PHONE NUMBER
    while True:
    
        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (chosen_route_number >= 0 and chosen_route_number < len(available_routes)):
            #if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    print(chosen_route_number)



if __name__ == "__main__":
    main()