#!usr/opt/lib
#!encoding: utf-8

import argparse
import cv2
import math
import numpy as np
import classImage as img
import fonction as fonction
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import variable




def donothing():
   x = 0

def openfile():
    global j
    j += 1
    root.filename = tkFileDialog.askopenfilename(initialdir = "/Users/Aoda/Documents/Cours/Frame-extractor/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
    fond = img.Image("bob" + str(j), cv2.imread(root.filename))
    variable.list_image.append(fond)
    for i in variable.list_image:
        i.affImage()

def detection():
    for i in variable.list_image:
        if i.active == True:
            i.process()


j = 0

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

fonctionmenu = Menu(menubar, tearoff=0)
fonctionmenu.add_command(label="Corner detections", command=detection)
fonctionmenu.add_command(label="Corner setting", command=donothing)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Fonctions", menu=fonctionmenu)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)


root.mainloop()

#boucle mere
while True:
#    cv2.imshow(fond.nom, image)
    key = cv2.waitKey(1) & 0xFF
#    print pos


    if key == ord("r"):
        image = clone.copy()

    #elif key == ord("x"):


    elif key == ord("c"):
        get()


cv2.destroyAllWindows()
