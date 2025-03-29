import tkinter
from tkinter import colorchooser

window = tkinter.Tk()
def kleur():
    kleur = colorchooser.askcolor()[1]
    if kleur:
        button.config(bg=kleur)

button = tkinter.Button(window, text="kies een kleur", command=kleur)
button.pack()

window.mainloop()