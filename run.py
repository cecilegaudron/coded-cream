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


def container_choice():
    """
    Call the first column with the details and display choices for containers
    """
    print("What is the container ?")
    container_details = ingredient.col_values(1)[1:] # get the container values
    
    #Assign a number to a cell value
    container_num = []
    for i in range(1, 4):
        container_num.append(i)

    container_convert = dict(zip(container_num, container_details))
    print(container_convert)

    # convert string to value

container_choice()


def container_selection():
    """
    Receive the selection of the container
    Input the client's choice
    """
    container_str = input("Enter the selection with a number between 1 and 3: ")
    # add a value linked with my containers
    # save this choice in the spreadsheet

container_selection()

