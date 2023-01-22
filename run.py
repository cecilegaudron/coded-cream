import gspread
from google.oauth2.service_account import Credentials

"""
Declare creds, access to the google drive and excel document 
Code from the Love Sandwiches project
"""

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]


CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
#SHEET = GSPREAD_CLIENT.open('coded-cream')


#ingredient = SHEET.worksheet('details')


def enter_name():
    """
    Ask the client's name with an input
    If the entry is correct, the user can go to the next step
    """
    while True:
        name_str = input("\nEnter the name of the client: \n")

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
flavors = ["Belgium Chocolate", "Madagascar Vanilla", "Sicilian Pistachio", 
 "Speculoos", "Indian Mango", "Peanut Butter", "Very Cherry", "Passion Fruit", 
 "Piedmont Hazelnut", "Salted Butter Caramel", "Rosemary Lemon", "Basil Apple"]


def differents_flavors():
    """
    Display list of flavors with names and index
    """
    print("\nPlease select the choice of flavor:\n")
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
    flavor_choice = input("Choose a number:\n")

    while True:
        try:
            flavor_number = int(flavor_choice)  # Convert input into integer
            if type(flavor_number) == int:  # Check if the value is an integer
                validate_flavor(flavor_number)

        except ValueError:
            print("The choice is not a number. Please enter the choice again.\n")
            return False

        return flavor_number


def validate_flavor(flavor_number):
    """
    Check if the input number is on the list
    """
    if flavor_number <= 12:
        print(f"\nThe choice is: '{flavors[flavor_number]}'.\n")
        suggestion_topping()
    else:
        print("The choosen number is not on the list. Please try again.\n")
        return False


def suggestion_topping():
    """
    Propose adding a topping to the client
    If yes, go to the toppings list
    If not, continue the order
    If incorrect entry, try again
    """
    print("Add a topping ? \n")
    want_topping = input("Enter 'yes' to add a topping and 'n' to continue the order.\n")

    while True:
        if want_topping == "y":
            print("Choose the topping on the list.\n")
            differents_toppings()  # Call function with topping list
            break
        
        elif want_topping == "n":
            print("No topping wanted, continue the order.\n")
            # Call next function
            break
        else:
            print("Incorrect entry, please enter 'y' or 'n'.\n")
            return False


# Define list of values with differents toppings
toppings = ["Chocolate chips", "Marshmallows", "Rainbow sprinkles", 
 "Chantilly cream", "Caramel"]


def differents_toppings():
    """
    Display list of differents toppings
    Enumerate name and index of toppings
    """
    list_toppings = enumerate(toppings)

    for topping in list_toppings:  # Display toppings with names and index
        print(topping)


def my_functions():
    """
    Calls different functions
    """
    enter_name()

my_functions()