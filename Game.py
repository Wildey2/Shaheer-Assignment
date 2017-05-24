import random
import time
import tkinter as tk
from tkinter import *


#***********************************************************************************************************************



class App:
    #ask self again
    def __init__(self):

#***********************************************************************************************************************
#Creating Game Window

        self.root = Tk()
        self.root.title("World Conquest Game") #The title


        def updates(pic): #this is to update photos. The PIC variable is going to be the name of the variable.

            self.game = tk.Canvas(self.root, width=675, height=707)  # creates the canvas where the image will go
            self.game.grid(column=1, row=0)  # places the image
            self.game.config(bg="black")  #makes it black to visible
            # ^^^Ask again

            self.world = tk.PhotoImage(file= pic)  # takes it and gets it
            self.world_img = self.game.create_image(345, 315, image=self.world)  # places the image

        updates ("Map1.png") #function which uploads the map
        #Map1 is provinces 1,2 red
        #Map2 is provines 1,2,3 red
        #Map3 is provinces 1,2,4 red
        #Map5 is provinces 1,2,3,4 red

        #creates the white display box in the top right corner which will be doing most of the inserting
        self.displayBox = Text(self.root) #creates it
        self.displayBox.grid(row=0,column=0)  #places it
        self.displayBox.config (height = 46)
        self.displayBox.config(state="disable") #the display box disabled
        """
        #creates entry box for inputs
        #learn how to take user input. and use it.
        self.ebox = Entry(self.root) #entry box
        self.ebox.config (width = 75)
        self.ebox.grid(row=2,column=0)  #where to put it
        """

        #For the information displayed into the stats box under the entry box
        self.statsWindow = Text(self.root)
        self.statsWindow.grid (row=3,column=1)
        self.statsWindow.config (width = 83, height = 7)
        self.statsWindow.config (state= "disabled", bg="yellow")


        self.enemyStatsWindow = Text(self.root)
        self.enemyStatsWindow.grid(row=3, column=0)
        self.enemyStatsWindow.config(width=79, height=7)
        self.enemyStatsWindow.config(state="disabled", bg="yellow")



#***********************************************************************************************************************
#Variables and Game Specific functions

        #Function which updates Statistics
        def runDisplay(*args): #defines the function
            #FRIENDLY STATS
            self.stats = SA3.fileToList("Statistics", ":")
            self.statsWindow.config(state="normal") #allows text to be inserted into the document
            self.statsWindow.delete("1.0", END)  #Clears any text in there before hand
            self.statsWindow.insert (END, "YOUR CURRENT STATS\n\n")
            self.statsWindow.insert (END,"Money: " + self.stats[0] + "\n") #inserts text, text is at the end
            self.statsWindow.insert (END, "Military Strength: " + self.stats[1] + "\n")
            self.statsWindow.insert (END, "Economic Power: " + self.stats[2] + "\n")
            self.statsWindow.config(state="disable") #re-disables the text boxes


            #ENEMY STATS
            self.enemyStatsWindow.config (state = "normal")
            self.enemyStatsWindow.delete("1.0", END)
            self.enemyStatsWindow.insert (END, "ENEMY STATS\n\n")
            self.enemyStatsWindow.insert (END, "Province 3 Garrison: " + self.stats[3] + "\n")
            self.enemyStatsWindow.insert(END, "Province 4 Garrison: " + self.stats[4] + "\n")
            self.enemyStatsWindow.insert(END, "Economic Power: " + self.stats [5] + "\n")

            self.enemyStatsWindow.config (state = "normal")
        self.root.bind("<k>", runDisplay) #binds updates to this key

        def newBind (part):
            self.root.unbind(">")
            self.root.bind (">", part)

        #Reduces long enable display line into shorter
        def open ():
           self.displayBox.config(state= "normal")

        #Reduces long disable display line into shorter one
        def close ():
            self.displayBox.config (state = "disable")

        #reduces long insert text display line into shorter one
        def type (var):
            open ()
            self.displayBox.insert (END, var)
            close ()

        def sleep (time):
            time = time * 1000
            self.root.after(time)
        #     [0]Money [1]Soldiers [2] economic power [3] Province 3 strength [4] Province 4 strength [5] enemy ecnomic strength
        self.stats = [5000, 7000, 3000, 4000, 6000, 3000]  #The first variable is the Money, the second variable is the soldiers the person has and the third is economic power
        SA3.statsUpdate(self.stats) #This updates the statistics into a list
        self.enemyStrength = [4000, 6000, 3000]  # garrison of province 3 then 4, enemy numbers.
        self.enemyStrength = SA3.converter(self.enemyStrength, "int")
        self.txt = SA3.fileToList("User Text", ";") #this file will hold ALL of the text in this assignment, so it doesn't make big lengthy lines of code
        self.casualties = 0


#***********************************************************************************************************************
#Introduction
        #elements 0-3  in txt are for the introduction
        self.txt = SA3.converter(self.txt, "str")   #string to avoid errors with string concatnation
        type ( "\t" + self.txt[1] + "\n")   #writes the first part of the intro
        type ( self.txt[2] + "\n")  #how to lose
        type( "\t" + self.txt[3])  #how to properly respond
        type ("\n" + self.txt[4]) #how to update statistics
       # sleep(5)
        type ("\n\n") #makes space between this and the next thing



#***********************************************************************************************************************
#First Decision: Choice between military or economic

        def part1 (*args):
            #elements 4-9 are for decision 1
            type ("\t" + self.txt[5]) #Introduces the question and economic
            type ("\n" + self.txt [6]) #economic effect economic power
            type("\n" + self.txt[7]) #economic effect money
            #sleep(3)
            type("\n" + self.txt[8]) #introduces military
            type("\n" + self.txt[9])  #military effect military power
            type("\n" + self.txt[10])  #military effect money

            def option1 (*args): #economic
                newBind (part2)
                #self.root.unbind(">")  #Unbinds > so it can be declared for part2
                self.stats = SA3.fileToList("Statistics", ":") #turns stats from file to list
                self.stats = SA3.converter(self.stats, "int") #converts it integers
                self.stats[2] = self.stats[2] + 3000  #Adds 3000 to economic power
                self.stats[0] = self.stats[0] + 2000 #Adds 2000 to Money
                self.stats[5] = self.stats[5] + 1000 #Enemy also gains strength over time, economic power
                SA3.statsUpdate(self.stats)  #Updates the file
                self.a.destroy()  #Destroys button a
                self.b.destroy()  #Destroys button b
                #lines 133-136 deletes the text in the displaybox
                open()
                self.displayBox.delete('1.0', END)
                close()




            def option2 (*args): #military
                newBind (part2)
                #self.root.unbind(">") #unbinds > so it can be used for part 2
                self.stats = SA3.fileToList("Statistics", ":")  #turns stats from file to list
                self.stats = SA3.converter(self.stats, "int")   #converts it to integers
                self.stats[1] = self.stats[1] + 3000  #adds 3000 to Soldiers
                self.stats[0] = self.stats[0] - 1000  #takes away 1000 from money
                self.stats [3] = self.stats[3] + 500 #increased garrison in province 3
                self.stats [4] = self.stats [4] + 500 #increase garrison in province 4
                SA3.statsUpdate(self.stats) #updates file
                self.a.destroy()  #destroys button a
                self.b.destroy()   #destroys button b
                #lines 147-150 delete the text in the text box
                open()
                self.displayBox.delete('1.0', END)
                close()

            type("\nPlease enter \">\" to move to the next part.")  #Tells the player how to progress

            self.a = Button(self.root, text="Option 1", command=option1)  #creates button representing option 1, allowing the user to click
            self.a.grid(row = 2, column = 0) #places the button


            self.b = Button (self.root, text = "Option 2", command = option2)  #creates a button representing option 2, allowing the user to click
            self.b.grid(row = 2, column = 1)  #places the button


        self.root.bind(">", part1)  #this is the first bind to start the entire part 1
#***********************************************************************************************************************
#Second Decision: Choice between invasion of 3 or 4

        def part2 (*args): #made in a function so it wouldn't type out immediately like it was doing before
            type (self.txt[11] + "\n")  #Declare province 3
            type ("\t" + self.txt[12]+ "\n")  #Smaller Garrison so easier
            type ("\t" + self.txt[13] + "\n") #Less Casualties
            type ("\t" + self.txt[14]+ "\n")  #if we lose, we lose the game
            type ("\t" + self.txt[15] + "\n") #4000 in loot
            type (self.txt[16]+ "\n\n") #-1000 in economic power
            type ("\t" + self.txt[17] + "\n") #invade province 4
            type ("\t" + self.txt[18]+ "\n")  #much harder only suggest if you military
            type ("\t" + self.txt[19] + "\n") #5000 in loot
            type ("\t" + self.txt[20]+ "\n")   #-2000 in economic power



            def province3 (*args): #if province 3 is chosen
                success = random.randint (0,100)  #success randomizer in the game
                self.stats = SA3.fileToList ("Statistics", ":")  #getting statistics
                self.stats = SA3.converter (self.stats, "int")      #converting to integers

                #clearing the display box
                open()
                self.displayBox.delete('1.0', END)
                close()


                if self.stats[1] > 9000: #if military upgrade was done previously, higher chance of success
                    if success < 20: #20% chance of failure
                        self.casualties = random.randint (3000, 8000) #higher casualties
                        print("INVASION FAILED. GAME LOST.\nCasualties: " + str(self.casualties)) #player told they lose the game
                        self.root.destroy()  #cut the program

                    else: #80% chance of success
                        newBind (part3)
                        #self.root.unbind(">")  # unbinds it so it can be declared for part3
                        self.casualties = random.randint (1500, 4000) #lower casualties
                        type ("INVASION SUCCESS.\nCasualties: "+ str(self.casualties)) #player told casualties and success
                        updates("Map2.png") #new map uploaded
                        self.a.destroy()  # button 'province 3' deleted
                        self.b.destroy()  # button 'province 4' deleted

                if self.stats[1] < 9000: #without military upgrade previously, lower chances of success
                    if success < 30: #30% chance of failure
                        self.casualties = random.randint (3000, 6000) #high casualties
                        print("INVASION FAILURE. \nCasualties: " + str(self.casualties)) #told of failure
                        self.root.destroy() #game cut

                    else:  #70% success
                        newBind(part3)
                        #self.root.unbind(">")  # unbinds it so it can be declared for part3
                        self.casualties = random.randint (2000, 4500) #lower casualties
                        type ("INVASION SUCCESS. \nCasualties" + str(self.casualties)) #player told
                        updates("Map2.png") #new map uploaded
                        self.a.destroy()  # button 'province 3' deleted
                        self.b.destroy()  # button 'province 4' deleted

                #if the program was not cut, the variables can be changed
                self.stats[1]= self.stats[1]-self.casualties  #casualties put onto the military power
                self.stats[0] = self.stats[0] + 4000 #loot taken into the money
                self.stats[2] = self.stats[2] - 1000 #economic power lost
                self.stats[3] = 0 #garrison of province 3 deleted
                SA3.statsUpdate(self.stats)   #stats updated for statsWindow



            def province4 (): #if province 4 chosen, much harder
                success = random.randint(0, 100) #success chances
                self.stats = SA3.fileToList("Statistics", ":") #values brought from list
                self.stats = SA3.converter(self.stats, "int") #converted to int

                #display box cleared
                open()
                self.displayBox.delete('1.0', END)
                close()


                if self.stats[1] > 9000:  # if military upgrade, harder than province 3
                    if success < 30:  # 30% chance of failure
                        self.casualties = random.randint(5000, 8000) #higher casualties
                        print("INVASION FAILED. GAME LOST.\nCasualties: " + str(self.casualties))
                        self.root.destroy() #program cut

                    else:  # 70% chance of success
                        newBind (part3)
                        #self.root.unbind(">")
                        self.casualties = random.randint(3000, 4000) #higher casualties than province 3
                        type("INVASION SUCCESS.\nCasualties: " + str(self.casualties))
                        updates("Map3.png") #updates to different map
                        self.a.destroy()  # button a gone
                        self.b.destroy()  # button b gone


                if self.stats[1] < 9000:  # without military upgrade
                    if success < 70:  # 70% chance of failure, likely to fail
                        self.casualties = random.randint(5000, 6000) #higher casualties
                        print("INVASION FAILURE. \nCasualties: " + str(self.casualties))
                        self.root.destroy() #program cut

                    else:  #30% success chance
                        newBind (part3)
                        #self.root.unbind (">") #unbinding it so it can be used for part3
                        self.casualties = random.randint(3500, 4500) #high casualties
                        type("INVASION SUCCESS. \nCasualties: " + str(self.casualties))
                        updates("Map3.png") #map updated
                        self.a.destroy()  # button a gone
                        self.b.destroy()  # button b gone

                self.stats[1] = self.stats[1] - self.casualties #manpower updated
                self.stats[0] = self.stats[0] + 5000 #loot added
                self.stats[2] = self.stats[2] - 2000 #economic power lost
                self.stats[4] = 0 #garrison for province 4 gone
                SA3.statsUpdate(self.stats) #added to file

            self.a = Button (self.root, text = "Province 3", command = province3)  #button for province 3 created
            self.a.grid (row = 2, column = 0) #placed

            self.b = Button(self.root, text="Province 4", command=province4) #button for province 4
            self.b.grid(row=2, column=1) #placed
            type("Please enter \">\" to move to the next part.") #tells the user how to progress


        type ("\n\n")
#***********************************************************************************************************************
#Third Decision: Economic or Military

        def part3 (*args):
            type (self.txt[21] + "\n") #introduces economic
            type (self.txt[22] + "\n") #money increase (3000)
            type ( self.txt[23] + "\n\n") #economic power (4000)
            type ("   " +self.txt[24] + "\n") #introduces military
            type (self.txt[25] + "\n") #military increase (4000)
            type (self.txt[26] + "\n") #money decrease  (2000)

            def option1(*args):  # economic
                self.root.unbind(">")  # unbinds it so it can be declared for part4
                self.stats = SA3.fileToList("Statistics", ":")  # turns stats from file to list
                self.stats = SA3.converter(self.stats, "int")  # converts it to integers
                self.stats[2] = self.stats[2] + 4000  # adds 4000 to Economic Power
                self.stats[0] = self.stats[0] + 2000  # adds 2000 from money


                if self.stats[3] != 0:
                    self.stats[3] = self.stat[3] + 3000
                else:
                    self.stats[4] = self.stats[4] + 3000

                SA3.statsUpdate(self.stats)  # updates file

                self.a.destroy()  # destroys button a
                self.b.destroy()  # destroys button b
                # lines 147-150 delete the text in the text box
                open()
                self.displayBox.delete('1.0', END)
                close()


            def option2(*args):  # military
                self.root.unbind(">")  # unbinds it so it can be declared for part4
                self.stats = SA3.fileToList("Statistics", ":")  # turns stats from file to list
                self.stats = SA3.converter(self.stats, "int")  # converts it to integers
                self.stats[1] = self.stats[1] + 4000  # adds 4000 to Soldiers
                self.stats[0] = self.stats[0] - 2000  # takes away 2000 from money

                if self.stats[3] != 0: #if province 3 was not captured, up enemy troop numbers to 7000
                    self.stats[3] = 7000
                else:  #if province 4 was not captured, up enemy troop numbers to 7000
                    self.stats[4] = 7000

                SA3.statsUpdate(self.stats)  # updates file

                self.a.destroy()  # destroys button a
                self.b.destroy()  # destroys button b

                #deletes the text in the text box
                open()
                self.displayBox.delete('1.0', END)
                close()

            self.a = Button(self.root, text="Option 1",
                            command=option1)  # creates button representing option 1, allowing the user to click
            self.a.grid(row=2, column=0)  # places the button

            self.b = Button(self.root, text="Option 2",
                            command=option2)  # creates a button representing option 2, allowing the user to click
            self.b.grid(row=2, column=1)  # places the button



#***********************************************************************************************************************
#Fourth Decision: Counter Attack (use funky equation)


#***********************************************************************************************************************
#Fifth Decision: convert how ever much money you want into soldiers


#***********************************************************************************************************************
#final invasion: Use economy to over power them, or military to invade them.



        self.root.mainloop() #ask again?

       #Let the user decide initially which type of game they would like to play green or red
game = True
while game == True:
    question = input ("Would you like to play this game? (Y/N):")
    if question == "Y" or question == "N":
        game = True
    else:
        game = False
    app = App()  #Ask again
