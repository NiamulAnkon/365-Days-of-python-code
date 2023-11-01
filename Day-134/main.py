from moviepy.editor import *

clip_1 = VideoFileClip("demo1.mp4").subclip(0, 10)
clip_2 = VideoFileClip("demo2.mp4").subclip(10,20)


comb = clips_array([[clip_1, clip_2]])

comb.write_videofile("test.mp4")
