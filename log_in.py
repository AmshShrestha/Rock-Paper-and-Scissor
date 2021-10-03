import database
from tkinter import *
def link():
    filename = open("data_base_rps.db", "r+")

    win.destroy()
win=Tk()

win.title("LOGIN")
win.geometry("300x110")

win.iconbitmap('icon.ico')


label_1=Label(win,text='E-mail:')
label_1.grid(row=3,column=1,padx=10,pady=10)
label_2=Label(win,text='Password:')
label_2.grid(row=4,column=1,padx=10,pady=10)


entry_1=Entry(win,width=30)
entry_1.grid(row=3,column=2)
entry_2=Entry(win,width=30)
entry_2.grid(row=4,column=2)


button_1=Button(win,text='LOGIN', command=database.submit)
button_1.grid(row=9,column=2,columnspan = 5)

var = IntVar()

win.mainloop()