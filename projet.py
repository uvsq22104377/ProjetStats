import random as rd
import tkinter as tk

t = 0
HEIGHT = 500
WIDTH = 500
liste_X = []
liste_Y = []


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
    for i in range(t):
        liste_X.append(liste[i][0])
        liste_Y.append(liste[i][1])
    print(liste_X)
    print(liste_Y)


def trace_nuage(nomf):
    lit_fichier(nomf)
    for m, n in liste_X, liste_Y:
        cv.create_line((int(m), int(n)), (int(m) + 1, int(n) + 1), width=1)

    return len(liste_X)


def trace_droite(a, b):
    cv.create_line((0, b), (500, 500 * a + b))


racine = tk.Tk()
racine.title('graphique')
cv = tk.Canvas(racine, height=HEIGHT, width=WIDTH)
cv.pack()
cree_fichier_alea(2, 'fichier')
trace_nuage('fichier')
trace_droite(2, 10)
racine.mainloop()


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
        somme = (i - average) ^ 2 + somme
    variancee = somme / len(serie)
    return variancee


def covariance(serie_x, serie_y):
    average_x = moyenne(serie_x)
    average_y = moyenne(serie_y)
    somme = 0
    for m, n in serie_x, serie_y:
        temp = (m - average_x) * (n - average_y)
        somme = somme + temp
    covariancee = somme / len(serie_x)
    return covariancee


def correlation(serie_x, serie_y):
    covariance_x_y = covariance(serie_x, serie_y)
    variance_x = variance(serie_x)
    variance_y = variance(serie_y)
    coefficient = covariance_x_y / (variance_x * variance_y) ^ 0, 5
    return coefficient


def forteCorrelation(serie_x, serie_y):
    correlation_coefficient = correlation(serie_x, serie_y)
    if correlation_coefficient > 0.8 or correlation_coefficient < -0.8:
        return True
    else:
        return False


def droite_reg(serie_x, serie_y):
    somme = 0
    sum_m = 0
    sum_n = 0
    i = 0
    moy_x = moyenne(serie_x)
    moy_y = moyenne(serie_y)
    for m, n in serie_x, serie_y:
        temp = m * n
        somme = temp + somme
        sum_m = m + sum_m
        sum_n = n + sum_n
        i = i + n ^ 2
    summ = sum_n * sum_m
    coef_dir = (len(serie_x) * somme - summ) / (len(serie_x) * i - (sum_m ^ 2))
    ord_orig = -coef_dir * moy_y + moy_x
    return coef_dir, ord_orig
