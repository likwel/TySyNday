import os
import os.path, time
import glob
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import ttk

def donothing():
   filewin = Toplevel(fenetre)
   button = Button(filewin, text="Do nothing button")
   button.pack()

#fonction de partage de fichier pour le bouton envoyer
def Partage_Fichier(source, destination):
    "copie intégrale d'un fichier"
    fs = open(source, 'r')
    fd = open(destination, 'w')
    while 1:
        txt = fs.read(50)
        if txt =="":
            break
        fd.write(txt)
    fs.close()
    fd.close()
    return

#fonction de selection/ajout de fichier par filedialog
def Selection_Fichier():
    #dossier = filedialog.filechooser(title="Sélectionnez un  fichier a partager",mustexist=True,parent=fenetre)
    fichier=  filedialog.askopenfilename(initialdir = "/Desktop",title = "Sélectionnez un  fichier a partager",filetypes = (("Image","*.jpg"),("Tous les fichiers","*.*")))
    chm.set(fichier)
    taille.set(round(os.path.getsize(fichier)))
    typ.set("Voici le type de fichier")
    creation.set(time.ctime(os.path.getctime(fichier)))
    modific.set(time.ctime(os.path.getmtime(fichier)))

fenetre = Tk()
fenetre.title("TySyNday Version 1.0.0")
fenetre.geometry("600x530")
fenetre.minsize(600,530)
fenetre.maxsize(600,530)

conteneur_affichage = Frame(fenetre)

# on rend le conteneur redimensionnable
conteneur_affichage.columnconfigure(0, weight=1)
conteneur_affichage.rowconfigure(1, weight=0)

#LabelFrame de selection de fichier
selection_fichier =LabelFrame(conteneur_affichage,text="Selection de fichier",fg="blue",font="sans 12 bold",height=10,width=20)
selection_fichier.grid(row=1, column=0, sticky=NS+EW,pady=8)
chm=StringVar()
Label(selection_fichier,text="Cliquer le bouton pour selectionner un fichier !").pack()
#chemin=Entry(selection_fichier,textvariable=chm).pack(pady=2,fill=Y)

#btn=Button(selection_fichier,text="Parcourir",command=Selection_Fichier).pack()

#panel de selection
pane_selection = PanedWindow(selection_fichier, orient=HORIZONTAL)
pane_selection.pack(side=RIGHT, expand=Y, pady=15, padx=5)
pane_selection.add(Entry(pane_selection,textvariable=chm,width=75))
pane_selection.add(Button(pane_selection,text="Parcourir",command=Selection_Fichier,width=13))

#LabelFrame de proprietes des fichiers
propriete_fichier = LabelFrame(conteneur_affichage,text="Proprietes de fichier",fg="blue",font="sans 12 bold",height=10,width=20)
propriete_fichier.grid(row=2, column=0, sticky=NS+EW,pady=8)

#taille de fichier
taille=StringVar()
pane_taille=PanedWindow(propriete_fichier,orient=HORIZONTAL)
pane_taille.pack()
pane_taille.add(Label(pane_taille,text="Taille de fichier (en octets) : ", width=30,pady=5))
pane_taille.add(Label(pane_taille,textvariable=taille, width=30,pady=5))
taille.set("")

#type de fihier
typ=StringVar()
pane_type=PanedWindow(propriete_fichier,orient=HORIZONTAL)
pane_type.pack()
pane_type.add(Label(pane_type,text="Type de fichier : ", width=30, pady=5))
pane_type.add(Label(pane_type,textvariable=typ, width=30,pady=5))
typ.set("")

#date de creation de fichier
creation=StringVar()
pane_creation=PanedWindow(propriete_fichier,orient=HORIZONTAL)
pane_creation.pack()
pane_creation.add(Label(pane_creation,text="Date de creation : ", width=30,pady=5))
pane_creation.add(Label(pane_creation,textvariable=creation, width=30,pady=5))
creation.set("")

#date de modification
modific=StringVar()
pane_modific=PanedWindow(propriete_fichier,orient=HORIZONTAL)
pane_modific.pack()
pane_modific.add(Label(pane_modific,text="Date de dern modification : ", width=30,pady=5))
pane_modific.add(Label(pane_modific,textvariable=modific, width=30,pady=5))
modific.set("")


#LabelFrame de progression
progression = LabelFrame(conteneur_affichage,text="Progression",fg="blue",font="sans 12 bold",height=10,width=20)
progression.grid(row=3, column=0, sticky=NS+EW,pady=8)
Label(progression,text="Voici la progresion de l'envoye de fichier !").pack()
#Bare de progression dans LabelFrame
progress_copie =ttk.Progressbar(progression, orient = HORIZONTAL,length = 550, mode = 'determinate')
progress_copie.pack(pady=15)

#LabelFrame des actions des boutons
action =LabelFrame(conteneur_affichage,text="Actions",fg="blue",font="sans 12 bold",height=10,width=20)
action.grid(row=4, column=0, sticky=NS+EW,pady=8)
Label(action,text="Voici les commandes de l'envoye du fichier !").pack()
#Contenu de LabelFrame des actions

#panel des actions
pane_action = PanedWindow(action, orient=HORIZONTAL)
pane_action.pack(side=RIGHT, expand=Y, pady=15, padx=5)
pane_action.add(Button(action,text="Envoyer",command=Partage_Fichier,width=18))
pane_action.add(Button(action,text="Pause",width=18))
pane_action.add(Button(action,text="Annuler",width=18))
pane_action.add(Button(action,text="Quitter",command=fenetre.destroy,width=18))
#Menu de la fenetre
menubar = Menu(fenetre)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=fenetre.destroy)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=fenetre.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_separator()
helpmenu.add_command(label="Setting", command=donothing)
menubar.add_cascade(label="About", menu=helpmenu)

conteneur_affichage.grid(row=0, column=1, sticky=NS+EW, padx=5, pady=5)
# on rend la fenêtre redimensionnable
fenetre.rowconfigure(0, weight=1)
fenetre.columnconfigure(1, weight=1)
fenetre.config(menu=menubar)
fenetre.mainloop()
