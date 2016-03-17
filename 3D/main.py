# -*- coding: utf-8 -*-

from paysage_triangulaire import Paysage
from sommet import Sommet

#Initialisation


def main():
    paysage = Paysage(Sommet(0,0,0),Sommet(1,0,0),Sommet(0,1,0))
    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")
    for i in range(int(nbre_coupe)):
        paysage.ajoutersommets()
    paysage.save("paysage3D.gnuplot")

    return

main()