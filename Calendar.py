from tkinter import *
import calendar
from datetime import datetime

w = Tk()

w.title("My Calendar")
w.geometry("720x620")
w.config(bg="#02111B")

top = Frame(w, bg="#06283D", height=70)
top.pack(fill=X)

title = Label(
    top,
    text="CALENDAR",
    font=("Montserrat", 28, "bold"),
    bg="#06283D",
    fg="#AEE2FF"
)

title.pack(pady=15)

now = datetime.now()

month = calendar.month_name[now.month]

month_label = Label(
    w,
    text=f"{month} {now.year}",
    font=("Century Gothic", 30, "bold"),
    bg="#02111B",
    fg="#DFF6FF"
)

month_label.pack(pady=25)

frame = Frame(
    w,
    bg="#06283D",
    padx=20,
    pady=20,
    highlightbackground="#7ED7FF",
    highlightthickness=2
)

frame.pack(pady=10)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for i in range(7):
    Label(
        frame,
        text=days[i],
        font=("Montserrat", 13, "bold"),
        bg="#06283D",
        fg="#7ED7FF",
        width=8,
        pady=10
    ).grid(row=0, column=i)

cal = calendar.monthcalendar(now.year, now.month)

for r in range(len(cal)):
    for c in range(7):

        day = cal[r][c]

        if day == 0:
            text = ""
            bgc = "#06283D"
            fgc = "#06283D"

        else:
            text = str(day)
            bgc = "#0B2447"
            fgc = "#EAF6FF"

        if day == now.day:
            bgc = "#7ED7FF"
            fgc = "#02111B"

        Label(
            frame,
            text=text,
            font=("Century Gothic", 14, "bold"),
            bg=bgc,
            fg=fgc,
            width=6,
            height=3
        ).grid(row=r+1, column=c, padx=6, pady=6)

quote = Label(
    w,
    text="floating through oceans of time",
    font=("Lucida Handwriting", 16),
    bg="#02111B",
    fg="#CFF5FF"
)

quote.pack(pady=30)

w.mainloop()