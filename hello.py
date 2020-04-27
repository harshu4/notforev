from os import listdir
import os
from os.path import isfile, join
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
print(onlyfiles)
x = 0 
for i in onlyfiles:
    stream = os.popen(f'sox {i} sound{str(x)}.mp3 repeat 20')