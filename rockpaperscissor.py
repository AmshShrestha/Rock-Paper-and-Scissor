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

def reset():
    button_1["state"]="active"
    button_2["state"] = "active"
    button_3["state"] = "active"
    l1.config(text="PLAYER          ")
    l3.config(text="COMPUTER")
    l4.config(text="")

Label(win, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)
frame=Frame(win)
frame.pack()

l1=Label(frame, text="PLAYER          ", font=10)
l1.pack(side=LEFT)

l2=Label(frame, text="VS          ", font= "10")
l2.pack(side=LEFT)

l3=Label(frame, text="COMPUTER          ", font="10")
l3.pack()

l4=Label(win, text="", font="20", bg="white", width=15, borderwidth= 2, relief="solid")
l4.pack(pady=20)

frame_1=Frame(win)
frame_1.pack()

button_1=Button(frame_1,text="Scissor", font="10", width=7)
button_1.pack(side=LEFT, padx=10)

button_2=Button(frame_1,text="Paper", font="10", width=7)
button_2.pack(side=LEFT, padx=10)

button_3=Button(frame_1,text="Rock", font="10", width=7)
button_3.pack(padx=10)

reset_button=Button(win, text="Reset", font="10", command=reset)
reset_button.pack(pady=20)

win.mainloop()