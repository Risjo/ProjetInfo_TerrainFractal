# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:23:52 2016

@author: tilletjo
"""

from random import random

class Sommet2D(object) :
    """Classe représentant une liste (simplement) chaînée de sommets.
    """

    def __init__(self, init=[]):
        """Créé un sommet (composé de deux coordonnées : son abscisse x et sa hauteur h).
        Si le paramètre init contient plusieurs tuples (donc plusieurs sommets), tous les sommets sont créés et sont
        chaînés entre eux dans l'ordre dans lequel ils étaient dans la liste init.
        """

        if init == []: # Créé un sommet vide.
            self.x, self.h = None, None
            self.next = None
        else:
            self.x, self.h = init[0]
            if init[1:] != []:
                self.next = Sommet2D(init[1:])
            else:
                self.next = None

    def creer_sommet(self, br, division):
        """Créé un sommet entre self et self.next en tenant compte du bruit (paramètre br) désiré et de la méthode de
        division voulue (paramètre division).
        Condition : Le sommet doit au moins avoir un sommet suivant.
        """

        assert self.next is not None

        if division == 1:
            fraction = 1/2
        elif division == 2:
            fraction = 1/3
        elif division == 3:
            fraction = 1/5
        elif division == 4:
            fraction = random()

        abscisse_decoupe = self.x + (self.next.x - self.x) * fraction

        if br == 1 :
            bruit = (2 * random() - 1) * (abs(self.next.x - self.x))
        elif br == 2:
            bruit = (2 * random() - 1) * (abs(self.next.x - self.x))**2
        elif br == 3:
            bruit = (2 * random() - 1) * (abs(self.next.x - self.x))**(1/2)
        save = self.next
        self.next = Sommet2D([(abscisse_decoupe, (self.h + self.next.h)/2 + bruit)])
        self.next.next = save

    def __str__(self):
        #TODO
        """
        :return:
        """
        return str(self.x) + " " + str(self.h)


if __name__ == "__main__":
    #TODO
    print("tests à faire")
