from tkinter import *
from socket import *
import sys
import threading
import os
import re
import subprocess
from tkinter import messagebox

#import InterfaceServeur

window = Tk()

def fonction_creer():
    #print("Vous envoyer un fichier")
    import socket
    HOST = socket.gethostname()
    PORT = 50000
    # 1) création du socket :
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2) liaison du socket à une adresse précise
    try:
        mySocket.bind((HOST, PORT))
    except socket.error:
        messagebox.showerror("Error", "La liaison du socket à l'adresse choisie a échoué.")
        #print ("La liaison du socket à l'adresse choisie a échoué.")
        sys.exit()

    mySocket.listen(5)

    if True:
    #while True:
        # 3) Attente de la requête de connexion d'un client :
        print ("Serveur prêt, en attente de requêtes ...")
        #mySocket.listen(5)
        # 4) Etablissement de la connexion :

        connexion, adresse = mySocket.accept()
        print ("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))
        import InterfaceC
        window.quit()
    else:
        print("connexion echouee")

def fonction_joindre():
    #print("Vous recevoire un fichier")
    import socket
    HOST = socket.gethostname()
    PORT = 50000
    # 1) création du socket :
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2) envoi d'une requête de connexion au serveur :
    try:
        mySocket.connect((HOST, PORT))

    except socket.error:
        print ("La connexion a échoué.")
        sys.exit()
    print ("Connexion établie avec le serveur.")
    import InterfaceC
    window.destroy()

frame=Frame(window,bg='#16f0f3')

window.title("TySyNday")
window.geometry("300x250")
window.minsize(300,250)
window.maxsize(300,250)
#window.iconbitmap("icon.png")
window.config(background='#16f0f3')

lab_titre=Label(frame,text="Bienvenu sur TySyNday",font=("Times",20),bg='#16f0f3')
lab_titre.pack(pady=5,fill=X)
lab_titre1=Label(frame,text="Transfert des fichiers",font=("Times",15),bg='#16f0f3')
lab_titre1.pack()

btn_creer=Button(frame,text="Creer",font=("Times",15),bg='red', command=fonction_creer)
btn_creer.pack(pady=25,fill=X)

btn_joindre=Button(frame,text="Joindre",font=("Times",15),bg='green', command=fonction_joindre)
btn_joindre.pack(pady=25,fill=X)

#frame.pack(expand=YES) #afficher en centre

frame.pack()

window.mainloop()
