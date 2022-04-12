import random as rd


def cree_fichier_alea(nb, nomfichier):
    nomfichier = open("fichier de texte", "a","w")
    for i in range(2):
        temp = rd.uniform(0, 500)
        nomfichier.write(temp, " ")
    nomfichier.write("\n")


def lit_fichier(nomfic):
