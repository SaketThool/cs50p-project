import pyfiglet
import sys
from db import (
    db_setup,
    get_all_routes,
    save_booking,
    number_bookings_for_train_route_and_date,
    get_booking,
    get_all_stations,
)
from pprint import pprint
from datetime import date
from booking import Booking
from tabulate import tabulate
from choose import (
    choose_dep_station,
    choose_arri_station,
    choose_date,
    choose_route,
    choose_name,
    choose_age,
    choose_gender,
    choose_phone_number,
    choose_pnr,
)

# This helps to run the project without prompting the input from the user
TEST = False

# Here are weekdays stored in weekdays in a dict where key is the week number.
WEEKDAYS = {0: "mon", 1: "tue", 2: "wed", 3: "thu", 4: "fri", 5: "sat", 6: "sun"}


def main():
    # In this it helps us to test the booking section.
    # It automatically set the booking values.
    global TEST
    if len(sys.argv) == 2 and sys.argv[1] == "-t":
        TEST = True

    # Setting up the table
    # con is the connection which help to connect with the database whenever it is been required in the project
    con = db_setup()

    # This is the figlet which make it little attractive
    figlet = pyfiglet.Figlet(font="slant")
    art = figlet.renderText("WELCOME :)")
    print(art)

    # Here are the option to choose
    print("1. Book Your Train Ticket")
    print("2. View Booking")
    print("3. Quit")

    # In this it ask for the choice and greet you with some message
    while True:
        option = input("Enter the number you want choose:\n")
        match (option.lower()):
            case "1":
                print("Welcome to the booking site.")
                book_a_train(con)
                break

            case "2":
                print("Welcome to the view booking site.")
                # In this you will review your booking with the help of PNR number
                view_your_booking(con)
                break

            case "3":
                print("Thank for visiting our website.")
                break
    con.close()


# It collect all the departure station without duplicate(The set removes the duplicate)
def all_departure_stations(
    routes,
):
    departure_stations = set()
    for route in routes:
        departure_stations.add(route.dep_station)
    departure_stations_sorted = sorted(departure_stations)
    return departure_stations_sorted


def all_arrival_stations(routes, chosen_dep_station):
    # It collect all the arrival station without duplicate(The set removes the duplicate)
    # that we can travel from chosen departure station
    arrival_stations = set()
    for route in routes:
        if route.dep_station == chosen_dep_station:
            arrival_stations.add(route.arri_station)
    arrival_stations_sorted = sorted(arrival_stations)
    return arrival_stations_sorted


def find_available_routes(
    routes, chosen_dep_station, chosen_arri_station, chosen_weekday, available_seats
):
    # In this we finds all the routes that matches for departure, arrival and free seats available for that day
    available_routes = []
    for route in routes:
        if (
            chosen_dep_station == route.dep_station
            and chosen_arri_station == route.arri_station
            and chosen_weekday in route.days_running
            and available_seats[route.id] > 0
        ):
            available_routes.append(route)
    return available_routes


# this function help to book the ticket
def book_a_train(con):
    routes = get_all_routes(con)

    full_stations = get_all_stations(con)

    # This part help to test the project with the help of command line argument.
    # It dont ask user the input to make it quickly with same input all the time
    if TEST:

        chosen_dep_station = "NGP"
        chosen_arri_station = "CSMT"
        chosen_date = date.fromisoformat("2025-07-21")
        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_seats = {}
        for route in routes:
            # In this we are finding the free seats for this route and chosen day
            available_seats[route.id] = (
                route.total_seats
                - number_bookings_for_train_route_and_date(con, route, chosen_date)
            )

        available_routes = find_available_routes(
            routes,
            chosen_dep_station,
            chosen_arri_station,
            chosen_weekday,
            available_seats,
        )
        if len(available_routes) == 0:
            sys.exit("Trains are not available")

        chosen_route_number = 0
        chosen_route = available_routes[chosen_route_number]

        passenger_name = "saket"
        passenger_age = 17
        passenger_gender = "M"
        passenger_phone_number = "9988776655"

    # This part help to get input from the user
    else:
        departure_stations = all_departure_stations(routes)
        chosen_dep_station = choose_dep_station(departure_stations, full_stations)

        arrival_stations = all_arrival_stations(routes, chosen_dep_station)
        chosen_arri_station = choose_arri_station(arrival_stations, full_stations)

        chosen_date = choose_date()
        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_seats = {}
        for route in routes:
            # In this we are finding the free seats for this route and chosen day
            available_seats[route.id] = (
                route.total_seats
                - number_bookings_for_train_route_and_date(con, route, chosen_date)
            )

        available_routes = find_available_routes(
            routes,
            chosen_dep_station,
            chosen_arri_station,
            chosen_weekday,
            available_seats,
        )

        if len(available_routes) == 0:
            sys.exit("Trains are not available. Please try Again :)")

        # In this preparing a table for user to select the route to book
        available_routes_to_print = []
        for i, route in enumerate(available_routes):
            # Go through each route with the index of the route
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
                "Days Running": route.days_running,
            }
            available_routes_to_print.append(print_route)
        print(tabulate(available_routes_to_print, headers="keys", tablefmt="grid"))
        chosen_route = choose_route(available_routes)

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

    # This save the booking to database and get a PNR number
    pnr = save_booking(con, booking)
    print(f"Thank you for your booking :), here is your PNR number: {pnr}")


# In this part the user will enter PNR and view its booking
def view_your_booking(con):

    chosen_pnr = choose_pnr()
    booking = get_booking(con, chosen_pnr)
    if not booking:
        sys.exit("Invalid PNR")

    booking_to_print = [
        {
            "PNR": chosen_pnr,
            "Date": booking.date,
            "Train Number": booking.route.number,
            "Train Name": booking.route.name,
            "Name": booking.name,
            "Age": booking.age,
            "Gender": booking.gender,
            "Phone Number": booking.phone_number,
        }
    ]
    print(tabulate(booking_to_print, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()
