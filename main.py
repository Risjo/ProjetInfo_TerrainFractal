# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:41:38 2016

@author: tilletjo
"""

from sommet import Sommet
from paysage import Paysage

#Initialisation
som_gauche = Sommet(0, 0)
som_droit = Sommet(1, 0)
hauteur = 1
som_milieu = Sommet(0.5, hauteur)

paysage = Paysage(som_gauche, som_milieu, som_droit)

fraction = 0.5

def main():
    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")
    for i in nbre_coupe:
        paysage.affine(fraction)

    paysage.save("paysage.gnuplot")

    return True

main()