class Booking:
    def __init__(self, route, date, name, age, gender, phone_number):

        # self.id = id_no
        self.route = route
        self.date = date
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def __str__(self):

        return f"Your route is: {self.route} | Date: {self.date} | Name: {self.name} Age: {self.age} | Gender: {self.gender} | Phone Number: {self.phone_number}"
