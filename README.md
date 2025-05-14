# CS50P Project: BookMyTrain
My final project for the CS50P Python course.

#### Video Demo: https://youtu.be/3VgocstiDVg


# How to run program
* install dependencies: `$ pip install -r requirements.txt`
* Run program: `$ python project.py`

# What My Program Does
* First the menu appear with a greeting WELCOME and give you three options to choose `Book Your Train Ticket`, `View Booking` and `Quit`. If user want to book the ticket they want to press `1` and if they already book the ticket so they need to enter `2` for viewing there booking and if they want to quit the program then press `3`. 

* For booking the ticket user input `1` and they got the list of departure station to choose where you need to go from. `Write` or use `up or down arrow` to choose departure station. After that you will get another list for arrival station to choose where you need to go to. `Write` or `use up or down arrow` to choose arrival station. After that you need to Enter the date of journey when you need to go to your destination. Then you will get a table of few train name with its `Row Number`, `Train Number`, `Train Name`, `Departure Station`, `Arrival Station`, `Departure Time`, `Arrival Time`, `Seats Available` and `Days Running` and you need to choose the row number to choose the train for booking. Then User need to input some details like `Name`, `Age`, `Gender` and `Phone Number`. After that at final you will get your PNR Number which will help user to view there booking.

* For viewing the booking done by user user need to input `2`. Then it will ask user to input there PNR Number which is been given by after booking the ticket. After user input the PNR Number they will see the table which contain `PNR Number`, `Date`, `Train Number`, `Train Name`, `User Name`, `age`, `Gender` and `Phone Number` they entered while giving there details

* For exiting the project user need to input `3` to Quit the Project.

# How Does It Work
* I use different packages to to run my project. I use `Figlet` to make Welcome in big slant font, then I use `datetime` package to to get current date and time, then I use `tabulate` to print some details in table and finally use `sys` to access some interpreter and variable. I use some database like `sqlite3` in my project and as we cannot store the data in git so I use `CSV` to store data of the database which help me to use the database in the product. The complex part of the project to calculate the details of the user in the table and see the available seats in the booking if the booking is been done to remove the seats to get free seats available. I use `survey` library to ask user for departure and arrival station good. Then finally used `black` to format the code.

## File Descriptions

* `README.md`: In this I Write about my project what my program does and how does it work 
* `booking.py`: In this I created the booking object to get booking information to user  
* `choose.py`: In this I created choice for the user to input  
* `db.py`: In this all the database work is been done  
* `project.py`: This is the main part of the project    
* `requirements.txt`: in this all the requirement is been stored
* `test_project.py`: In this the test cases for this project is been written  
* `train.db`: In this all the table is been stored with the help of csv  
* `train.py`: In this all the train details is been stored
* `train_routes.csv`: In this all the routes with name and code of station is been stored using csv  
* `train_stations.csv`: In this all the station is been stored in the csv


## Train Resources
* https://www.prokerala.com/travel/indian-railway/maharashtra-stations/
* https://indiarailinfo.com/
