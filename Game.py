import random
import time
import tkinter as tk
from tkinter import *


class App():

    def __init__(self):


        root = Tk()

        self.displayBox = Text(root)
        self.displayBox.grid(row=0,column=0)
        self.displayBox.config(state="disable")

        ebox = Entry(root)
        ebox.grid(row=0,column=1)

        def run(*args):


            self.displayBox.config(state="normal")

            self.displayBox.insert(END,"Dildo Baggins\n\n")

            self.displayBox.config(state="disable")




        root.bind("<k>",run)













        root.mainloop()

app = App()