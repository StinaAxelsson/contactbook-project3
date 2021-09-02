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
print(data)

print("-------------------------------------------------------")
print("------------------------WELCOME!-----------------------")
print("---------------This is a contact book app--------------")
print("------Please choose what you want to do in the menu----")
print("-------------------------------------------------------\n")


print("MENU")
print("1. Add a contact")
print("2. Search for a contact")
print("3. Delete a contact")
print("4. Show all contacts in contact book")
print("5. Delete all contact")
print("6. Exit")
