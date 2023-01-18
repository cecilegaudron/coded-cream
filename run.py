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
    Input the client's choice
    """
    print("What is the container ?")
    container_details = ingredient.col_values(1)[1:] # get the container values
    print(indcontainer_details)


container_choice()


