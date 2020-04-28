import os
import subprocess
from random import sample
from random import randint
story_audio="./input/in.mp3"
photo_to_video_tempfile="./temp/temp_p2v.mp4"
mid_out_file="./temp/temp_mid.mp4"
intro_file="./static/intro.mp4"
outro_file="./static/outro.mp4"
final_file="./output/yt.mp4"

if os.path.exists("./temp"):
    os.popen("rm -r ./temp").readlines()

os.makedirs("./temp")

#select random images from static folder and cp it to temp folder
images=os.popen("cd static && ls | grep .jpg").readlines()
total_images=len(images)
selction_number=randint(4,total_images)
selected=sample(images,selction_number)
xselcted=["./temp/"+str(x)+".jpg" for x in range(1,selction_number+1)]
selected=((" ./static/".join(selected)).replace("\n","")).split(" ")
for x in range(selction_number):
    os.system("cp "+selected[x]+" "+xselcted[x])



#get length of audio in sec
cmd=f'ffprobe -i {story_audio} -show_entries format=duration -v quiet -of csv="p=0"'
ffprobe_out = os.popen(cmd).readlines()
audio_duration=float(ffprobe_out[0].replace("\n",""))

#length of audio/4  to get time in sec per each frame
frame_rate=1/(audio_duration/selction_number)

#photo to video convert
cmd=f"ffmpeg -framerate {frame_rate} -i ./temp/%d.jpg -s 1920x1280 -r 25 -pix_fmt yuv420p {photo_to_video_tempfile}".split(" ")
subprocess.Popen(cmd).wait()

#add audio to p2v file
cmd=f"ffmpeg -i {photo_to_video_tempfile} -i {story_audio} {mid_out_file}".split(" ")
subprocess.Popen(cmd).wait()

#merge intro and outro
cmd=f'ffmpeg -i {intro_file} -i {mid_out_file} -i {outro_file}   -filter_complex "[0:v]scale=1920x1280,setdar=16/9[v0]; [1:v]scale=1920x1280,setdar=16/9[v1]; [2:v]scale=1920x1280,setdar=16/9[v2]; [v0][0:a][v1][1:a][v2][2:a]concat=n=3:v=1:a=1" {final_file}'
#cmd=f"MP4Box -cat {intro_file} -cat {mid_out_file} -cat {outro_file} -new {final_file}".split(" ")
os.system(cmd)


print("\n\nOutput genrated at ./output/yt.mp4")
