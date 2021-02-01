from tkinter import *

window = Tk()
window.geometry('500x400')
window.title("Mark your attendance")

headWindow = Frame(window, bg="#000000")
headWindow.pack(expand=True, fill="both")

btnRow1 = Frame(window)
btnRow1.pack(expand=True, fill="both")

btnsWindow2 = Frame(window)
btnsWindow2.pack(expand=True, fill="both")

btnsWindow3 = Frame(window)
btnsWindow3.pack(expand=True, fill="both")


def clicked():
    lable.configure(text="Clicked")


lable = Label(headWindow, text="Mark Your Attenedance",
              font=("Arial Bold", 30),
              anchor=CENTER,
              justify=CENTER,
              bg="#000000",
              fg="white")

btn = Button(btnRow1, text="English",
             font=("Arial Bold", 20),
             bg="#E51E2B", fg="white",
             command=clicked,
             bd=1,
             width=7,
             height=1,
             anchor=CENTER,
             justify=CENTER)

btn2 = Button(btnRow1, text="DSA",
              font=("Arial Bold", 20),
              bg="#050B2B", fg="white",
              command=clicked,
              bd=1,
              width=7,
              height=1,
              anchor=CENTER,
              justify=CENTER)

btn3 = Button(btnsWindow2, text="DBMS",
              font=("Arial Bold", 20),
              bg="#495B53", fg="white",
              command=clicked,
              bd=1,
              width=7,
              height=1,
              anchor=CENTER,
              justify=CENTER)

btn4 = Button(btnsWindow2, text="JAVA",
              font=("Arial Bold", 20),
              bg="#D4173F", fg="yellow",
              command=clicked,
              bd=1,
              width=7,
              height=1,
              anchor=CENTER,
              justify=CENTER)

btn5 = Button(btnsWindow3, text="NETWORKING",
              font=("Arial Bold", 20),
              bg="#151060", fg="white",
              command=clicked,
              bd=1,
              width=7,
              height=1,
              anchor=CENTER,
              justify=CENTER)

btn6 = Button(btnsWindow3, text="WEBDEV",
              font=("Arial Bold", 20),
              bg="#0D6628", fg="white",
              command=clicked,
              bd=1,
              width=7,
              height=1,
              anchor=CENTER,
              justify=CENTER)

lable.pack(side=TOP, expand=True)
btn.pack(side=LEFT, expand=True, fill="both")
btn2.pack(side=LEFT, expand=True, fill="both")
btn3.pack(side=LEFT, expand=True, fill="both")
btn4.pack(side=LEFT, expand=True, fill="both")
btn5.pack(side=LEFT, expand=True, fill="both")
btn6.pack(side=LEFT, expand=True, fill="both")

window.mainloop()
