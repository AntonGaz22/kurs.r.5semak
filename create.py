import json
import shutil
import os
import tkinter as tk
from tkinter import *
from datetime import datetime
from tkinter import ttk, scrolledtext
from tkinter import filedialog
from database import get_marki
from database import get_models

ADVERTISEMENTS = []

def create_add_window(parent=None):
    CARS = json.load(open('cars.json', encoding='utf-8'))

    TRANSMISSIONS = [
        {'id': 1, 'title': 'Механическая'},
        {'id': 2, 'title': 'Автоматическая'},
        {'id': 3, 'title': 'Вариатор'},
        {'id': 4, 'title': 'Робот'},
    ]

    IMAGES = []  # Список для хранения путей к изображениям

    # Функция, которая вызывается при выборе марки машины из Combobox
    def update_models(event):
        selected_make = selected_make_var.get()
        if selected_make in CARS:
            car_models = CARS[selected_make]
            model_combobox['values'] = [model['model'] for model in car_models]
            selected_model_var.set("")  # Очистите выбранную модель


    # Функция для загрузки фотографий
    def load_images():
        file_paths = filedialog.askopenfilenames(title="Выберите фотографии", filetypes=(("Image files", "*.jpg *.jpeg *.png *.gif"), ("All files", "*.*")))
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        image_paths = []

        for file_path in file_paths:
            # Определяем расширение файла
            _, file_extension = os.path.splitext(file_path)
            # Генерируем имя файла с временной меткой в качестве части имени
            new_file_name = f"{timestamp}_{os.path.basename(file_path)}"
            new_path = os.path.join("images", new_file_name)

            # Копируем исходное изображение в новый путь
            shutil.copy(file_path, new_path)
            image_paths.append(new_path)

        IMAGES.extend(image_paths)
        # Обновляем текст в виджете images_label и выравниваем его по левому краю
        images_label.config(text="\n".join(IMAGES), anchor='w')

    def clear_screnn():
        year_entry.delete(0, END)
        phone_entry.delete(0, END)
        comment_text.delete('1.0', END)
        make_combobox.set('')
        model_combobox.set('')
        transmission_combobox.set('')
        images_label.config(text="")


    def collect_data():
        data = {
            "make": make_combobox.get(),
            "model": model_combobox.get(),
            "year": year_entry.get(),
            "transmission": transmission_combobox.get(),
            "phone": phone_entry.get(),
            "comment": comment_text.get(1.0, END),
            "images": ';'.join(IMAGES)
        }

        ADVERTISEMENTS.append(data)
        clear_screnn()

    # Создаем главное окно
    root_new = tk.Toplevel(parent)
    root_new.title("Добавить объявление")
    root_new.geometry("800x600")  #  размер окна

    # Label "Марка машины"
    label_make = tk.Label(root_new, text="Марка машины")
    label_make.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    # Combobox (выпадающий список) с марками машин
    selected_make_var = tk.StringVar()
    make_combobox = ttk.Combobox(root_new, textvariable=selected_make_var, values=get_marki())
    make_combobox.grid(row=0, column=1, padx=10, pady=10, columnspan=2, sticky="ew")  # Используйте sticky="ew" для растяжения Combobox
    make_combobox.bind("<<ComboboxSelected>>", update_models)

    # Label "Модель машины"
    label_model = tk.Label(root_new, text="Модель машины")
    label_model.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    # Combobox (выпадающий список) с моделями машин
    selected_model_var = tk.StringVar()
    model_combobox = ttk.Combobox(root_new, textvariable=selected_model_var, values=get_models())
    model_combobox.grid(row=1, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label "Год выпуска"
    label_year = tk.Label(root_new, text="Год выпуска")
    label_year.grid(row=2, column=0, padx=10, pady=10, sticky="w")

    # Text Entry для года выпуска
    year_entry = tk.Entry(root_new)
    year_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label "Коробка передач"
    label_transmission = tk.Label(root_new, text="Коробка передач")
    label_transmission.grid(row=3, column=0, padx=10, pady=10, sticky="w")

    # Combobox (выпадающий список) с коробкой передач
    selected_transmission_var = tk.StringVar()
    transmission_combobox = ttk.Combobox(root_new, textvariable=selected_transmission_var, values=[transmission['title'] for transmission in TRANSMISSIONS])
    transmission_combobox.grid(row=3, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label "Телефон"
    label_phone = tk.Label(root_new, text="Телефон")
    label_phone.grid(row=4, column=0, padx=10, pady=10, sticky="w")

    # Text Entry для телефона
    phone_entry = tk.Entry(root_new)
    phone_entry.grid(row=4, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label "Комментарий"
    label_comment = tk.Label(root_new, text="Комментарий")
    label_comment.grid(row=5, column=0, padx=10, pady=10, sticky="w")

    # Text Area для комментария (используйте scrolledtext)
    comment_text = scrolledtext.ScrolledText(root_new, width=40, height=10)
    comment_text.grid(row=5, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label "Фотографии"
    label_images = tk.Label(root_new, text="Фотографии")
    label_images.grid(row=6, column=0, padx=10, pady=10, sticky="w")

    # Кнопка "Загрузить фотографии"
    load_images_button = tk.Button(root_new, text="Загрузить фотографии", command=load_images)
    load_images_button.grid(row=6, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Label для отображения путей к изображениям
    images_label = tk.Label(root_new, text="", wraplength=400)
    images_label.grid(row=8, column=1, padx=10, pady=10, columnspan=2, sticky="ew")

    # Создаем кнопку на главном окне
    button = tk.Button(root_new, text="Загрузить данные", command=collect_data)
    button.grid(row=9, column=0, padx=10, pady=10, columnspan=3, sticky="ew")
