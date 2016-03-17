# -*- coding: utf-8 -*-

from paysage_3D_matricielle import Paysage

def main():
    paysage= Paysage(0,0,0,0)
    paysage.generer_nouveaux_millieux()
    paysage.generer_nouveaux_contours()
    print(paysage.creer_la_matrice())

    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")
    for i in range(int(nbre_coupe)):
        paysage.developper()
        paysage.generer_nouveaux_millieux()
        paysage.generer_nouveaux_contours()

    matrice= paysage.creer_la_matrice()

    for i in range(len(matrice)):
        print(matrice[i])

main()
