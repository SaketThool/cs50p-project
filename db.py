import sqlite3
import csv

def db_setup():

    con = sqlite3.connect("train.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS stations(code TEXT PRIMARY KEY, name TEXT)")

    try:
        with open("train_stations.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                cur.execute("INSERT INTO stations (code, name) VALUES(?, ?)", (row["station_Code"], row["station_Name"]))
            cur.connection.commit()
    except FileNotFoundError:
        sys.exit("File does not exist")