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
import sys
import os
from tkinter import *


def download():
  link = inputer.get()

  if (not link.startswith('https://')):
    link = 'https://' + link.replace('http://', '')

  request = requests.get(link)

  file = open('index.html', 'w', encoding="utf-8")
  file.write(request.text)
  file.close()

  os.startfile(os.path.abspath(os.path.dirname(sys.argv[0])))


tkinter = Tk()
tkinter.resizable(False, False)
tkinter.title("opinhd")
canvas = Canvas(tkinter, width=400, height=200)
canvas.columnconfigure(0, weight=1)
inputer = Entry(width=50)
button = Button(text='Download', command=download)
inputer.pack()
button.pack()

canvas.pack()
tkinter.mainloop()

```

# Download
[Link](opihd.exe)
