from pytube import YouTube
from tkinter import *

def Download(link,path):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution() #It doesnt get highest res. Only 720p

    try:
        youtubeObject.download(path)
    except:
        pass

# declare the window and its properities
window = Tk()
window.title("Ruix's You Tube Video Downloader v1.0")
window.configure(width=500, height=500)
window.configure(bg='#121212')
window.iconbitmap("res/project.ico")

#Canvas
#canvas = Canvas(window,width=250,height=125)
#canvas.pack()

#Input Box & label
entryBox = Entry(window,bg="#2c2c2c",fg="#ffffff",width=60)
entryBoxLabel = Label(text="Youtube Link: ",bg="#121212",fg="white")

locationBox = Entry(window,bg="#2c2c2c",fg="#ffffff",width=60)
locationBoxLabel = Label(text="Download Path :",bg="#121212",fg="white")
locationBox.insert(0,'Videos')

#Button
okButton = Button(text="Download",bg="#2c2c2c",command=lambda: Download(entryBox.get(),locationBox.get()))


#Grid
entryBoxLabel.grid(row=0,column=0)
entryBox.grid(row=0,column=1)

locationBoxLabel.grid(row=1,column=0)
locationBox.grid(row=1,column=1)

okButton.grid(row=0,column=2)

window.mainloop()
