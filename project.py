from tkinter import *
import sqlite3

win = Tk()
win.geometry('700x800')
win.title("Auto Email")

f = LabelFrame(win)
f.pack(fill="both", expand="yes")

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
        print_records += str(record[0]) + "\n"

    query_label = Label(f, text=print_records)
    query_label.pack()
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
    c.execute("DELETE from user WHERE oid=PLACEHOLDER")
    user.commit()
    user.close()


email_label = Label(f, text="Email")
email_label.pack(padx=20)
Email = Entry(f, font=40)
Email.pack()


password_label = Label(f, text="Password")
password_label.pack()
Password = Entry(f, font=40)
Password.pack()

button = Button(f, text="submit", font=40, command=lambda: submit())
button.pack()

# query Button
Qbutton = Button(f, text="Test", command=query)
Qbutton.pack()

# create database
createbtn = Button(f, text="Create Database", command=create)
createbtn.pack()

Dbtn = Button(f, text="Delete", command=delete)
Dbtn.pack()


win.mainloop()
