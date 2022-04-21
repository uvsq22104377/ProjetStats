import random as rd
import tkinter as tk

t = 0
HEIGHT = 500
WIDTH = 500
liste_X = []
liste_Y = []


def cree_fichier_alea(nb, nomfichier):
    t = nb
    global t
    nomfichier = open("fichier de texte", "w")
    for i in range(nb):
        for j in range(2):
            temp = rd.uniform(0, 500)
            nomfichier.write(temp, " ")
        nomfichier.write("\n")


def lit_fichier(nomfic):
    global liste_X,liste_Y
    liste = []
    nomfic = open(nomfic,'r')
    while True:
        texte = nomfic.readline()
        liste.append(texte.split())
        if texte == '':
            break
    for i in range(t):
        liste_X.append(liste[i][0])
        liste_Y.append(liste[i][1])


def trace_nuage(nomf):
    lit_fichier(nomf)
    for m, n in liste_X, liste_Y:
        cv.create_line((m, n), (m+1, n+1), width=1)
    return len(liste_X)


def trace_droite(a, b):
    cv.create_line((0, b), (500, 500*int(a)+int(b)))


racine = tk.Tk()
cv = tk.Canvas(racine, height=HEIGHT, width=WIDTH)











