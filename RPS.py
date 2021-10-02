from tkinter import *
from random import randint
from tkinter import ttk

win = Tk()
win.title("Rock Paper Scissor")

# Deine images
rock = PhotoImage(file="Rock.png")
paper = PhotoImage(file="Paper.png")
scissor = PhotoImage(file="Scissor.png")

# Add images to a list
image_list = [rock, paper, scissor]

# Random number between 0 and 2
number_pick = randint(0, 2)

# Throw up an image when the program starts
image_label = Label(win, image=image_list[number_pick], bd=0)
image_label.pack(pady=20)


def spin():
    number_pick = randint(0,2)

    # show image
    image_label.config(image=image_list[number_pick])

    # convert drop down choice to a number
    if user_choice.get() == "Rock":
        user_choice_value = 0
    elif user_choice.get() == "Paper":
        user_choice_value = 1
    elif user_choice.get() == "Scissor":
        user_choice_value = 2

    # Determine if we won or lost
    if user_choice_value == 0:  # rock
        if number_pick == 0:
            win_lose_label.config(text="Tie! Spin Again..")
        elif number_pick == 1:  # paper
            win_lose_label.config(text="Lose! Paper Beats Rock")
        elif number_pick == 2:  # scissor
            win_lose_label.config(text="Win! Rock Breaks Scissor")

    if user_choice_value == 1:  # paper
        if number_pick == 0:
            win_lose_label.config(text="Win! Paper Beats Rock")
        elif number_pick == 1:  # paper
            win_lose_label.config(text="Tie! Spin Again")
        elif number_pick == 2:  # scissor
            win_lose_label.config(text="Lose! Scissor Cuts Paper")

    if user_choice_value == 2:  # scissor
        if number_pick == 2:  # rock
            win_lose_label.config(text="Lose! Rock Breaks Scissor")
        elif number_pick == 1:  # paper
            win_lose_label.config(text="Win! Scissor Cuts Paper ")
        elif number_pick == 2:  # scissor
            win_lose_label.config(text="Tie! Spin Again")


# make our choice
user_choice = ttk.Combobox(win, value=("Rock", "Paper", "Scissor"))
user_choice.current (0)
user_choice.pack(pady=20)

# Create spin Button
spin_button = Button(win, text="Spin!", command=spin)
spin_button.pack(pady=10)

#win or lose
win_lose_label = Label(win, text="", font="helvetica" "18")
win_lose_label.pack(pady=50)

win.mainloop()