import webbrowser
import random
import pafy
from googlesearch import search
import tkinter as tk
import sys

wd = tk.Tk()
wd.title('Youtube video downloader')


def button_c(i):
    # global videoideo
    print(i)
    print("downloading.....")
    i.download(quiet=True, callback=mycb)
    print("download completed")


def mycb(total, recvd, ratio, rate, eta):
    sys.stdout.flush()
    total = int(total) / 1000000
    recvd = int(recvd) / 1000000
    total = "{:.2f}".format(total)
    recvd = "{:.2f}".format(recvd)
    rate = "{:.2f}".format(rate)

    sys.stdout.write(f"\rtotal = {total}")
    sys.stdout.write(f"\rtotal : {total}MB   recived : {recvd}MB  ETA : {eta}sec  speed : {rate}kbps")


song = input("enter the name of the song:-> ")
flag = True
name = song + " official music video youtube"
query = ''
name = name.split()
for a in name:
    query = query + ' ' + a
for urls in search(query, tld="co.in", num=10, stop=1, pause=2):
    if urls.__contains__("www.youtube.com"):
        print(urls)
        break

video = pafy.new(urls)
tk.Label(wd, text=f"{video.title}").grid(row=0, column=2, columnspan=2)
n = 0
ro = 2
for i in video.streams:
    if n > 5:
        ro += 1
        n = 0
    bi = tk.Button(wd, text=i, command=lambda i=i: button_c(i)).grid(row=ro, column=n)
    n += 1
best = video.getbestvideo()
b2 = tk.Button(wd, text=best, command=lambda best=i: button_c(i)).grid(row=ro, column=n)
n += 1
for i in video.audiostreams:
    if n > 5:
        ro += 1
        n = 0
    bi = tk.Button(wd, text=i, command=lambda i=i: button_c(i)).grid(row=ro, column=n)
    n += 1
wd.mainloop()