from flask import Flask, render_template
from wordpick5 import wordlist
from time import *
from schedule import *
from sys import *
from tkinter import *
from random import *

def randomcolours():
    hex = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    code = '#'
    for x in range(0,6):
        code = code + choice(hex)
    return code

UI = Tk()
UI.title("Find Names!")
UI.iconbitmap("image.ico")
UI.configure(bg = randomcolours())
UI.geometry("400x400")

def click(event):
    Namer = Label(UI, text = wordlist)
    Namer.pack()

thebu = Button(UI, text = "Click Here To Make Names")
thebu.bind("<Button-1>", click)
thebu.pack(pady=20)

UI.mainloop()

app = Flask(__name__)
@app.route("/")

def home():
    return render_template("index.html", listed = thebu, slept = sleep(2))


if __name__ == "__main__":
    app.run()

exit()

every(30).seconds.do(app.run())
while 1:
    run_pending()
    sleep(2)
