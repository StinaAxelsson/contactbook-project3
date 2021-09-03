# start - a welcome message and a menu with 6 different task to choose between
# a while loop while user use the program
# funtions for every task in the menu
# validating function so the user input the right value
# add contact + update sheet
# search for existing contact (by name, number or email)
# delete a contact
# Show all the existing contacts with a linebreak after every contact
# Delete all the contats in the book
# Exit to break the program from anywhere the user is

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('contact_book')

contact = SHEET.worksheet('contacts')
data = contact.get_all_values()


def start():
    """
    Start menu with a welcome message and a menu
    that the user can choose between 6 different tasks.
    """
    while True:
        print("MENU")
        print("1. Add new contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Exit\n")

        user_input = input("Please enter the number of the task here: \n")     
        if user_input == '1':
            break
        else:
            print("not valid")

    return user_input


def main():
    """
    contains alla the functions for the program
    """
    start()


print("-------------------------------------------------------")
print("------------------------WELCOME!-----------------------")
print("---------------This is a contact book app--------------")
print("------Please choose what you want to do in the menu----")
print("-------------------------------------------------------\n")
main()
