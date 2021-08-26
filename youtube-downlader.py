from pytube import YouTube
from pytube.contrib.playlist import Playlist 
link = 'https://www.youtube.com/watch?v=U-PXEe-qeK4'
#link = input("please enter the video url: ")

video = YouTube(link)
#print(f"The video tite is:\n{video.title} \n_____________________")
#print(f"The video description is: \n{video.description}\n______________________")
#print(f"The video views are: {video.views} \n_________________________")
#print(f"The video rating is: {video.rating}\n_________________________________")
#print(f"The video duration is : {video.length/60} minutes \n_____________________________")
streams = video.streams 
for stream in streams:
    print(stream)

#for stream in streams.filter(progressive= True):
#    print(stream)
#for stream in streams.filter(res="480p"):
#    print(stream)
#print(video.streams.get_highest_resolution())
#print(video.streams.get_lowest_resolution())
def finish():
    print("download done")

video.streams.filter(abr = "160kbps",type="audio").download(output_path="C:/Users/hp/Videos/videos download")
#video.streams.get_highest_resolution().download(output_path="C:/Users/hp/Videos/videos download")
video.register_on_complete_callback(finish())

#from pytube import Playlist

#playlist_link = ""
#playlist = Playlist(link)

#for video in playlist.videos:
#   video.streams.get_highes_resolution().download(output_path="C:/Users/hp/Videos/videos download")

