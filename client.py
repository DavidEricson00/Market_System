import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_products():
    print('List Products')

def buy_product():
    print('Update Product')

def menu():
    print('1. List Products')
    print('2. Buy Product')
    print('3. Exit')

def clientheader():
    print('-------------------------------------')
    print('   Welcome to the Client interface   ')
    print('-------------------------------------')

def header():
    print('------------------------------------')

def main():
    option = 0
    while option != 3:
        clientheader()
        menu()
        try:
            option = int(input('Select the desired option: '))
        except ValueError:
            clear_screen()
            print('Invalid input, please enter a number')
            continue

        if option == 1:
            clear_screen()
            list_products()
        elif option == 2:
            clear_screen()
            buy_product()
        elif option == 3:
            clear_screen()
            print('Exiting the Client Interface...')
        else:
            clear_screen()
            print('Invalid option')