import getpass
from utils import clear_screen, header
import db

def find_product_by_id(product_id):
    return db.execute_query('SELECT * FROM products WHERE id = ?', (product_id,))

def login_authentication(username, password):
    return username == "Admin" and password == "0000"

def add_product():
    try:
        name = input('Enter product name: ').strip()
        price = float(input('Enter product price: '))
        quantity = int(input('Enter product quantity: '))

        if not name or price < 0 or quantity < 0:
            print("Invalid product data. Please try again.")
            return

        print(f'{name} with the price {price} and quantity {quantity}')
        confirm = input('Are you sure you want to add this product to the system? [Y/N]: ').strip().lower()

        if confirm == 'y':
            db.execute_commit('INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)', (name, price, quantity))
            print('Product added successfully!')
        else:
            print('Product was not added to the database.')
    except ValueError:
        print('Invalid input. Please enter valid numbers for price and quantity.')

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
    try:
        product_id = int(input('Enter the product ID to update: '))
        product = find_product_by_id(product_id)

        if product:
            product = product[0]
            name, price, quantity = product[1], product[2], product[3]

            print(f'Current product: {name}, Price: {price:.2f}, Quantity: {quantity}')

            new_name = input(f'Enter new name (current: {name}): ').strip() or name
            new_price = float(input(f'Enter new price (current: {price}): ') or price)
            new_quantity = int(input(f'Enter new quantity (current: {quantity}): ') or quantity)

            if new_name and new_price >= 0 and new_quantity >= 0:
                db.execute_commit('UPDATE products SET name = ?, price = ?, quantity = ? WHERE id = ?', 
                                  (new_name, new_price, new_quantity, product_id))
                print('Product updated successfully!')
            else:
                print('Invalid product data.')
        else:
            print('Product not found.')
    except ValueError:
        print('Invalid input. Please enter valid numbers.')

def remove_product():
    try:
        product_id = int(input('Enter the product ID to remove: '))
        product = find_product_by_id(product_id)

        if product:
            product = product[0]
            name, price, quantity = product[1], product[2], product[3]
            
            print(f'Product: {name} with the price {price:.2f} and quantity {quantity}')
            confirm = input('Are you sure you want to remove this product? [Y/N]: ').strip().lower()

            if confirm == 'y':
                db.execute_commit('DELETE FROM products WHERE id = ?', (product_id,))
                print('Product removed successfully!')
            else:
                print('Product was not removed.')
        else:
            print('Product not found.')
    except ValueError:
        print('Invalid input. Please enter a valid product ID.')

def menu():
    print('1. Add Product')
    print('2. List Products')
    print('3. Update Product')
    print('4. Remove Product')
    print('5. Clear Screen')
    print('6. Exit')

def admin_interface():
    option = 0
    while option != 6:
        header('Admin Interface')
        menu()
        try:
            option = int(input('Select the desired option: '))
            clear_screen()

            if option == 1:
                add_product()
            elif option == 2:
                list_products()
            elif option == 3:
                list_products()
                update_product()
            elif option == 4:
                list_products()
                remove_product()
            elif option == 5:
                clear_screen()
            elif option == 6:
                print('Exiting the Admin Interface...')
            else:
                print('Invalid option.')
        except ValueError:
            clear_screen()
            print('Invalid input. Please enter a number.')

def main():
    login = input('Enter login: ')
    password = getpass.getpass('Enter password: ')
    
    if login_authentication(login, password):
        clear_screen()
        admin_interface()
    else:
        print('Access denied. Please try again.')

if __name__ == "__main__":
    main()