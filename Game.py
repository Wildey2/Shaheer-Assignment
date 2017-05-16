import random
import time
import tkinter as tk
from tkinter import *


class App:

    def __init__(self):

        self.root = Tk()
        self.root.title("World Conquest Game")
        self.gameC = tk.Canvas(self.root, width=2000, height=600)
        self.gameC.grid(column=1, row=0)
        self.gameC.config(bg="black")

        self.world = tk.PhotoImage(file="Map.png")
        self.world_img = self.gameC.create_image(650,315,image=self.world)

        self.displayBox = Text(self.root)
        self.displayBox.grid(row=0,column=0)
        self.displayBox.config(state="disable")

        self.ebox = Entry(self.root)
        self.ebox.grid(row=2,column=0)

        def run(*args):

            self.displayBox.config(state="normal")

            self.displayBox.insert(END,"Dildo Baggins\n\n")

            self.displayBox.config(state="disable")

        self.root.bind("<k>",run)

        self.root.mainloop()

app = App()