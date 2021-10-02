from tkinter import *
import sqlite3
import log_in
root =Tk()
coon=sqlite3.connect("data_base_rps.db")
# c=coon.cursor()
# c.execute("""CREATE TABLE everyone(
#             username text,
#             mail text,
#             password text,
#             phone integer)
# """)
# print("DATABASE created")
#
#
def submit():
    coon=sqlite3.connect("data_base_rps.db")
    c=coon.cursor()
    c.execute("INSERT INTO everyone VALUES(:E-mail,:Password)", {

        'E-mail': log_in.entry_1.get(),
        'Password': log_in.entry_2.get()
    })
    coon.commit()
    coon.close()
    log_in.entry_1.delete(0,END)
    log_in.entry_2.delete(0, END)


def query():
    coon=sqlite3.connect("data_base_rps.db")
    c=coon.cursor()
    c.execute("SELECT *,oid FROM everyone" )
    records = c.fetchall()
    print(records,'\n')
    print_record=''
    for record in records:
        print_record += str(record[1])+' '+str(record[2])+'\n'
    query_label = Label(root, text = print_record)
    query_label.grid(row = 10, column = 0, columnspan = 2)
    coon.commit()
    coon.close()


def delete():
    coon=sqlite3.connect("data_base_rps.db")
    c=coon.cursor()
    c.execute("DELETE FROM everyone WHERE oid="+delete_box.get())
    print("successfully deleted")
    c.execute("SELECT *,oid FROM everyone")
    records=c.fetchall()
    print_record=""
    for record in records:
        print_record+=str(record[1])+' '+str(record[2])+'\n'
    query_label = Label(root,text=print_record)
    query_label.grid(row=11,column=0,columnspan=2)
    coon.commit()
    coon.close()


def update():
    coon=sqlite3.connect("data_base_rps.db")
    c=coon.cursor()
    record_id = delete_box.get()
    c.execute("""UPDATE everyone SET
            E-mail = :E-mail,
            Password = :Password,
            WHERE oid = :oid """,
              {'E-mail':mail_editor.get(),
                'Password': password_editor.get(),
                'oid':record_id
              }
              )
    coon.commit()
    coon.close()
    editor.destroy()

def edit():
    global editor
    editor = Toplevel()
    editor.title("Update data")
    editor.geometry('300x480')
    coon=sqlite3.connect("data_base_rps.db")
    c=coon.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM everyone WHERE oid="+delete_box.get())
    records=c.fetchall()


    global mail_editor
    global password_editor


    mail_editor = Entry(editor, width = 30)
    mail_editor.grid(row = 1, column = 1)
    password_editor = Entry(editor, width = 30)
    password_editor.grid(row = 2, column = 1)

    mail_label = Label(editor, text = "E-mail")
    mail_label.grid(row = 1, column = 0)
    password_label = Label(editor, text = "Password")
    password_label.grid(row = 2, column = 0)


    for record in records:
        mail_editor.insert(0,record[1])
        password_editor.insert(0,record[2])


    edit_button = Button(editor,text = "SAVE",command=update)
    edit_button.grid(row=5,column=0, columnspan=2, pady=10, padx=10, ipadx=70)

delete_box = Entry(root,width=30)
delete_box.grid(row=7,column=1)



add_record_button = Button(root,text="Add Record",command=submit)
add_record_button.grid(row=5,column=0,columnspan=2,padx=30,pady=10,ipadx=70)

show_btn = Button(root, text="Show Record", command=query)
show_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=30, ipadx=70)

delete_box_button = Button(root,text = "Delete Record",command = delete)
delete_box_button.grid(row=8,column=0,columnspan=2,padx=30,pady=10,ipadx=70)

update_button = Button(root,text="Update record",command=edit)
update_button.grid(row=9,column=0,columnspan=2,padx=30,pady=10,ipadx=70)

root.mainloop()

