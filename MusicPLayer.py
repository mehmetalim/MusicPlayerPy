#TechVidvan- Import Modules
from tkinter import *
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
import pygame
from pygame import mixer
from PIL import ImageTk,Image
import os
import time
from mutagen.mp3 import MP3



root=Tk()
root.title('Music Player')
root.geometry("920x720+60+30")
root.configure(bg= "black")
root.resizable(False, False)
mixer.init()

height = root.winfo_screenheight()
width = root.winfo_screenwidth()


def Refresh_Music():

    filetypes = (('text files', '*.mp3'), ('All files', '*.*'))

    Playlist.delete(0, END)
    if 1:
        os.chdir('./')
        songs = os.listdir('./')
        
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
                print()

def get_time():
    current_time = pygame.mixer.music.get_pos() / 1000
    formated_time = time.strftime("%H:%M:%S", time.gmtime(current_time))
    next_one =Playlist.curselection()
    songs = Playlist.get(next_one)
    song_timer = MP3(songs)

    height = root.winfo_screenheight()
    width = root.winfo_screenwidth()

    song_length = int(song_timer.info.length)
    format_for_length = time.strftime("%H:%M:%S", time.gmtime(song_length))
    label_time.config(text=f"{format_for_length} / {formated_time}")
    progress["maximum"] = song_length
    progress["value"] = int(current_time)
    root.after(100, get_time)


def Play_Music():
    Music_Name = Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play(-1, 0.0)
    get_time()


bg = ImageTk.PhotoImage(Image.open("default.jpg"))


# Create Canvas
canvas1 = Canvas(root)#
canvas1.create_image( 0, 0, image = bg, anchor = "nw")
canvas1.pack(fill= "both", side="left", expand=TRUE)

# icon
Icon_Image = PhotoImage(file="musix.png")
root.iconphoto(False, Icon_Image)


# Button
play_pic=Image.open("play.png")
resized_play=play_pic.resize((50,50))
new_play=ImageTk.PhotoImage(resized_play)
Button(root, image=new_play, command=Play_Music, compound = LEFT).place(x=415, y=430)
label = Label(root, text="Play",
              border=0, fg="black", bg="white", font=("Helvetica", 11))
label.place(x=428, y=490)


stop_pic=Image.open("stop.png")
resized_stop=stop_pic.resize((50,50))
new_stop=ImageTk.PhotoImage(resized_stop)
Button(root, image=new_stop,  command=mixer.music.stop, compound = LEFT).place(x=300, y=540)
label = Label(root, text="Stop",
              border=0, fg="black", bg="white", font=("Helvetica", 11))
label.place(x=312, y=600)


resume_pic=Image.open("resume.png")
resized_resume=resume_pic.resize((50,50))
new_resume=ImageTk.PhotoImage(resized_resume)
Button(root, image=new_resume, command=mixer.music.unpause, compound = LEFT).place(x=415, y=540)
label = Label(root, text="Resume",
              border=0, fg="black", bg="white", font=("Helvetica", 11))
label.place(x=415, y=600)


pause_pic=Image.open("pause2.png")
new_pause=ImageTk.PhotoImage(pause_pic)
Button(root, image=new_pause, command=mixer.music.pause,compound = LEFT).place(x=530, y=540)
label = Label(root, text="Pause",
              border=0, fg="black", bg="white", font=("Helvetica", 11))
label.place(x=537, y=600)


Frame_Music = Frame(root, relief=RIDGE)
Frame_Music.place(x=200, y=110, width=400, height=250)

Button(root, text="Refresh Music", border=0 , width=15, height=2, font=("times new roman", 12, "bold"), fg="Black", bg="red",
       command=Refresh_Music).place(x=200, y=50)

#Listbox
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, border=0  , font=("Times new roman", 10), bg="green", fg="black",
                   selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)

#Line
progress = ttk.Progressbar(orient=HORIZONTAL, value=0, length=453, mode='determinate')
progress.place(x=200, y=380)

label_time = Label(text="00:00:00 / 00:00:00", width=20, font="Helvetica, 10", bg="black", fg="white")
label_time.place(x=653, y=380)

Refresh_Music()

root.mainloop()






