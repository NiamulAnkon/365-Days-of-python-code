from pytube import YouTube

def download_video(url, path_save):
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True, file_extension="mp4")
        highest_res = streams.get_highest_resolution()
        highest_res.download(output_path=path_save)
        print("video DOwnloaded succesfuly")
    except Exception as e:
        print(e)

url= "https://www.youtube.com/watch?v=zT7niRUOs9o"
path_save = "D:/ankonFolder/365daysofcode/Day-317"

download_video(url , path_save)
