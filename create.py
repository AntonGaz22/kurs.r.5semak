import json
import shutil
import os
import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import ttk, scrolledtext
from tkinter import filedialog
from database import *

ADVERTISEMENTS = []

def create_add_window(parent=None):
    '''создаем функцию create_add_window, которая создает окно и определяет все необходимые элементы интерфейса и их функциональность.'''
    form_data = get_data_from_form()

    CARS = form_data['cars']
    TRANSMISSIONS = form_data['transmissions']
    '''переменная form_data используется для хранения данных из базы данных, в частности, доступных марок, моделей автомобилей и трансмиссий'''

    IMAGES = []
    '''список для хранения путей к изображениям'''

    def update_models(event):
        '''определяем функцию update_models для выбора марки машины из Combobox  '''
        selected_make = selected_make_var.get()
        if selected_make in CARS:
            car_models = CARS[selected_make]
            model_combobox['values'] = [model['model'] for model in car_models]
            selected_model_var.set("")


    def load_images():
        '''создаем функцию load_images для загрузки фотографий'''

        file_paths = filedialog.askopenfilenames(title="Выберите фотографии", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        image_paths = []

        for file_path in file_paths:
            '''определяем расширение файла'''
            _, file_extension = os.path.splitext(file_path)
            '''генерируем имя файла с временной меткой в качестве части имени'''
            new_file_name = f"{timestamp}_{os.path.basename(file_path)}"
            new_path = os.path.join("images", new_file_name)

            shutil.copy(file_path, new_path)
            image_paths.append(new_path)
            '''делаем копию исходного изображения в новый путь'''

        IMAGES.extend(image_paths)
        images_label.config(text="\n".join(IMAGES), anchor='w')
        '''Обновляем текст в виджете images_label и выравниваем его по левому краю'''

    def clear_screnn():
        '''создаем функцию clear_screnn, которая очищает некоторые виджеты в пользовательском интерфейсе'''
        year_entry.delete(0, END)
        phone_entry.delete(0, END)
        comment_text.delete('1.0', END)
        make_combobox.set('')
        model_combobox.set('')
        transmission_combobox.set('')
        images_label.config(text="")


    def collect_data():
        '''создаем функцию collect_data собирает данные из различных полей формы или пользовательского интерфейса и сохраняет их в словаре data'''
        data = {
            "make": make_combobox.get(),
            "model": model_combobox.get(),
            "transmission": transmission_combobox.get(),
            "year": year_entry.get(),
            "phone": phone_entry.get(),
            "comment": comment_text.get(1.0, END),
            "images": ';'.join(IMAGES)
        }

        add_new_advertisement(data)
        clear_screnn()


    root_new = tk.Toplevel(parent)
    root_new.title("Добавить объявление")
    root_new.geometry("800x600")
    '''создаем окно, указываем название и размер '''


    label_make = tk.Label(root_new, text="Марка машины")
    label_make.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    selected_make_var = tk.StringVar()
    make_combobox = ttk.Combobox(root_new, textvariable=selected_make_var, values=list(CARS.keys()))
    make_combobox.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="ew")  # Используйте sticky="ew" для растяжения Combobox
    make_combobox.bind("<<ComboboxSelected>>", update_models)
    '''создаем выпадающий список make_combobox с марками машин'''


    label_model = tk.Label(root_new, text="Модель машины")
    label_model.grid(row=1, column=0, padx=10, pady=10, sticky="w")


    selected_model_var = tk.StringVar()
    model_combobox = ttk.Combobox(root_new, textvariable=selected_model_var, values=[])
    model_combobox.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")
    '''создаем выпадающий список model_combobox с моделями машин'''


    label_year = tk.Label(root_new, text="Год выпуска")
    label_year.grid(row=2, column=0, padx=10, pady=10, sticky="w")


    year_entry = tk.Entry(root_new)
    year_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


    label_transmission = tk.Label(root_new, text="Коробка передач")
    label_transmission.grid(row=3, column=0, padx=10, pady=10, sticky="w")


    selected_transmission_var = tk.StringVar()
    transmission_combobox = ttk.Combobox(root_new, textvariable=selected_transmission_var, values=[transmission['title'] for transmission in TRANSMISSIONS])
    transmission_combobox.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")
    '''создаем выпадающий список transmission_combobox с выбором коробки передач'''


    label_phone = tk.Label(root_new, text="Телефон")
    label_phone.grid(row=4, column=0, padx=10, pady=10, sticky="w")


    phone_entry = tk.Entry(root_new)
    phone_entry.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


    label_comment = tk.Label(root_new, text="Комментарий")
    label_comment.grid(row=5, column=0, padx=10, pady=10, sticky="w")


    comment_text = scrolledtext.ScrolledText(root_new, width=40, height=10)
    comment_text.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


    label_images = tk.Label(root_new, text="Фотографии")
    label_images.grid(row=6, column=0, padx=10, pady=10, sticky="w")


    load_images_button = tk.Button(root_new, text="Загрузить фотографии", command=load_images)
    load_images_button.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


    images_label = tk.Label(root_new, text="", wraplength=400)
    images_label.grid(row=8, column=1, padx=10, pady=10, columnspan=2, sticky="ew")


    button = tk.Button(root_new, text="Загрузить данные", command=collect_data)
    button.grid(row=9, column=0, padx=10, pady=10, columnspan=3, sticky="ew")

