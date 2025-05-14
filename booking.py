# Here is the Booking class which store the booking information of the user
class Booking:
    def __init__(self, route, date, name, age, gender, phone_number):
        self.route = route
        self.date = date
        self.name = name
        self.age = age
        self.gender = gender
        self.phone_number = phone_number

    def __str__(self):  # This help to call the object when class is created
        return f"Your Booking is: {self.route} | Date: {self.date} | Name: {self.name} Age: {self.age} | Gender: {self.gender} | Phone Number: {self.phone_number}"
