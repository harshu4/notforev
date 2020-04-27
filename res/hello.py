from os import listdir
import os
from os.path import isfile, join
onlyfiles = [f for f in listdir(".") if isfile(join(".", f))]
print(onlyfiles)
onlyfiles.remove('hello.py')
x = 0 
for i in onlyfiles:
    print(i)
    print(x)
    stream = os.system('sox {} sound{}.mp3 repeat 10'.format(i,str(x)))
    x=x+1
