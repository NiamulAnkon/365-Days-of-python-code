import moviepy.editor
from tkinter.filedialog import *
import os

vid = askopenfilename()

video = moviepy.editor.VideoFileClip(vid)

aud = video.audio

output_folder = "D:/ankonFolder/365daysofcode/Day-124"

output_filename = "audio.mp3"

output_path = os.path.join(output_folder, output_filename)

aud.write_audiofile(output_path)

print(f"Audio saved to: {output_path}")
print("--- Done ---")
