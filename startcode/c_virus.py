import tkinter
from tkinter import messagebox
import random

titels=["critical error", "you're gonna die"]
messages=["you're gonna die", "you ain't gonna live any longer"]

for i in range(20):
    messagebox.showinfo(random.choice(titels),random.choice(messages))