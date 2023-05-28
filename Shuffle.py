import os, shutil, tkinter.filedialog, random, string, tqdm

src_dir = tkinter.filedialog.askdirectory()
temp_dir = os.path.join(src_dir, 'temp')
os.makedirs(temp_dir, exist_ok=True)

for file in tqdm.tqdm(os.listdir(src_dir), smoothing=3, desc='Перенос и перемешивание'):
    if '.mp3' in file:
        src_file = os.path.join(src_dir, file)
        dst_file = os.path.join(temp_dir, os.path.join(temp_dir, ''.join(random.choices(string.ascii_lowercase, k=50)) + os.path.splitext(file)[1]))
        shutil.move(src_file, dst_file)

files = [f for f in os.listdir(temp_dir) if os.path.isfile(os.path.join(temp_dir, f))]
x = 1
for file in tqdm.tqdm(files, smoothing=3, desc='Возврат'):
    src_file = os.path.join(temp_dir, file)
    dst_file = os.path.join(src_dir, str(x)+'.mp3')
    os.rename(src_file, dst_file)
    x+=1

shutil.rmtree(temp_dir)
