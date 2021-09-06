# start - a welcome message and a menu with 6 different task to choose between
# a while loop while user use the program (check)
# funtions for every task in the menu
# validating function so the user input the right value (check)
# add contact + update sheet (check)
# search for existing contact (by name, number or relaton (email))
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
    print("""
                --------MENU--------
                1. Add new contact\n\
                2. View all contacts\n\
                3. Delete a contact\n\
                4. Search contact\n\
                5. Reset contactbook\n\
                4. Exit\n
                    """)
    while True:
        choise = int(input("Choose the number of the task you want to do: "))
        if choise == 1:
            print("go to add contact")
            add_new_contact()
            break
        elif choise == 2:
            print("you chose 2")
        elif choise == 3:
            print("you chose 3")
        elif choise == 4:
            print("you chose 4")
        elif choise == 5:
            print("You chose 5")
        elif choise == 6:
            print("You exit")
        else:
            print("Not a valid please enter a number 1-6")


def add_new_contact():
    """
    Add a new contact with first name, last name, phone number and email
    and check so the user input is correct, otherwise a error shows.
    """
    print("add new contact is chosen")    


def update_worksheet_contact(add_new_contact):
    """
    Updating the google sheet with new contact informaion in contactbook.
    Provides a validation message for user that the update is done.
    """
    new_worksheet = SHEET.worksheet('contacts')
    new_worksheet.append_row([x for x in add_new_contact.values()])
    print("Contact is now saved and contactbook is updated! \n")
    start()


# not working
def show_all_contacts(task_number):
    """
    Open a list with all the existing contacts in the 
    contactbook from google sheet.
    """
    pass


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
