from tkinter import *
top = Tk()
top.geometry("200x300")
top.title("registation form")
define = Label(top, text="registation form", width=20,font=("bold", 20)).place(x=5, y=10)
define = Label(top, text="Name").place(x=30,y=60)
define = Label(top, text="Crn").place(x=30, y=100)
define = Label(top, text="Urn").place(x=30, y=140)
define = Label(top, text="Address").place(x=30, y=180)
define = Label(top, text="Branch").place(x=30, y=220)
list_of_branch = ['CS','IT','ECE','CIVIL','ME',]
c = StringVar()
dropdown=OptionMenu(top,c,*list_of_branch)
dropdown.place(x=80,y=220)

define = Label(top, text="Gender").place(x=30, y=290)
var = IntVar()
Radiobutton(top, text="Male",padx=5, variable=var, value=1).place(x=90, y=290)
Radiobutton(top, text="Female",padx=10, variable=var, value=2).place(x=190, y=290)

e1 = Entry(top).place(x=80, y=60)
e2 = Entry(top).place(x=80, y=100)
e3 = Entry(top).place(x=80, y=140)
e4 = Entry(top).place(x=80, y=180)
e5 = Entry(top).place(x=80, y=140)


top.mainloop()
