from moviepy.editor import *


video = VideoFileClip("Dominating.mp4").subclip(46,48)
video.write_gif("test.gif")
print("Done")
