# -*- coding: utf-8 -*-

class Triangle:
    def __init__(self, som1, som2, som3):
        self.som1 = som1
        self.som2 = som2
        self.som3 = som3

    def aire_projetee(self):
        p = (self.som1.dist(self.som2)+self.som2.dist(self.som3)+self.som3.dist(self.som1))/3
        pass

    def creer_sommet(self):
        vec = self.trouve_milieu()
        bruit = Sommet(0, 0, (2 * random() - 1) )
        return vec + bruit

    def trouve_milieu(self):
        return Sommet((self.som1.x + self.som2.x + self.som3.x) / 3, (self.som1.y + self.som2.y + self.som3.y) / 3, (self.som1.z + self.som2.z + self.som3.z) / 3)

    def __str__(self):
        return str("Segment définit par les deux sommets suivants : ") + str(self.som1) + str(self.som2)

