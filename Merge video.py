from tkinter import Tk
from PIL import Image
import numpy as np
import cv2

# Открываем диалог выбора файлов
root = Tk()
root.withdraw()
video = "video.mp4"
out = "output.png"
cap = cv2.VideoCapture(video)
i = 0

# Преобразуем изображения в массив numpy и находим среднее арифметическое
means = None
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    arr = np.array(frame)

    # Если это первое изображение, то создаем массив для сохранения среднего
    if i == 0:
        means = np.zeros_like(arr, dtype=np.float32)

    # Добавляем значения изображения к массиву среднего
    means += arr.astype(np.float32)
    i += 1
# Вычисляем среднее арифметическое и сохраняем его в файл
means /= i
means[:, :, [0, 2]] = means[:, :, [2, 0]]
means = means.astype(np.uint8)
Image.fromarray(means).save(out)