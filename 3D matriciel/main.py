# -*- coding: utf-8 -*-

from paysage import Paysage

#Initialisation
paysage = Paysage([[0,0,0],[0,1,0],[0,0,0]])

def main():
    nbre_coupe = ''
    while not nbre_coupe.isnumeric():
        nbre_coupe = input("Combien d'itération voulez-vous effectuer ?")

    for i in range(int(nbre_coupe)):
        paysage.affine()

    paysage.save("paysage3D_mat.gnuplot")

    return

main()
