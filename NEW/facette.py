# -*- coding: utf-8 -*-
from point import Point
from random import random

class Facette():
    def __init__(self, liste_points, pere = None) :
        self.liste_points = liste_points
        self.__nb_points = len(liste_points)
        self.fils = []
        self.pere = pere

    def trouve_milieu(self, fraction):
        """Retourne le milieu de la facette"""
        if self.liste_points[0].est_3D :
            milieu = Point(0, 0, 0)
            for p in self.liste_points:
                milieu += p
            milieu *= 1 / self.__nb_points

        else :
            milieu = (self.liste_points[0] + self.liste_points[1] ) * fraction

        return milieu


    def distance_caracteristique(self):
        max = self.liste_points[0].distance(self.liste_points[-1])
        for i in range(self.__nb_points - 1):
            dist = self.liste_points[i].distance(self.liste_points[i+1])
            if dist > max :
                max = dist

        return max


    def subdivise(self, puiss, fraction = 0.5):
        """Découpe une facette en sous-facettes. Ajoute les nouvelles facettes créées à la liste des fils de la facette
        originale. Pour créer ces nouvelles facettes, le milieu de la facette d'origine est trouvé, puis un bruit est
        ajouté :
            le bruit ajouté dépend de la distance caractéristique à la puissance 'puiss' de la facette.
        """
        milieu = self.trouve_milieu(fraction)
        dist_carac = self.distance_caracteristique()
        if milieu.est_3D:
            bruit = Point(0, 0, 0.5 * random() * dist_carac**puiss)
        else :
            bruit = Point(0, 0.5 * random() * dist_carac**puiss)
        milieu += bruit
        if self.__nb_points == 2:
            for f in self.liste_points:
                self.fils.append(Facette([f, milieu], self))

        else:
            for i in range(self.__nb_points - 1):
                self.fils.append(Facette([self.liste_points[i], self.liste_points[i+1], milieu], self))

    def __str__(self):
        texte = "Facette constituée des points \n"
        for p in self.liste_points :
            texte += str(p) + "\n"
        return texte

