import os

a=os.popen("ls| grep .jpg").readlines()
l=len(a)
for i in range(1,l):
    n=a[i]
    n=n.replace("\n","")
    os.system("mv "+n+" "+str(i)+".jpg")
