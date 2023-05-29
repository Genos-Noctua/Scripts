import os, shutil, tkinter.filedialog, tqdm, hashlib
#Can be used to search for bitwise identical files and separate them from the main set
src_dir = tkinter.filedialog.askdirectory()
temp_dir = os.path.join(src_dir, 'Duplicates')
os.makedirs(temp_dir, exist_ok=True)
map = set()

def hash(file):
    with open(file, "rb") as f:
        data = f.read()
        hash_object = hashlib.sha256(data)
    return hash_object.hexdigest()

for file in tqdm.tqdm(os.listdir(src_dir), smoothing=0, desc='Проверка'):
    if '.mp3' in file:
        src_file = os.path.join(src_dir, file)
        sum = hash(src_file)
        if sum in map:
            dst_file = os.path.join(temp_dir, file)
            shutil.move(src_file, dst_file)
        else:
            map.add(sum)
