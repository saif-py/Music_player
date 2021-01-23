from tkinter import *
import urllib.request
import re
import webbrowser
# import random
import pafy
import time


# import pygame


def Playsong(name):
    a = ''
    flag = True
    name = name + " official song"
    for i in name.split():
        a = a + '+' + i
    a = a[2:]
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + a)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video = ("https://www.youtube.com/watch?v=" + video_ids[0])
    url = video
    videod = pafy.new(url)
    texxt = "playing -> " + videod.title
    print(video)
    song_label = Label(wd, text=texxt)
    song_label.grid(row=4, column=0)
    webbrowser.open_new_tab(video)
    # ab = open('history.txt', 'a+')
    # abd = ab.readlines()
    # for i in abd:
    #     if videod.title == i:
    #         flag = False
    #     if flag:
    #         ab.write(videod.title)
    # ab.close()
    # time.sleep(20)
    # song_label.destroy()
    print("assds")


wd = Tk()
wd.title('Music Player')
Label(wd, text="enter the name of the song or").grid(row=0, column=0)
e1 = Entry(wd)
e1.grid(row=1)


def buttonPress():
    a = e1.get()
    e1.delete(0, END)
    print(a)
    Playsong(a)


def callback(event):
    buttonPress()


def calll():
    # e1.delete(0, END)
    print(1)
    clear_text()
    # time.sleep(2)
    print(2)
    buttonPress()


def clear_text(self):
    self.e1.delete(0, 'end')


b1 = Button(wd, text="command", command=calll)
b1.grid(row=3)

wd.bind('<Return>', callback)
wd.mainloop()
