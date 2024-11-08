import os
import time

for root, dirs, files in os.walk(r'C:\Users\Сергей\PycharmProjects\pythonProject7\.venv\modul_7\modul_7_3'):
    for file in files:
        filepath = os.path.join(r'C:\Users\Сергей\PycharmProjects\pythonProject7\.venv\modul_7\modul_7_3', file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')