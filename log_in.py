from tkinter import *
import sqlite3
from tkinter import messagebox

def select():
    conn = sqlite3.connect("Rock Paper Scissor.db")
    c = conn.cursor()
    c.execute("SELECT *, oid FROM user WHERE e_mail=? AND password=?",(e_mail.get(), password.get()))
    records = c.fetchone()
    if records:
        win.destroy()
    else:
        messagebox.showinfo("Info", "Try again!")
    conn.commit()
    conn.close()

win=Tk()
win.title("LOGIN")
win.geometry("320x250")
win.resizable(0,0)
win.iconbitmap('icon.ico')
win.configure(bg="magenta")

e_mail=Entry(win,width=30)
e_mail.grid(row=2,column=1)
password=Entry(win, width=30, show="*")
password.grid(row=3, column=1)

e_mail_label=Label(win,text="E-mail",font="ArialBlack",bg="magenta", fg="black")
e_mail_label.grid(row=2,column=0,padx=10,pady=10)
password_label=Label(win,text="Password", font="ArialBlack",bg="magenta", fg="black")
password_label.grid(row=3,column=0,padx=10,pady=10)


login_btn=Button(win,text='Login', font="ArialBlack",bg="red", fg="black",command=select)
login_btn.grid(row=5,column=1,columnspan = 5)

win.mainloop()

