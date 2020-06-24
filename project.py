from tkinter import *
import sqlite3

win = Tk()
win.geometry('400x400')
win.title("Auto Email")

f = LabelFrame(win)
f.place(anchor="center")

# submit email and password and insert into sql database
user = sqlite3.connect('user.db')
c = user.cursor()


def submit():
    user = sqlite3.connect('user.db')
    c = user.cursor()
    c.execute("INSERT INTO user VALUES (:Email, :Password)",
              {
                  'Email': Email.get(),
                  'Password': Password.get()
              })
    Email.delete(0, END)
    Password.delete(0, END)
    user.commit()
    user.close()

# print all valuse in database


def query():
    user = sqlite3.connect('user.db')
    c = user.cursor()
    # query database
    c.execute("SELECT *, oid FROM user")
    records = c.fetchall()

    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[2]) + "\n "

    query_label = Label(win, text=print_records, font=10)
    query_label.place(relx=.4, rely=.65)

    user.commit()
    user.close()


def create():

    c.execute("""CREATE TABLE user(
            user_name text,
            password text
            )
    """)
    user.commit()
    user.close()
    msg = Label(f, text="Database Created")
    msg.pack()


def delete():
    user = sqlite3.connect('user.db')
    c = user.cursor()
    c.execute("DELETE from user WHERE oid=" + Dety.get())
    Dety.delete(0, END)
    user.commit()
    user.close()


# Labels
email_label = Label(win, text="Email", font=40)
email_label.place(relx=.25, rely=.3)
password_label = Label(win, text="Password", font=40)
password_label.place(relx=.2, rely=.38)

# Entries
Email = Entry(win, font=40, bg="light gray")
Email.place(relx=.40, rely=.3)

Password = Entry(win, font=40, bg="light gray", show="*")
Password.place(relx=.40, rely=.38)

Dety = Entry(win, font=40)
Dety.place(relx=.35, rely=.55)


# Buttons
Subtn = Button(win, text="Submit", font=40,
               width=20, relief=GROOVE, command=lambda: submit())
Subtn.place(relx=.30, rely=.46)

# query Button
Qbutton = Button(win, text="Print Records", command=query, font=40)
Qbutton.place(relx=.1, rely=.65)

# create database
createbtn = Button(win, text="Create Database", command=create)
createbtn.pack()

Dbtn = Button(win, text="Delete", command=delete, font=40)
Dbtn.place(relx=.2, rely=.55)


win.mainloop()
