import client
import admin
import os

def header():
    print('-------------------------')
    print('     Market System       ')
    print('-------------------------')

def main_menu():
    print('Please select an option:')
    print('1. Client Menu')
    print('2. Admin Menu')
    print('3. Exit')

def main():
    option = 0
    header()
    while option != 3:
        main_menu()
        option = int(input('Select the desired option: '))
        if option == 1:
            os.system('cls')
            client.main()
        elif option == 2:
            os.system('cls')
            admin.main()
        elif option == 3:
            pass
        else:
            os.system('cls')
            print('Invalid option')
            header()

main()