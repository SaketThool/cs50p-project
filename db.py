import sqlite3
import csv
import sys
from pprint import pprint
from train import TrainRoute
from booking import Booking
from datetime import date

# It help us to create some necessary database files and table which help to run the program 
# It help to input the data in the table which import the data in the table 
def db_setup():

    # In this it connects with the sqlite3 database which connect to the database file which is been present in the file or need to be created in the file
    con = sqlite3.connect("train.db")
    cur = con.cursor() # cur is the corsor which help to read and write in the data base   
    
    setup_station_table(cur)  # This function use to store the station name and station code in the table  
    setup_routes_table(cur)   # This function use to store the train route details in the table
    setup_booking_table(cur)  # This function use to store the booking detail of the user in the table
    return con


def get_all_routes(con): # This function is use to get the route detail which is been inputed by the user both departure and arrival station

    cur = con.cursor()

    rows = cur.execute("SELECT * FROM routes").fetchall() # TODO

    # It store the detalis which the user input
    trains = []  
    for row in rows:
        train = TrainRoute(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
        trains.append(train)
    return trains


def save_booking(con, booking): # This function help to save the booking details of the user which is been input

    cur = con.cursor()

    #TODO
    cur.execute(
        "INSERT INTO bookings (route_id, date, name, age, gender, phone_number) VALUES(?, ?, ?, ?, ?, ?)",
        (
            booking.route.id,
            booking.date.isoformat(),
            booking.name,
            booking.age,
            booking.gender,
            booking.phone_number
        ),
    )
    cur.connection.commit()  #TODO

    return cur.lastrowid  #TODO

def number_booking_for_train_route_and_date(con, route, date):  #TODO

    cur = con.cursor()

    #TODO
    number_of_booking = cur.execute("SELECT COUNT(*) FROM bookings WHERE route_id = ? AND date = ?",(route.id, date.isoformat())).fetchone()[0]
    return number_of_booking

def get_booking(con, pnr): # This function help to get the booking information which is been stored in booking class

    cur = con.cursor()

    #TODO
    row = cur.execute("SELECT * FROM bookings WHERE pnr = ? ",(pnr,)).fetchone()
    if row:
        route = get_route(con, row[1])
        if not route:
            return None
        
        booking = Booking(
           route, date.fromisoformat(row[2]), row[3], row[4], row[5], row[6]
        )

        return booking
    
    else:
        return None
    
def get_route(con, route_id): # It help to get the id for the train detail which help to select the train user want to book

    cur = con.cursor()

    #TODO
    row = cur.execute("SELECT * FROM routes WHERE id = ? ",(route_id,)).fetchone()
    if row:
        route = TrainRoute(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )

        return route
    
    else:
        return None
    
def setup_station_table(cur):

    cur.execute("CREATE TABLE IF NOT EXISTS stations(code TEXT PRIMARY KEY, name TEXT)")
    no_of_stations = cur.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
    if no_of_stations == 0:
        try:
            with open("train_stations.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    cur.execute(
                        "INSERT INTO stations (code, name) VALUES(?, ?)",
                        (row["station_Code"], row["station_Name"]),
                    )
                cur.connection.commit()
        except FileNotFoundError:
            sys.exit("File does not exist")

def setup_routes_table(cur):

    cur.execute(
        "CREATE TABLE IF NOT EXISTS routes(id INTEGER PRIMARY KEY AUTOINCREMENT , number NUMBER , name TEXT , dep_station TEXT , arri_station TEXT , dep_time TEXT , arri_time TEXT , total_seats NUMBER , days_running TEXT )"
    )
    no_of_stations = cur.execute("SELECT COUNT(*) FROM routes").fetchone()[0]
    if no_of_stations == 0:
        try:
            with open("train_routes.csv", "r") as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    cur.execute(
                        "INSERT INTO routes (number, name, dep_station, arri_station, dep_time, arri_time, total_seats, days_running) VALUES(?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            row["train_No"],
                            row["train_Name"],
                            row["dep_station"],
                            row["arri_station"],
                            row["dep_time"],
                            row["arri_time"],
                            row["total_seats"],
                            row["days_running"],
                        ),
                    )
                cur.connection.commit()
        except FileNotFoundError:
            sys.exit("File does not exist")

def setup_booking_table(cur):

    cur.execute(
        "CREATE TABLE IF NOT EXISTS bookings(pnr INTEGER PRIMARY KEY AUTOINCREMENT, route_id INTEGER, date TEXT, name TEXT, age INTEGER, gender TEXT, phone_number TEXT, FOREIGN KEY (route_id) REFERENCES routes(id))"
    )
          