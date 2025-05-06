import pyfiglet
import sys
import re
from db import db_setup, get_all_routes, save_booking
from pprint import pprint
from datetime import date
from booking import Booking

TEST = False

WEEKDAYS = {0: "mon", 1: "tue", 2: "wed", 3: "thu", 4: "fri", 5: "sat", 6: "sun"}


def main():

    global TEST
    if len(sys.argv) == 2 and sys.argv[1] == "-t":
        TEST = True

    con = db_setup()

    figlet = pyfiglet.Figlet(font="slant")
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


def choose_dep_station(departure_stations):
    while True:
        chosen_dep_station = input("Enter the DEPARTURE STATION: ").strip()
        if chosen_dep_station in departure_stations:
            break
        else:
            print("Invalid Station code")

    return chosen_dep_station


def choose_arri_station(arrival_stations):
    while True:
        chosen_arri_station = input("Enter the ARRIVAL STATION: ").strip()
        if chosen_arri_station in arrival_stations:
            break
        else:
            print("Invalid Station code")

    return chosen_arri_station


def choose_date():
    while True:
        chosen_date_string = input("Enter your DATE for journey(YYYY-MM-DD): ").strip()

        try:
            chosen_date = date.fromisoformat(chosen_date_string)
            break
        except ValueError:
            print("Invalid date")
            continue

    return chosen_date


def choose_route_number(available_routes):
    while True:

        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (
                chosen_route_number >= 0 and chosen_route_number < len(available_routes)
            ):
                # if chosen_route_number < 0 or chosen_route_number >= len(available_routes):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue

    return chosen_route_number


def choose_name():

    # NAME
    while True:

        try:
            passanger_name = input("Enter your NAME: ").strip()
            if len(passanger_name) == 0:

                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue

    return passanger_name


def choose_age():

    # AGE
    while True:

        try:
            passanger_age = int(input("Enter your AGE: "))
            if passanger_age <= 3:

                raise ValueError
            break
        except ValueError:
            print("Invalid age")
            continue

        return passanger_age


def choose_gender():

    # GENDER
    while True:

        try:
            passanger_gender = input("Enter your GENDER[M/F/O]: ").strip()
            if passanger_gender not in ["M", "F", "O"]:

                raise ValueError
            break
        except ValueError:
            print("Invalid Gender")
            continue

    return passanger_gender


def choose_phone_number():

    # PHONE NUMBER
    while True:

        try:
            passanger_phone_number = input("Enter your PHONE NUMBER: ").strip()
            if not re.match(r"[7-9][0-9]{9}", passanger_phone_number):

                raise ValueError
            break
        except ValueError:
            print("Invalid Phone Number")
            continue

    return passanger_phone_number


def book_a_train(con):
    routes = get_all_routes(con)
    if TEST:

        chosen_dep_station = "NGP"

        chosen_arri_station = "CSMT"

        chosen_date = date.fromisoformat("2025-07-21")

        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_routes = []  # TODO check the available seats
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

        passanger_name = "saket"
        passanger_age = 17
        passanger_gender = "M"
        passanger_phone_number = "9988776655"

    else:

        print("Here are all the arrival stations available")

        departure_stations = set()
        for route in routes:
            departure_stations.add(route.dep_station)
        departure_stations = sorted(departure_stations)
        pprint(departure_stations)  # TODO proper print

        chosen_dep_station = choose_dep_station(departure_stations)

        arrival_stations = set()
        for route in routes:
            if chosen_dep_station == route.dep_station:
                arrival_stations.add(route.arri_station)
        arri_stations = sorted(arrival_stations)
        pprint(
            arrival_stations
        )  # TODO proper print , print full station name , use survey package

        chosen_arri_station = choose_arri_station(arrival_stations)

        chosen_date = choose_date()

        chosen_weekday = WEEKDAYS[chosen_date.weekday()]

        available_routes = []  # TODO check the available seats
        for route in routes:
            if (
                chosen_dep_station == route.dep_station
                and chosen_arri_station == route.arri_station
                and chosen_weekday in route.days_running
            ):
                available_routes.append(route)
        if len(available_routes) == 0:
            sys.exit("Trains are not available")
        # TODO to print it nicely like pizza.py , print all information of train
        for i, route in enumerate(available_routes):
            print(f"{i}: {route}")  # TODO print number of seats free

        chosen_route_number = choose_route_number(available_routes)

        print(chosen_route_number)  ## TODO name, age, gender, ph. number
        chosen_route = available_routes[chosen_route_number]

        passanger_name = choose_name()
        passanger_age = choose_age()
        passanger_gender = choose_gender()
        passanger_phone_number = choose_phone_number()

    booking = Booking(
        chosen_route,
        passanger_name,
        passanger_age,
        passanger_gender,
        passanger_phone_number,
    )

    save_booking(con, booking)


if __name__ == "__main__":
    main()
