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
    cur = (
        con.cursor()
    )  # cur is the cursor which help to read and write in the data base

    setup_station_table(cur)
    setup_routes_table(cur)
    setup_booking_table(cur)
    return con


# This function is used to get all the route detail. This will be used later by the user to choose both departure and arrival station
def get_all_routes(con):

    cur = con.cursor()

    rows = cur.execute(
        "SELECT * FROM routes"
    ).fetchall()  # In this we get all the rows and columns from the route table.'*' means all columns.

    # To make code easier to understand and get details easily
    # Instead of returning this rows = [[1, "34343", "duronto","NGP", "CSMT", ....], [2, "34343",  "pro"]]
    # It returns [TrainRoute, TrainRoute]
    # Instead of doing route[3] you can do route.dep_station
    # It convert database row in one train object
    trains = []  #
    for row in rows:
        train = TrainRoute(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
        trains.append(train)
    return trains

def get_all_stations(con):

    cur = con.cursor()

    rows = cur.execute(
        "SELECT * FROM stations"
    ).fetchall()  # In this we get all the rows and columns from the route table.'*' means all columns.

    stations = {}  
    for row in rows:
       stations[row[0]] = row[1]
    return stations

def save_booking(
    con, booking
):  # This function help to save the booking details of the user which is been input and give back PNR
    cur = con.cursor()

    cur.execute(
        "INSERT INTO bookings (route_id, date, name, age, gender, phone_number) VALUES(?, ?, ?, ?, ?, ?)",
        (
            booking.route.id,
            booking.date.isoformat(),
            booking.name,
            booking.age,
            booking.gender,
            booking.phone_number,
        ),
    )
    cur.connection.commit()

    return (
        cur.lastrowid
    )  # The primary key of the table is PNR which is automatically created
    # The gives the last newly created primary key(PNR)


# It tells us that how many booking are there for the specific route and specific date that day
def number_bookings_for_train_route_and_date(con, route, date):

    cur = con.cursor()

    # In this we wil count the number of booking present for that route and for that day(WHERE is a limit)
    number_of_booking = cur.execute(
        "SELECT COUNT(*) FROM bookings WHERE route_id = ? AND date = ?",
        (route.id, date.isoformat()),
    ).fetchone()[0]
    return number_of_booking


def get_booking(
    con, pnr
):  # This function help to get the booking information for the chosen PNR that has been stored in booking table
    cur = con.cursor()

    # In this we get all column and we get only 1 row that has the PNR
    row = cur.execute("SELECT * FROM bookings WHERE pnr = ? ", (pnr,)).fetchone()
    if row:  # If we find a booking with given PNR it will continue
        route = get_route(con, row[1])  # row[1] is a route_id
        if not route:
            return None

        # It convert the database row to booking object
        booking = Booking(
            route,
            date.fromisoformat(
                row[2]
            ),  # row[2] is a string(yyyy-mm-dd) convert into the python date object
            row[3],
            row[4],
            row[5],
            row[6],
        )

        return booking

    else:  # No booking with the PNR found
        return None


def get_route(con, route_id):  # It help to get the train detail for route with route id

    cur = con.cursor()

    row = cur.execute("SELECT * FROM routes WHERE id = ? ", (route_id,)).fetchone()
    if row:
        route = TrainRoute(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )

        return route

    else:
        return None


def setup_station_table(
    cur,
):  # This function use to store the station name and station code in the table

    cur.execute("CREATE TABLE IF NOT EXISTS stations(code TEXT PRIMARY KEY, name TEXT)")
    # This counts the number of row in the table. Fetchone gives one row instead of list of rows
    no_of_stations = cur.execute("SELECT COUNT(*) FROM stations").fetchone()[0]
    if no_of_stations == 0:
        try:
            with open(
                "train_stations.csv", "r"
            ) as csvfile:  # This line opens the file object
                reader = csv.DictReader(csvfile)  # The file object open as a csvfile

                # In this every csvrow will be converted into database table row
                for row in reader:
                    cur.execute(
                        "INSERT INTO stations (code, name) VALUES(?, ?)",
                        (row["station_Code"], row["station_Name"]),
                    )
                cur.connection.commit()  # This will run all the above sql in one run to make it faster
        except FileNotFoundError:
            sys.exit("File does not exist")


def setup_routes_table(
    cur,
):  # This function use to store the train route details in the table

    cur.execute(
        "CREATE TABLE IF NOT EXISTS routes(id INTEGER PRIMARY KEY AUTOINCREMENT , number NUMBER , name TEXT , dep_station TEXT , arri_station TEXT , dep_time TEXT , arri_time TEXT , total_seats NUMBER , days_running TEXT )"
    )  # Autoincrement automatically add id for new row
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


def setup_booking_table(
    cur,
):  # This function use to store the booking detail of the user in the table

    cur.execute(
        "CREATE TABLE IF NOT EXISTS bookings(pnr INTEGER PRIMARY KEY AUTOINCREMENT, route_id INTEGER, date TEXT, name TEXT, age INTEGER, gender TEXT, phone_number TEXT, FOREIGN KEY (route_id) REFERENCES routes(id))"
    )  # route_id belongs to another table called route and route_id points to one row in the route table
