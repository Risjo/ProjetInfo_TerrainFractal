# -*- coding: utf-8 -*-

from paysage import *

def main():

    dimension = ''
    while not (dimension == '2D' or dimension == '3D'):
        dimension = input("Dans quelle dimension voulez-vous générer le terrain ? (Entrez '2D' ou '3D')")

    print("Méthodes de découpe disponibles :")
    print("1. Moitié du segment")
    print("2. Tiers du segment")
    print("3. Cinquième du segment")
    print("4. Fraction aléatoire du segment")
    methode = ''
    while not methode.isnumeric() or not int(methode) in {1,2,3,4}:
        methode = input("Quelle méthode de découpe voulez-vous utiliser ? (Entrez un nombre entre 1 et 4 compris)")

    print("\n")
    print("Bruits possibles :")
    print("1. Dépendant de la longueur du segment")
    print("2. Dépendant du carré de la longueur du segment")
    print("3. Dépendant de la racine de la longueur du segment")
    print("\n")
    bruit = ''
    while not bruit.isnumeric() or not int(bruit) in {1,2,3}:
        bruit =  input("Quel type de bruit voulez-vous avoir ? (Entrez un nombre entre 1 et 3 compris)")

    print("\n")
    nbre_coupe = ''
    while not nbre_coupe.isnumeric():
        nbre_coupe = input("Combien d'itération voulez-vous effectuer ?")


    paysage = Paysage(dimension, int(nbre_coupe), int(bruit), int(methode))

    return

main()