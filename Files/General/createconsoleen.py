import os
from tkinter import*


while True:

    cd = os.getcwd()

    a = input(f'{cd} > ')

    if a == '.create(arg=console)':
        print('Temporarily Unavailable')
        print()

    elif '.create' in a:
        print('There is no argument or it is not correct')
        print()

    else:
        print(f'The {a} command is not an internal or external CreateConsole command')
        print()