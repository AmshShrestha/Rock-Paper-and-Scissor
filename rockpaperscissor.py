from tkinter import*
from random import randint
import pytest


win=Tk()
win.geometry("500x500")
win.resizable(0,0)
win.title("Scissor Paper Rock")
win.configure(bg="cyan")
computer_value={
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}

#reset the game
def reset():
    button_1["state"]="active"
    button_2["state"] = "active"
    button_3["state"] = "active"
    l1.config(text="PLAYER          ")
    l3.config(text="COMPUTER")
    l4.config(text="")

#disable the button
def button_disable():
    button_1["state"]="disable"
    button_2["state"] = "disable"
    button_3["state"] = "disable"





#coding for rock
def rock():
    comp_val=computer_value[str(randint(0,2))]
    if comp_val=="Rock":
        match_result="Draw!"

    elif comp_val == "Scissor":
        match_result = "Player Win!"

    else:
        match_result = "Computer Win!"
    l4.config(text=match_result)
    l1.config(text="Rock         ")
    l3.config(text=comp_val)
    button_disable()

#coding for paper
def paper():
    comp_val = computer_value[str(randint(0, 2))]
    if comp_val == "Rock":
        match_result = "Player Win!"
    elif comp_val == "Scissor":
        match_result = "Computer Win!"
    else:
        match_result = "Draw!"
    l4.config(text=match_result)
    l1.config(text="Paper        ")
    l3.config(text=comp_val)
    button_disable()

#coding for scissor
def scissor():
    comp_val = computer_value[str(randint(0, 2))]
    if comp_val == "Rock":
        match_result = "Computer Win!"
    elif comp_val == "Scissor":
        match_result = "Draw!"
    else:
        match_result = "Player Win!"
    l4.config(text=match_result)
    l1.config(text="Scissor         ")
    l3.config(text=comp_val)
    button_disable()

Label(win, text="Rock Paper Scissor", font="normal 20 bold", fg="red", bg="cyan").pack(pady=20)
frame=Frame(win)
frame.pack()

l1=Label(frame, text="PLAYER          ", font=10, bg="cyan", fg="orange")
l1.pack(side=LEFT)

l2=Label(frame, text="VS          ", font= "10", bg="cyan", fg="purple")
l2.pack(side=LEFT)

l3=Label(frame, text="COMPUTER", font="10", bg="cyan", fg="crimson")
l3.pack()

l4=Label(win, text="", font="20", bg="white", width=15, borderwidth= 2, relief="solid")
l4.pack(pady=20)

frame_1=Frame(win)
frame_1.configure(bg="cyan")
frame_1.pack()

button_1=Button(frame_1,text="Scissor", font="10", width=7, bg="red",command = scissor)
button_1.pack(side=LEFT, padx=10)

button_2=Button(frame_1,text="Paper", font="10", width=7, bg="green",command = paper)
button_2.pack(side=LEFT, padx=10)

button_3=Button(frame_1,text="Rock", font="10", width=7,bg="yellow",command=rock)
button_3.pack(padx=10)

reset_button=Button(win, text="Reset", font="10",bg="magenta", command=reset)
reset_button.pack(pady=20)

win.mainloop()