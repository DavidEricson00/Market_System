import getpass
import os
import db

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_authentication(loginx, passwordx):
    return loginx == "Admin" and passwordx == "0000"

def add_product():
    name = input('Enter product name: ')
    price = float(input('Enter product price: '))
    quantity = int(input('Enter product quantity: '))

    print(f'{name} with the price {price} and quantity {quantity}')
    print('Are you sure you want to add this product to the system?')
    confirm = input('[Y/N]: ').strip().lower()

    if confirm == 'y':
        db.execute_commit('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
        print('Product added successfully!')
    else:
        print('Product was not added to the database.')

def list_products():
    products = db.execute_query('SELECT * FROM products')
    
    if products:
        print('ID | Name        | Price   | Quantity')
        print('--------------------------------------')
        for product in products:
            print(f'{product[0]:<2} | {product[1]:<10} | {product[2]:<7.2f} | {product[3]:<8}')
    else:
        print('No products found.')

def update_product():
    id = int(input('Enter the product ID to update: '))

    product = db.execute_query('SELECT * FROM products WHERE id = ?', (id,))
    
    if product:
        product = product[0]
        name, price, quantity = product[1], product[2], product[3]

        print('Current product information:')
        print(f'Product: {name} with the price {price:.2f} and quantity {quantity}')

        name = input('Enter the new product name: ')
        price = float(input('Enter the new product price: '))
        quantity = int(input('Enter the new product quantity: '))

        print(f'Product: {name} with the price {price} and quantity {quantity}')
        print('Are you sure you want to update this product?')
        confirm = input('[Y/N]: ').strip().lower()

        if confirm == 'y':
            db.execute_commit('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?', (name, price, quantity, id))
            print('Product updated successfully!')
        else:
            print('Product was not updated.')
    else:
        print('Product not found.')

def remove_product():
    id = int(input('Enter the product ID to remove: '))
    
    product = db.execute_query('SELECT * FROM products WHERE id = ?', (id,))
    
    if product:
        product = product[0]
        name, price, quantity = product[1], product[2], product[3]
        
        print(f'Product: {name} with the price {price:.2f} and quantity {quantity}')
        print('Are you sure you want to remove this product?')
        confirm = input('[Y/N]: ').strip().lower()

        if confirm == 'y':
            db.execute_commit('DELETE FROM products WHERE id = ?', (id,))
            print('Product removed successfully!')
        else:
            print('Product was not removed.')
    else:
        print('Product not found.')


def menu():
    print('1. Add Product')
    print('2. List Products')
    print('3. Update Product')
    print('4. Remove Product')
    print('5. Clear Screen')
    print('6. Exit')

def admheader():
    print('------------------------------------')
    print('   Welcome to the Admin Interface   ')
    print('------------------------------------')

def header():
    print('------------------------------------')

def admin_interface():
    option = 0
    while option != 6:
        admheader()
        menu()
        try:
            option = int(input('Select the desired option: '))
        except ValueError:
            clear_screen()
            print('Invalid input. Please enter a number.')
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
        elif option == 6:
            clear_screen()
            print('Exiting the Admin Interface...')
        else:
            clear_screen()
            print('Invalid option.')

def main():
    login = input('Enter login: ')
    password = getpass.getpass('Enter password: ')
    
    if login_authentication(login, password):
        clear_screen()
        admin_interface()
    else:
        header()
        print('Access denied. Please try again.')
        header()
        main()