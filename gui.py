from Tkinter import *
win = Tk()
win.geometry('700x800')
win.title("Auto Email")


def click(entry):
    print("This is Your entry", entry)
    button1 = Button(text=entry)
    button1.pack()


frame = Frame(win, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=.75,
            relheight=.1, anchor='n')

entry = Entry(frame, font=40)
entry.place(relwidth=.65, relheight=1)

button = Button(frame, text="boi", font=40, command=lambda: click(entry.get()))
button.place(relx=.7, relheight=1, relwidth=.3)


win.mainloop()
