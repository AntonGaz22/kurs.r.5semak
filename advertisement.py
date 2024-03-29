import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk # pip install pillow


def create_vehicle_window(info, parent=None):
    ''' Создаем окно Tkinter, указываем название и размер'''
    vehicle_window = tk.Toplevel(parent)
    vehicle_window.title("Все объявления")
    vehicle_window.geometry("800x600")


    canvas = tk.Canvas(vehicle_window)
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(bg='grey')
    '''Создаем canvas для размещения фреймов'''


    scrollbar = tk.Scrollbar(vehicle_window, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.configure(yscrollcommand=scrollbar.set)
    '''Добавляем полосу прокрутки для canvas'''


    frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")
    '''Создаем фрейм для хранения информации по объявлению.'''

    def create_vehicle_frame(vehicle_info):
        frame_vehicle = tk.Frame(frame, relief=tk.RIDGE, borderwidth=2)
        frame_vehicle.pack(side="top", fill="x")
        '''определяем функцию create_vehicle_frame(vehicle_info), которая принимает словарь vehicle_info в качестве входных данных'''


        for key, value in vehicle_info.items():
            if key != 'images':
                label = tk.Label(frame_vehicle, text=f"{key.capitalize()}: {value}")
                label.pack(anchor="w")
        '''отображение информации внутри фрейма'''

        image_frame = tk.Frame(frame_vehicle)
        image_frame.pack(anchor="w")


        images = vehicle_info.get('images', '').split(';')
        '''Разделение строки 'images' на ";" и отобразить каждое изображение'''

        for image_path in images:
            '''запускает цикл for, который перебирает список путей к файлам изображений, хранящихся в переменной images'''
            try:
                '''начало блока try, указывающее на то, что код внутри него потенциально может вызывать исключения, и программа должна корректно обрабатывать эти исключения.'''
                image = Image.open(image_path)
                height = 100  # высота изображения
                width = int((height / image.size[1]) * image.size[0])  # ширина пропорционально высоте
                image = image.resize((width, height))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(image_frame, image=photo)
                image_label.image = photo
                image_label.pack(side="left")
            except:
                pass


    for vehicle in info:
        '''цикл for, который выполняет итерацию по списку объектов vehicle, хранящихся в переменной info. '''
        create_vehicle_frame(vehicle)

    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))