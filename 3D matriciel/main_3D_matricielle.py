# -*- coding: utf-8 -*-

from paysage_3D_matricielle import Paysage

def main():
    paysage= Paysage(0,0,0,0)
    paysage.terrain[0][0].generermillieu()
    paysage.terrain[0][0].generer_arrete_g()
    paysage.terrain[0][0].generer_arrete_d()
    paysage.terrain[0][0].generer_arrete_superieure()
    paysage.terrain[0][0].generer_arrete_inferieure()
    print(paysage.creer_la_matrice())

main()
