from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from PIL import Image
import numpy as np

root = Tk()
root.withdraw()

files = askopenfilenames()

arr_list = []
max_size = (0, 0)

for file in files:
    with Image.open(file) as img:
        arr = np.array(img)
        arr_list.append(arr)
        if img.size > max_size:
            max_size = img.size

means = np.zeros(max_size[::-1] + (3,), dtype=np.float32)

for arr in arr_list:
    img_arr = Image.fromarray(arr)
    img_arr = img_arr.resize(max_size, resample=Image.Resampling.BICUBIC)
    arr = np.array(img_arr)
    means += arr.astype(np.float32)

means /= len(arr_list)
means = means.astype(np.uint8)
Image.fromarray(means).save("output.png")

root.quit()
root.destroy()