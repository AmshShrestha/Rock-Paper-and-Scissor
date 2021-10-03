from tkinter import*
import sqlite3

win=Tk()
win.geometry("300x350")

conn=sqlite3.connect("Rock Paper Scissor.db")

c=conn.cursor()

#c.execute("""CREATE TABLE user(
#            username text,
#            e_mail text,
#            password text,
#            phone integer)""")

def add():
    conn=sqlite3.connect("Rock Paper Scissor.db")
    c=conn.cursor()
    c.execute("INSERT INTO user VALUES(:username, :mail, :password, :phone)",
              {
               "username":   name.get(),
               "mail": e_mail.get(),
               "password":password.get(),
               "phone":phone.get()
               })
    conn.commit()
    conn.close()

    name.delete(0,END)
    e_mail.delete(0, END)
    password.delete(0, END)
    phone.delete(0, END)

def delete():
    conn=sqlite3.connect("Rock Paper Scissor.db")
    c=conn.cursor()
    c.execute("DELETE FROM user WHERE oid=" + del_box.get())
    del_box.delete(0,END)
    conn.commit()
    conn.close()


def show():
    conn=sqlite3.connect("Rock Paper Scissor.db")
    c=conn.cursor()
    c.execute("SELECT *, oid FROM user")
    records=c.fetchall()
    print(records)

    print_records=""
    for record in records:
        print_records += str(record[1]) + " \n"+ str(record[3]) +str(record[4]) + "\n"
    query_label = Label(win, text = print_records)
    query_label.grid(row =10, column=1)
    conn.commit()
    conn.close()

name=Entry(win, width=30)
name.grid(row=0,column=1, padx=10)
e_mail=Entry(win, width=30)
e_mail.grid(row=1,column=1, padx=10)
password=Entry(win, width=30)
password.grid(row=2,column=1, padx=10)
phone=Entry(win, width=30)
phone.grid(row=3,column=1, padx=10)
del_box=Entry(win, width=30)
del_box.grid(row=7, column=1)

name_label=Label(win, text="Username")
name_label.grid(row=0, column=0, padx=10)
e_mail_label=Label(win, text="E-mail")
e_mail_label.grid(row=1, column=0, padx=10)
password_label=Label(win, text="Password")
password_label.grid(row=2, column=0, padx=10)
phone_label=Label(win, text="Phone")
phone_label.grid(row=3, column=0, padx=10)
del_box_label=Label(win, text="Select account")
del_box_label.grid(row=7, column=0)

add_btn=Button(win, text="Add Record", command = add)
add_btn.grid(row=5, column=0, columnspan=3,pady=5, ipadx=116)

show_btn=Button(win, text="Show Record", command = show)
show_btn.grid(row=6, column=0, columnspan=3,pady=5, ipadx=112)

del_btn=Button(win, text="Delete Record", command=delete)
del_btn.grid(row=8, column=0,columnspan=3, pady=5,ipadx=110)

update_btn=Button(win, text="Edit Record")
update_btn.grid(row=9, column=0, columnspan=3, pady=5, ipadx=116)


conn.commit()

conn.close()

win.mainloop()