# -*- coding: utf-8 -*-
from math import sqrt

class Point():
    
    def __init__(self, x, y, z = None) :
        self.__x = x
        self.__y = y
        self.__z = z
        
        self.est_3D = self.z is not None

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z
        
    def __add__(self, other) :
        assert self.est_3D == other.est_3D
        
        if self.est_3D :
            return Point(self.x + other.x, self.y + other.y, self.z + other.z)
        else :
            return Point(self.x + other.x, self.y + other.y)
            
    def __sub__(self, other) :
        assert self.est_3D == other.est_3D
        
        if self.est_3D :
            return Point(self.x - other.x, self.y - other.y, self.z - other.z)
        else :
            return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, const) :
        if self.est_3D :
            return Point(self.x * const, self.y * const, self.z * const)
        else :
            return Point(self.x * const, self.y * const)

    def __abs__(self):
        if self.est_3D :
            return Point(abs(self.x), abs(self.y), abs(self.z))
        else :
            return Point(abs(self.x), abs(self.y))

    def min(self, other):
        """Retourne le point qui a la plus petite abscisse"""
        if self.x <= other.x:
            return self
        else:
            return other

    def max(self, other):
        """Retourne le point qui a la plus grande abscisse"""
        if self.x <= other.x:
            return other
        else:
            return self

    def distance(self, other):
        """Calcule la distance euclidienne entre deux points, mais ne prend pas en compte l'altitude du point,
        car seul la distance au sol nous importe ici."""
        assert self.est_3D == other.est_3D
        if self.est_3D :
            return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
        else :
            return abs(self.x-other.x)
            
        
    def __str__(self):
        if self.est_3D :
            return str(self.x) + ' ' + str(self.y) + ' ' + str(self.z)
        else :
            return str(self.x) + ' ' + str(self.y)
            
            

if __name__ == "__main__":
    p1 = Point(1,1)
    p2 = Point( -5,1)
    
    p3 = Point(2,3,2)
    p4 = Point(0,-1,3)
    
    print('p1 = ' + str(p1))
    print('p2 = ' + str(p2))
    print('p3 = ' + str(p3))
    print('p4 = ' + str(p4))
    print()

    print('p1 est 3D ? ' + str(p1.est_3D))
    print('p3 est 3D ? ' + str(p3.est_3D))
    print()
    
    print('p1 + p2 = ' + str(p1 + p2))
    print('p1 - p2 = ' + str(p1 - p2))
    print('p1 * 3 = ' + str(p1 * 3))
    print()
    
    print('p3 + p4 = ' + str(p3 + p4))
    print('p3 - p4 = ' + str(p3 - p4))
    print('p3 * 3 = ' + str(p3 * 3))