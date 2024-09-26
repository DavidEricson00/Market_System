import getpass
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_authentication(loginx, passwordx):
    return loginx == "Admin" and passwordx == "0000"

def add_product():
    print('Add Product')

def list_products():
    print('List Products')

def update_product():
    print('Update Product')

def remove_product():
    print('Remove Product')

def menu():
    print('1. Add Product')
    print('2. List Products')
    print('3. Update Product')
    print('4. Remove Product')
    print('5. Exit')

def admheader():
    print('------------------------------------')
    print('   Welcome to the Admin interface   ')
    print('------------------------------------')

def header():
    print('------------------------------------')

def admin_interface():
    option = 0
    while option != 5:
        admheader()
        menu()
        try:
            option = int(input('Select the desired option: '))
        except ValueError:
            clear_screen()
            print('Invalid input, please enter a number')
            continue

        if option == 1:
            clear_screen()
            add_product()
        elif option == 2:
            clear_screen()
            list_products()
        elif option == 3:
            clear_screen()
            update_product()
        elif option == 4:
            clear_screen()
            remove_product()
        elif option == 5:
            clear_screen()
            print('Exiting the Admin Interface...')
        else:
            clear_screen()
            print('Invalid option')

def main():
    login = input('Insert the login: ')
    password = getpass.getpass('Insert the password: ')
    
    if login_authentication(login, password):
        clear_screen()
        admin_interface()
    else:
        header()
        print('Access denied, try again')
        header()
        main()