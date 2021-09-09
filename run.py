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
CONTACTS = SHEET.worksheet('contacts')


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
        choise = (input("Choose the number of the task you want to do: \n"))
        if choise == '1':
            print("go to add contact")
            add_new_contact()
            break
        elif choise == '2':
            print("Open Contact Book...\n")
            show_all_contacts()
            break
        elif choise == '3':
            print("you chose 3")
        elif choise == '4':
            print("you chose 4")
            search_contact()
            break
        elif choise == '5':
            print("Reset contact book")
            break
        elif choise == '6':
            print("Exit programme...")
            exit_programme()
            break
        else:
            print("Not a valid input please enter a number 1-6")


def add_new_contact():
    """
    Add a new contact with first name, last name, phone number and email
    and check so the user input is correct, otherwise a error shows.
    """
    add_new_contact = {}

    while True:
        first_name = input("First Name: \n")
        if not first_name.capitalize():
            print("Please enter First Name with letters a-z")
        else:
            break
    add_new_contact["FIRST NAME"] = first_name

    while True:
        last_name = input("Last Name: \n")
        if not last_name.capitalize():
            print("Please enter Last Name with letters a-z")
        else:
            break
    add_new_contact["Lname"] = last_name

    while True:
        # To valid phone number using help from
        # https://www.sololearn.com/Discuss/2588446/solved-python-phone-number-validator
        phone_number = input("Phone Number: \n")
        pattern = r"^[189][0-9]"
        match = re.match(pattern, phone_number)
        if match and len(phone_number) == 8:
            print("valid")
            break
        else:
            print("Inavalid, please start number with 1, 8 or 9\
                and be 8 digits long")
            continue
    add_new_contact["Number"] = phone_number

    while True:
        email = input("E-Mail: \n")
        if validate_email_input(email):
            break
        else:
            continue
    add_new_contact["E-Mail"] = email

    print("-----------------------------------")
    print("ADDED:\n")
    print(f"Name: {first_name.upper()} {last_name.upper()}")
    print(f'Number: {phone_number}')
    print(f'E-Mail: {email}\n')
    print("-----------------------------------")

    return update_worksheet_contact(add_new_contact)


def validate_email_input(email):
    """
    check if the input email is validate
    using help from this site:
    https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
    """
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(regex, email)):
        return True
    else:
        print("E-Mail is invalid, please try again")
        return False


def back_to_menu():
    """
    Instead of get the whole menu after every task, user get a question if
    they want to go back to menu or quit.
    """
    while True:
        user_choise = input("Back to menu: B, Quit programme: Q \n")
        if user_choise == "B" or user_choise == "b":
            start()
            break
        elif user_choise == "Q" or user_choise == "q":
            exit_programme()
            break
        else:
            print("Invalid input, Try again")
        return False


def add_one_more():
    """
    if user want to add more contacts in a row, this is a short way to do that
    instead of get to start menu after adding a contact.
    """
    while True:
        again = input("Add another contact: A, Back to menu: B \n")
        if again == "A" or again == "a":
            add_new_contact()
            break
        elif again == "B" or again == "b":
            start()
            break
        else:
            print("Invalid input, Try again")
        return False


def update_worksheet_contact(add_new_contact):
    """
    Updating the google sheet with new contact informaion in contactbook.
    Provides a validation message for user that the update is done.
    """
    new_worksheet = SHEET.worksheet('contacts')
    new_worksheet.append_row([x for x in add_new_contact.values()])
    print("Contact is now saved and contactbook is updated! \n")
    add_one_more()


# SHOW ALL EXISTING CONTACTS
def show_all_contacts():
    """
    Function to get all the contacts from google sheet
    and show them as a list for each person in the
    contact book
    """
    get_all = CONTACTS.get_all_records()
    for contact in get_all:
        printing_all_contacts(contact)
    back_to_menu()


def printing_all_contacts(existing):
    """
    Function that takes all the existing contacts from worksheet
    and make it a loop with the headers as keys and the contact
    information as value in a list for each contact.
    """
    one_contact = []
    for title, info in existing.items():
        print(f'{title}: {info}')
        one_contact.append(info)
    print("-----------------------------------")
    return one_contact


# SEARCH CONTACTS
def search_contact():
    """
    Search function with a menu for the user to enter what
    they want to search for in contact book.
    """
    print("SEARCH:")
    print("1. First Name")
    print("2. Last Name")
    print("3. Phone Number")
    print("4. E-Mail")
    print("5. Back to Menu")
    while True:
        search_input = input("Please enter a number 1-5: \n")
        if search_input == '1':
            get_from_search('fname')  # make a new function
        elif search_input == '2':
            get_from_search('lname')  # make a new function
        elif search_input == '3':
            print("here goes a input")  # make a new function
        elif search_input == '4':
            print("here goes a input")  # make a new function
        elif search_input == '5':
            print("here goes a input")  # make a new function
        else:
            back_to_menu()
        return False


def get_from_search(find_search):
    """
    Get input from user in search task, to find the contacts
    that user is searching after from name, number of email
    and the function looking for it in the contact worksheet.
    """
    if find_search == 'fname':
        find = input('First Name: \n').capitalize()
    elif find_search == 'lname':
        find = input('Last Name: \n').capitalize()
    else:
        print("print something")

    output = list(filter(
        lambda existing: existing[find_search] == find or
        find in existing[find_search], CONTACTS.get_all_records()
    ))
    if len(output) != 0:
        for existing in output:
            printing_all_contacts(existing)
        back_to_menu()
    else:
        print("There is no contact with that name, Try again")
        search_contact()


# EXIT PROGRAMME
def exit_programme():
    """
    Shutting down programme when user choose the exit task in menu
    """
    print("-------------------------------------------------------")
    print("-------------Thank you for using contact app-----------")
    print("-------------------------------------------------------")
    print("------------------------GOODBYE------------------------")
    print("-------------------------------------------------------")


def main():
    """
    contains all the functions for the program
    """
    start()


print("-------------------------------------------------------")
print("-----------------------WELCOME!------------------------")
print("---------------This is a contact book app--------------")
print("-------------Please choose a number of what------------")
print("---------------you want to do in the menu--------------")
print("-------------------------------------------------------\n")
main()
