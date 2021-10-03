from tkinter import*
import sqlite3

win=Tk()
win.geometry("300x350")

conn=sqlite3.connect("Rock Paper Scissor.db")

c=conn.cursor()

# c.execute("""CREATE TABLE user(
#             username text,
#             e_mail text,
#             password text
#             phone integer
#             )""")


name=Entry(win, width=30)
name.grid(row=0,column=1, padx=10)
e_mail=Entry(win, width=30)
e_mail.grid(row=1,column=1, padx=10)
password=Entry(win, width=30)
password.grid(row=2,column=1, padx=10)
phone=Entry(win, width=30)
phone.grid(row=3,column=1, padx=10)

name_label=Label(win, text="Username")
name_label.grid(row=0, column=0, padx=10)
e_mail_label=Label(win, text="E-mail")
e_mail_label.grid(row=1, column=0, padx=10)
password_label=Label(win, text="Password")
password_label.grid(row=2, column=0, padx=10)
phone_label=Label(win, text="Phone")
phone_label.grid(row=3, column=0, padx=10)

add_btn=Button(win, text="Add Record")
add_btn.grid(row=5, column=0, columnspan=3,pady=5, ipadx=116)

show_btn=Button(win, text="Show Record")
show_btn.grid(row=6, column=0, columnspan=3,pady=5, ipadx=112)

del_btn=Button(win, text="Delete Record")
del_btn.grid(row=7, column=0,columnspan=3, pady=5,ipadx=110)

update_btn=Button(win, text="Edit Record")
update_btn.grid(row=8, column=0, columnspan=3, pady=5, ipadx=116)


conn.commit()

conn.close()

win.mainloop()