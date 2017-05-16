import random
import time
import tkinter as tk
from tkinter import *


class App():

    def __init__(self):


        self.root = Tk()

        self.displayBox = Text(self.root)
        self.displayBox.grid(row=0,column=0)
        self.displayBox.config(state="disable")

        ebox = Entry(self.root)
        ebox.grid(row=0,column=1)

        def run(*args):


            self.displayBox.config(state="normal")

            self.displayBox.insert(END,"Dildo Baggins\n\n")

            self.displayBox.config(state="disable")




        self.root.bind("<k>",run)













        self.root.mainloop()

app = App()