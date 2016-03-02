# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:23:52 2016

@author: tilletjo
"""

class Sommet :
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, som2):
        return Sommet(self.x + som2.x, self.y + som2.y, self.z + som2.z)

    def __sub__(self, som2):
        return Sommet(self.x - som2.x, self.y - som2.y, self.z - som2.z)

    def mul(self, c):
        return Sommet(self.x * c, self.y * c, self.z * c)

    def div(self, c):
        assert c != 0
        return Sommet(self.x / c, self.y / c, self.z / c)

    def __str__(self):
        return str(self.x) + " " + str(self.y) + " " + str(self.z)


if __name__ == "__main__":
    print("tests à faire")
