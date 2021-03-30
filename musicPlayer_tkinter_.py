import tkinter as tk
import webbrowser
from functools import partial
from googlesearch import search
import pafy
from tkinter import ttk
from tkinter import messagebox
import random
import socket

try:

    root = tk.Tk()
    root.geometry('275x107')
    # root.

    bg_image = tk.PhotoImage(file=r"name.png")
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


    # backg.place(x=0, y=0, relwidth=1, relheight=1)

    def _on_mouse_wheel(event):
        my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")


    # import pygame
    def buttonPress():
        a = e1.get()
        e1.delete(1)
        # print(a)
        Playsong(a)


    def callback(event):
        a = e1.get()
        e1.delete(1)
        Playsong(a)


    def calll():
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
        playy = tk.messagebox.askokcancel(title=None, message=f'play:- "{videod.title} "?')
        if playy:
            webbrowser.open_new_tab(urls)
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


    def song_name(e2):
        search_word = e2.get
        flag = True
        name = search_word + " song (official video) youtube"
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
        addd = tk.messagebox.askokcancel(title=None, message=f'add:- "{videod.title}" ?')
        if addd:
            playy = tk.messagebox.askokcancel(title=None, message=f'play:- "{videod.title}" ?')
            if playy:
                webbrowser.open_new_tab(urls)


    # def search_song(e2):
    #     e22 = e2.get()
    #     song_name(e22)

    def add_song():
        e2 = tk.Entry(second_frame).grid(row=1, column=4)
        searchsong = partial(song_name, e2)
        bb4 = tk.Button(second_frame, text='add', command=searchsong).grid(row=1, column=5)


    def play_list():
        root.geometry('800x400')
        with open("ex.txt", "r") as f:
            liness = f.readlines()
        i = 2
        col = 3

        add = tk.Button(second_frame, text="add a song", command=add_song)
        add.grid(row=1, column=3)
        for ab in liness:
            i += 1
            playy = partial(sonf, ab)
            buttonn = tk.Button(second_frame, text=ab, command=playy)
            buttonn.grid(row=i, column=col, columnspan=3)


    def downloader():
        import downloader


    def random():
        with open("ex.txt", "r") as f:
            line = random.choice(f.readlines())
            ask = tk.messagebox.askyesnocancel(title='random song', message=f'would you like to play: {line} ?')
            if ask:
                Playsong(name=line)


    # backg = tk.Label(second_frame, image=bg_image).grid(row=1, column=0)
    label1 = tk.Label(second_frame, image=bg_image)
    label1.place(x=0, y=0)
    ab = tk.Label(second_frame, text=' ').grid(row=4, column=1)
    bb1 = tk.Button(second_frame, text='play list', command=play_list)
    bb1.grid(row=1, column=0)
    tk.Label(second_frame, text="enter the name of the song or").grid(row=3, column=0, columnspan=2)
    e1 = tk.Entry(second_frame)
    e1.grid(row=4, column=0, columnspan=2)
    b1 = tk.Button(second_frame, text="command", command=calll)
    b1.grid(row=5, column=0, columnspan=2)
    bb2 = tk.Button(second_frame, text='download', command=downloader)
    bb3 = tk.Button(second_frame, text='random', command=random)
    bb2.grid(row=1, column=1)
    bb3.grid(row=1, column=2)

    root.bind_all("<MouseWheel>", _on_mouse_wheel)

    root.bind('<Return>', callback)

    root.mainloop()
except:
    tk.messagebox.showerror(title='error', message='check your internet connection')
