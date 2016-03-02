# -*- coding: utf-8 -*-


#Initialisation


def main():
    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")

    for i in range(int(nbre_coupe)):
        paysage.affine(fraction)
    paysage.save("paysage.gnuplot")

    return True