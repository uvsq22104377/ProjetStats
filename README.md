# ProjetStats
Deuxieme projet: STATISTIQUE DESCRIPTIVES A DEUX VARIABLES: DROITE DE REGRESSION

########################
#GROUPE 7 MIASHS TD2
#YANG Xinlei  (22106398)
#NGOMA Frederique   (22102710)
#MAUCLAIRE Moana    ()  
#https://github.com/uvsq22106398/ProjetStats



Notre projet consiste à programmer un ensemble de fonctions permettant de repondre à un certain nombres de problèmes de statistiques comme par exemple
- créer des nuages aléatoires de points et les représenter graphiquement,
- calculer leur coefficient de corrélation, 
- décider s'il est pertinent de réaliser un ajustement linéaire (c'est à dire de tracer la droite des moindres
carrés) et si oui, tracer la droite des moindres carrés.
Pour realiser ce projet, notre travail a été divisé en 3 partie.


Dans une premiere partie destiné à la mise en place d'outils, nous avons programmer 4 fonctions differrentes:
-La premiere nommée cree_fichier_alea(), permet de creer des fichiers d'un certain nombres de lignes de facon aleatoires. Sur chaque ligne on a deux nombres flottants choisis de maniere alaeatoire grace à la methode random.uniform(), separés chacun d'un espace. Nous rappelons que pour créer des fichiers tout court il suffit de faire: 
Fichier = open("nomdevotrefichier", "w"), avec "w" qui signifie write et qui permet donc d'écrire dans le fichier

-La deuxième fonction nommée lit_fichier(), permet dans une premiere partie de lire un fichier quelconque qui sera rentré en parametre, et de retourner deux listes contenant les coordonnées d'un nuage de point qui sera tracer dans la suite. Une liste contiendra les abcisses des points du nuage et seront tirées des nombres de la premiere colonne du fichier et le second fichier qui regroupera les nombres de la deuxieme colonne representera les ordonnées des points du nuage.

-La troisième trace_nuage() prenant un argument de type chaîne de caractères, représentant le nom d'un fichier. Ce fichier sera supposé contenir les coordonnées des points d'un nuage obtenus grace à la fonction lit_fichier(). Ensuite elle tracera un nuage points ou chaque points sera tracé sous forme de ligne de faible epaissaur ( widht=2) et dont les points aux extremités sont tres proches pouvant ainsi etre confondu à un point.
Enfin, elle renverra le nombre de points
dessinés dans le canvas.

-Et en le dernière fonction de cette partie nommée trace_droite()...................................



La deuxième partie de notre projet qui permet maintenant de faire de scalculs statistiques est composée de:
- la fonction moyenne() qui calcule tout simplement la moyenne d'une serie statistique en se referant la formule mathématiques connu de tous (la somme de tous les nombres de la série divisé par le nombre total de nombre de la série) et ensuite retourne cette valeur.

- la fonction variance() qui permet de calculer la variance d'une serie statistique. Elle appelle la fonction moyenne() recupere la valeur de la moyenne l'affecte à une variable et procede au calcul grace à une boucle. A la fin on retourne la valeur de la vraince

- la fonction covariance() qui recupere les moyennes de deux series differentes et calcule la covariance entre les deux series. Cette valeur est retourné par la fonction à la fin.

- la fonction correlation(): elle recupere la covariance et la variance de deux series diffenrentes et calcule le coefficient de correlation puis retourne la valeur de ce dernier.

- La fonction fortecorrelation() qui regarde si les deux series differrentes sot fortement liés ou pas. Pour ca elle recupere le coefficient de correlation  puis grace à une boucle verifie si ce dernier est superieur à 0.8 ou inferieur à -0.8(donc proche de -1 et 1 ) ou pas.

 -Et enfin la fonction droite_reg() qui tracera sur le canvas la droite de regession.



 Dans la derniere partie de notre projet qui est considérée comme le programme principal nosu avons crée:
 -lancer l'ouverture d'une fenetre 
 -creer un canvas
 -creer des bouttons chacun avec des fonctions differrentes