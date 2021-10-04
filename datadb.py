from tkinter import*
import sqlite3
win=Tk()
win.geometry("500x500")
win.configure(bg="wheat")
conn=sqlite3.connect("Rock Paper Scissor.db")
c=conn.cursor()

#c.execute("""CREATE TABLE user(
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


    name.delete(0,END)
    e_mail.delete(0, END)
    password.delete(0, END)
    phone.delete(0, END)


def update():
    conn=sqlite3.connect("Rock Paper Scissor.db")
    c=conn.cursor()
    record_id = del_box.get()
    c.execute("""UPDATE user SET
     username = :first,
     e_mail = :second,
     password = :third,
     phone = :fourth
     
     WHERE oid = :oid""",
               {
                 "first":name_editor.get(),
                 "second":e_mail_editor.get(),
                 "third": password_editor.get(),
                 "fourth":phone_editor.get(),
                 "oid" : record_id
               })

    conn.commit()
    conn.close()

def edit():
    editor=Tk()
    editor.title("Update record")
    editor.geometry("500x400")
    editor.configure(bg="magenta")
    conn=sqlite3.connect("Rock Paper Scissor.db")
    c=conn.cursor()
    record_id = del_box.get()
    c.execute("SELECT * FROM user WHERE oid=" + record_id)
    records=c.fetchall()

    global name_editor
    global e_mail_editor
    global password_editor
    global phone_editor


    name_editor = Entry(editor, width=30)
    name_editor.grid(row=0, column=1, padx=10, pady=10)
    e_mail_editor = Entry(editor, width=30)
    e_mail_editor.grid(row=1, column=1, padx=10,pady=10)
    password_editor = Entry(editor, width=30, show="*")
    password_editor.grid(row=2, column=1, padx=10,pady=10)
    phone_editor = Entry(editor, width=30)
    phone_editor.grid(row=3, column=1, padx=10,pady=10)

    name_label = Label(editor, text="Username",bg="magenta")
    name_label.grid(row=0, column=0, padx=10)
    e_mail_label = Label(editor, text="E-mail",bg="magenta")
    e_mail_label.grid(row=1, column=0, padx=10)
    password_label = Label(editor, text="Password",bg="magenta")
    password_label.grid(row=2, column=0, padx=10)
    phone_label = Label(editor, text="Phone",bg="magenta")
    phone_label.grid(row=3, column=0, padx=10)

    for record in records:
        name_editor.insert(0,record[0])
        e_mail_editor.insert(0, record[1])
        password_editor.insert(0, record[2])
        phone_editor.insert(0, record[3])

    edit_button= Button(editor, text = "Save Record", bg="cyan", command=update)
    edit_button.grid(row=4, column=1, padx=10)

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
        print_records += str(record[4])+ "  " + str(record[0])+ "  " +str(record[1])+ "  " + str(record[2])+ "  " +str(record[3]) + "\n"
    query_label = Label(win, text = print_records, bg="wheat", fg="green", font="heltevica 10 bold")
    query_label.grid(row =10, pady=20, padx=5, column=0, columnspan=2)
    conn.commit()
    conn.close()
    win.destroy()

def show():
     conn=sqlite3.connect("Rock Paper Scissor.db")
     c=conn.cursor()
     c.execute("SELECT *, oid FROM user")
     records=c.fetchall()
     print(records)

     print_records=""
     for record in records:
         print_records += str(record[4])+ "  " + str(record[0])+ "  " +str(record[1])+ "  " + str(record[2])+ "  " +str(record[3]) + "\n"
     query_label = Label(win, text = print_records, bg="wheat", fg="green", font="heltevica 10 bold")
     query_label.grid(row =10, pady=20, padx=5, column=0, columnspan=2)#     conn.commit()
     conn.close()

name=Entry(win, width=55)
name.grid(row=0,column=1, columnspan=2, padx=10, pady=10)
e_mail=Entry(win,width=55)
e_mail.grid(row=1,column=1, columnspan=2,padx=10,pady=10)
password=Entry(win, width=55)
password.grid(row=2,column=1, columnspan=2,padx=10, pady=10)
phone=Entry(win, width=55)
phone.grid(row=3,column=1, columnspan=2,padx=10, pady=10)
del_box=Entry(win, width=10)
del_box.grid(row=6,column=1)

name_label=Label(win, text="Username", bg="wheat", font="heltevica 10")
name_label.grid(row=0, column=0, padx=10, pady=10)
e_mail_label=Label(win, text="E-mail", bg="wheat", font="heltevica 10")
e_mail_label.grid(row=1, column=0, padx=10,pady=10)
password_label=Label(win, text="Password", bg="wheat", font="heltevica 10")
password_label.grid(row=2, column=0, padx=10,pady=10)
phone_label=Label(win, text="Phone", bg="wheat", font="heltevica 10")
phone_label.grid(row=3, column=0, padx=10,pady=10)
del_box_label=Label(win, text="Select account", bg="wheat", font="heltevica 10")
del_box_label.grid(row=6, column=0,padx=10, pady=10)

add_btn=Button(win, text="Add Record", bg="cyan", command = add)
add_btn.grid(row=7, column=0,padx=20, pady=10 )

show_btn=Button(win, text="Show Record", bg="cyan", command = show)
show_btn.grid(row=8, column=1,padx=20, pady=10 )

del_btn=Button(win, text="Delete Record",bg="cyan", command=delete)
del_btn.grid(row=7, column=1, padx=50, pady=10)

update_btn=Button(win, text="Edit Record", bg="cyan", command=lambda:edit())
update_btn.grid(row=7, column=2, padx=20,pady=10)


conn.commit()

conn.close()

win.mainloop()