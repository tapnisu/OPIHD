# opihd

## Introduction
Want to save a webpage? This programm is for you.

Why this one? Because:
* It is **easy**,
* It has **short name**,
* It is **open source**,
* It is **free**.

## [Code](main.py)
```py
import requests
import os
from tkinter import *
from tkinter import filedialog

def download():
  link = inputer.get()
  HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
  }

  if (not link.startswith('https://')):
    link = 'https://' + link.replace('http://', '')

  request = requests.get(link, headers = HEADERS)

  directory = filedialog.askdirectory()

  file = open(directory + '/index.html', 'w', encoding="utf-8")
  file.write(request.text)
  file.close()

  os.startfile(directory)


tkinter = Tk()
tkinter.resizable(False, False)
tkinter.title("opihd")
canvas = Canvas(tkinter, width=400, height=200)
canvas.columnconfigure(0, weight=1)

label = Label(text="opihd", font='Consolas 50')
inputer = Entry(width=50)
button = Button(text='Download', command=download)

label.pack()
inputer.pack()
button.pack()
button.place(x=300, y=200)
canvas.pack()

tkinter.mainloop()
```

# Download
[Link](dist/opihd.exe)
