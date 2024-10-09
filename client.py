import db
import shopping
from utils import clear_screen, header

def list_products():
    products = db.execute_query('SELECT * FROM products')
    
    if products:
        print('ID | Name        | Price   | Quantity')
        print('--------------------------------------')
        for product in products:
            print(f'{product[0]:<2} | {product[1]:<10} | {product[2]:<7.2f} | {product[3]:<8}')
    else:
        print('No products found.')

def client_menu():
    print('1. List Products')
    print('2. Add Product to Cart')
    print('3. Remove Product from Cart')
    print('4. View Cart')
    print('5. Purchase')
    print('6. Clear Screen')
    print('7. Exit')

def client_header():
    header('Client Interface')

def client_interface():
    option = 0
    while option != 7:
        client_header()
        client_menu()
        try:
            option = int(input('Select the desired option: '))
        except ValueError:
            clear_screen()
            print('Invalid input. Please enter a number.')
            continue

        if option == 1:
            clear_screen()
            list_products()
        elif option == 2:
            clear_screen()
            list_products()
            print()
            try:
                product_id = int(input('Enter the product ID to add to the cart: '))
                quantity = int(input('Enter the quantity: '))
            except ValueError:
                print('Invalid input. Product ID and quantity must be numbers.')
                continue
            clear_screen()
            shopping.add_to_cart(product_id, quantity)
        elif option == 3:
            clear_screen()
            shopping.view_cart()
            try:
                product_id = int(input('Enter the product ID to remove from the cart: '))
                quantity = int(input('Enter the quantity to remove: '))
            except ValueError:
                print('Invalid input. Product ID and quantity must be numbers.')
                continue
            shopping.remove_from_cart(product_id, quantity)
        elif option == 4:
            clear_screen()
            shopping.view_cart()
        elif option == 5:
            clear_screen()
            shopping.view_cart()
            confirmation = input('Are you sure you want to proceed with the purchase? (Y/N): ').strip().lower()
            if confirmation == 'y':
                clear_screen()
                shopping.purchase()
            else:
                print('Purchase canceled.')
        elif option == 6:
            clear_screen()
        elif option == 7:
            clear_screen()
            print('Exiting the Client Interface...')
        else:
            clear_screen()
            print('Invalid option.')

def main():
    client_interface()

if __name__ == "__main__":
    main()
