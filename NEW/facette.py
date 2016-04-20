# -*- coding: utf-8 -*-
from point import Point

class Facette():
    def __init__(self, liste_points) :
        self.__liste_points = liste_points
        self.__nb_points = len(liste_points)
        self.fils = []

    def trouve_milieu(self):
        """Retourne le milieu de la facette"""
        if self.__liste_points[0].__est_3D :
            milieu = Point(0, 0, 0)
        else :
            milieu = Point(0, 0)

        for p in self.__liste_points:
            milieu += p
        milieu /= self.__nb_points

        return milieu

    def subdivise(self):
        milieu = self.trouve_milieu()
        if self.__nb_points == 2:
            for f in self.__liste_points:
                self.fils.append(Facette([f, milieu]))

        else:
            for i in range(self.__nb_points - 1):
                self.fils.append(Facette([self.__liste_points[i], self.__liste_points[i+1], milieu]))


