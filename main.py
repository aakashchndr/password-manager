import random
import database
import pyperclip
from cryptography.fernet import Fernet



def alphanumeric_pass(length):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    Low_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z']
    Up_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z']
    Symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<', '&']

    concatenated = "".join(
        (random.choice(digits+Low_case+Up_case+Symbols) for i in range(length)))

    print('\n', concatenated)
    pyperclip.copy(concatenated)




# Menu
while(True):

    print('\n------ MENU ------\n')
    print('1. Generate a Password')
    print('2. Update a previously generated password')
    print('3. Search a password for website')
    print('4. Delete an entry')
    print('5. Show the entire database')
    print('6. Exit')
    option_no = int(input('\n\nEnter the number to select:\t'))

    # if else for the menu

    # 1 for generating a password
    if option_no == 1:
        length = int(input("\n\nEnter length: "))
        alphanumeric_pass(length)

        use = input('\nDo you want to use this password? (Y/N):  ')
        if (use == 'Y' or use == 'y'):
            pwd = pyperclip.paste()
            print('\nPassword copied to clipboard!\n\n')

        else:
            pass

        to_save = input('\nDo you want to save this password? (Y/N):  ')
        if (to_save == 'Y' or to_save == 'y'):
            user_name = input('\nEnter the username for that password:  ')
            web_site = input(
                '\nEnter the Website where you would use it for:  ')

        else:
            exit()

        database.add_one(user_name, web_site, pwd)
        print('')

    # 2 for updating
    elif option_no == 2:
        web_site = input('Enter the Website name:   ')
        new_pwd = input('Enter the new password:    ')
        database.update_one(new_pwd, web_site)

    # 3 for search
    elif option_no == 3:
        web_site = input("Enter the website name to show the password:  ")
        database.search(web_site)

    # 4 for deleting an entry
    elif option_no == 4:
        web_site = input(
            'Enter the website name to delete it from the database:  ')
        database.delete_one(web_site)

    elif option_no == 5:
        database.show_all()

    elif option_no == 6:
        exit()

    else:
        print('\nInvalid selection! Choose from the menu options.\n')
