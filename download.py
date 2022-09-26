import os

path = '/home/bsanse/Downloads/'
files = os.listdir(path)

for file in files:
    if '.jpg' in file:
        os.remove(path + file)
