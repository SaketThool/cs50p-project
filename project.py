import pyfiglet
def main():


    figlet = pyfiglet.Figlet(font='slant')
    art = figlet.renderText("WELCOME")
    print(art)

    print("1. Book Your Train Ticket")
    print("2. Quit")



if __name__ == "__main__":
    main()