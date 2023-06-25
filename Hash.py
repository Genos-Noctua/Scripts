import os, hashlib
from tkinter import filedialog

def get_folder_hash(path):
    # Создаем объект алгоритма хеширования SHA-256
    hash_object = hashlib.sha256()

    # Рекурсивно обходим все файлы и подпапки в папке
    for root, dirs, files in os.walk(path):
        # Сортируем имена файлов, чтобы сохранить одинаковый порядок обхода
        files.sort()

        # Читаем данные из каждого файла и обновляем хеш-объект
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'rb') as f:
                # Обновляем хеш-объект блоками
                chunk = f.read(4096)
                while chunk:
                    hash_object.update(chunk)
                    chunk = f.read(4096)

    # Получаем и выводим финальный хеш в виде шестнадцатеричной строки
    final_hash = hash_object.hexdigest()
    return final_hash

print(get_folder_hash(filedialog.askdirectory()))