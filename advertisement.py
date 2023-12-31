import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk # pip install pillow


def create_vehicle_window(info, parent=None):
    # Создает новое окно Tkinter
    vehicle_window = tk.Toplevel(parent)
    vehicle_window.title("Все объявления")
    vehicle_window.geometry("800x600")


    # Создает canvas для размещения фреймов
    canvas = tk.Canvas(vehicle_window)
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(bg='grey')

    # Добавляет полосу прокрутки для canvas
    scrollbar = tk.Scrollbar(vehicle_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Создает фрейм для хранения информации по объявлению.
    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def create_vehicle_frame(vehicle_info):
        frame_vehicle = tk.Frame(frame, relief=tk.RIDGE, borderwidth=2)
        frame_vehicle.pack(side="top", fill="x")

        # Отображение информации внутри фрейма
        for key, value in vehicle_info.items():
            if key != 'images':
                label = tk.Label(frame_vehicle, text=f"{key.capitalize()}: {value}")
                label.pack(anchor="w")  # выравнивание по левому краю

        image_frame = tk.Frame(frame_vehicle)
        image_frame.pack(anchor="w")

        # # Разделить строку 'images' на ";" и отобразить каждое изображение
        images = vehicle_info.get('images', '').split(';')
        for image_path in images:
            image = Image.open(image_path)
            height = 100  # высота изображения
            width = int((height / image.size[1]) * image.size[0])  # ширина пропорционально высоте
            image = image.resize((width, height))
            photo = ImageTk.PhotoImage(image)
            image_label = tk.Label(image_frame, image=photo)
            image_label.image = photo
            image_label.pack(side="left")


    for vehicle in info:
        create_vehicle_frame(vehicle)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))
