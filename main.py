import tkinter as tk
from create import create_add_window, ADVERTISEMENTS
from advertisement import create_vehicle_window
from database import all_advertisements

root = tk.Tk()
'''Создаем главное окно с помощью tk.Tk()'''
root.title("Авторынок")
'''Задаем заголовок окна с помощью метода title()'''


root.geometry("800x600")
'''Задаем размер окна с помощью метода geometry()'''
#root['background']='#856ff8'
root.configure(bg='grey')
'''Задаем цвет окна с помощью метода configure() или установкой атрибута bg'''

'''Определяем функции add_advert() и all_advert() для обработки нажатия кнопок'''
def add_advert():
    '''Определяем функцию add_advert() для обработки нажатия кнопки для создания объявления'''
    create_add_window(root)

def all_advert():
    '''Определяем функцию all_advert() для обработки нажатия кнопки дл просмотра всех объявлений'''
    create_vehicle_window(info=all_advertisements(), parent=root)



font = ("Helvetica", 14)
'''Устанавливаем размер шрифта кнопок с помощью аргумента font'''


btn_new = tk.Button(root, text="Добавить объявление", command=add_advert, font=font, bg='black', fg='white')
btn_all = tk.Button(root, text="Просмотреть объявления", command=all_advert, font=font, bg='black', fg='white' )
'''Создаем кнопки с помощью tk.Button(), oпределяем обработчики нажатия кнопок с помощью аргумента command'''


btn_new.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
btn_all.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
'''Размещаем кнопки на окне с помощью метода place()'''


root.mainloop()
'''Запускаем главное окно с помощью метода mainloop()'''