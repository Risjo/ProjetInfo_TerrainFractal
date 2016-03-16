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

    for i in range(int(nbre_coupe)):
        paysage.affine(int(methode), int(bruit)) # Découpe chaque segments du paysage en deux segments
    paysage.save("new_paysage.gnuplot") #Sauvegarde le paysage dans un fichier texte sous forme de coordonnées successives.

    return

main()