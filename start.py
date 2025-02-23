import os
from tkinter import*
from art import text2art

text = "CreateConsole"
ascii_art = text2art(text)  # Создание ASCII-арта
print(ascii_art)





while True:

    cd = os.getcwd()

    a = input(f'{cd} > ')

    if a == '.create(arg=console)':
        print('Временно Недоступно >(')
        print()

    elif '.create' in a:
        print('Аргумента нет или он не верный')
        print()

    else:
        print(f'Команда {a} не является внутренней или внешней командой CreateConsole')
        print()
