from tkinter import*
from random import randint
from tkinter import ttk

win=Tk()
win.iconbitmap("")
win.title("rps.png")


#Deine images
rock=PhotoImage(file="Rock.png")
paper=PhotoImage(file="Paper.png")
scissor=PhotoImage(file="Scissor.png")

#Add images to a list
image_list=[rock,paper, scissor]

#Random number between 0 and 2
number_pick=randint(0,2)

#Throw up an image when the program starts
image_label=Label(win, image=image_list[number_pick])
image_label.pack(pady=20)

def spin():
    number_pick = randint(0, 2)
    image_label.config(win, image=image_list[number_pick], bd=0)

#make our choice
user_choice = ttk. Combobox(win, value =("Rock", "Paper", "Scissor"))
user_choice.current=(0)
user_choice.pack(pady=20)


#Create spin Button
spin_button=Button(win, text="Spin!", command=spin)


win.mainloop()