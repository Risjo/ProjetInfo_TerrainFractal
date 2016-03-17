# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AjouteCoursEau(metaclass=ABCMeta):#TODO
    """Classe abstraite pour rajouter un cours d'eau à un terrain en 2D ou en 3D.
    """

    @abstractmethod
    def ajoute(self, paysage):
        """Méthode permettant de rajouter le cours d'eau à paysage.
        """

        pass


class Ajoute_2D(AjouteCoursEau):
    """Ajoute le cours d'eau à un terrain en 2D.
    """

    def sommet_voisin_min(self, sommet):
        """Retourn le sommet voisin où l'eau ira naturellement, c'est-à-dire le plus bas. Si les deux voisins sont
        plus hauts que le sommet actuel, ou que le cours d'eau est arrivé au bord du terrain, le sommet renvoyé est le
        même sommet que celui entré en argument dans la fonction.
        """

        if sommet.next is None :
            return sommet

        pente_gauche = - sommet.prev.pente()
        pente_droite = sommet.pente()

        if pente_gauche >= 0 and pente_droite >=0 :
            return sommet

        if pente_gauche > pente_droite :
            return sommet.next

        else :
            return sommet.prev

    def ajoute(self, paysage):
        """Rajoute à la liste paysage.__cours_eau une liste de sommets par lesquels passera un nouveau cours d'eau.
        """

        som_max = paysage.trouve_sommet_max()
        liste_sommets = [som_max]
        som_suivant = self.sommet_voisin_min(som_max)

        while som_suivant != liste_sommets[-1]:
            liste_sommets.append(som_suivant)
            som_suivant = self.sommet_voisin_min(som_suivant)

        paysage.__cours_eau.append(liste_sommets)


class Ajoute_3D(AjouteCoursEau):
    """Ajoute le cours d'eau à un terrain en 3D.
    """

    def ajoute(self, paysage):
        pass


