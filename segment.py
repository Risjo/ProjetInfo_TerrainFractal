# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:32:28 2016

@author: tilletjo
"""

from random import random
from sommet import Sommet

class Segment:
    def __init__(self, som1, som2):
        self.som1 = som1
        self.som2 = som2
    def longueur(self):
        return ((self.som2.x - self.som1.x)**2 + (self.som2.h - self.som1.h)**2)**(1/2)
    def pente(self):
        return (self.som2.h - self.som1.h) / (self.som2.x - self.som1.x)
    def creer_sommet(self, fraction):
        vec = (self.som2 - self.som1).mul(fraction)
        bruit = Sommet(0, (2 * random() - 1) * (abs(self.som2.x - self.som1.x)))
        return self.som1 + vec + bruit
    def __str__(self):
        return str("Segment définit par les deux sommets suivants : ") + str(self.som1) + str(self.som2)
        
    
if __name__ == "__main__":
    s1 = Sommet(3,4)
    s2 = Sommet(5,-7)
    s3 = Sommet(8,-1)
    seg1 = Segment(s1, s2)
    seg2 = Segment(s1, s3)
    seg3 = Segment(s2, s3)
    print(seg1, seg2, seg3)
    print(seg1.nouveau_sommet(1/2))
    
    
        
        
        
        