import random as rd
import tkinter as tk

t = 0
HEIGHT = 500
WIDTH = 500
liste_X = []
liste_Y = []
couleur = ['green', 'blue', 'white', 'cyan', 'yellow', 'purple']


def cree_fichier_alea(nb, nomfichier):
    global t
    t = nb
    fichier = open(nomfichier, "w")
    for i in range(nb):
        for j in range(2):
            temp = round(rd.uniform(0, 500))
            fichier.write(str(temp))
            fichier.write(' ')
        fichier.write("\n")
    fichier.close()


def lit_fichier(nomfic):
    global liste_X, liste_Y
    liste = []
    fichier = open(nomfic, 'r')
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
    lit_fichier(nomf)
    for i in range(len(liste_X)):
        cv.create_line((liste_X[i], liste_Y[i]), (liste_X[i] + 1, liste_Y[i] + 1), width=1)
    return len(liste_X)


def trace_droite(a, b):
    cv.create_line((0, b), (500, 500 * a + b), fill='red')


# Deuxieme Partie
def moyenne(serie):
    somme = 0
    for i in serie:
        somme = somme + i
    average = somme / len(serie)
    return average


def variance(serie):
    average = moyenne(serie)
    somme = 0
    for i in serie:
        somme = ((i - average) ** 2) + somme
    variancee = somme / len(serie)
    return variancee


def covariance(serie_x, serie_y):
    average_x = moyenne(serie_x)
    average_y = moyenne(serie_y)
    somme = 0
    for i in range(len(serie_x)):
        temp = (serie_x[i] - average_x) * (serie_y[i] - average_y)
        somme = somme + temp
    covariancee = somme / len(serie_x)
    return covariancee


def correlation(serie_x, serie_y):
    covariance_x_y = covariance(serie_x, serie_y)
    variance_x = variance(serie_x)
    variance_y = variance(serie_y)
    coefficient = covariance_x_y / ((variance_x * variance_y) ** 0.5)
    return coefficient


def forteCorrelation(serie_x, serie_y):
    correlation_coefficient = correlation(serie_x, serie_y)
    if correlation_coefficient > 0.8 or correlation_coefficient < -0.8:
        return True
    else:
        return False


def droite_reg(serie_x, serie_y):
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

racine.mainloop()
