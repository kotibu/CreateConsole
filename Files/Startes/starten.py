import os
from tkinter import *
from art import text2art

file_path = f'{os.getcwd()}\start.py'
file_path2 = f'{os.getcwd()}\Files\General\createconsoleru.py'

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

if a == '2':
    os.startfile(file_path2)