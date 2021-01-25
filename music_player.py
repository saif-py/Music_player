import webbrowser
import random
import pafy
from googlesearch import search

print("""
enter'@ny'(any) for random song
'@dd' to add a new song in the library 
'@list' to see the playlist or
'@his' to see the history of played song 
'@down' to download a song
simply the name of the song you want to play ↓
    
    """)


def playsong(name):  # give name of the song to play it
    flag = True
    name = name + " official music video youtube"
    query = ''
    name = name.split()
    for a in name:
        query = query + ' ' + a
    for urls in search(query, tld="co.in", num=10, stop=1, pause=2):
        print(urls)
    webbrowser.open_new_tab(urls)
    videod = pafy.new(urls)
    print("playing -> " + videod.title)
    ab = open('history.txt', 'a+')
    abd = ab.readlines()
    for i in abd:
        if videod.title == i:
            flag = False
        if flag:
            ab.write(videod.title)
    ab.close()
    if flag:
        with open("history.txt", "a") as f:
            f.write('\n' + videod.title)
            f.close()


while True:

    a = " "
    search_keyword = input("enter your command:->")
    if search_keyword.strip() == "@ny":

        with open("ex.txt", "r") as f:
            lines = f.readlines()
            line = random.choice(lines)
            print(line)
            playsong(line)

    elif search_keyword.strip() == "@dd":
        with open("ex.txt", "a") as f:
            name = input("name of the song-> ")
            name = name + " official music video"
            query = ''
            name = name.split()
            for a in name:
                query = query + ' ' + a
            for urls in search(query, tld="co.in", num=10, stop=10, pause=2):
                if urls.__contains__("www.youtube.com"):
                    print(urls)
                    break
            videod = pafy.new(urls)
            f.write('\n' + videod.title)
            f.close()
            print("song added to the library -> " + videod.title)
            print("would you like to play it now(y/n)")
            if input(":-> ").lower() == 'y':
                print("playing->" + videod.title)
                webbrowser.open_new_tab(urls)

    elif search_keyword.strip() == "@list":
        with open("ex.txt", "r") as f:
            liness = f.readlines()
        datta = []
        i = 1
        for ab in liness:
            data = f'{i}->{ab}'
            datta.append(data)
            i += 1
            print(data)
        print("""
-> enter the number assigned to the song you wanna play or
-> if you don't want to play any from this simply write the name of the song
-> enter '@del' to delete a song
-> or press escape to go back
            """)
        num = input(":-> ")
        if num.isdigit():
            name = ' '
            for i in datta:
                i = i.split('->')
                if i[0] == num:
                    name = name.join(i[1:])
                    playsong(name)
        elif num == "@del":
            de = input('enter the number of the song you wanna delete-> ')
            dele = ''
            if de.isdigit():
                new = open("ex.txt", "w")
                for i in datta:
                    i = i.split('->')
                    if i[0] == de:
                        dele = dele.join(i[1:])
                for line in liness:
                    if line == dele:
                        print(f'deleting the song ->{dele}')
                    else:
                        new.write(line)
                new.close()
        else:
            playsong(num)

    elif search_keyword.lower().strip() == '@his':
        with open('history.txt', 'r') as s:
            print(s.read())
            # print("****press 'n' to play recent song***")
            hist_command = input("->enter 'del' to delete history or just hit enter:         ")
            if hist_command.lower().strip() == 'del':
                hist_text = open("history.txt", 'w')
                hist_text.close()
                print("***history deleted***")
    elif search_keyword.lower().strip() == '@down':
        import downloader

    else:
        playsong(search_keyword)
