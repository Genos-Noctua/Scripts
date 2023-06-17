from os import listdir, rename
import tkinter.filedialog, tqdm
from os.path import isfile, join

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
for x in tqdm.tqdm(range(len(holes)), smoothing=0):
    rename(
        str(music_dir) + "/" + str(files.pop()) + ".mp3",
        str(music_dir) + "/" + str(holes.pop()) + ".mp3",
    )
