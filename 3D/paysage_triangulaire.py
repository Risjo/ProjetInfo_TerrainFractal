# -*- coding: utf-8 -*-

from triangle import Triangle
from sommet import Sommet


class Paysage:
    """classe principale regroupant l'ensemble des objet de la génération de terrain."""
    def __init__(self,som1,som2,som3):
        """on initie le paysage avec un triangle horizontale et trois sommets"""
        self.liste_sommets = [som1,som2,som3]
        self.liste_triangles = [Triangle(som1,som2,som3)]

    def ajoutersommets(self):
        """on fait générer des sommets à tout les triangles"""
        nouvliste_triangles = []
        for triangle in self.liste_triangles:
            (nouvsommet,triangle1,triangle2,triangle3)= triangle.creer_sommet()
            nouvliste_triangles += [triangle1,triangle2,triangle3]
            self.liste_sommets.append(nouvsommet)       #on rajoute les nouveaux sommets crées à la liste des sommet du paysage
        self.liste_triangles = nouvliste_triangles      #on remplace les anciens triangles par les nouveaux, plus petits"
        return True

    def __str__(self):
        """écrit la liste des sommets. Utile pour sauvegarder les données"""
        string = ""
        for sommet in self.liste_sommets:
            string+= str(sommet) +"\n"
        return string

    def save(self, nom_fichier):
        """méthode copiant les sommets dans un fichier texte exploitable par l'interface graphique"""
        with open(nom_fichier, 'w') as f:
            for som in self.liste_sommets:
                f.write(str(som))
                f.write("\n")


if __name__ == "__main__":
    paysage = Paysage(Sommet(0,0,0),Sommet(1,0,0),Sommet(0,1,0))
    print("paysage:")
    print(paysage)
    paysage.ajoutersommets()
    print("nouveaupaysage")
    print(paysage)
    paysage.save