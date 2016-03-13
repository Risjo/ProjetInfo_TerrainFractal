# -*- coding: utf-8 -*-

from paysage import Paysage
from numpy import zeros

#Initialisation
som_gauche = (0, 0)
som_droit = (1, 0)
hauteur = 1
som_milieu = (0.5, hauteur)

paysage = Paysage(som_gauche, som_milieu, som_droit)


def main():
    nbre_coupe = ''
    while not nbre_coupe.isnumeric():
        nbre_coupe = input("Combien d'itération voulez-vous effectuer ?")

    points = zeros((2**(nbre_coupe+1)+1, 2**(nbre_coupe+1)+1,))
