import glob
import os
import tkinter.filedialog

music_dir = tkinter.filedialog.askdirectory()
files = sorted(
    [int(os.path.splitext(os.path.basename(f))[0]) for f in glob.glob(os.path.join(music_dir, "*.mp3")) if os.path.isfile(f)]
)
holes = [x for x in range(1, len(files)) if x not in files] + [len(files)]

while len(holes) > 0:
    src = os.path.join(music_dir, f"{files.pop()}.mp3")
    dst = os.path.join(music_dir, f"{holes.pop()}.mp3")
    os.rename(src, dst)

print("Done")