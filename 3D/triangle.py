# -*- coding: utf-8 -*-

from sommet import Sommet
from random import random

class Triangle:
    def __init__(self, som1, som2, som3):
        self.som1 = som1
        self.som2 = som2
        self.som3 = som3

    def aire_projetee(self):
        """on calcule l'air au sol du triangle. On utilise pour cela la formule de Héron"""
        a=self.som1.dist(self.som2)
        b=self.som2.dist(self.som3)
        c=self.som3.dist(self.som1)
        p = (a+b+c)/2
        return ((p*(p-a)*(p-b)*(p-c))**(1/2))

    def creer_sommet(self):
        """le triangle crée un nouveau sommet en son centre. Le bruit dépend de la surface au sol du triangle"""
        vec = self.trouve_milieu()
        bruit = Sommet(0, 0, (2 * random() - 1)*self.aire_projetee()*1)
        nouveausommet=  vec + bruit
        triangle1 =Triangle(self.som1,self.som2,nouveausommet)  #On crée les traingles associé au nouveau points
        triangle2 =Triangle(self.som1,self.som3,nouveausommet)
        triangle3 =Triangle(self.som2,self.som3,nouveausommet)
        return (nouveausommet,triangle1,triangle2,triangle3) #Renvoie le sommet ainsi crée et les trois triangles fils dont il est l'un des sommets

    def trouve_milieu(self):
        """renvoie le milieu du triangle"""
        return Sommet((self.som1.x + self.som2.x + self.som3.x) / 3, (self.som1.y + self.som2.y + self.som3.y) / 3, (self.som1.z + self.som2.z + self.som3.z) / 3)

    def __str__(self):
        """utile au débug"""
        return str("triangle définit par les trois sommets suivants : ") + str(self.som1) +"   "+ str(self.som2) +"   " +str(self.som3)


if __name__ == "__main__":
    Sommet1 = Sommet(1,0,0)
    Sommet2 = Sommet(0,1,0)
    Sommet3 = Sommet(0,0,1)
    triangle=  Triangle(Sommet1,Sommet2,Sommet3)
    print(triangle)
    print("aire de triangle:")
    print(triangle.aire_projetee())
    print("milieu de triangle:")
    print(triangle.trouve_milieu())
    (nouveausommet,triangle1,triangle2,triangle3)=triangle.creer_sommet()
    print("nouveau sommet généré:")
    print(nouveausommet)
    print("nouveaux triangles générés:")
    print(triangle1)
    print(triangle2)
    print(triangle3)