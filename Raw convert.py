import os, numpy, rawpy
from tkinter.filedialog import *
from PIL import Image as im

file = askopenfilenames()
for x in file:
    with rawpy.imread(x) as raw:
        rgb = raw.postprocess()
        rgb = im.fromarray(rgb)
        rgb.save(x + '.png')