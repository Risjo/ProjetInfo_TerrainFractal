# -*- coding: utf-8 -*-

from random import random

class Sommet2D(object) :
    """Classe représentant une liste (doublement) chaînée de sommets.
    """

    def __init__(self, init=[], prev=None):
        """Créé un sommet (composé de deux coordonnées : son abscisse x et sa hauteur h).
        Si le paramètre init contient plusieurs tuples (donc plusieurs sommets), tous les sommets sont créés et sont
        chaînés entre eux dans l'ordre dans lequel ils étaient dans la liste init.
        """

        if init == []: # Créé un sommet vide.
            self.x, self.h = None, None
            self.next = None
            self.prev = prev
        else:
            self.x, self.h = init[0]
            self.prev = prev
            if init[1:] != []:
                self.next = Sommet2D(init[1:], self)
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
        self.next = Sommet2D([(abscisse_decoupe, (self.h + self.next.h)/2 + bruit)], self)
        self.next.next = save
        self.next.next.prev = self.next

    def pente(self):
        """Retourn la pente entre le sommet actuel et le suivant.
        Le sommet suivant doit exister
        """
        assert self.next is not None

        return (self.next.h - self.h) / (self.next.x - self.x)

    def __str__(self):
        """Retourne la chaîne de caractère contenant les deux coordonnées du sommet.
        """
        return str(self.x) + " " + str(self.h)


if __name__ == "__main__":
    som1 = Sommet2D([(1,1)])
    som2 = Sommet2D([(0,-5), (1,-3), (3,4)])

    print("som1 = " + str(som1))

    print("som2 = ")
    som = som2
    while som is not None:
        print(som)
        som = som.next

    print("Pente de som2 = " + str(som2.next.pente()))

    print("Ajout d'un nouveau sommet à som2.next...")
    som2.next.creer_sommet(1,1)

    print("som2 = ")
    som = som2
    while som is not None:
        print(som)
        som = som.next





