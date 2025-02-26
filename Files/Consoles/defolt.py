import tkinter as tk
from tkinter import ttk, messagebox, filedialog

def open_file():
    """Открывает файл."""
    messagebox.showinfo("Открытие", f"Открытие не работает. Открывается тоже самое.")
    filepath = filedialog.askopenfilename(title="Открыть файл")
    if filepath:
        messagebox.showinfo("Открытие файла", f"Файл {filepath} открыт.")
        # Здесь можно добавить код для работы с файлом

def save_file():
    """Сохраняет файл."""
    messagebox.showinfo("Сохранение файла", f"Сохранение не работает. Сохраняется тоже самое.")
    filepath = filedialog.asksaveasfilename(title="Сохранить файл")
    if filepath:
        messagebox.showinfo("Сохранение файла", f"Файл сохранен как {filepath}.")
        # Здесь можно добавить код для сохранения файла

def exit_app():
    """Выходит из приложения."""
    if messagebox.askokcancel("Выход", "Вы уверены, что хотите выйти?"):
        root.destroy()

def show_about():
    """Показывает окно "О программе"."""
    messagebox.showinfo("О программе", "Прочитайте README.md")

def change_theme(theme_name):
    """Изменяет тему приложения."""
    ttk.Style().theme_use(theme_name)
    messagebox.showinfo("Смена темы", f"Тема изменена на {theme_name}.")


# Создание основного окна
root = tk.Tk()
root.title("Пример меню")

# Создание главного меню
main_menu = tk.Menu(root)
root.geometry('250x250')
root.config(menu=main_menu)

# ---- Меню "Файл" ----
file_menu = tk.Menu(main_menu, tearoff=0)  # tearoff=0 убирает отрывную линию
main_menu.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Открыть...", command=open_file)
file_menu.add_command(label="Сохранить как...", command=save_file)
file_menu.add_separator() # Добавляет разделитель
file_menu.add_command(label="Выход", command=exit_app)

# ---- Меню "Редактировать" ----
edit_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Редактировать", menu=edit_menu)

edit_menu.add_command(label="Проверить работу", command=lambda: print('Связь с окном есть.'))
edit_menu.add_command(label="Вставить", command=lambda: messagebox.showinfo("Редактирование", "Вставить"))
edit_menu.add_command(label="Вырезать", command=lambda: messagebox.showinfo("Редактирование", "Вырезать"))

# ---- Меню "Вид" ----
view_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Вид", menu=view_menu)

# Создание подменю "Темы"
themes_menu = tk.Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Темы", menu=themes_menu)

themes_menu.add_command(label="clam", command=lambda: change_theme("clam"))
themes_menu.add_command(label="alt", command=lambda: change_theme("alt"))
themes_menu.add_command(label="default", command=lambda: change_theme("default"))
themes_menu.add_command(label="classic", command=lambda: change_theme("classic"))


# ---- Меню "Справка" ----
help_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Справка", menu=help_menu)

help_menu.add_command(label="О программе...", command=show_about)


# ---- Контент окна (для примера) ----


# Запуск основного цикла
root.mainloop()