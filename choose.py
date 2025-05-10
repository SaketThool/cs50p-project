import re
import survey

def choose_dep_station(departure_stations):  # This part is for choice of the departure station
    # while True:
    #     chosen_dep_station = input("Enter the DEPARTURE STATION: ").strip()
    #     if chosen_dep_station in departure_stations:
    #         break
    #     else:
    #         print("Invalid Station code")

    # return chosen_dep_station
    departure_stations_sorted = sorted(departure_stations)
    # This function help to give the chosen index in departure_station_sorted
    chosen_index = survey.routines.select("Enter the DEPARTURE STATION: ", options = departure_stations_sorted)
    return departure_stations_sorted[chosen_index] # In this we get the actual station code

def choose_arri_station(arrival_stations):   # this part is for choice of the arrival station
    
    arrival_stations_sorted = sorted(arrival_stations)
    chosen_index = survey.routines.select("Enter the ARRIVAL STATION: ", options = arrival_stations_sorted)
    return arrival_stations_sorted[chosen_index]

def choose_date(): # part is for input the date

    chosen_datetime = survey.routines.datetime("Enter your DATE for journey(YYYY-MM-DD): ", attrs = ("year", "month", "day"))
    return chosen_datetime.date()

def choose_route(available_routes):   # This part is for the choice of selecting the train with its information 
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

def choose_name(): # This part is for input of the name of the user
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

def choose_age():  # This part is for input of the age of the user
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

def choose_gender():  # This part is for the input of the gender of the user
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

def choose_phone_number():   # This part is for the input of the Phone Number of the User
    while True:
        try:
            passenger_phone_number = input("Enter your PHONE NUMBER(Start from 7 to 9 and 10 digits in total): ").strip()
            if not re.match(r"[7-9][0-9]{9}$", passenger_phone_number):
                raise ValueError
            break
        except ValueError:
            print("Invalid Phone Number")
            continue
    return passenger_phone_number

def choose_pnr():  # In this you will enter your PNR number which you will get after our booking
    while True:
        try:
            chosen_pnr = int(input("Enter your PNR Number: "))           
            break
        except ValueError:
            print("Invalid PNR")
            continue
    return chosen_pnr