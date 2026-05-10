from tkinter import *

win = Tk()

win.title("Calculator")

win.geometry("320x470")

win.config(bg="#0b1020")

data = ""

screen = StringVar()


def add(x):

    global data

    data = data + str(x)

    screen.set(data)


def equal():

    global data

    try:

        ans = str(eval(data))

        screen.set(ans)

        data = ans

    except:

        screen.set("error")

        data = ""


def clear():

    global data

    data = ""

    screen.set("")


Entry(
    win,
    textvariable=screen,
    font=("Arial", 28),
    bg="#111827",
    fg="#67e8f9",
    bd=0,
    justify="right"
).place(x=20, y=30, width=280, height=70)


buttons = [

    ("7", 20, 130), ("8", 95, 130), ("9", 170, 130), ("/", 245, 130),

    ("4", 20, 205), ("5", 95, 205), ("6", 170, 205), ("*", 245, 205),

    ("1", 20, 280), ("2", 95, 280), ("3", 170, 280), ("-", 245, 280),

    ("C", 20, 355), ("0", 95, 355), ("=", 170, 355), ("+", 245, 355)

]

for (txt, x, y) in buttons:

    if txt == "=":

        cmd = equal

    elif txt == "C":

        cmd = clear

    else:

        cmd = lambda t=txt: add(t)

    Button(
        win,
        text=txt,
        command=cmd,
        font=("Arial", 18),
        bg="#1e293b",
        fg="white",
        activebackground="#67e8f9",
        activeforeground="black",
        bd=0
    ).place(x=x, y=y, width=55, height=55)

win.mainloop()