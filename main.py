import tkinter as tk
from create import create_add_window, ADVERTISEMENTS
from advertisement import create_vehicle_window
from database import all_advertisements

# Создаем главное окно
root = tk.Tk()
root.title("Авторынок")

# Задаем размер окна и цвет
root.geometry("800x600")
#root['background']='#856ff8'
root.configure(bg='grey')
# Функции для кнопок
def add_advert():
    # открытие окна для добавления объявления
    create_add_window(root)

def all_advert():
    # открытие окна просмотра всех объявлений
    create_vehicle_window(info=all_advertisements(), parent=root)

# Создаем шрифт с размером 14px
font = ("Helvetica", 14)

# Создаем кнопки с установленным размером шрифта
btn_new = tk.Button(root, text="Добавить объявление", command=add_advert, font=font, bg='black', fg='white')
btn_all = tk.Button(root, text="Просмотреть объявления", command=all_advert, font=font, bg='black', fg='white' )

# Размещаем кнопки по центру по горизонтали и вертикали
btn_new.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
btn_all.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Запускаем главное окно
root.mainloop()