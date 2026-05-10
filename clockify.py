from tkinter import *
from time import strftime

w = Tk()

w.title("Clockify")
w.geometry("500x320")
w.config(bg="#031926")

top = Frame(w, bg="#0A2647", height=50)
top.pack(fill=X)

title = Label(
    top,
    text="CLOCKIFY",
    font=("Montserrat", 22, "bold"),
    bg="#0A2647",
    fg="#9EE8FF"
)

title.pack(pady=8)

wave = Label(
    w,
    text="⋆｡𖦹°🌊⋆｡𖦹°🫧⋆｡𖦹°",
    font=("Arial", 18),
    bg="#031926",
    fg="#6EC6FF"
)

wave.pack(pady=12)

def clock():
    t = strftime("%I:%M:%S %p")
    time_label.config(text=t)
    time_label.after(1000, clock)

time_label = Label(
    w,
    font=("Century Gothic", 42, "bold"),
    bg="#031926",
    fg="#B9F3FC"
)

time_label.pack(pady=20)

line = Label(
    w,
    text="────────────",
    font=("Arial", 16),
    bg="#031926",
    fg="#4682A9"
)

line.pack()

text = Label(
    w,
    text="lost in blue moments",
    font=("Lucida Handwriting", 14),
    bg="#031926",
    fg="#DFF6FF"
)

text.pack(pady=15)

box = Frame(
    w,
    bg="#0A2647",
    highlightbackground="#6EC6FF",
    highlightthickness=2,
    padx=15,
    pady=10
)

box.pack(pady=10)

quote = Label(
    box,
    text="time flows like water",
    font=("Georgia", 12, "italic"),
    bg="#0A2647",
    fg="white"
)

quote.pack()

clock()

w.mainloop()