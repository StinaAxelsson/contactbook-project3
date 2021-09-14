
# Contact book python application
Author: Stina Axelsson
![](https://github.com/StinaAxelsson/contactbook-project3/blob/main/assets/wireframes/responsive.png)
# Project Description
This project is developed as my third portfolio project during my course at Code Institute. It is a back-end appplication using Python programming langugae.

In this contact book programme, you can add new contacts and save it in a google sheet document. You can search for specific contacts that is saved, view all existing contacts and delete one or all. 
# Content
* Project Description
* UX
  * User Stories
  * Site Owner Goals
  * Structure
* Features
  * Existing Features
  * Features Left To Implement
* Technologies Used
  * Languages
  * Other Programmes
* Testing
  * Validator Testing
* Deployment
* Credits
* Ackmowledgements

# UX
## User Stories
## Site Owner Goals

## Structure
![](https://github.com/StinaAxelsson/contactbook-project3/blob/main/assets/wireframes/flowchart-contactbook.pdf)

Structure of this programme is what you can see in the flowchart here. There is six different task from a menu that get the user to the function depending on what the user input. Every function has a way to get back to the menu or quit the programme after the task is done. 
In the flowchart every function has a own colour just to make it easy to follow. 
# Features
## Existing Features
* Start Menu
  - Programme starts with this welcome message and a list of choises. The user needs to input the number of what task they want to follow and the programme open that function.
* Add a new contact
  * When add a new contact, user need to fill in first name, last name, phone number and email and then the information will be saved in the worksheet gspread.
* view all existing contacts
  * This function will open all the existing contacts that is saved in the worksheet and print them out.
* Delete one contact
  * If a user wants to delete a contact, they have to search for the contact first and will be giving 4 choises to search after. "First name", "Last name", "Phonenumber" or their "Email" and then the contact will be printed out.
  * If the user wants to delete it, they have to validate it with Yes or No and then the row with that contacts information will be deleted from the worksheet.
* Search contact
  * This feature is similar to delete because it takes the user to the same function. To search after the specific contact by first name, last name, phone number or email address. And gives the user choise to delete it.
* Reset the contactbook
  * This feature will reset the worksheet and alla the information that was stored deletes. Only the headers in the worksheet will remain for store new contacts.
* Exit programme
  * This feature exit the programme and can be reach from some of the other features also.
# Credits
Credits:
https://stackoverflow.com/questions/45175995/gspread-reading-a-google-sheet-file-using-python-3 
This is for the opening of the gspred showing all contacts
https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/ - for fix the list to just strings in search function using join() method

