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


def start():
    """
    Start menu that the user can choose between 6 different tasks.
    """
    while True:
        print("MENU")
        print("1. Add new contact")
        print("2. Delete contact")
        print("3. Search contact")
        print("4. Exit\n")

        user_input = input("Please enter the number of the task here: \n")     

        if validate_menu_choise(user_input):
            break
    add_new_contact(user_input)


def validate_menu_choise(task_number):
    """
    Check so the user input is a number between 1-6 for the menu, 
    and provide an error messege if its not!
    """
    try:
        if(int(task_number) < 1 or int(task_number) > 6):
            raise ValueError(f'{task_number} is not a valid number')
    except ValueError as e:
        print(f'Try again, {e} enter a number between 1-6')
        return False

    return True


def add_new_contact(task_number):
    """
    Add a new contact with first name, last name, phone number and email
    and check so the user input is correct, otherwise a error shows.
    """
    if task_number == "1":
        add_new_contact = {}

        while True:
            first_name = input("First Name: \n")
            if not first_name.isalpha():
                print("Invalid characters. Please enter First Name with letters a-z")
            else:
                break
        add_new_contact["Fname"] = first_name

        return update_worksheet_contact(add_new_contact)


def update_worksheet_contact(add_new_contact):
    """
    Updating the google sheet with new contact informaion in contactbook.
    Provides a validation message for user that the update is done. 
    """
    print("saving contact in contactbook...\n")
    new_worksheet = SHEET.worksheet('contacts')
    new_worksheet.append_row([x for x in add_new_contact.values()])
    print("Contact is now saved and contactbook is updated! \n")
    start()


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
