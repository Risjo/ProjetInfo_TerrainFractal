# -*- coding: utf-8 -*-
from facette import Facette
from point import Point
from cours_eau import CoursEau

class Paysage():
    def __init__(self, facette = None):
        self.racine = facette
        self.cours_eau = []

    def liste_sous_facettes(self):
        """retourne la liste des facettes qui sont le plus profond dans l'arbre."""
        if self.racine.fils == []:
            return [self.racine]
        else :
            liste = []
            for f in self.racine.fils:
                liste += Paysage(f).liste_sous_facettes()
            return liste

    def itere(self, puiss):
        """Augmente la profondeur de l'arbre de 1 en divisant toutes les facettes de profondeur maximum en
        sous-facettes."""
        for f in self.liste_sous_facettes():
            f.subdivise(puiss)

    def __str__(self):
        return "Arbre dont la racine est : " + str(self.racine)

    def save(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            ensemble = set()
            for facette in terrain.liste_sous_facettes():
                for p in facette.liste_points:
                    if p.est_3D :
                        ensemble.add((p.x, p.y, p.z))
                    else :
                        ensemble.add((p.x, p.y))

            for point in ensemble:
                texte = ''
                for coord in point:
                    texte += str(coord) + ' '
                f.write(texte + '\n')

    def trouve_voisins(self, point):
        if point.est_3D:
            pass

        else :
            vois1 = self.racine.liste_points[0]
            vois2 = self.racine.liste_points[-1]
            for f in self.liste_sous_facettes():
                for p in f.liste_points:
                    if p.x < point.x and abs(point.x - p.x) < abs(point.x - vois1.x):
                        vois1 = p
                    elif p.x > point.x and abs(point.x - p.x) < abs(point.x - vois1.x):
                        vois2 = p
            return vois1, vois2

    def ajoute_cours_eau(self, start = None):
        if start is None:
            start = self.racine.liste_points[0]
            for f in self.liste_sous_facettes():
                for p in f.liste_points:
                    if p.est_3D and p.z > start.z :
                        start = p
                    elif (not p.est_3D) and p.y > start.y:
                        start = p

        self.cours_eau.append(CoursEau(start, self).coule())


if __name__ == "__main__":

    p1 = Point(0,0)
    p2 = Point(1,0)
    base = Facette([p1, p2])
    terrain = Paysage(base)
    print(terrain)
    for i in range(8):
        terrain.itere(1)

    for f in terrain.liste_sous_facettes():
        print(f)
    terrain.save('test')


    p1 = Point(0,0,0)
    p2 = Point(1,0,0)
    p3 = Point(0,1,0)
    p4 = Point(1,1,0)
    base = Facette([p1, p2, p3, p4])
    terrain = Paysage(base)
    print(terrain)
    for i in range(8):
        terrain.itere(1)

    for f in terrain.liste_sous_facettes():
        print(f)
    terrain.save('test2')