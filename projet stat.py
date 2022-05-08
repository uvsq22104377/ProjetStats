########################
# GROUPE 7 MIASHS TD2
# YANG Xinlei
# NGOMA Frederique
# MAUCLAIRE Moana
# https://github.com/uvsq22106398/ProjetStats


###########################
# import des modules
import random as rd
import tkinter as tk
import pandas as pd

# definition des variables
HEIGHT = 500
WIDTH = 500
liste_X = []
liste_Y = []
list1, list2 = [], []
couleur = ['green', 'blue', 'white', 'cyan', 'yellow', 'purple']


# Premiere partie

# definition des fonctions
def cree_fichier_alea(nb, nomfichier):
    """fonction qui crée un fichier nommée 'nom fichier' contenant 'nb' de
    lignes, tout deux passé en argument.Chaque ligne contient deux nombres 
    flottants aleatoires entre 0 et 500"""

    fichier = open(nomfichier, "w")
    for i in range(nb):  # debut de la boucle
        for j in range(2):
            temp = rd.uniform(0, 500)  # generation des floats aleatoires
            fichier.write(str(temp))  # ecriture du fichier
            fichier.write(' ')
        fichier.write("\n")  # changement de ligne
    fichier.close()  # fermeture du fichier


def lit_fichier(nomfic):
    """fonction qui prends en argument un fichier enregistré sur le disque dur 
    passer, le lit et retoune deux listes: listeX qui contient les abcisses pour
    tracer le nuage de point par la suite et listeY qui contient les ordonées """
    global liste_X, liste_Y  # globalisation des variables
    fichier = open(nomfic, 'r')
    liste = []  # generation
    while True:  # debut de la boucle
        texte = fichier.readline()
        liste.append(texte.split())  # il genere une liste entiere d'ou les termes sont les chaines de caracteres
        if texte == '':
            break
    for i in range(len(liste) - 1):  # creation de listeX et liste Y
        liste_X.append(float(liste[i][0]))
        liste_Y.append(float(liste[i][1]))
    return liste_X, liste_Y


def trace_nuage(nomf):
    """fontion qui prends en argument un fichier supposé contenir un certain nombre de
    ligne avec chaque contenant deux float séparé par un espace. Cette fonction appeler
    par la suite la fonction lit_fichier(nomfic) qui founira les abcisses et ordonnés pour
    tracer un nuage de point. Enfin la fonction retournera le nombre de point dessinés"""

    lit_fichier(nomf)
    for i in range(len(liste_X)):
        cv.create_line((float(liste_X[i]), float(liste_Y[i])), (float(liste_X[i]) + 2, float(liste_Y[i]) + 2), width=2)
        # simulation des points par des lignes carrees
    return len(liste_X)


def trace_droite(a, b):
    """fonction prenant 2 arguments flottants représentant le coefficient directeur a et
    l'ordonnée à l'origine b d'une droite............................................"""

    cv.create_line((0, b), (500, 500 * a + b),
                   fill='red')  # tracage d une droite d'ou a est le coefficient directeur b est l'ordonne a l'origine


# Deuxieme Partie

def moyenne(serie):
    """fonction qui prend sen argument une liste de réels representant une serie statistique
    et retourne la moyenne de cette serie"""

    somme = 0
    for i in serie:
        somme = somme + i
    average = somme / len(serie)
    return average


def variance(serie):
    """fonction qui prend en argument une liste de réels representant une serie statistique.
    Elle devra appeler la fonction moyenne(serie) puis calculer la variance de cette série """

    average = moyenne(serie)
    somme = 0
    for i in serie:
        somme = ((i - average) ** 2) + somme
    variancee = somme / len(serie)
    return variancee


def covariance(serie_x, serie_y):
    """fonction qui prend en argument 2 listes represant deux series statistique différentes X
    et Y. Elle appelera la fonction moyenne(serie) et retorunera la covariance entre les 
    variables X et Y"""

    average_x = moyenne(serie_x)
    average_y = moyenne(serie_y)
    somme = 0
    for i in range(len(serie_x)):
        temp = (serie_x[i] - average_x) * (serie_y[i] - average_y)
        somme = somme + temp
    covariancee = somme / len(serie_x)
    return covariancee


def correlation(serie_x, serie_y):
    """fontion qui prend en argument 2 listes represant deux series statistique différentes X
    et Y. Elle appelera les fonction moyenne(serie) et variance(serie) et retorunera le
    coefficient de correlation entre les variables X et Y"""

    covariance_x_y = covariance(serie_x, serie_y)
    variance_x = variance(serie_x)
    variance_y = variance(serie_y)
    coefficient = covariance_x_y / ((variance_x * variance_y) ** 0.5)
    return coefficient


def forteCorrelation(serie_x, serie_y):
    """fonction qui prend en argument 2 listes represant deux series  statistique différentes X
    et Y. Elle appelera la fonction correlation(serieX,serieY) et decidera si les variables X 
    et Y sont fortement liées ou pas. Enfin elle retournera un booleen selon les cas """

    correlation_coefficient = correlation(serie_x, serie_y)
    if correlation_coefficient > 0.8 or correlation_coefficient < -0.8:
        return True
    else:
        return False


def droite_reg(serie_x, serie_y):
    """Commentaire à faire """

    variance_x = variance(serie_x)
    covariance_x_y = covariance(serie_x, serie_y)
    average_x = moyenne(serie_x)
    average_y = moyenne(serie_y)
    coef_dir = covariance_x_y / variance_x
    ord_orig = average_y - coef_dir * average_x
    return coef_dir, ord_orig


# Troisieme partie
def dessiner(n):
    """commentaire à faire """

    global list1, list2
    # tracage des points avec la souris lors du clic gauche
    cv.create_line((float(n.x), float(n.y)), (float(n.x) + 2, float(n.y) + 2), fill='purple')
    list1.append(n.x)  # creation des listes des coordonnes de la souris
    list2.append(n.y)


def activer_dessin():
    """fonction qui actionne le mode dessin avec la souris """

    racine.bind('<Button-1>', dessiner)  # association de l'evenement au racine


def desactiver():
    """fonction qui annule desactive le mode dessin avec un clic sur la souris"""

    racine.unbind('<Button-1>')  # dissociation de l'evenement au racine


#  Programme principale
racine = tk.Tk()
racine.title('graphique')

# creation de canvas
cv = tk.Canvas(racine, height=HEIGHT, width=WIDTH)

# definition des buttons
butt = tk.Button(racine, text='Tracer la droite de regression',
                 command=lambda: trace_droite(droite_reg(list1, list2)[0], droite_reg(list1, list2)[1]))
butt_2 = tk.Button(racine, text='Autre couleur',
                   command=lambda: cv.create_line((50, 200), (350, 200), fill=rd.choice(couleur)))
butt_3 = tk.Button(racine, text='Quitter', command=racine.destroy)
butt_4 = tk.Button(racine, text='Activer le mode Dessin', command=activer_dessin)
butt_5 = tk.Button(racine, text='Desactiver le mode Dessin', command=desactiver)
butt_6 = tk.Button(racine, text='Tracer la droite',
                   command=lambda: cv.create_line((50, 200), (350, 200), fill='red'))
cv.pack()  # position des widgets
butt_6.pack()
butt_2.pack()
butt_4.pack()
butt_5.pack()
butt.pack()
butt_3.pack()

# test du fichier aleatoire
"""
cree_fichier_alea(10, 'fichier alea')
lit_fichier('fichier alea')
trace_nuage('fichier alea')
m = forteCorrelation(liste_X, liste_Y)
n = droite_reg(liste_X, liste_Y)
print(m)
print(n)
if m is True:
    trace_droite(n[0], n[1])
else:
    pass
"""
# test du fichier exemple.txt
"""
trace_nuage('exemple.txt')
a = forteCorrelation(liste_X, liste_Y)
b = droite_reg(liste_X, liste_Y)
print(a)
print(b)
if a is True:
    trace_droite(b[0], b[1])
else:
    pass
"""

# test du fichier villes_virgule.csv avec pandas
# par contre là il faudra vraiment que tu m'explique stp (fred)
"""
info = pd.read_csv("villes_virgule.csv")   # lire le fichier
villes_2010 = info.loc[info["nb_hab_2010"] <= 500, ['nb_hab_2010']]   # selection des donnees
villes_2012 = info.loc[info["nb_hab_2012"] <= 500, ['nb_hab_2012']]

list_2010 = list(villes_2010['nb_hab_2010'])   # transformation des dataframes en liste
list_2012 = list(villes_2012['nb_hab_2012'])

fort = forteCorrelation(list_2010, list_2012)
droite = droite_reg(list_2010, list_2012)

for i in range(int(input())):
    cv.create_line((list_2010[i], list_2012[i]), (list_2010[i] + 2, list_2012[i] + 2), width=2)

print(correlation(list_2010, list_2012))
print(fort)

if fort is True:
    trace_droite(droite[0], droite[1])
else:
    pass
"""

# Lancement de la boucle principal

racine.mainloop()
