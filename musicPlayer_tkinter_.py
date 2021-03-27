import tkinter as tk
import urllib.request
import re
import webbrowser
from functools import partial
from googlesearch import search
import pafy
import time
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.geometry('900x400')

# create a main frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# create a canvas
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# connfigure  the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

# create ANOTHER frame inside canvas
second_frame = tk.Frame(my_canvas)

# add that new frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")


def _on_mouse_wheel(event):
    my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)


# import pygame
def buttonPress():
    a = e1.get()
    e1.delete(1)
    print(a)
    Playsong(a)


def callback(event):
    a = e1.get()
    e1.delete(1)
    Playsong(a)


def calll():
    # e1.delete(0, END)
    print(1)
    # clear_text()
    # time.sleep(2)
    print(2)
    buttonPress()


def clear_text(self):
    self.e1.delete(0, 'end')


def Playsong(name):
    flag = True
    name = name + " song (official video) youtube"
    query = ''
    name = name.split()
    for a in name:
        query = query + ' ' + a
    print(query)
    for urls in search(query, tld="co.in", num=10, stop=1, pause=2):
        if urls.__contains__("www.youtube.com"):
            print(urls)
            break
    videod = pafy.new(urls)
    tk.messagebox.showinfo(title=None, message=f'play:- "{videod.title} "?')
    webbrowser.open_new_tab(urls)
    # print("playing -> " + videod.title)
    ab = open('history.txt', 'a+')
    abd = ab.readlines()
    for i in abd:
        if videod.title == i:
            flag = False
        if flag:
            ab.write(videod.title)
            flag = False
        ab.close()


def sonf(name):
    Playsong(name)


def play_list():
    with open("ex.txt", "r") as f:
        liness = f.readlines()
    i = 1
    col = 3
    for ab in liness:
        i += 1
        playy = partial(sonf, ab)
        buttonn = tk.Button(second_frame, text=ab, command=playy)
        buttonn.grid(row=i, column=col)


lab = tk.Label(second_frame, text=' ').grid(row=4, column=1)
bb1 = tk.Button(second_frame, text='play list', command=play_list)
bb1.grid(row=1)
tk.Label(second_frame, text="enter the name of the song or").grid(row=2, column=0)
e1 = tk.Entry(second_frame)
e1.grid(row=3)
b1 = tk.Button(second_frame, text="command", command=calll)
b1.grid(row=4)
second_frame.bind('<Return>', callback)

root.mainloop()
