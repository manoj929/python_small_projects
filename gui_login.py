from tkinter import *
from tkinter import messagebox

def Ok():
    uname = e1.get()
    passwod = e2.get()

    if (uname == '' and passwod == ''):
        messagebox.showinfo("", "blank not allowed")
    elif(uname == "Admin" and passwod == '123'):
        messagebox.showinfo('', 'Login Success')
        root.destroy()
    else:
        messagebox.showinfo('', 'Incorrect username and password')


root = Tk()
root.title("Login")
root.geometry('300x200')
global e1
global e2

Label(root, text="Username").place(x=10, y=10)
Label(root, text="password").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)
e2.config(show="*")

Button(root, text="Login", command=Ok, height=3, width=13).place(x=10, y=10)

root.mainloop()