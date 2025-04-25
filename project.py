import pyfiglet
from db import db_setup
def main():

    db_setup()

    # figlet = pyfiglet.Figlet(font='slant')
    # art = figlet.renderText("WELCOME")
    # print(art)

    # print("1. Book Your Train Ticket")
    # print("2. Quit")

    # while True:
    #     option = input("Enter the number you want choose\n")
    #     match (option.lower()):
    #         case "1":
    #             print("Welcome to our website")
    #             break
    #         case "2":
    #             print("Thank for visiting our website")
    #             break



if __name__ == "__main__":
    main()