
########################
#GROUPE 7 MIASHS TD2
#YANG
#NGOMA
#MAUCLAIRE
#https://github.com/uvsq22106398/ProjetStats


############################
# import des modules
import random as rd
import tkinter as tk

##########################
# constantes
HEIGHT = 500
WIDTH = 500
t = 0

# variables 

#liste
liste_X = []
liste_Y = []
couleur = ['green', 'blue', 'white', 'cyan', 'yellow', 'purple']


#############################
#fonctions

#Premiere partie
def cree_fichier_alea(nb, nomfichier):
    """fonction qui crée un fichier nommée 'nom fichier'
    contenant 'nb' de lignes, tout deux passé en argument.
    Chaque ligne contient deux nombres flottants aleatoires
    entre 0 et 500"""

    global t
    t = nb
    fichier = open(nomfichier, "w")
    for i in range(nb):
        for j in range(2):
            temp = (rd.uniform(0, 500))
            fichier.write(str(temp))
            fichier.write(' ')
        fichier.write("\n")
    fichier.close()



def lit_fichier(nomfic):
    """fonction qui prends en argument un fichier enregistré
    sur le disque dur passer, le lit et retoune deux listes:
    listeX qui contient les abcisses pour tracer le nuage de
    point par la suite et listeY qui contient les ordonées """

    global liste_X, liste_Y
    liste = []
    fichier = open(nomfic, "r")
    while True:
        texte = fichier.readline()
        liste.append(texte.split())
        if texte == '':
            break
    for i in range(len(liste)-1):
        liste_X.append(liste[i][0])
        liste_Y.append(liste[i][1])
        liste_X[i] = float(liste_X[i])
        liste_Y[i] = float(liste_Y[i])



def trace_nuage(nomf):
    """fontion qui prends en argument un fichier supposé
    contenir un certain nombre de ligne avec chaque contenant
    deux float séparé par un espace. Cette fonction appelera par 
    la suite la fonction lit_fichier(nomfic) qui founira les
    abcisses et ordonnés pour tracer un nuage de point.
    Enfin la fonction retournera le nombre de point dessinés"""

    lit_fichier(nomf)
    for i in range(len(liste_X)):
        cv.create_line((liste_X[i], liste_Y[i]), (liste_X[i] + 1, liste_Y[i] + 1), width=1)
    return len(liste_X)



def trace_droite(a, b):
    """fonction prenant 2 arguments flottants représentant le 
    coefficient directeur a et l'ordonnée à l'origine b d'une 
    droite................................................."""

    cv.create_line((0, b), (500, 500 * a + b), fill='red')


#Test des 4 fonctions
#cree_fichier_alea(50, "fichier.txt")
#lit_fichier("fichier.txt")
#trace_nuage("fichier.txt")
#trace_droite("")



# Deuxieme Partie
def moyenne(serie): 
    """fonction qui prend sen argument une liste de réels representant
    une serie statistique et retourne ma moyenne de cette serie"""

    somme = 0
    for i in serie:
        somme = somme + i
    average = somme / len(serie)
    return average



def variance(serie):
    """fonction qui prend en argument une liste de réels representant
    une serie statistique. Elle devra appeler la fonction moyenne(serie)
    puis calculer la variance de cette série """

    average = moyenne(serie)
    somme = 0
    for i in serie:
        somme = ((i - average) ** 2) + somme
    variancee = somme / len(serie)
    return variancee



def covariance(serie_x, serie_y):
    """fonction qui prend en argument 2 listes represant deux series 
    statistique différentes X et Y. Elle appelera la fonction moyenne(serie)
    et retorunera la covariance entre les variables X et Y"""

    average_x = moyenne(serie_x)
    average_y = moyenne(serie_y)
    somme = 0
    for i in range(len(serie_x)):
        temp = (serie_x[i] - average_x) * (serie_y[i] - average_y)
        somme = somme + temp
    covariancee = somme / len(serie_x)
    return covariancee



def correlation(serie_x, serie_y):
    """fontion qui prend en argument 2 listes represant deux series 
    statistique différentes X et Y. Elle appelera les fonction moyenne(serie)
    et variance(serie) et retorunera le coefficient de correlation entre les
     variables X et Y"""

    covariance_x_y = covariance(serie_x, serie_y)
    variance_x = variance(serie_x)
    variance_y = variance(serie_y)
    coefficient = covariance_x_y / ((variance_x * variance_y) ** 0.5)
    return coefficient



def forteCorrelation(serie_x, serie_y):
    """fonction qui prend en argument 2 listes represant deux series 
    statistique différentes X et Y. Elle appelera la fonction correlation(serieX, 
    serieY) et decidera si les variables X et Y sont fortement liées ou pas.
    Enfin elle retournera un booleen selon les cas """

    correlation_coefficient = correlation(serie_x, serie_y)
    if correlation_coefficient > 0.8 or correlation_coefficient < -0.8:
        return True
    else:
        return False



def droite_reg(serie_x, serie_y):
    """fonction..............................
    .......................................... """

    somme = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    moy_x = moyenne(serie_x)
    moy_y = moyenne(serie_y)
    for m in range(len(liste_X)):
        temp = liste_X[m] * liste_Y[m]
        somme = temp + somme
        sum_x = liste_X[m] + sum_x
        sum_y = liste_Y[m] + sum_y
        sum_x2 = sum_x2 + liste_X[m] ** 2
    coef_dir = (len(serie_x) * somme - sum_x * sum_y) / (len(serie_x) * sum_x2 - sum_x ** 2)
    ord_orig = moy_y - coef_dir * moy_x
    return coef_dir, ord_orig



#Troiseme partie 

#programme principal 
racine = tk.Tk()
racine.title('graphique')
cv = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
butt = tk.Button(racine, text='Tracer la droite', command=lambda: cv.create_line((50, 200), (450, 200), fill='red'))
butt_2 = tk.Button(racine, text='Autre couleur',
                   command=lambda: cv.create_line((50, 200), (450, 200), fill=rd.choice(couleur)))
butt_3 = tk.Button(racine, text='Quitter', command=racine.destroy)
cv.pack()
butt.pack()
butt_2.pack()
butt_3.pack()


#pratique
trace_nuage('exemple.txt')
correlation(liste_X, liste_Y)
a = forteCorrelation(liste_X, liste_Y)
b = droite_reg(liste_X, liste_Y)
print(a)
print(b)
if a is True:
    trace_droite(b[0], b[1])
else:
    pass


#lancement de la boucle principal
racine.mainloop()
