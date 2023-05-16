"""
Import the Colorama module to have some colors
on the code, especially for the inputs
"""
from colorama import Fore, Style


def enter_name():
    """
    Ask the client's name with an input
    If the entry is correct, the user can go to the next step
    """
    while True:
        name_str = input(Fore.BLUE + "\nEnter the name of the client: \n"
                         + Style.RESET_ALL)

        if validate_name(name_str):
            print("Thank you!")
            print(f"Order of '{name_str}' is in progress.\n")
            break

    choose_flavor(flavors)

    return name_str


def validate_name(name_str):
    """
    If/Else function for validating name
    If no valid characters are entered, or if name is too short or too long
    The user must add again the name until the input is good
    """
    if not name_str.isalpha():  # Check if all characters are letters
        print(f"You filled in: '{name_str}'.")
        print("This is not valid.\nPlease enter only letters.")
        return False
    elif len(name_str) <= 1:  # Check if the entry is more than 1 character
        print(f"You filled in: '{name_str}'.")
        print("The name should be longer than 1 character.\nPlease try again.")
        return False
    elif len(name_str) >= 10:  # check if the entry is less than 10 characters
        print(f"You filled in: '{name_str}'.")
        print("The name should be shorter than 10 characters.\nPlease try again.")
        return False
    else:
        return True


# Define list of values with differents flavors
flavors = ["Belgium Chocolate", "Madagascar Vanilla", "Sicilian Pistachio",
           "Speculoos", "Indian Mango", "Peanut Butter", "Very Cherry",
           "Passion Fruit", "Piedmont Hazelnut", "Salted Butter Caramel",
           "Rosemary Lemon", "Basil Apple"]


def choose_flavor(flavor_number):
    """
    Ask the client's flavor choice
    If it is a number, convert into integer
    Check if the input number is on the list
    """
    print("Please select the choice of flavor:")
    list_flavors = enumerate(flavors)  # Display the index number from list

    for flavor in list_flavors:
        print(flavor)

    while True:
        try:
            flavor_number = input(Fore.BLUE + "\nChoose a number:\n" + Style.RESET_ALL)
            flavor_number = int(flavor_number)
            if type(flavor_number) == int:  # Check if the value is an integer
                if flavor_number >= 12:  # Check if the entry is more than 1 character
                    print(f"You filled in: '{flavor_number}'.")
                    print("The chosen number is not in the list.\nPlease try again.")
                    continue
                else:
                    print(f"You choose '{flavors[flavor_number]}'")
                    suggestion_topping()
                    break
        except ValueError:
            print(f"You filled in: '{flavor_number}'.")
            print("It is not a number.\nPlease try again.")
            continue
        break

    return flavor_number


def suggestion_topping():
    """
    Propose adding a topping to the client
    If yes, go to the toppings list
    If not, continue the order
    If incorrect entry, try again
    """
    print("Add a topping ?")
    print("Enter 'y' for add one and 'n' for no and go to payment.")
    #want_topping = input(Fore.BLUE + "Enter 'y' to add one topping \n \
    #Enter 'n' to finish the order.\n" + Style.RESET_ALL)

    while True:
        want_topping = input(Fore.BLUE + "Enter 'y' or 'n':\n" + Style.RESET_ALL)
        if want_topping == "y":
            print("You want a topping !")
            differents_toppings()  # Call function with topping list
        elif want_topping == "n":
            print("No topping wanted, go to payment.")
            flavor_payment()
            break
        else:
            print(f"You filled in: '{want_topping}'.")
            print("Incorrect entry.\nPlease try again.")
            continue
        break


# Define list of values with differents toppings
toppings = ["Chocolate chips", "Marshmallows", "Rainbow sprinkles",
            "Chantilly cream", "Caramel"]


def differents_toppings():
    """
    Display list of differents toppings
    Enumerate name and index of toppings
    """
    print("Please select a topping in the list:")
    list_toppings = enumerate(toppings)

    for topping in list_toppings:  # Display toppings with names and index
        print(topping)

    while True:
        try:
            topping_choice = int(input(Fore.BLUE + "Enter the topping number:\n"
                               + Style.RESET_ALL))
            if type(topping_choice) == int and topping_choice <= 4:
                print(f"\nThe choice is: '{toppings[topping_choice]}'.\n")
                topping_payment()
                break
            else:
                print(f"You filled in: '{topping_choice}'.")
                print("The number is not on the list. Please try again.")
                continue
        except ValueError:
            print("The choice is not a number. Please enter the choice again.")
            continue
        break

    return topping_choice


# Define flavor and topping prices
_PRICES = [2, 1.5]


def flavor_payment():
    """
    Print the amount to be paid when just a flavor is ordered
    """
    print(f"The order is a flavor. The amount to be paid is {_PRICES[0]}€.")
    exit()


def topping_payment():
    """
    Calculate the price with addition between flavor price and topping price
    Convert the flavor price into float number
    Print the amount to be paid
    """
    calcul_price = float(_PRICES[0]) + _PRICES[1]
    print(f"A flavor is {_PRICES[0]}€ and a topping is {_PRICES[1]}€.\n")
    print(f"The amount to be paid is {calcul_price}€.")
    exit()


print(Fore.GREEN + "WELCOME TO THE CODED CREAM PROGRAMM!"
      + Style.RESET_ALL)

# Start running the programm with the first function
enter_name()
