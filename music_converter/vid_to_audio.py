from moviepy.editor import VideoFileClip
import os

def path_to_name(path):
    small_path = path.split('/')
    total_dir = len(small_path)
    name = small_path[total_dir-1]
    splitted = name.split('.')
    name = splitted[0]
    return name

def convert_vid_to_audio(path):
    name = path_to_name(path)
    output_path = "/Users/emmasullivan/Downloads/Audios/" + name + ".mp3"

    video=VideoFileClip(path)
    video.audio.write_audiofile(output_path)