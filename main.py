from colored import Fore, Back, Style

from classes.carpark import Carpark
from functions.carpark_functions import add_slot, list_slots, delete_slot, park_car

print(f"{Fore.yellow}{Back.red}Welcome to the Carpark Application!!!{Style.reset}\n")

def create_menu():
    print("Enter 1 to add a parking slot.")
    print("Enter 2 to remove a parking slot.")
    print("Enter 3 to display all current parking spaces.")
    print("Enter 4 to park a car.")
    print("Enter 5 to find a parked car.")
    print("Enter 6 to remove a parked car.")
    print("Enter 7 to exit the application.\n")

    choice = input("Enter a number: ")

    return choice

choice = ""

carpark = Carpark("Carpark")

while choice != "7":
    choice = create_menu()
    
    if choice == "1":
        add_slot(carpark)
    elif choice == "2":
        delete_slot(carpark)
    elif choice == "3":
        list_slots(carpark)
    elif choice == "4":
        park_car(carpark)
    elif choice == "5":
        print("Finding a parked car...")
    elif choice == "6":
        print("Removing a parked car...")
    elif choice == "7":
        print("Exiting the application...")
    else:
        print("Invalid choice. Please try again.\n")

print("Thank you for using the Carpark Application!")