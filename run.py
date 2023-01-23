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
        name_str = input(Fore.BLUE + "\nEnter the name of the client: \n" \
            + Style.RESET_ALL)

        if validate_name(name_str):
            print("Thank you!")
            print(f"Order of '{name_str}' is in progress.\n")
            break

    differents_flavors()

    return name_str


def validate_name(name_str):
    """
    If/Else function for validating name
    If no valid characters are entered, or if name is too short or too long
    The user must add again the name until the input is good
    """
    if not name_str.isalpha():  # Check if all characters are letters
        print(f"You filled in: '{name_str}'.\nThis is not valid. \n")
        print("Please enter only letters.")
        return False
    elif len(name_str) <= 1:  # Check if the entry is more than 1 character
        print(f"You filled in: '{name_str}'. \n")
        print("The name should be longer than 1 character.\nPlease try again.")
        return False
    elif len(name_str) >= 10:  # check if the entry is less than 10 characters
        print(f"You filled in: '{name_str}'. \n")
        print("The name should be shorter than 10 characters. \n")
        print("Please try again.")
        return False
    else:
        return True


# Define list of values with differents flavors
flavors = ["Belgium Chocolate", "Madagascar Vanilla", "Sicilian Pistachio", \
    "Speculoos", "Indian Mango", "Peanut Butter", "Very Cherry", \
        "Passion Fruit", "Piedmont Hazelnut", "Salted Butter Caramel",\
             "Rosemary Lemon", "Basil Apple"]


def differents_flavors():
    """
    Display list of flavors with names and index
    """
    print("Please select the choice of flavor:")
    list_flavors = enumerate(flavors)  # Display the index number from list

    for flavor in list_flavors:
        print(flavor)

    choose_flavor()


def choose_flavor():
    """
    Ask the client's flavor choice
    If it is a number, convert into integer
    And call the validate data function
    """
    flavor_choice = input(Fore.BLUE + "\nChoose a number:\n" + Style.RESET_ALL)

    while True:
        try:
            flavor_number = int(flavor_choice)  # Convert input into integer
            if type(flavor_number) == int:  # Check if the value is an integer
                validate_flavor(flavor_number)

        except ValueError:
            print("It is not a number. Please enter the choice again.\n")
            return False


def validate_flavor(flavor_number):
    """
    Check if the input number is on the list
    """
    if flavor_number <= 12:
        print(f"\nThe choice is: '{flavors[flavor_number]}'.\n")
        suggestion_topping()
    else:
        print("The choosen number is not in the list. Please try again.\n")
        choose_flavor()

    return flavor_number


def suggestion_topping():
    """
    Propose adding a topping to the client
    If yes, go to the toppings list
    If not, continue the order
    If incorrect entry, try again
    """
    print("Add a topping ? \n")
    want_topping = input(Fore.BLUE + "Enter 'y' to add one topping \n \
    Enter 'n' to finish the order.\n" + Style.RESET_ALL)

    while True:
        if want_topping == "y":
            print("Choose the topping on the list.")
            differents_toppings()  # Call function with topping list
        elif want_topping == "n":
            print("No topping wanted, continue the order.\n")
            flavor_payment()
            break
        else:
            print("Incorrect entry, please enter 'y' or 'n'.\n")
            return False


# Define list of values with differents toppings
toppings = ["Chocolate chips", "Marshmallows", "Rainbow sprinkles", \
    "Chantilly cream", "Caramel"]


def differents_toppings():
    """
    Display list of differents toppings
    Enumerate name and index of toppings
    """
    list_toppings = enumerate(toppings)

    for topping in list_toppings:  # Display toppings with names and index
        print(topping)

    topping_choice = int(input(Fore.BLUE + "Please add a topping by indicating \
        its number:\n" + Style.RESET_ALL))

    while True:
        try:
            if type(topping_choice) == int and topping_choice <= 4:
                print(f"\nThe choice is: '{toppings[topping_choice]}'.\n")
                topping_payment()
                break
            else:
                print("The choosen number is not on the list. Please try again.\n")
                return False

        except ValueError:
            print("The choice is not a number. Pleaser enter the choice again.\n")
            return False

    return topping_choice


# Define flavor and topping prices
flavor_price = 2
topping_price = 1.5


def flavor_payment():
    """
    Print the amount to be paid when just a flavor is ordered
    """
    print(f"The amount to be paid is {flavor_price}€.")
    exit()


def topping_payment():
    """
    Calculate the price with addition between flavor price and topping price
    Convert the flavor price into float number
    Print the amount to be paid
    """
    calcul_price = float(flavor_price) + topping_price
    print(f"A flavor is {flavor_price}€ and a topping is {topping_price}€.\n")
    print(f"The amount to be paid is {calcul_price}€.")
    exit()


print(Fore.GREEN + "WELCOME TO THE CODED CREAM PROGRAMM!" \
    + Style.RESET_ALL)

# Start running the programm with the first function
enter_name()
