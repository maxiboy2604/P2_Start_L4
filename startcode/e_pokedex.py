import tkinter

window = tkinter.Tk()
window.title("pokemon informatie applicatie")
label = tkinter.Label(window, text="Voer een pokémonnaam in:")
label.pack()
tkinter.Entry(window)
button = tkinter.Button(window, text="Haal pokémon informatie op")
button.pack()

window.mainloop()