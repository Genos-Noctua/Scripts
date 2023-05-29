import os
import shutil
import tkinter.filedialog
import tqdm
from mutagen.mp3 import MP3
# Can be used to search for audio files with the same metadata (author and title) 
# and separate them from the main set
src_dir = tkinter.filedialog.askdirectory()
temp_dir = os.path.join(src_dir, 'Duplicates')
os.makedirs(temp_dir, exist_ok=True)
map = {}

def get_audio_info(file):
	audio = MP3(file)
	return audio['TPE1'].text[0], audio['TIT2'].text[0]

for file in tqdm.tqdm(os.listdir(src_dir), smoothing=0, desc='Проверка'):
	if file.lower().endswith('.mp3'):
		src_file = os.path.join(src_dir, file)
		try:
			author, title = get_audio_info(src_file)
		except:
			continue
		key = f'{author}_{title}'
		if key in map:
			dst_file = os.path.join(temp_dir, file)
			shutil.move(src_file, dst_file)
		else:
			map[key] = src_file