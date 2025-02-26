import os
from tkinter import*


while True:

    cd = os.getcwd()

    a = input(f'{cd} > ')

    if a == '.create(arg=console)':
        os.startfile(f'{os.getcwd()}\Files\Consoles\defolt.py')
        print()

    elif '.create' in a:
        print('Аргумента нет или он не верный')
        print()

    else:
        print(f'Команда {a} не является внутренней или внешней командой CreateConsole')
        print()