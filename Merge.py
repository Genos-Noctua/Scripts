from tkinter import Tk
from tkinter.filedialog import askopenfilenames
from PIL import Image
import numpy as np
from tqdm import tqdm

root = Tk()
root.withdraw()
files = askopenfilenames()

max_size = (0, 0)
with Image.open(files[1]) as img:
    arr = np.array(img)
    typee = arr.dtype
    max_size = img.size

means = np.zeros(max_size[::-1] + (3,), dtype=np.uint64)

for fil in tqdm(files): 
    with Image.open(fil) as img: 
        arr = np.array(img).astype(np.uint64) 
        means += arr

means = means.astype(np.float64)
means /= len(files)
means = means.astype(np.uint8)
Image.fromarray(means).save("output.png")

root.quit()
root.destroy()
