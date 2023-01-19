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
SHEET = GSPREAD_CLIENT.open('coded-cream')


ingredient = SHEET.worksheet('details')

""" CODE WILL SEE AFTER
def container_choice():
    #Call the first column with the details and display choices for containers
    print("What is the container ?")
    container_details = ingredient.col_values(1)[1:] # get the container values
    
    # Assign a number to a cell value
    container_num = []
    for i in range(1, 4):
        container_num.append(i)

    container_convert = dict(zip(container_num, container_details))
    print(container_convert)


container_choice()


def container_selection():
   # Receive the selection of the container
    #Input the client's choice
    container_str = input("Enter the selection with a number between 1 and 3: ")
    # check and valid the input
    # save this choice in the spreadsheet

container_selection()
"""

def enter_name():
    """
    Ask the client's name with an input
    
    If the entry is correct, the user can go to the next step
    """
    while True:
        name_str = input("Enter the name of the client: \n")

        if validate_name(name_str):
            print("Thank you!")
            print(f"Order of '{name_str} 'is in progress.")
            break
    
    return name_str


def validate_name(name_str):
    """
    If/Else function for validating name
    If no valid characters are entered, or if name is too short or too long
    The user must add again the name until the input is good
    """
    if not name_str.isalpha(): # check if all characters are letters
        print(f"You filled in: '{name_str}'.\n This is not valid. \n")
        print("Please enter only letters.")
        return False
    elif len(name_str) <= 1: # check if the entry is more than 1 character
        print(f"You filled in: '{name_str}'. \n")
        print("The name should be longer than 1 character.\nPlease try again.")
        return False
    elif len(name_str) >= 10: # check if the entry is less than 10 characters
        print(f"You filled in: '{name_str}'. \n")
        print("The name should be shorter than 10 character. \n")
        print("Please try again.")
        return False
    else:
        return True


def my_functions():
    """
    Calls different functions
    """
    enter_name()

my_functions()