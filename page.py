#!usr/opt/lib
#!encoding: utf-8
from Tkinter import *
from functools import partial
from PIL import Image, ImageTk
import PIL


def donothing():
   x = 0

def show_selection(label, choices, listbox):
    choices = choices.get()
    text = ""
    for index in listbox.curselection():
        text += choices[index] + " "

    label.config(text=text)
    listbox.insert('end','e')

def addPerso():
    global list_perso, list_perso_present
    val = list_perso.get(list_perso.curselection())
    print val
    list_perso_present.insert('end', val)



def update_label(stringvar):
    global input_perso
    text = stringvar.get()
    input_perso.insert('end', text)
    print text

def addPersoGen():
    pop = Tk()
    text = StringVar(pop)
    entry_name = Entry(pop, textvariable=text)
    entry_name.grid(row=0, column=0)

    new_perso = Button(pop, text="Ajouter", command=partial(update_label, text)).grid(row=1, column=0)



def editPerso():
    global list_perso, personnage, input_perso

    perso = Tk()
    print personnage
    input_perso = Listbox(perso, listvariable=personnage, selectmode="single")
    input_perso.grid(row=0, column=0, rowspan=4)
    add_perso_gen = Button(perso, text='Ajouter personnage', command=addPersoGen).grid(row=0, column=1)
    dele_perso_gen = Button(perso, text='Supprimer personnage', command=lambda input_perso=input_perso: input_perso.delete(ANCHOR)).grid(row=1, column=1)



global list_perso, personnage

root = Tk()

####### Menu #######

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)

editemenu = Menu(menubar, tearoff=0)
editemenu.add_command(label="Edition personnage", command=editPerso)

menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Edition", menu=editemenu)

root.config(menu=menubar)


image = PIL.Image.open("planche1.png")
photo = ImageTk.PhotoImage(image)

label = Label(root, image=photo)
label.image = photo # keep a reference!
label.grid(row=0, column=0, rowspan=4)


####### ListBox #######

personnage = Variable(root, ('Bob', 'Roger', 'Hubert'))
list_perso = Listbox(root, listvariable=personnage, selectmode="single")
list_perso.grid(row=3, column=2)

personnage_resent = Variable(root, ('none'))
list_perso_present = Listbox(root, listvariable=personnage_resent, selectmode="single")
list_perso_present.grid(row=3, column=3)


####### Button #######

add_perso = Button(root, text='Ajouter personnage', command=addPerso).grid(row=4, column=2)
dele_perso = Button(root, text='Supprimer personnage', command=lambda list_perso_present=list_perso_present: list_perso_present.delete(ANCHOR)).grid(row=4, column=3)



####### Label #######

text_page = Label(root, text="Textes :").grid(row=6, column=1)
nom_perso = Label(root, text="Personnages :", padx="10", pady="4").grid(row=3, column=1)
nom_page = Label(root, text="Numéros de page :", padx="10", pady="4").grid(row=0, column=1)
entree_page = Entry(root, textvariable='').grid(row=0, column=2)
nom_position_frame = Label(root, text="Position de page :", padx="10", pady="4").grid(row=1, column=1)
entree_position = Entry(root, textvariable='').grid(row=1, column=2)



root.mainloop()
