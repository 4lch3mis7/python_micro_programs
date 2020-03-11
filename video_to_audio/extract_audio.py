import sys
from moviepy.editor import *

video = VideoFileClip(sys.argv[1])
audio = video.audio
audio.write_audiofile(sys.argv[2])

# 1. Save this file as extract_audio.py
# 2. Type $python extract_audio.py video_for_audio.mp4 audio_from_video.mp3
