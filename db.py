import sqlite3
import csv
from train import TrainRoute


def db_setup():

    con = sqlite3.connect("train.db")
    cur = con.cursor()

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

    cur.execute(
        "CREATE TABLE IF NOT EXISTS bookings(pnr INTEGER PRIMARY KEY AUTOINCREMENT, route_id INTEGER, date TEXT, name TEXT, age INTEGER, gender TEXT, phone_number TEXT, FOREIGN KEY (route_id) REFERENCES routes(id))"
    )
    return con


def get_all_routes(con):

    cur = con.cursor()

    rows = cur.execute("SELECT * FROM routes").fetchall()

    trains = []
    for row in rows:
        train = TrainRoute(
            row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]
        )
        trains.append(train)
    return trains


def save_booking(con, booking):

    cur = con.cursor()

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
    cur.connection.commit()

    return cur.lastrowid

def number_booking_for_train_route_and_date(con, route, date):

    cur = con.cursor()

    number_of_booking = cur.execute("SELECT COUNT(*) FROM bookings WHERE route_id = ? AND date = ?",(route.id, date.isoformat())).fetchone()[0]
    return number_of_booking