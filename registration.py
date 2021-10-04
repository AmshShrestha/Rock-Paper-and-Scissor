from tkinter import *
import sqlite3

win = Tk()
win.geometry("500x500")
win.configure(bg="wheat")
conn = sqlite3.connect("Rock Paper Scissor.db")
c = conn.cursor()


# c.execute("""CREATE TABLE user(
#            username text,
#            e_mail text,
#            password text,
#            phone integer)""")
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

    name.delete(0, END)
    e_mail.delete(0, END)
    password.delete(0, END)
    phone.delete(0, END)


name = Entry(win, width=55)
name.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
e_mail = Entry(win, width=55)
e_mail.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
password = Entry(win, width=55)
password.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
phone = Entry(win, width=55)
phone.grid(row=3, column=1, columnspan=2, padx=10, pady=10)


name_label = Label(win, text="Username", bg="wheat", font="heltevica 10")
name_label.grid(row=0, column=0, padx=10, pady=10)
e_mail_label = Label(win, text="E-mail", bg="wheat", font="heltevica 10")
e_mail_label.grid(row=1, column=0, padx=10, pady=10)
password_label = Label(win, text="Password", bg="wheat", font="heltevica 10")
password_label.grid(row=2, column=0, padx=10, pady=10)
phone_label = Label(win, text="Phone", bg="wheat", font="heltevica 10")
phone_label.grid(row=3, column=0, padx=10, pady=10)


add_btn = Button(win, text="Add Record", bg="cyan", command=add)
add_btn.grid(row=7, column=1, padx=20, pady=10)



conn.commit()

conn.close()

win.mainloop()