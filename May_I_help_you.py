"""Prepared by Rishabh Jain
    Simple GUI development for the purpose of learning Tkinter
    Acts as a basic level assistant for common tasks
    Uses various web scraping modules like requests and beautiful soup
    datetime for getting time , psutil for getting battery percentage
    
    Python must be installed along with various packages mentioned above.
    
    Project is in development stage, depending upon various things I learn, further things may be added up. 
    
    Here I am : https://github.com/rj1997
    rishabhrjjain1997@gmail.com
    Feel free to provide valuable advices.

"""

from tkinter import *
import time
import webbrowser
from selenium import webdriver
import bs4,requests
from datetime import datetime
import tkinter.messagebox
import psutil

#Function to convert seconds to hours
def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d:%02d:%02d" % (hh, mm, ss)

#Function that generates a message box telling the current time
def gettime():
    ansstring=str(datetime.now())
    print(ansstring)
    tkinter.messagebox.showinfo("Current time..",ansstring)

#Function that regulates tasks when button is pressed.
def okpressed():

    str2=query.get()

    #Tells the current time.
    if "time" in str2:
        ansstring = str(datetime.now())
        tkinter.messagebox.showinfo("Current time..", ansstring)

    #Tells the current battery status
    if "battery" in str2:
        battery = psutil.sensors_battery()
        ansstring=("charge = %s%%, time left = %s" % (battery.percent, secs2hours(battery.secsleft)))
        tkinter.messagebox.showinfo("Battery Stats", ansstring)

    #Plays mp3 from the system memory
    if ".mp3" in str2:
        play,space,rest=str2.partition(' ')
        #print(rest)
        webbrowser.open(rest)

    #Plays mp4 from the system memory
    if ".mp4" in str2:
        play,space,rest=str2.partition(' ')
        #print(rest)
        webbrowser.open(rest)

    #Opens word files from the system memory
    if ".docx" in str2:
        open,space,rest=str2.partition(' ')
        #print(rest)
        webbrowser.open(rest)

    #Opens excel files from the system memory
    if ".xls" in str2:
        open,space,rest=str2.partition(' ')
        #print(rest)
        webbrowser.open(rest)

    # Opens ppt files from the system memory
    if "ppt" in str2:
        open,space,rest=str2.partition(' ')
        #print(rest)
        webbrowser.open(rest)

    #Opens the first link encountered on google search, a.k.a. I am feeling Lucky.
    if "search" in str2:
        initial="https://www.google.co.in/search?q="
        search,space,rest=str2.partition(' ')
        rest=rest.replace(' ','+')
        url=initial+rest
        res=requests.get(url)
        soup=bs4.BeautifulSoup(res.text,"html.parser")
        collect = soup.select('.r a')
        count = 0
        for elems in collect:
            str3 = elems.get('href')
            flag = re.search('http://(.+?)&sa', str3)
            if count >= 1:
                break
            if flag:
                found = flag.group(1)
                finalstr = 'http://' + found
                path = "C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe"
                browser = webdriver.Chrome(path)
                browser.get(finalstr)
                count = count + 1

    #Plays the youtube video you have asked for
    if "youtube" in str2:
        initial="https://www.youtube.com/results?q="#jeena+jeena"
        play,space,rest=str2.partition(' ')
        rest=rest.replace(' ','+')
        url=initial+rest
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        collect = soup.select('.yt-lockup-title a')
        temp = str(collect)
        ind = temp.find('href')
        partofurl = ""
        for i in range(ind + 6, ind + 1000):
            if temp[i] == "\"":
                break
            partofurl = partofurl + temp[i]
        finalurl = 'https://www.youtube.com' + partofurl
        path = "C:\\Users\\Rishabh Jain\\Downloads\\chromedriver_win32\\chromedriver.exe"
        browser = webdriver.Chrome(path)
        browser.get(finalurl)

#Uses Tkinter GUI package from Python
root=Tk()

root.minsize(height=300,width=430)
root.maxsize(height=700,width=900)
root.configure(background="grey")

firstframe = Frame(root)

headtext=Label(firstframe,text="May I help you?")
headtext.config(font=("Courier", 34),bg="Blue",foreground="yellow",padx=20,pady=10)
headtext.pack(fill=X)

description=Label(firstframe,text="Your multi-tasker")
description.config(font=("Sans Serif", 24),bg="grey",foreground="black",padx=20,pady=10)
description.pack(fill=X)

firstframe.pack(side=TOP,fill=X)

secondframe=Frame(root)

first=Label(secondframe,text="Enter your query : ")
first.config(font=("Sans Serif", 20),bg="grey",foreground="white",padx=20,pady=10)
first.grid(row=0,column=0)

query=Entry(secondframe)
query.config(font=("Courier", 16),bg="white",foreground="black")
query.grid(row=0,column=1)

Button(secondframe, text='Show', command=okpressed).grid(row=0, column=2, sticky=W, pady=4)

secondframe.pack(side=TOP,fill=X)

root.mainloop()
