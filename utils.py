import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def header(title=''):
    print('-------------------------')
    if title:
        print(f'     {title}       ')
    else:
        print('     Market System     ')
    print('-------------------------')
