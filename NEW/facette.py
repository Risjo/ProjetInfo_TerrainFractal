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
        """Retourne le 'milieu' de la facette (en fonction de la valeur de la fraction pour la 2D)"""
        if self.liste_points[0].est_3D :
            milieu = Point(0, 0, 0)
            for p in self.liste_points:
                milieu += p
            milieu *= 1 / self.__nb_points

        else :
            milieu = abs((self.liste_points[1] - self.liste_points[0])) * fraction + self.liste_points[0].min(self.liste_points[1])

        return milieu


    def distance_caracteristique(self):
        max = self.liste_points[0].distance(self.liste_points[1])
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
        print(milieu, dist_carac)
        if milieu.est_3D:
            bruit = Point(0, 0, (random()-0.5) * dist_carac**puiss)
        else :
            bruit = Point(0, (random()-0.5) * dist_carac**puiss)

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

if __name__ == "__main__":
    f = Facette([Point(0,0), Point(1,0)])
    print(f)
    print(f.trouve_milieu(0.7))
    print(f.distance_caracteristique())
    f.subdivise(1,0.7)
    for fils in f.fils:
        fils.subdivise(1,0.7)

    for fils in f.fils:
        for fi in fils.fils:
            print(fi)

