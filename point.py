# -*- coding: utf-8 -*-


class Point():
    
    def __init__(self, x, y, z = None) :
        self.__x = x
        self.__y = y
        self.__z = z
        
        self.__est_3D = self.__z is not None
        
    def __add__(self, other) :
        assert self.__est_3D == other.__est_3D
        
        if self.__est_3D :
            return Point(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)
        else :
            return Point(self.__x + other.__x, self.__y + other.__y)
            
    def __sub__(self, other) :
        assert self.__est_3D == other.__est_3D
        
        if self.__est_3D :
            return Point(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)
        else :
            return Point(self.__x - other.__x, self.__y - other.__y)
    
    def __mul__(self, const) :
        if self.__est_3D :
            return Point(self.__x * const, self.__y * const, self.__z * const)
        else :
            return Point(self.__x * const, self.__y * const)
            
        
    def __str__(self):
        if self.__est_3D :
            return str(self.__x) + ' ' + str(self.__y) + ' ' + str(self.__z)
        else :
            return str(self.__x) + ' ' + str(self.__y)
            
            

if __name__ == "__main__":
    p1 = Point(1,1)
    p2 = Point( -5,1)
    
    p3 = Point(2,3,2)
    p4 = Point(0,-1,3)
    
    print('p1 = ' + str(p1))
    print('p2 = ' + str(p2))
    print('p3 = ' + str(p3))
    print('p4 = ' + str(p4))
    
    print('p1 + p2 = ' + str(p1 + p2))
    print('p1 - p2 = ' + str(p1 - p2))
    print('p1 * 3 = ' + str(p1 * 3))
    
    print('p3 + p4 = ' + str(p3 + p4))
    print('p3 - p4 = ' + str(p3 - p4))
    print('p3 * 3 = ' + str(p3 * 3))