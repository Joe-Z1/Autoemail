from tkinter import *
import sqlite3
from selenium import webdriver
import time

win = Tk()
win.geometry('400x400')
win.title("Auto Email")

f = LabelFrame(win)
f.place(anchor="center")

# submit email and password and insert into sql database
user = sqlite3.connect('user.db')
c = user.cursor()

url = ["https://login.live.com/", "google.com"]


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


# print all values in database


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

    for record in records:
        btn = Button(win, text=record[0], command=lambda: login())
        btn.place(relx=.2, rely=.8)
        # login and use first record to fill in username

    def login():
        driver = webdriver.Chrome()
        driver.get(url[0])
        username = driver.find_element_by_id(
            "i0116").send_keys(str(record[0]))
        nextScreen = driver.find_element_by_id("idSIButton9").click()
        time.sleep(1)
        password = driver.find_element_by_id("i0118").send_keys(record[1])


def create():

    c.execute("""CREATE TABLE user(
            user_name text,
            password text
            )
    """)
    user.commit()
    user.close()
    msg = Label(win, text="Database Created")
    msg.place(relx=.38, rely=.1)


def delete():
    user = sqlite3.connect('user.db')
    c = user.cursor()
    c.execute("DELETE from user WHERE oid=" + Dety.get())
    Dety.delete(0, END)
    user.commit()
    user.close()


# Labels
email_label = Label(win, text="Email", font=40)
email_label.place(relx=.25, rely=.2)
password_label = Label(win, text="Password", font=40)
password_label.place(relx=.2, rely=.28)

# Entries
Email = Entry(win, font=40, bg="light gray")
Email.place(relx=.40, rely=.2)

Password = Entry(win, font=40, bg="light gray", show="*")
Password.place(relx=.40, rely=.28)

Dety = Entry(win, font=40, bg="light gray")
Dety.place(relx=.4, rely=.56)


# Buttons
Subtn = Button(win, text="Submit", font=40,
               width=20, relief=GROOVE, command=lambda: submit())
Subtn.place(relx=.30, rely=.36)

# query Button
Qbutton = Button(win, text="Create Buttons", command=query, font=40)
Qbutton.place(relx=.1, rely=.65)

# create database
createbtn = Button(win, text="Create Database", command=create)
createbtn.pack()

Dbtn = Button(win, text="Delete by ID", command=delete, font=40)
Dbtn.place(relx=.10, rely=.55)

v = Scrollbar(win)
v.pack(side=RIGHT, fill=Y)

win.mainloop()
