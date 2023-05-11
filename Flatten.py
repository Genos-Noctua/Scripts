from os import path, listdir, mkdir, rename
import tkinter.filedialog
from os.path import isfile, join, isdir

music_dir = tkinter.filedialog.askdirectory()
files = [f for f in listdir(music_dir) if isfile(join(music_dir, f))]
length = len(files)
for x in range(length):
    try:
        files[x] = int(files[x][:-4])
    except ValueError:
        files.pop(x)
files = sorted(files)
holes = list()
for x in range(1, length):
    if not isfile(join(music_dir, str(str(x) + ".mp3"))):
        holes.append(x)
for x in range(len(holes)):
    rename(
        str(music_dir) + "/" + str(files[len(files) - 1]) + ".mp3",
        str(music_dir) + "/" + str(holes[len(holes) - 1]) + ".mp3",
    )
    files.pop(len(files) - 1)
    holes.pop(len(holes) - 1)
