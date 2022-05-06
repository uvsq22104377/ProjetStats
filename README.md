# ProjetStats
Deuxieme projet: STATISTIQUE DESCRIPTIVES A DEUX VARIABLES: DROITE DE REGRESSION

########################
#GROUPE 7 MIASHS TD2
#YANG Xinlei  (22106398)
#NGOMA Frederique   (22102710)
#MAUCLAIRE Moana    ()  
#https://github.com/uvsq22106398/ProjetStats



Notre projet consiste à programmer un ensemble de fonctions qui permettent de repondre à certains nombres de problèmes de statistiques.

Dans une premiere partie nous avons programmer 4 fonctions differrentes:
-La premiere nommée cree_fichier_alea(), permet de creer des fichiers d'un certain nombres de lignes de facon aleatoires. Sur chaque ligne on a deux nombres flottants choisis de maniere alaeatoire grace à la methode random.uniform(), separés chacun d'un espace. Nous rappelons que pour créer des fichiers tout court il suffit de faire: 
Fichier = open("nomdevotrefichier", "w"), avec "w" qui signifie write et qui permet donc d'écrire dans le fichier

-La deuxième fonction nommée lit_fichier(), permet dans une premiere partie de lire un fichier quelconque qui sera rentré en parametre, et de retourner deux listes contenant les coordonnées d'un nuage de point qui sera tracer dans la suite. Une liste contiendra les abcisses des points du nuage et seront tirées des nombres de la premiere colonne du fichier et le second fichier qui regroupera les nombres de la deuxieme colonne representera les ordonnées des points du nuage.

-La troisième trace_nuage()   