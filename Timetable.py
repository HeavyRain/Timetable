"""
Timetable 2.6.3
Copyright (C) 2011 Constantin Lorenz

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses>.
"""

import time, Gamelibrary, os, sys
from Tkinter import *
from getch import * # getch is needed for Unix compatibility (cf. source file)
gl = Gamelibrary

#setting up the window
window = Tk()
window.title("Timetable")

frame = Frame(borderwidth=10)
frame.grid()

# defining an "About" pop-up window
def about():
   top = Toplevel()
   top.title("About Timetable 2.6.3")
   
   msg = Message(top, borderwidth=10, text="Timetable 2.6.3\nCopyright (C) 2011 Constantin Lorenz\n\nThis program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.\n\nThis program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.\n\nSee the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses>.")
   msg.pack()

def edit_gamelibrary():
   window.destroy()
   os.system("ren Gamelibrary.py Gamelibrary.txt && Gamelibrary.txt && ren Gamelibrary.txt Gamelibrary.py && Timetable.py")
   sys.exit(0)

def exit():
   window.destroy()
   sys.exit(0)

#setting up the menu
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=exit)
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_command(label="Edit Gamelibrary", command=edit_gamelibrary)
menubar.add_command(label="About", command=about)
window.config(menu=menubar)

# dirty hack to put some space between the buttons
Label(frame, text="                                                  ").grid()

# create a matrix with all the game variables in it
games = ((gl.game1, gl.game2, gl.game3, gl.game4, gl.game5, gl.game6, gl.game7, gl.game8, gl.game9, gl.game10), (gl.game11, gl.game12, gl.game13, gl.game14, gl.game15, gl.game16, gl.game17, gl.game18, gl.game19, gl.game20))

# draws the gamebuttons
def spawnbutton(game, row, column):
  gamebutton = Button(frame, text=game, width=18, borderwidth=3, command=lambda: main(game)) # lambda is needed to actually pass an argument to "main"
  gamebutton.grid(row=row, column=column)

# the mainfunction that does the actual work
def main(path_to_file):
   try: # this ensures that the window is only killed once (in case a new game has been added)
      window.destroy()
      print "Your choice: " + path_to_file
   except:
      pass
   
   while 1:
      try: # check if game.txt already exists
         fileobj = open(path_to_file, "r")
         temptime = fileobj.read() # read time in file...

      except: # create a new file if game.txt doesn't exist
         fileobj = open(path_to_file, "w")
         fileobj.write("0")
         fileobj.close()
         main(path_to_file)
      
      start = time.time()
      print "\n\nTimer started. Press any key to pause."
      getch()
      end = time.time()
      gametime = ((end - start) / 3600) # time played in hours
      
      fileobj = open(path_to_file, "r")
      temptime = fileobj.read() # read time in file...
      fileobj.close
      totaltime = (float(temptime) + gametime) # ...and add time played (converted to a float)

      fileobj = open(path_to_file, "w")
      fileobj.write(str(totaltime)) # write sum in file (converted to a string)
      fileobj.close()
      
      print "\nTimer paused. Press any key to continue."
      getch() # implementation of a pause feature

# spawn only buttons that are actually defined in Gamelibrary
row = 0
for game in games[0]:
   if game is not None:
      spawnbutton(game, row, 0)
      row = row + 1
      
row = 0
for game in games[1]:
   if game is not None:
      spawnbutton(game, row, 2)
      row = row + 1
            
      
raw_input()