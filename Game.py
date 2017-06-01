import SA3
import tkinter as tk
from tkinter import *

import random
import math

#***********************************************************************************************************************
#There are many requirements which are being filled in this assignment but are difficult to find.
#Nested Loops: The question function uses the "standardize" function from the SA3 file. The "standardize function uses the "lower" function also from the SA3 file. the lower function does make use of nested loops
#Account for invalid inputs: This is the task of the question function
#Account for type considerations: This is done when given the number for decision 5 and for the question functione everytime
#Length of string: the length of a string is calculated multiple times in for loops. The eliminate function as well as the lower function from the SA3 file use it.
#part of a string was acccessed: A part of a string was accessed in the lower function in order to find an upper case word
#.append is used: It is used numerous times throughout the program. in the eliminate function, and in many of the functions are drawn from the SA3 file and used here
#an element of a list is removed: an element of the list was removed in the elminate function
#conditional loop: one was used in the eliminate function

class App(Frame):

    def __init__(self):
        self.root = Tk()  #Creates the window
        self.root.title ("World Conquest Game") #Titles the Window
        Frame.__init__(self)

        self.updates("Map1.png")  # function which uploads the map
        # Map1 is provinces 1,2 red
        # Map2 is provines 1,2,3 red
        # Map3 is provinces 1,2,4 red
        # Map5 is provinces 1,2,3,4 red
        self.createGameComponents() #Creates all the widgetin the game
        self.bindings() #Creates all the bindings in the game
        self.variables() #creates all the variables in the game
        self.root.mainloop() #starts the game

    def updates(self, pic):  # this is to update photos. The PIC variable is going to be the name of the variable.

        self.game = tk.Canvas(self.root, width=675, height=707)  # creates the canvas where the image will go
        self.game.grid(column=1, row=0)  # places the image
        self.game.config(bg="black")  # makes it black to visible

        self.world = tk.PhotoImage(file=pic)  # takes it and gets it
        self.world_img = self.game.create_image(345, 315, image=self.world)  # places the image

    #Function to create all the widgets of the game
    def createGameComponents(self):
        # creates the white display box in the top right corner which will be doing most of the inserting
        self.displayBox = Text(self.root)  # creates it
        self.displayBox.grid(row=0, column=0)  # places it
        self.displayBox.config(height=46) #sizes the window
        self.displayBox.config(state="disable")  # the display box disabled

        # creates entry box for inputs
        # learn how to take user input. and use it.
        self.ebox = Entry(self.root)  # entry box
        self.ebox.config(width=75) #sizes the entry box
        self.ebox.grid(row=2, column=0)  # where to put it

        # For the information displayed into the stats box under the entry box
        self.statsWindow = Text(self.root)  #Creates the statistics window
        self.statsWindow.grid(row=3, column=1) #Places the window
        self.statsWindow.config(width=83, height=7) #Sizes it
        self.statsWindow.config(state="disabled", bg="yellow") #Creates the color and disables it

        #Enemy statistics window displaying the stats of the enemy on the left
        self.enemyStatsWindow = Text(self.root)  #Creates the window
        self.enemyStatsWindow.grid(row=3, column=0) #places the window
        self.enemyStatsWindow.config(width=79, height=7) #sizes the window
        self.enemyStatsWindow.config(state="disabled", bg="yellow") #disables and colors the window


# ***********************************************************************************************************************
# Variables and Game Specific functions

    # Function which updates Statistics
    def runDisplay(self,*args):  # defines the function
        # FRIENDLY STATS
        self.stats = SA3.fileToList("Statistics", ":")
        self.statsWindow.config(state="normal")  # allows text to be inserted into the document
        self.statsWindow.delete("1.0", END)  # Clears any text in there before hand
        self.statsWindow.insert(END, "YOUR CURRENT STATS\n\n")
        self.statsWindow.insert(END, "Money: " + self.stats[0] + "\n")  # inserts text, text is at the end
        self.statsWindow.insert(END, "Military Strength: " + self.stats[1] + "\n")
        self.statsWindow.insert(END, "Economic Power: " + self.stats[2] + "\n")
        self.statsWindow.config(state="disable")  # re-disables the text boxes

        # ENEMY STATS
        self.enemyStatsWindow.config(state="normal") #opens the window so text can be entered
        self.enemyStatsWindow.delete("1.0", END) #empties the window from previously
        self.enemyStatsWindow.insert(END, "ENEMY STATS\n\n") #Title of the window
        self.enemyStatsWindow.insert(END, "Province 3 Garrison: " + self.stats[3] + "\n") #military garrison of province 3
        self.enemyStatsWindow.insert(END, "Province 4 Garrison: " + self.stats[4] + "\n") #military garrison of province 4
        self.enemyStatsWindow.insert(END, "Economic Power: " + self.stats[5] + "\n") #economic power of the enemy

        self.enemyStatsWindow.config(state="disable") #re disables the text boxes

    # Reduces long enable display line into shorter
    def open(self):
        self.displayBox.config(state="normal")

    # Reduces long disable display line into shorter one
    def close(self):
        self.displayBox.config(state="disable")

    # reduces long insert text display line into shorter one
    def type(self, var):

        self.displayBox.config(state="normal")
        self.displayBox.insert(END, var)
        self.displayBox.config(state="disable")

    #Used for the inputs taken from the entry box. Takes the "~" out of the user entries so it is easier to process
    def eliminate (self, str):
        word = []  #List created
        newstr = "" #New string created
        for i in range (0, len(str), 1):  #For loop to turn the string into a list
            word.append(str[i]) #adds to the list

        word.pop() #Deletes the last character
        x = 0
        while x < len(word): #while loop to turn back into a string
            newstr = newstr + word[x]
            x = x + 1
        return newstr #returns the new word

    #Function used to make sure the user entry is proper
    def question(self,*args):
        stop = 0
        self.decision = "" #declares the value
        self.decision = self.ebox.get() #the information is retrieved
        self.ebox.delete(0, END) #the box is cleared
        self.decision = str(self.decision) #the decision is turned into a string
        self.decision = SA3.standardize(self.decision) #the decision is standardized (this includes the nested and while loops with the functions it uses lower function
        self.decision = self.eliminate(self.decision) #eliminates the"~"
        if self.decision != "option1" and self.decision != "option2": #if the decision isn't proper
            self.type("\nImproper Entry. Please enter your decision. Option 1-2\n") #user told to do it properly
            self.close()


        elif self.decision == "option1" or self.decision == "option2": #if the decision is proper

            return self.decision #value is returned and the game progresses

    def bindings (self):
        self.root.bind("k", self.runDisplay)
        self.type ("Press \">\" to get started.")
        self.root.bind(">", self.intro)

    def variables (self):
        #     [0]Money [1]Soldiers [2] economic power [3] Province 3 strength [4] Province 4 strength [5] enemy ecnomic strength
        stats = [5000, 7000, 3000, 6000, 6000, 3000]  # The first variable is the Money, the second variable is the soldiers the person has and the third is economic power
        SA3.statsUpdate(stats)  # This updates the statistics into a list
        self.txt = SA3.fileToList("User Text",";")  # this file will hold ALL of the text in this assignment, so it doesn't make big lengthy lines of code
        self.txt = SA3.converter(self.txt, "str")  # string to avoid errors with string concatnation
        self.casualties = 0


    def quit (self, *args):
        self.root.destroy()
#***********************************************************************************************************************
#Intro


    def intro (self,*args):

        # elements 0-3  in txt are for the introduction
        self.txt = SA3.fileToList("User Text",";")  # this file will hold ALL of the text in this assignment, so it doesn't make big lengthy lines of code
        self.txt = SA3.converter(self.txt, "str")  # string to avoid errors with string concatnation
        self.type("\t" + self.txt[1] + "\n")  # writes the first part of the intro
        self.type(self.txt[2] + "\n")  # how to lose
        self.type("\t" + self.txt[3])  # how to properly respond
        self.type("\n" + self.txt[4])  # how to update statistics
        type("\n\n")  # makes space between this and the next thing
        self.a = Button (self.root, text = "Next", command = self.part1)
        self.a.grid(row=2, column=1)


    #***********************************************************************************************************************
# elements 4-9 are for decision 1

    def part1(self,*args):
        self.root.unbind (">")
        self.type("\t" + self.txt[5])  # Introduces the question and economic
        self.type("\n" + self.txt[6])  # economic effect economic power
        self.type("\n" + self.txt[7])  # economic effect money
        self.type("\n" + self.txt[8])  # introduces military
        self.type("\n" + self.txt[9])  # military effect military power
        self.type("\n" + self.txt[10])  # military effect money
        self.type ("\n" +self.txt[0]) #The "what do you choose" line


        def options1 (*args):
            stats = SA3.fileToList("Statistics", ":")  # turns stats from file to list
            stats = SA3.converter(stats, "int")  # converts it integers

            response = self.question()

            if response == "option1":
                self.root.unbind ("~")

                stats[2] = stats[2] + 3000  # Adds 3000 to economic power
                stats[0] = stats[0] + 2000  # Adds 2000 to Money
                stats[5] = stats[5] + 1000  # Enemy also gains strength over time, economic power

                self.a.configure(command=self.part2)
                self.type("\n" + self.txt[27])  # tells user how to continue

            if response == "option2":  # military
                self.root.unbind ("~")

                stats[1] = stats[1] + 3000  # adds 3000 to Soldiers
                stats[0] = stats[0] - 1000  # takes away 1000 from money
                stats[3] = stats[3] + 500  # increased garrison in province 3
                stats[4] = stats[4] + 500  # increase garrison in province 4

                self.a.configure(command=self.part2)
                self.type("\n" + self.txt[27])  # tells user how to continue

            SA3.statsUpdate(stats)  # Updates the file


        self.root.bind ("~", options1)


#***********************************************************************************************************************
#Second Decision: Choice between invasion of 3 or 4

    def part2 (self, *args): #made in a function so it wouldn't type out immediately like it was doing before

        self.open()
        self.displayBox.delete('1.0', END)
        self.close()

        self.type (self.txt[11] + "\n")  #Declare province 3
        self.type ("\t" + self.txt[12]+ "\n")  #Smaller Garrison so easier
        self.type ("\t" + self.txt[13] + "\n") #Less Casualties
        self.type ("\t" + self.txt[14]+ "\n")  #if we lose, we lose the game
        self.type ("\t" + self.txt[15] + "\n") #4000 in loot
        self.type (self.txt[16]+ "\n\n") #-1000 in economic power
        self.type ("\t" + self.txt[17] + "\n") #invade province 4
        self.type ("\t" + self.txt[18]+ "\n")  #much harder only suggest if you military
        self.type ("\t" + self.txt[19] + "\n") #5000 in loot
        self.type ("\t" + self.txt[20]+ "\n")   #-2000 in economic power
        self.type ("\n" + self.txt[0]) #what do you choose line

        def options2(*args):

            stats = SA3.fileToList("Statistics", ":")  # getting statistics
            stats = SA3.converter(stats, "int")  # converting to integers

            response = self.question()

            if response == "option1": #if province 3 is chosen
                success = random.randint (0,100)  #success randomizer in the game

                #clearing the display box
                self.open()
                self.displayBox.delete('1.0', END)
                self.close()

                self.root.unbind ("~")

                if stats[1] > 9000: #if military upgrade was done previously, higher chance of success
                    if success < 20: #20% chance of failure
                        self.casualties = random.randint (3000, 8000) #higher casualties
                        self.type("INVASION FAILED. GAME LOST.\nCasualties: " + str(self.casualties)) #player told they lose the game
                        self.a.configure (text = "Exit", command = self.quit) #cut the program


                    else: #80% chance of success

                        self.casualties = random.randint (1500, 3000) #lower casualties
                        self.type("INVASION SUCCESS.\nCasualties: "+ str(self.casualties) + "\n") #player told casualties and success
                        self.updates("Map2.png") #new map uploaded
                        self.type("\n" + self.txt[27]) #tells user how to continue
                        self.a.configure(command=self.part3)

                if stats[1] < 9000: #without military upgrade previously, lower chances of success
                    if success < 30: #30% chance of failure

                        self.casualties = random.randint (3000, 6000) #high casualties
                        self.type("INVASION FAILURE. \nCasualties: " + str(self.casualties)) #told of failure
                        self.a.configure (text = "Exit", command = self.quit) #cut the program
                    else:  #70% success

                        self.casualties = random.randint (1000, 3500) #lower casualties
                        self.type("INVASION SUCCESS. \nCasualties: " + str(self.casualties) + "\n") #player told
                        self.updates("Map2.png") #new map uploaded
                        self.type("\n" + self.txt[27])  # tells user how to continue
                        self.a.configure(command=self.part3)
                #if the program was not cut, the variables can be changed
                stats[1]= stats[1]-self.casualties  #casualties put onto the military power
                stats[0] = stats[0] + 4000 #loot taken into the money
                stats[2] = stats[2] - 1000 #economic power lost
                stats[3] = 0 #garrison of province 3 deleted
                SA3.statsUpdate(stats)   #stats updated for statsWindow



            if response == "option2": #if province 4 chosen, much harder
                success = random.randint(0, 100) #success chances

                #display box cleared
                self.open()
                self.displayBox.delete('1.0', END)
                self.close()

                self.root.unbind ("~")

                if stats[1] > 9000:  # if military upgrade, harder than province 3
                    if success < 30:  # 30% chance of failure
                        self.casualties = random.randint(5000, 8000) #higher casualties
                        self.type("INVASION FAILED. GAME LOST.\nCasualties: " + str(self.casualties))
                        self.a.configure(text="Exit", command=self.quit)  # cut the program

                    else:  # 70% chance of success

                        self.casualties = random.randint(2000, 3000) #higher casualties than province 3
                        self.type("INVASION SUCCESS.\nCasualties: " + str(self.casualties) + "\n")
                        self.updates("Map3.png") #updates to different map
                        self.type("\n" + self.txt[27]) #tells user how to continue
                        self.a.configure(command=self.part3)

                if stats[1] < 9000:  # without military upgrade
                    if success < 70:  # 70% chance of failure, likely to fail
                        self.casualties = random.randint(5000, 6000) #higher casualties
                        self.type("INVASION FAILURE. \nCasualties: " + str(self.casualties))
                        self.a.configure(text="Exit", command=self.quit)  # cut the program

                    else:  #30% success chance

                        self.casualties = random.randint(2500, 3500) #high casualties
                        self.type("INVASION SUCCESS. \nCasualties: " + str(self.casualties) + "\n")
                        self.updates("Map3.png") #map updated
                        self.type("\n" + self.txt[27]) #tells user how to continue
                        self.a.configure(command=self.part3)

                stats[1] = stats[1] - self.casualties #manpower updated
                stats[0] = stats[0] + 5000 #loot added
                stats[2] = stats[2] - 2000 #economic power lost
                stats[4] = 0 #garrison for province 4 gone
                SA3.statsUpdate(stats) #added to file

        self.root.bind ("~", options2)  #sets the new key to start the new options for
        self.type ("\n\n")

#***********************************************************************************************************************
#Third Decision: Economic or Military

    def part3 (self, *args):

        self.type (self.txt[21] + "\n") #introduces economic
        self.type (self.txt[22] + "\n") #money increase (3000)
        self.type ( self.txt[23] + "\n\n") #economic power (4000)
        self.type ("   " +self.txt[24] + "\n") #introduces military
        self.type (self.txt[25] + "\n") #military increase (4000)
        self.type (self.txt[26] + "\n") #money decrease  (2000)

        def options3 (*args):
            stats = SA3.fileToList("Statistics", ":")  # turns stats from file to list
            stats = SA3.converter(stats, "int")  # converts it to integers

            response = self.question () #retrieves the text

            if response == "option1":  # economic

                self.root.unbind ("~")

                stats[2] = stats[2] + 4000  # adds 4000 to Economic Power
                stats[0] = stats[0] + 2000  # adds 2000 from money


                if stats[3] != 0: #if province 3 was not captured
                    stats[3] = stats[3] + 3000 #the garrison of province 3 is given 3000 more military
                else:  #if province 4 was not captured
                    stats[4] = stats[4] + 3000 #the garrison is increased by 4

                self.a.configure (command = self.part4)
                self.type("\n" + self.txt[27])
                SA3.statsUpdate(stats)  # updates file


            if response == "option2":  # military

                self.root.unbind ("~")

                stats[1] = stats[1] + 4000  # adds 4000 to Soldiers
                stats[0] = stats[0] - 2000  # takes away 2000 from money

                if stats[3] != 0: #if province 3 was not captured
                    stats[3] = 7000 #the garrison of province 3 is made 7000
                else:  #if province 4 was not captured
                    stats[4] = 7000 #the garrison is made 7000

                self.a.configure (command = self.part4)
                self.type ("\n" + self.txt[27])
                SA3.statsUpdate(stats)  # updates file

        self.root.bind ("~", options3)


#***********************************************************************************************************************
#Fourth Decision: Counter Attack (use funky equation)

    def part4 (self, *args):
        stats = SA3.fileToList("Statistics", ":")
        stats = SA3.converter(stats, "int")

        def winOrLose (*args):
            stats = SA3.fileToList("Statistics", ":")
            stats = SA3.converter(stats, "int")
            failure = None
            success = random.randint(0, 100)
            attackForce = 0
            if stats [3] != 0:
                attackForce = stats[3]*0.75
                stats[3] = stats[3] - attackForce

            if stats [4] !=0:
                attackForce = stats[4] * 0.75
                stats[4] = stats[4] - attackForce

            if attackForce > stats[1]:

                if success < 40:
                    failure = True
                else:
                    failure = False
            else:

                if success < 20:
                    failure = True
                else:
                    failure = False
            return failure
        result = winOrLose ()
        if result == True:
            self.type ("GAME LOST. The enemy counter attacked your captured province and won, defeating your entire military.")
            self.type ("You have been forced to surrender to the Greddan Empire, losing your game.")
            self.a.configure(text="Exit", command=self.quit)  # cut the program

        elif result == False:

            self.open()
            self.displayBox.delete("1.0", END)
            self.close()

            self.type ("\n" + self.txt[28] + "\n")
            self.casualties = random.randint ((math.floor(stats[1] * .35)),(math.floor(stats[1] * .65)))
            stats [1] = stats[1] - self.casualties
            SA3.statsUpdate(stats)

            self.type ("Casualties: " + str(self.casualties))
            self.a.configure(command = self.part5)
            self.type ("\n" + self.txt[27] + "\n")

#***********************************************************************************************************************
#Fifth Decision: convert how ever much money you want into soldiers
    def part5 (self, *args):

        self.open()
        self.displayBox.delete("1.0", END)
        self.close()

        self.type("\n\n")
        self.type (self.txt [29] + "\n")
        self.type (self.txt [30] + "\n\n")
        self.type (self.txt [31] + "\n")
        self.type (self.txt [32] + "\n")

        def soldierConversion (*args):
            stats = SA3.fileToList("Statistics", ":")
            stats = SA3.converter(stats, "int")

            num = self.ebox.get ()
            self.ebox.delete(0, END)
            num = self.eliminate (str(num))
            proper = True
            print (num)

            try:
                num = int(num)
            except ValueError:
                proper = False

            if proper == False:
                self.type("\nYou are required to enter a NUMBER with no decimals. Please enter a NUMBER with no decimals.\n")

            else:

                if num > stats[0]:
                    self.type("\nThe value you entered is too large. It cannot exceed the Money you have. Please re-enter.\n")

                else:
                    stats[1] = stats[1] + num
                    stats[0] = stats[0] - num

                    if stats[3] != 0:
                        stats[3] = stats[3] + stats[5]
                        stats [5] = 0
                    elif stats [4] !=0:
                        stats[4] = stats[4] + stats [5]
                        stats [5] = 0

                    self.type("The miltary reform is done.\n")
                    SA3.statsUpdate(stats)
                    self.root.unbind ("~")
                    self.a.configure (command = self.part6)
                    self.type (self.txt [27])



        self.root.bind ("~", soldierConversion)

#***********************************************************************************************************************
#final invasion: Use economy to over power them, or military to invade them.

    def part6 (self, *args):

        self.open ()
        self.displayBox.delete ("1.0", END)
        self.close ()
        self.type ("\n\n")
        self.type (self.txt[33] + "\n")
        self.type (self.txt[34] + "\n")
        self.type (self.txt[35] + "\n")
        self.type (self.txt[36] + "\n")
        self.type (self.txt[37] + "\n")
        self.type (self.txt[38] + "\n")
        self.type (self.txt[39] + "\n")
        self.type (self.txt[40] + "\n")
        self.type (self.txt[41] + "\n")
        self.type (self.txt[0] + "\n")

        def options6 (*args):
            stats = SA3.fileToList("Statistics", ":")
            stats = SA3.converter(stats, "int")
            success = random.randint (0, 100)
            failure = None
            casualties = 0

            response = self.question ()

            if response == "option1":
                print ("Economic Worked")

                if stats[2] < 3000:
                    self.root.unbind ("~")
                    print ("Economic One has worked")


                    if success < 70:
                        failure = True
                        stats[2] = stats[2] * .70

                    else:
                        failure = False
                        stats[2] = stats[2] * .50
                else:
                    print ("Economic Two Has Worked")

                    if success < 30:
                        failure = True
                        stats[2] = stats[2] * .50

                    else:
                        failure = False
                        stats[2] = stats[2] * .35

                casualties = random.randint ((math.floor(stats[1] * .25)), (math.floor(stats[1] * .50)))

            elif response == "option2":
                self.root.unbind ("~")
                print ("military has worked")

                if stats [1] < 9000:
                    print ("Military One has worked")
                    if success < 40:
                        failure = True

                    else:
                        failure = False

                else:
                    print ("Military Two has worked")
                    if success < 25:
                        failure = True

                    else:
                        failure = False

                casualties = random.randint((math.floor(stats[1] * .70)), (math.floor(stats[1] * .90)))

            if failure == True:


                self.open()
                self.displayBox.delete("1.0", END)
                self.close()
                self.type("President, we have failed to finish the job. The enemy has defeated our attempt to subdue them. You were able gain ground against them, but our advantage is lost and the task to unite the island is now the burden of our kin.\n")
                self.type ("Your country thanks your for you contributions. The game has not been a win for you, but not a lose either.\n Casualties: " + str(casualties))

                stats[1] = stats[1] - casualties
                SA3.statsUpdate(stats)

                self.a.configure (text = "Exit", command = self.quit)

            elif failure == False:

                self.open()
                self.displayBox.delete("1.0", END)
                self.close()

                self.type("President, you have done it! You have united the island and freed it from the oppressive Greddan Empire! You shall go down in history as the liberator and unifier of our glorious island.\n")
                self.type ("Your country thanks your for you contributions. The game has been one by you!\n Casualties: " + str(casualties))

                stats [0] = stats [0] + 5000
                stats[1] = stats [1] - casualties

                SA3.statsUpdate(stats)
                self.updates("Map4.png")

                if stats[3] != 0:
                    stats [3] = 0
                else:
                    stats[4] = 0

                SA3.statsUpdate(stats)
                self.updates("Map4.png")
                self.a.configure(text="Exit", command=self.quit)


        self.root.bind ("~", options6)


app = App()  # Ask again

