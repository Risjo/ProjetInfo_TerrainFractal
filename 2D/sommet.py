# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:23:52 2016

@author: tilletjo
"""

from random import random

class Sommet :
    def __init__(self, init=[]):
        if init == []:
            self.x, self.h = None, None
            self.next = None
        else:
            self.x, self.h = init[0]
            if init[1:] != []:
                self.next = Sommet(init[1:])
            else:
                self.next = None

    def creer_sommet(self, fraction): #self.next is not None
        abscisse_decoupe = self.x + (self.next.x - self.x) * fraction
        bruit = (2 * random() - 1) * (abs(self.next.x - self.x))
        save = self.next
        self.next = Sommet([(abscisse_decoupe, (self.h + self.next.h)/2 + bruit)])
        self.next.next = save

    def __str__(self):
        return str(self.x) + " " + str(self.h)


if __name__ == "__main__":
    print("tests à faire")
    