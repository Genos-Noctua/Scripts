import os
import random
import shutil
import string
import tkinter.filedialog

# запрашиваем исходную директорию через диалоговое окно
src_dir = tkinter.filedialog.askdirectory()

# создаем временную директорию
temp_dir = os.path.join(src_dir, 'temp')
os.makedirs(temp_dir, exist_ok=True)

# копируем все файлы во временную директорию
for file in os.listdir(src_dir):
    src_file = os.path.join(src_dir, file)
    dst_file = os.path.join(temp_dir, file)
    shutil.copy(src_file, dst_file)

# получаем список файлов во временной директории
files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]

# перемешиваем имена файлов
random.shuffle(files)

# создаем список новых имен файлов без коллизий
new_names = []
for i, file in enumerate(files):
    while True:
        new_name = ''.join(random.choices(string.ascii_lowercase, k=8)) + os.path.splitext(file)[1]
        if new_name not in new_names:
            new_names.append(new_name)
            break

# переименовываем каждый файл и переносим в исходную директорию
for i, file in enumerate(files):
    src_file = os.path.join(temp_dir, file)
    dst_file = os.path.join(src_dir, new_names[i])
    os.rename(src_file, dst_file)

# удаляем временную директорию
shutil.rmtree(temp_dir)