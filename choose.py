import re
import survey


def choose_dep_station(
    departure_stations, full_stations
):  # This part is for choice of the departure station
    # while True:
    #     chosen_dep_station = input("Enter the DEPARTURE STATION: ").strip()
    #     if chosen_dep_station in departure_stations:
    #         break
    #     else:
    #         print("Invalid Station code")

    # return chosen_dep_station
    departure_stations_sorted = sorted(departure_stations)
    station_to_display = []
    for station in departure_stations_sorted:
        fullstation = f"{full_stations[station]} ({station})"
        station_to_display.append(fullstation)
    # This function help to give the chosen index in departure_station_sorted
    chosen_index = survey.routines.select(
        "Enter the DEPARTURE STATION: ", options=station_to_display
    )
    # In this we get the actual station code
    return departure_stations_sorted[chosen_index]


# this part is for choice of the arrival station
def choose_arri_station(arrival_stations, full_stations):

    arrival_stations_sorted = sorted(arrival_stations)
    station_to_display = []
    for station in arrival_stations_sorted:
        fullstation = f"{full_stations[station]} ({station})"
        station_to_display.append(fullstation)
    chosen_index = survey.routines.select(
        "Enter the ARRIVAL STATION: ", options=station_to_display
    )
    return arrival_stations_sorted[chosen_index]


# part is for input the date
def choose_date():

    chosen_datetime = survey.routines.datetime(
        "Enter your DATE for journey(YYYY-MM-DD): ", attrs=("year", "month", "day")
    )
    return chosen_datetime.date()


# This part is for the choice of selecting the train with its information
def choose_route(
    available_routes,
):
    while True:
        try:
            chosen_route_number = int(input("Enter ROW number to book your train: "))
            if not (0 <= chosen_route_number < len(available_routes)):
                raise ValueError
            break
        except ValueError:
            print("Invalid choice")
            continue
    chosen_route = available_routes[chosen_route_number]
    return chosen_route


# This part is for input of the name of the user
def choose_name():
    while True:
        try:
            passenger_name = input("Enter your NAME: ").strip()
            if len(passenger_name) == 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid Name")
            continue
    return passenger_name


# This part is for input of the age of the user
def choose_age():
    while True:
        try:
            passenger_age = int(input("Enter your AGE: "))
            if passenger_age <= 3:
                print("Too Young")
                raise ValueError
            break
        except ValueError:
            print("Invalid age")
            continue
    return passenger_age


# This part is for the input of the gender of the user
def choose_gender():
    while True:
        try:
            passenger_gender = input("Enter your GENDER[M/F/O]: ").strip()
            if passenger_gender not in ["M", "F", "O"]:
                raise ValueError
            break
        except ValueError:
            print("Invalid Gender")
            continue
    return passenger_gender


# This part is for the input of the Phone Number of the User
def choose_phone_number():
    while True:
        try:
            passenger_phone_number = input(
                "Enter your PHONE NUMBER(Start from 7 to 9 and 10 digits in total): "
            ).strip()
            if not re.match(r"[7-9][0-9]{9}$", passenger_phone_number):
                raise ValueError
            break
        except ValueError:
            print("Invalid Phone Number")
            continue
    return passenger_phone_number


# In this you will enter your PNR number which you will get after our booking
def choose_pnr():
    while True:
        try:
            chosen_pnr = int(input("Enter your PNR Number: "))
            break
        except ValueError:
            print("Invalid PNR")
            continue
    return chosen_pnr
