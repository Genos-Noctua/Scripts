import os.path
import shutil
import random
import tkinter.filedialog
from os import listdir
from os.path import isfile, join

music_dir = tkinter.filedialog.askdirectory()
if not os.path.isdir(str(music_dir) + "/Music here"):
  os.mkdir(str(music_dir) + "/Music here")
files = [f for f in listdir(music_dir) if isfile(join(music_dir, f))]

list = []
while (len(list) != 1000):
  file = files[random.randint(0, len(files))]
  if file not in list:
    list.append(file)
for x in range(1000):
  file = list[x]
  shutil.move(str(music_dir) + "/" + file, str(music_dir) + "/Music here/" + file)
pass