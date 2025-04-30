import pyfiglet
from db import db_setup, get_all_routes
from pprint import pprint

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
    
    print("Here are all the departure stations available")

    departure_stations = []
    for route in routes:
        departure_stations.append(route.dep_station)
    pprint(departure_stations)
if __name__ == "__main__":
    main()