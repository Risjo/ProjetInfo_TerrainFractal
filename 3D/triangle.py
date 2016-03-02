# -*- coding: utf-8 -*-
from math import sqrt
from sommet import Sommet


class Triangle:
    def __init__(self, som1, som2, som3):
        self.som1 = som1
        self.som2 = som2
        self.som3 = som3

    def aire_projetee(self):
        a = (self.som2.x - self.som1.x)**2 + (self.som2.y - self.som1.y)**2)**(1/2)
        b = (self.som3.x - self.som2.x)**2 + (self.som3.y - self.som2.y)**2)**(1/2)
        c = (self.som3.x - self.som1.x)**2 + (self.som3.y - self.som1.y)**2)**(1/2)

        s = 1/2 * (a + b + c)

        return sqrt(s*(s-a)*(s-b)*(s-c))


    def creer_sommet(self):
        vec = self.trouve_milieu()
        bruit = Sommet(0, 0, (2 * random() - 1) * self.aire_projetee())
        return vec + bruit

    def trouve_milieu(self):
        return Sommet((self.som1.x + self.som2.x + self.som3.x) / 3, (self.som1.y + self.som2.y + self.som3.y) / 3, (self.som1.z + self.som2.z + self.som3.z) / 3)

    def __str__(self):
        return str("Triangle définit par les trois sommets suivants : ") + str(self.som1) + str(self.som2) + str(self.som3)

