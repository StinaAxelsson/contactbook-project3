# start a welcome message and -
# -a menu with 6 different task to choose between (check)
# a while loop while user use the program (check)
# funtions for every task in the menu
# validating functions so the user input the right value
# add contact + update sheet (check)
# search for existing contact (by name, number or relaton (email))
# delete a contact
# Show all the existing contacts with a linebreak after every contact
# Delete all the contats in the book (check(have to fix it))
# Exit to break the program from anywhere the user is
# import libraby that make color of the feedbacks in code

import gspread
import re
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
                6. Exit\n
                    """)
    while True:
        choise = int(input("Choose the number of the task you want to do: \n"))
        if choise == 1:
            print("go to add contact")
            add_new_contact()
            break
        elif choise == 2:
            print("Open Contact Book...")
            show_all_contacts()
            break
        elif choise == 3:
            print("you chose 3")
        elif choise == 4:
            print("you chose 4")
        elif choise == 5:
            print("Reset contact book")
            delete_all_contacts()
            break
        elif choise == 6:
            print("You exit")
            break
        else:
            print("Not a valid input please enter a number 1-6")


def add_new_contact():
    """
    Add a new contact with first name, last name, phone number and email
    and check so the user input is correct, otherwise a error shows.
    """
    print("add new contact is chosen")
    add_new_contact = {}

    while True:
        first_name = input("First Name: \n")
        if not first_name.capitalize():
            print("Please enter First Name with letters a-z")
        else:
            break
    add_new_contact["Fname"] = first_name

    while True:
        last_name = input("Last Name: \n")
        if not last_name.capitalize():
            print("Please enter Last Name with letters a-z")
        else:
            break
    add_new_contact["Lname"] = last_name

    while True:
        phone_number = int(input("Phone Number: \n"))
        if not phone_number.__int__():
            print("Please use digits only\n")
        else:
            break
    add_new_contact["Number"] = phone_number

    while True:
        email = input("E-Mail: \n")
        if validate_email_input(email):
            break
        else:
            continue
    add_new_contact["E-Mail"] = email

    print("You have added:\n")
    print(f"Name: {first_name.upper()} {last_name.upper()}")
    print(f'Number: {phone_number}')
    print(f'E-Mail: {email}\n')

    return update_worksheet_contact(add_new_contact)


def validate_email_input(email):
    """
    check if the input email is validate
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    else:
        print("E-Mail is invalid, please try again")
        return False


def update_worksheet_contact(add_new_contact):
    """
    Updating the google sheet with new contact informaion in contactbook.
    Provides a validation message for user that the update is done.
    """
    new_worksheet = SHEET.worksheet('contacts')
    new_worksheet.append_row([x for x in add_new_contact.values()])
    print("Contact is now saved and contactbook is updated! \n")
    start()


def show_all_contacts():
    """
    Open a list with all the existing contacts in the
    contactbook from google sheet.
    """
    print("ALL CONTACTS:\n")
    contact_list = SHEET.worksheet('contacts')
    open_cnt_list = list()

    for all in range(1, 5):
        open_cnt_list = contact_list.col_values(all)
        print(open_cnt_list)
    start()


def delete_all_contacts():
    """
    Deleting all the existing contacts that been saved in
    the contact - worksheet.
    """
    while True:
        delete_all = input("Delete alla existing contacts? Y/N: \n")
        if delete_all == "Y" or delete_all == "y":
            SHEET.worksheet('contacts').clear()
            print("All contacts have been deleted!")
            break
        elif delete_all == "N" or delete_all == "n":
            print("NO, go back to menu")
            start()
            break
        else:
            print("Not Valid input, You have to enter Y or N, Try again")
    return start()


def main():
    """
    contains alla the functions for the program
    """
    start()


print("-------------------------------------------------------")
print("-----------------------WELCOME!------------------------")
print("---------------This is a contact book app--------------")
print("-------------Please choose a number of what------------")
print("---------------you want to do in the menu--------------")
print("-------------------------------------------------------\n")
main()
