########################
#GROUPE 7 MIASHS TD2
#YANG
#NGOMA
#MAUCLAIRE
#https://github.com/uvsq22106398/ProjetStats


############################
# import des modules
import random as rd

#creation fichier
fichier = open (nomfichier,"w")

##########################
# constantes

#nombre de ligne du fichier
nb = 10
#liste
liste1 = []
liste2 = []


############################
# fonctions 

#1ere partie

def cree_fichier_alea(nb, nomfichier):
    """commentaire à faire"""
    fichier = open(nomfichier,"w")   #cette fois ci le 1er fichier crée sera ecraser et remplacer par celui là
    for i in range (1, nb+1):
        for i in range(2):
            temp = str(rd.uniform(0, 500))  #quel est la difference avec randint
            fichier.write(temp, " ")
        fichier.write("\n")
    fichier.close()


def lit_fichier(nomfic):
    """commentaire à faire"""
    global liste1 , liste2
    fichier = open(nomfic, "r")
    for ligne in nomfic:    #j'aurai bien aime faire un readline(), mais j'ai du mal pour la suite
         val = ligne.split()
         liste1.append(val[0])
         liste2.append(val[1])
    fichier.close()
    return (liste1, liste2)


def trace_nuage(nomf):   #Note nomfichier, nomfic, nomf represente tous des fichiers sur le disque dur
    """commentaire à faire"""
    lit_fichier(nomfic)
    pass


def trace_droite(a, b):
    """commentaire à faire"""
    pass


#2eme partie

def moyenne(serie):     #serie correspond à une liste, soit celle des X soit celle des Y
    """commentaire à faire"""
    somme = 0
    for elem in serie:
        somme += elem
    moyen = somme / len(serie)
    return moyen


def variance(serie):
    """commentaire à faire"""
    moyenne(serie)
    res = moyenne(serie)  #ou res = moyen mais ca marche et j'ai pris sur le net
    som = 0
    for x in serie:
        som += (x - res)**2
    var = som / len(serie)
    return var


def covariance(serieX, serieY):
    """commentaire à faire"""
    #moyenne(serie)
    res1 = moyenne(serieX)  # à comprendre
    res2 = moyenne(serieY)  # à comprendre
    sommme = 0 
    for x, y in res1, res2:
        somme += (x-res1)*(y-res2)
        covar= somme / len(serieX) #ou serieY vu que les deux deux ont normalement la meme dimension
    return covar
    

def correlation(serieX, serieY):
    """commentaire à faire"""
    #variance(serie)
    covariance(serieX, serieY)
    result = covariance(serieX, serieY)
    res1 = variance(serieX)
    res2 = variance(serieY)
    corre = result / ((res1)*(res2))**0.5
    return corre


def forte_correlation(serieX, serieY):
    """commentaire à faire"""
    pass


def droite_reg(serieX, serieY):
    """commentaire à faire"""
    pass




