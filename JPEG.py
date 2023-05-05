from concurrent.futures import ThreadPoolExecutor
from os.path import splitext
from PIL import Image, ImageFile
from tkinter.filedialog import *
import os.path

ImageFile.LOAD_TRUNCATED_IMAGES = True
files = askopenfilenames()

def convert_image(file):
    with Image.open(file) as im:
        output_path = splitext(file)[0] + '.jpg'
        if not os.path.exists(output_path):
            im = im.convert('RGB')
            im.save(output_path, "JPEG", quality=100)
        else:
            print(f'File {output_path} already exists.')

with ThreadPoolExecutor() as executor:
    executor.map(convert_image, files)