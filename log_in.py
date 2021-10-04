from tkinter import *
import sqlite3

def add():
    conn = sqlite3.connect("Rock Paper Scissor.db")
    c = conn.cursor()
    c.execute("INSERT INTO user VALUES(:username, :mail, :password, :phone)",
              {
                  "username": name.get(),
                  "mail": e_mail.get(),
                  "password": password.get(),
                  "phone": phone.get()
              })
    conn.commit()

    conn.close()


    name.delete(0,END)
    e_mail.delete(0, END)
    password.delete(0, END)
    phone.delete(0, END)
    win.destroy()

win=Tk()
win.title("LOGIN")
win.geometry("320x250")
win.resizable(0,0)
win.iconbitmap('icon.ico')
win.configure(bg="magenta")


filename = open("Rock Paper Scissor.db", "r+")

name=Entry(win,width=30)
name.grid(row=1,column=1)
e_mail=Entry(win,width=30)
e_mail.grid(row=2,column=1)
password=Entry(win, width=30, show="*")
password.grid(row=3, column=1)
phone=Entry(win, width=30)
phone.grid(row=4, column=1)

name_label=Label(win, text = "Username", font="ArialBlack",bg="magenta", fg="black")
name_label.grid(row=1, column=0, padx=10, pady=10)
e_mail_label=Label(win,text="E-mail",font="ArialBlack",bg="magenta", fg="black")
e_mail_label.grid(row=2,column=0,padx=10,pady=10)
password_label=Label(win,text="Password", font="ArialBlack",bg="magenta", fg="black")
password_label.grid(row=3,column=0,padx=10,pady=10)
phone_label=Label(win,text="Phone", font="ArialBlack",bg="magenta", fg="black")
phone_label.grid(row=4,column=0,padx=10,pady=10)

login_btn=Button(win,text='Login', font="ArialBlack",bg="red", fg="black",command=add)
login_btn.grid(row=5,column=1,columnspan = 5)




win.mainloop()

