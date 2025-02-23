import os
from tkinter import *
from art import text2art

file_path = f'{os.getcwd()}\start.py'

text = "CreateConsole"
ascii_art = text2art(text)
print(ascii_art)

print('Language - 1')
print()
print('Start - 2')
print()
a = input('')

if a == '1':
    os.startfile(file_path)