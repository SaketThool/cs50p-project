import pyfiglet
import sys
from db import db_setup, get_all_routes, save_booking, number_booking_for_train_route_and_date, get_booking
from pprint import pprint
from datetime import date
from booking import Booking
from tabulate import tabulate
from choose import choose_dep_station, choose_arri_station, choose_date, choose_route_number, choose_name, choose_age, choose_gender, choose_phone_number,choose_pnr

TEST = False

WEEKDAYS = {0: "mon", 1: "tue", 2: "wed", 3: "thu", 4: "fri", 5: "sat", 6: "sun"}


def main():

    global TEST
    if len(sys.argv) == 2 and sys.argv[1] == "-t":
        TEST = True

    con = db_setup()

    figlet = pyfiglet.Figlet(font="slant")
    art = figlet.renderText("WELCOME :)")
    print(art)

    print("1. Book Your Train Ticket")
    print("2. View Booking")
    print("3. Quit")

    while True:
        option = input("Enter the number you want choose:\n")
        match (option.lower()):
            case "1":
                print("Welcome to the booking site.")
                book_a_train(con)
                break

            case "2":
                print("Welcome to the view booking site.")
                view_your_booking(con)
                break

            case "3":
                print("Thank for visiting our website.")
                break
    con.close()
    
def book_a_train(con):
    routes = get_all_routes(con)
    if TEST:

        chosen_dep_station = "NGP"

        chosen_arri_station = "CSMT"

        chosen_date = date.fromisoformat("2025-07-21")

        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_routes = []  
        for route in routes:
            if (
                chosen_dep_station == route.dep_station
                and chosen_arri_station == route.arri_station
                and chosen_weekday in route.days_running
            ):
                available_routes.append(route)
        if len(available_routes) == 0:
            sys.exit("Trains are not available")

        chosen_route_number = 0

        chosen_route = available_routes[chosen_route_number]

        passenger_name = "saket"
        passenger_age = 17
        passenger_gender = "M"
        passenger_phone_number = "9988776655"

    else:

        departure_stations = set()
        for route in routes:
            departure_stations.add(route.dep_station)
        departure_stations_sorted = sorted(departure_stations)
        chosen_dep_station = choose_dep_station(departure_stations_sorted)

        arrival_stations = set()
        for route in routes:
            if chosen_dep_station == route.dep_station:
                arrival_stations.add(route.arri_station)
        arrival_stations_sorted = sorted(arrival_stations)
        chosen_arri_station = choose_arri_station(arrival_stations_sorted)

        chosen_date = choose_date()
        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_routes = []
        available_seats = {}  
        for route in routes:
            available_seats[route.id] = route.total_seats - number_booking_for_train_route_and_date(con, route, chosen_date) 
            if (
                chosen_dep_station == route.dep_station
                and chosen_arri_station == route.arri_station
                and chosen_weekday in route.days_running
                and available_seats[route.id] > 0
            ):
                available_routes.append(route)
        if len(available_routes) == 0:
            sys.exit("Trains are not available")
        
        available_routes_to_print = []
        for i, route in enumerate(available_routes):
            # print(f"{i}: {route}, {available_seats[route.id]}")  
            print_route = {
                "Row Number": i,
                "Train Number": route.number,
                "Train Name": route.name,
                "Departure Station": route.dep_station,
                "Arrival Station": route.arri_station,
                "Departure Time": route.dep_time,
                "Arrival Time": route.arri_time,
                "Seats Available": available_seats[route.id],
                "Days Running": route.days_running
            }
            available_routes_to_print.append(print_route)
        print(tabulate(available_routes_to_print, headers="keys", tablefmt="grid"))

        chosen_route_number = choose_route_number(available_routes)
        chosen_route = available_routes[chosen_route_number]

        passenger_name = choose_name()
        passenger_age = choose_age()
        passenger_gender = choose_gender()
        passenger_phone_number = choose_phone_number()

    booking = Booking(
        chosen_route,
        chosen_date,
        passenger_name,
        passenger_age,
        passenger_gender,
        passenger_phone_number,
    )

    
    pnr = save_booking(con, booking)
    print(f"Thank you for your booking :), here is your PNR number: {pnr}")

def view_your_booking(con):

    chosen_pnr = choose_pnr()
    booking = get_booking(con, chosen_pnr)
    if not booking:
        sys.exit("Invalid PNR")

    booking_to_print = [{
        "PNR": chosen_pnr,
        "Date": booking.date,
        "Train Number": booking.route.number,
        "Train Name": booking.route.name,
        "Name": booking.name,
        "Age": booking.age,
        "Gender": booking.gender,
        "Phone Number": booking.phone_number
    }]
    print(tabulate(booking_to_print, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
