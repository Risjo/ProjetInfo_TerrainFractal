# -*- coding: utf-8 -*-
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from numpy import *
import operator
from paysage import *

def trace(terrain):
    """Retourne une figure matplotlib représentant le terrain généré à partir du terrain entré en paramètre.
    """

    #On récupère tous les points constituant le terrain
    ensemble = set() #On utilise la structure d'ensemble pour éviter les doublons (qui ralentiraient la génération)
    for facette in terrain.liste_sous_facettes():
        for p in facette.liste_points:
            if p.est_3D :
                ensemble.add((p.x, p.y, p.z))
            else :
                ensemble.add((p.x, p.y))

    #On les met dans des listes
    X, Y, Z = [], [], []
    for p in ensemble:
        X.append(p[0])
        Y.append(p[1])
        if len(p)==3:
            Z.append(p[2])


    if len(Z)>0: #3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_trisurf(X, Y, Z)

    else : #2D
        X,Y = array(sorted(array([X,Y]).T, key=operator.itemgetter(0))).T#Pour que le terrain s'affiche correctement en 2D,
                                                               # il faut que les points soient dans l'ordre
                                                               # croissant des abscisses.
        plt.plot(X,Y)

    return X, Y, Z
