# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 11:41:38 2016

@author: tilletjo
"""

from paysage import Paysage

#Initialisation
som_gauche = (0, 0)
som_droit = (1, 0)
hauteur = 1
som_milieu = (0.5, hauteur)

paysage = Paysage(som_gauche, som_milieu, som_droit)

#On découpe les segments au milieu systématiquement
fraction = 0.5

def main():
    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")

    for i in range(int(nbre_coupe)):
        paysage.affine(fraction) # Découpe chaque segments du paysage en deux segments
    paysage.save("new_paysage.gnuplot") #Sauvegarde le paysage dans un fichier texte sous forme de coordonnées successives.

    return

main()