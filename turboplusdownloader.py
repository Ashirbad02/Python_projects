from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
Folder_Name=""
def openlocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name)>1):
        locationError.config(text="Folder_Name",fg="green")

    else:
        locationError.config(text="please choose valid folder ",fg="red")

def downloadvideo():
    choice = turbomaxchoices.get()
    url = turbomaxEntry.get()
    if(len(url)>1):
        turbomaxError.config(text="")
        yt = YouTube(url)

        if(choice==choices[0]):
               select = yt.streams.filter(progressive=True).first()
        elif(choice==choices[1]):
               select = yt.streams.filter(progressive=True,file_extension='mp4').last()
        elif(choice==choices[2]):
               select = yt.streams.filter(only_audio=True,).first()
        else:
               turbomaxError.config(text="paste link again!!!",fg="red")


    select.download(Folder_Name)
    turbomaxError.config(text="Download Completed!!")




window = Tk()
window.title("Turbomax youtube Downloader",)
window.geometry("400x350")
window.columnconfigure(0,weight=1)
turbomaxLabel = Label(window,text="Enter the link of the video ", font=("arial",18))
turbomaxLabel.grid()
turbomaxEntryVar = StringVar()
turbomaxEntry = Entry(window,width=50,textvariable=turbomaxEntryVar)
turbomaxEntry.grid()
turbomaxError = Label(window,text=" ",fg="red",font=("arial",12))
turbomaxError.grid()
saveLabel=Label(window,text="Save the video ...",font=("jost",18,"bold"),)
saveLabel.grid()
saveEntry = Button(window,width=10,bg="green",fg="white",text="Choose path...",command=openlocation)
saveEntry.grid()
locationError = Label(window,text=" ",fg="red",font=("jost",12))
locationError.grid()
turbomaxQuality = Label(window,text="Select the Type: ",font=("arial",18))
turbomaxQuality.grid()
choices = ["720p","144p","Audio file"]
turbomaxchoices = ttk.Combobox(window,values=choices)
turbomaxchoices.grid()
downloadbtn = Button(window,text="Download File...",width=30,bg="green",fg="white",command=downloadvideo)
downloadbtn.grid()
developlabel = Label(window,text=" Developed by Ashirwad",fg="red",font=("arial",18))
developlabel.grid()

window.mainloop()
