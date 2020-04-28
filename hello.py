from os import listdir
import os
from os.path import isfile, join
import sys
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS 
import random
import subprocess
from pymongo import MongoClient 
client = MongoClient("mongodb+srv://admin:harsh619qwe@cluster0-049tw.mongodb.net/test?retryWrites=true&w=majority") 
story_obj = client.horror.stories.find_one()


if os.path.exists("./temp"):
    os.popen("rm -r ./temp").readlines()
sys.exit()
os.makedirs("./temp")

img = Image.open('res/thumb.jpg')

fnt = ImageFont.truetype('res/ab.otf', 225)
d = ImageDraw.Draw(img)
d.text((100, 50), story_obj['title'], font=fnt, fill=(229, 9, 20))
img.save('./temp/pil_text_font.png')
sys.exit()
mytext = open('horr.txt','r').read()
myobj = gTTS(text=mytext, lang='hi', slow=False) 
myobj.save("./temp/welcome.mp3")
num = random.randint(0,0)
os.system('ffmpeg -i ./temp/welcome.mp3 -i res/sound{}.mp3 -filter_complex "[0:a]volume=1[a0]; [1:a]volume=0.2[a1]; [a0][a1]amix=inputs=2:duration=shortest" ./temp/output.mp3'.format(str(num)))
os.system('sox ./temp/output.mp3 ./temp/oyee.mp3  speed 1.1 pitch -100 gain -10')
images=os.popen("cd res && ls | grep .jpg").readlines()
total_images=len(images)
selction_number=randint(4,total_images)
selected=sample(images,selction_number)
xselcted=["./temp/"+str(x)+".jpg" for x in range(1,selction_number+1)]
selected=((" ./res/".join(selected)).replace("\n","")).split(" ")
for x in range(selction_number):
    os.system("cp "+selected[x]+" "+xselcted[x])

story_audio="./temp/oyee.mp3"
photo_to_video_tempfile="./temp/temp_p2v.mp4"
mid_out_file="./temp/temp_mid.mp4"
intro_file="res/intro.mp4"
outro_file="res/outro.mp4"
final_file="./temp/yt.mp4"

#get length of audio in sec
cmd=f'ffprobe -i {story_audio} -show_entries format=duration -v quiet -of csv="p=0"'
ffprobe_out = os.popen(cmd).readlines()
audio_duration=float(ffprobe_out[0].replace("\n",""))

#length of audio/4  to get time in sec per each frame
frame_rate=1/(audio_duration/4)

#photo to video convert
cmd=f"ffmpeg -framerate {frame_rate} -i res/%d.jpg -s 1920x1280 -r 25 -pix_fmt yuv420p {photo_to_video_tempfile}".split(" ")
subprocess.Popen(cmd).wait()

#add audio to p2v file
cmd=f"ffmpeg -i {photo_to_video_tempfile} -i {story_audio} {mid_out_file}".split(" ")
subprocess.Popen(cmd).wait()

#merge intro and outro
os.system(f'ffmpeg -i {intro_file} -i {mid_out_file} -i {outro_file} -filter_complex "[0:v]scale=1920x1280,setdar=16/9[v0]; [1:v]scale=1920x1280,setdar=16/9[v1]; [2:v]scale=1920x1280,setdar=16/9[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1"  {final_file}')

clinet.horror.stories.delete_many({"title":story_obj['title']})
print("\n\nOutput genrated at ./output/yt.mp4")


   