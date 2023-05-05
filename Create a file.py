from tkinter.filedialog import *
from tqdm import tqdm

dir = askdirectory()
print('Enter size:')
f = open(dir + '/Target_file.txt', 'w')
size = input()
match size[-1]:
  case 'B':
    mode = 0
  case 'K':
    mode = 1
  case 'M':
    mode = 2
  case 'G':
    mode = 3
  case 'T':
    mode = 4
string='A'
size=float(size[:-1])
if mode>1:
  for x in range(mode-1):
    size*=1024
  for x in tqdm(range(1024)):
    print(string*int(size), file=f, end='')
else:
  print(string*int(size), file=f, end='')
pass