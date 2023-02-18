from pytube import YouTube
from pytube import Playlist
from tkinter import *
import os

def download(link,path,filterAudio):
    youtubeObject = YouTube(link)

    if not filterAudio: #false
        dwo = youtubeObject.streams.get_highest_resolution() #It doesnt get highest res. Only 720p
        dwo.download(path)

    else: #true
        dwo = youtubeObject.streams.filter(only_audio=True)[0].download(path)
        os.rename(dwo,path + "\\" + youtubeObject.title + ".mp3")


# declare the window and its properities
window = Tk()
window.title("Ruix's You Tube Video Downloader v1.1")
window.configure(width=500, height=500)
window.configure(bg='#121212')
window.iconbitmap("res/project.ico")
window.resizable(False,False)

#Input Box & label
entryBox = Entry(window,bg="#2c2c2c",fg="#ffffff",width=60)
entryBoxLabel = Label(text="Youtube Link: ",bg="#121212",fg="white")

#playlistBox = Entry(window,bg="#2c2c2c",fg="#ffffff",width=60)
#playlistBoxLabel = Label(text="Playlist Link: ",bg="#121212",fg="white")

locationBox = Entry(window,bg="#2c2c2c",fg="#ffffff",width=60)
locationBoxLabel = Label(text="Download Path :",bg="#121212",fg="white")
locationBox.insert(0,'Media')

#Button
mp4Button = Button(text="Download MP4",bg="#2c2c2c",command=lambda: download(entryBox.get(),locationBox.get(),False))
mp3Button = Button(text="Download MP3",bg="#2c2c2c",command=lambda: download(entryBox.get(),locationBox.get(),True))

#Add Playlist download https://pytube.io/en/latest/user/playlist.html   

#Grid
entryBoxLabel.grid(row=0,column=0)
entryBox.grid(row=0,column=1)

#playlistBoxLabel.grid(row=1,column=0)
#playlistBox.grid(row=1,column=1)

locationBoxLabel.grid(row=1,column=0)
locationBox.grid(row=1,column=1)

mp4Button.grid(row=0,column=2)
mp3Button.grid(row=1,column=2)

window.mainloop()
