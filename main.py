import requests, sys, os
from tkinter import *
from tkinter import filedialog

def download():
  link = inputer.get()

  if (not link.startswith('https://')):
    link = 'https://' + link.replace('http://', '')

  request = requests.get(link)

  directory = filedialog.askdirectory()

  file = open(directory +
              '/index.html', 'w', encoding="utf-8")
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
