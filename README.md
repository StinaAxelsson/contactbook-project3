
# Contact book python application
Author: Stina Axelsson
![](https://github.com/StinaAxelsson/contactbook-project3/blob/main/assets/wireframes/responsive.png)

# Project Description
This project is developed as my third portfolio project during my course at Code Institute. It is an command-line application using only Python as programming language.

This programme is a contact book that can provide the user to add their contacts and store them all in one place. You can use this program to add new contacts with relevant information like first name, last name, phonenumber and e-mail address and save it in a google sheet document. You can search for specific contacts that is saved, view all existing contacts and you can delete single contacts or all at once. 
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
As a user I want...
* ..that the programme is simple to understand and what it is about.
* .. to get feedback of what is happening when navigate thrue the programme/app.
* .. to add contact, be able to see all my saved contacts and to delete one or all.
* .. ways to get back to start or menu easy.

## Site Owner Goals
As a developer of this programme, my goals was..
* To build a programme that can store and add information from a user.
* Make it easy for user to understand what it is about and how to use it.
* To make functions that add and store user inputs in API google sheets.
* Create functions like add a contact, open exisiting contacts and delete. 


## Structure
![](https://github.com/StinaAxelsson/contactbook-project3/blob/main/assets/wireframes/flowchart.jpg)

Structure of this programme is what you can see in the flowchart here. There is six different task from a menu that get the user to the function depending on what the user input. Every function has a way to get back to the menu or quit the programme after the task is done. 
In the flowchart every function has a own colour just to make it easy to follow. 
# Features
## Existing Features
* Start Menu
  - Programme starts with this welcome message and a list of choises. The user needs to input the number of what task they want to follow and the programme open that function.
![]()
* Add a new contact
  * When add a new contact, user need to fill in first name, last name, phone number and email and then the information will be saved in the worksheet gspread.
![]()
* view all existing contacts
  * This function will open all the existing contacts that is saved in the worksheet and print them out.
![]()
* Delete one contact
  * If a user wants to delete a contact, they have to search for the contact first and will be giving 4 choises to search after. "First name", "Last name", "Phonenumber" or their "Email" and then the contact will be printed out.
  * If the user wants to delete it, they have to validate it with Yes or No and then the row with that contacts information will be deleted from the worksheet.
![]()
* Search contact
  * This feature is similar to delete because it takes the user to the same function. To search after the specific contact by first name, last name, phone number or email address. And gives the user choise to delete it.
![]()
* Reset the contactbook
  * This feature will reset the worksheet and alla the information that was stored deletes. Only the headers in the worksheet will remain for store new contacts.
![]()
* Exit programme
  * This feature exit the programme and can be reach from some of the other features also.
![]()

## Features Left to Implement
This is what I want to impement in future on this programme to make it complete. But that I did not prioritate right now for the short of time.
* Edit contact
  * This features is something I want to implement, and it is a feature that is missing in this programme. So the user easy can change some details about a contact instead of delete it and start over.
* Categorys
  * So the user can have som structure of the contacts. Like "Family", "Co-Workers", "Friends" etc. It is a nice detail for the user experience.

# Technologies Used
## Language
* Python3 - This project is written only with Python as a the programming language.
## Other programmes
* Google sheets - To get my google sheet document (gspread) for store the information the user insert, and to remove information.
* Gspread - The API to connect my to my programme.
* GitHub - Making my repository and push my commited code.
* Git - Save and commit my workspace.
* Heroku - To deploy my programme and get a livelink.
* Am I responsive - For the print screen of my deployed programme for this readme.
* Draw.io - For make my flowchart.
* PEP8 - To validate python code
* Re - to import re library for using regrexpressions for email. https://docs.python.org/3/library/re.html
# Testing
## Validator Testing
When I checked my code for PEP8 requirements it's showed ALL RIGHT
![](https://github.com/StinaAxelsson/contactbook-project3/blob/main/assets/wireframes/validation.png)

# Deployment
To build this program, I have used the Code Institutes template to be able to deploy it on Heroku and to be able to use the program on a web server. 
And using Gitpod IDE, in order to save my work I always git add, git commit and then push it to my Github repository.

## Project Deployment:
For deploy this project in Heroku I followed these steps:

1. Log in to my account at Heroku
2. Select "new" and "Create new app" from the dashboard.
3. Create a unique name for the project
4. Navigate from the deploy tab at the top and select the setting tab.
5. Because I use Code Institute template, I need to add a config var for creating this app. 
(Not necessary if you do not use the template)
6. Select Reveal config vars button. In KEY field, input PORT with capital letters.
In VALUE field, input 8000 and then select add button.
7. Then add buildpacks below the config var section.
8. Select Python as yout first bulid pack in buildpacks window and save that.
9. Add another buildpack and add node.JS and save.
The order of the buildpacks is importent to be Python at the top and node.JS at the bottom.
10. Select the deploy tab again and go to the deployment method section.
11. Select GitHub - connect to GitHub button and follow the steps to connect to your GitHub account.
12. Select your account and enter the name of yout repository and then select search.
13. When Heroku has find your repository select connect to connect the repository to the app within Heroku.
14. Below App connected section, I choose to manual deployments options further down. 
15. When that is done correctly this will provide me the live link for this programe.
16. Then I choose Automatic Deploys button that will automatically rebuild the app everytime you add, commit and push from GitPod.

### Here is the final deployed link:

https://contact-book-pp3.herokuapp.com/

# Credits
Credits:
https://stackoverflow.com/questions/45175995/gspread-reading-a-google-sheet-file-using-python-3 
This is for the opening of the gspred showing all contacts
https://www.geeksforgeeks.org/python-program-to-convert-a-list-to-string/ - for fix the list to just strings in search function using join() method

# Acknowledgement


