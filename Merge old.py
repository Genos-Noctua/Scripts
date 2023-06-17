import numpy as np
from PIL import Image
from tqdm import tqdm
from os.path import dirname
from tkinter.filedialog import askopenfilenames

files = askopenfilenames()

size = (0, 0)
with Image.open(files[0]) as img: size = img.size
means = np.zeros(size[::-1] + (3,), dtype=np.float64)

for fil in tqdm(files, smoothing=0):
    with Image.open(fil) as img: 
        arr = np.array(img).astype(np.float64) 
        means += arr

means /= len(files)
means = means.astype(np.uint8)
output_dir = dirname(files[0])
Image.fromarray(means).save(output_dir + '/output.png')