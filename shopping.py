import db
from utils import clear_screen

cart = {}

def add_to_cart(product_id, quantity):
    product = db.execute_query('SELECT * FROM products WHERE id = ?', (product_id,))
    
    if not product:
        print('Product does not exist.')
        return
    
    available_quantity = product[0][3]
    
    if quantity > available_quantity:
        print(f'Insufficient quantity. Only {available_quantity} available.')
        return
    
    db.execute_commit('UPDATE products SET quantity = quantity - ? WHERE id = ?', (quantity, product_id))
    
    if product_id in cart:
        cart[product_id]['quantity'] += quantity
    else:
        cart[product_id] = {
            'name': product[0][1],
            'price': product[0][2],
            'quantity': quantity
        }

    print(f'Added {quantity} of {product[0][1]} to the cart.')

def remove_from_cart(product_id, quantity):
    if product_id not in cart:
        print('Product is not in the cart.')
        return
    
    if quantity > cart[product_id]['quantity']:
        print('Cannot remove more than what is in the cart.')
        return
    
    db.execute_commit('UPDATE products SET quantity = quantity + ? WHERE id = ?', (quantity, product_id))
    
    cart[product_id]['quantity'] -= quantity
    
    if cart[product_id]['quantity'] == 0:
        del cart[product_id]
        print('Product removed from the cart.')
    else:
        print(f'{quantity} of {cart[product_id]["name"]} removed from the cart.')

def view_cart():
    if not cart:
        print('Cart is empty.')
        return
    
    total_price = 0
    print('ID | Name        | Price    | Quantity | Total Price')
    print('-------------------------------------------------------')
    
    for product_id, details in cart.items():
        item_total = details['price'] * details['quantity']
        total_price += item_total
        print(f'{product_id:<2} | {details["name"]:<10} | {details["price"]:<8.2f} | {details["quantity"]:<10} | {item_total:<11.2f}')
    
    print(f'Total: {total_price:.2f}')

def purchase():
    if not cart:
        print('Cart is empty.')
        return
    
    print('Purchase completed successfully!')
    clear_cart()

def clear_cart():
    global cart
    cart = {}
    print('Cart cleared.')