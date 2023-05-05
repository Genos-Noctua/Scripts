import cv2
import os
import tkinter as tk
from tkinter import filedialog

# Создаем окно tkinter для выбора файла
root = tk.Tk()
root.withdraw()

# Открываем файловый диалог для выбора видео
file_path = filedialog.askopenfilename()

# Загружаем видео из выбранного файла
cap = cv2.VideoCapture(file_path)

# Создаем директорию для кадров с названием видео
video_name = os.path.splitext(os.path.basename(file_path))[0]
if not os.path.exists(video_name):
    os.makedirs(video_name)

# Обрабатываем каждый кадр видео
frame_count = 0
while(cap.isOpened()):
    # Читаем кадр
    ret, frame = cap.read()
    
    if ret==True:
        # Сохраняем кадр в папку
        cv2.imwrite(os.path.join(video_name, "frame%08d.jpg" % frame_count), frame) 
        frame_count += 1
        
        # Если нажата клавиша q - выход из цикла
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()