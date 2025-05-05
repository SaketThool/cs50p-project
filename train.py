class TrainRoute:
    def __init__(
        self,
        id_no,
        number,
        name,
        dep_station,
        arri_station,
        dep_time,
        arri_time,
        total_seats,
        days_running,
    ):

        self.id = id_no
        self.number = number
        self.name = name
        self.dep_station = dep_station
        self.arri_station = arri_station
        self.dep_time = dep_time
        self.arri_time = arri_time
        self.total_seats = total_seats
        self.days_running = days_running

    def __str__(self):

        return f"train with train id: {self.id} | train number: {self.number} | train name: {self.name}"
