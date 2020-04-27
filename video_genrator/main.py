import os
import subprocess

story_audio="./input/in.mp3"
photo_to_video_tempfile="./temp/temp_p2v.mp4"
mid_out_file="./temp/temp_mid.mp4"
intro_file="./static/intro.mp4"
outro_file="./static/outro.mp4"
final_file="./output/yt.mp4"

if os.path.exists("./temp"):
    os.popen("rm -r ./temp").readlines()

os.makedirs("./temp")

#get length of audio in sec
cmd=f'ffprobe -i {story_audio} -show_entries format=duration -v quiet -of csv="p=0"'
ffprobe_out = os.popen(cmd).readlines()
audio_duration=float(ffprobe_out[0].replace("\n",""))

#length of audio/4  to get time in sec per each frame
frame_rate=1/(audio_duration/4)

#photo to video convert
cmd=f"ffmpeg -framerate {frame_rate} -i ./static/%d.jpg -s 1920x1280 -r 25 -pix_fmt yuv420p {photo_to_video_tempfile}".split(" ")
subprocess.Popen(cmd).wait()

#add audio to p2v file
cmd=f"ffmpeg -i {photo_to_video_tempfile} -i {story_audio} {mid_out_file}".split(" ")
subprocess.Popen(cmd).wait()

#merge intro and outro
cmd=f"MP4Box -cat {intro_file} -cat {mid_out_file} -cat {outro_file} -new {final_file}".split(" ")
subprocess.Popen(cmd).wait()


print("\n\nOutput genrated at ./output/yt.mp4")
