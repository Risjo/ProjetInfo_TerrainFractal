# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:23:52 2016

@author: tilletjo
"""

class Sommet :
    def __init__(self, x, h):
        self.x = x
        self.h = h
    def __add__(self, som2):
        return Sommet(self.x + som2.x, self.h + som2.h)
    def __sub__(self, som2):
        return Sommet(self.x - som2.x, self.h - som2.h)
    def mul(self, c):
        return Sommet(self.x * c, self.h * c)
    def div(self, c):
        assert c != 0
        return Sommet(self.x / c, self.h / c)
    def __str__(self):
        return str(self.x) + " " + str(self.h)
        
        
if __name__ == "__main__":
    s1 = Sommet(0,0)
    s2 = Sommet(5,-7)
    print("s1 = " + str(s1))
    print("s2 = " + str(s2))
    print("s1 + s2 = " + str(s1 + s2))
    print("s1 - s2 = " + str(s1 - s2))
    print("s2 * 2 = " + str(s2.mul(2)))
    print("s2 / 3 = " + str(s2.div(3)))
    