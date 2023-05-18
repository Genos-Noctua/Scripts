import numpy as np
from PIL import Image
from tqdm import tqdm
from tkinter import Tk
from os.path import dirname
from tkinter.filedialog import askopenfilenames

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
output_dir = dirname(files[0])
Image.fromarray(means).save(output_dir + '/output.png')

root.quit()
root.destroy()
