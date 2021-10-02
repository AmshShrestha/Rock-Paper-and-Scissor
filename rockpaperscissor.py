from tkinter import*
import random

win=Tk()
win.geometry("500x500")
win.title("Scissor Paper Rock")

computer_value={
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

Label(win, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)
frame=Frame(win)
frame.pack()




win.mainloop()