import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("oefening 2")

def open_messagebox():
    messagebox.showinfo("oefening 2","dit is een massagebox")

button = tkinter.Button(window, text="open messagebox", command=open_messagebox)
button.pack()

window.mainloop()