from tkinter import *
def link():
    filename = open("data_base_rps.db", "r+")

    root.destroy()
root=Tk()

root.title("LOGIN")
root.geometry("300x110")

root.iconbitmap('icon.ico')


label_1=Label(root,text='E-mail:')
label_1.grid(row=3,column=1,padx=10,pady=10)
label_2=Label(root,text='Password:')
label_2.grid(row=4,column=1,padx=10,pady=10)


entry_1=Entry(root,width=30)
entry_1.grid(row=3,column=2)
entry_2=Entry(root,width=30)
entry_2.grid(row=4,column=2)


button_1=Button(root,text='LOGIN')
button_1.grid(row=9,column=2,columnspan = 5)

var = IntVar()

root.mainloop()