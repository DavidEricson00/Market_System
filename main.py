import client
import admin
import db
from utils import clear_screen, header

def main_menu():
    print('Select an option:')
    print('1. Client Menu')
    print('2. Admin Menu')
    print('3. Exit')

def main():
    db.create_table()
    
    option = 0
    while option != 3:
        header()
        main_menu()
        try:
            option = int(input('Select the desired option: '))
        except ValueError:
            clear_screen()
            print('Invalid input. Please enter a valid number.')
            continue
        
        if option == 1:
            clear_screen()
            client.main()
        elif option == 2:
            clear_screen()
            admin.main()
        elif option == 3:
            clear_screen()
            print('Exiting the Market System. Goodbye!')
        else:
            clear_screen()
            print('Invalid option.')
            
if __name__ == "__main__":
    main()