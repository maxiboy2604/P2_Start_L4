import tkinter

window = tkinter.Tk()
window.title("GUI les")
window.geometry("300x200")

label = tkinter.Label(window, text="Welkom bij mijn eerste GUI!")
label.pack()

def verander_tekst():
    label.config(text="Knop ingedrukt!")

def tkinter_label():
    label.config(text="Welkom bij mij eerste GUI")

button = tkinter.Button(window, text="Klik op mij!", command=verander_tekst)
button.pack()

button2 = tkinter.Button(window, text="Klik op mij!", command=tkinter_label)
button2.pack()

window.mainloop()