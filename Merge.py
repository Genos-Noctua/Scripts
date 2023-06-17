import numpy as np
import time
from PIL import Image
from factory import *
from os.path import dirname
from tkinter.filedialog import askopenfilenames

def summer(package):
    list = package.special['imgs']
    mean = package.special['mean']
    for x in range(len(list)):
        img = list.pop()
        with Image.open(img) as img: 
            mean += np.array(img).astype(np.float64) 
    package.special['mean'] = mean
    package.dst = -1
    return package

if __name__ == '__main__':
    pros = mp.cpu_count()
    files = askopenfilenames()
    start_time = time.time()
    max_size = (0, 0)
    with Image.open(files[0]) as img: max_size = img.size
    factory = Factory((summer,), processes=pros, pressure=100)
    lists = [[] for _ in range(pros)]
    for x in range(len(files)):
        lists[x%pros].append(files[x])
    for x in range(pros):
        pack = factory.get_pack()
        pack.special = {'imgs': lists[x], 'mean': np.zeros(max_size[::-1] + (3,), dtype=np.float64)}
        factory.add(pack)
    del(lists)
    x = 1
    mean = factory.drain.get().special['mean']
    while x < pros:
        mean += factory.drain.get().special['mean']
        x+=1
    factory.kill()
    mean /= len(files)
    mean = mean.astype(np.uint8)
    end_time = time.time()
    Image.fromarray(mean).save(dirname(files[0]) + '/output.png')
    print("Прошло", int(end_time - start_time), "секунд")