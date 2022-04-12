import random as rd


def cree_fichier_alea(nb, nomfichier):
    global nb
    nomfichier = open("fichier de texte", "w")
    for i in range(nb):
        for j in range(2):
            temp = rd.uniform(0, 500)
            nomfichier.write(temp, " ")
        nomfichier.write("\n")


def lit_fichier(nomfic):
    nomfic = open(nomfic,'r')
    liste = nomfic.split()
    liste_X = []
    liste_Y = []
    for i in range(nb):
        if i % 2:
            liste_X.append(liste[i])
        else:
            liste_Y.append(liste[i])
    return liste_X,liste_Y


def trace_Nuage(nomf):
    lit_fichier(nomf)
    pass



