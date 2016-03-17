# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:23:52 2016

@author: tilletjo
"""

class Sommet :
    """point de la simulation. avec une série de méthode le rendant plus facile à manipuler"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, som2):
        """on définit une notion d'addition pour le point"""
        return Sommet(self.x + som2.x, self.y + som2.y, self.z + som2.z)

    def __sub__(self, som2):
        """on fait de même avec la soustraction"""
        return Sommet(self.x - som2.x, self.y - som2.y, self.z - som2.z)

    def __mul__(self, c):
        """on fait de même avec la multicplication avec un scalaire"""
        return Sommet(self.x * c, self.y * c, self.z * c)

    def dist(self,som2):
        """on renvoie la distance au sol entre deux points"""
        return ((self.x-som2.x)**2+(self.y-som2.y)**2)**(1/2)

    def __div__(self, c):
        """on définit la division avec un scalaire"""
        assert c != 0
        return Sommet(self.x / c, self.y / c, self.z / c)

    def __str__(self):
        """le print permet d'ecrire le texte finale et à débuguer"""
        return str(self.x) + " " + str(self.y) + " " + str(self.z)


if __name__ == "__main__":
    print("tests à faire")
    Sommet1 = Sommet(1,0,0)
    Sommet2 = Sommet(0,1,0)
    Sommet3 = Sommet(0,0,1)
    print(Sommet1+Sommet2*3)
    print(Sommet3-Sommet1/2)
