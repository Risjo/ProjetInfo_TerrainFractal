# -*- coding: utf-8 -*-

class Paysage():
    def __init__(self, facette = None):
        self.racine = facette

    def liste_sous_facettes(self):
        """retourne la liste des facettes qui sont le plus profond dans l'arbre."""
        if self.racine.fils == []:
            return [self.racine]
        else :
            liste = []
            for f in self.racine.fils:
                liste += Paysage(f).liste_sous_facettes()
            return liste

    def itere(self):
        """Augmente la profondeur de l'arbre de 1 en divisant toutes les facettes de profondeur maximum en
        sous-facettes."""
        for f in self.liste_sous_facettes():
            f.subdivise()