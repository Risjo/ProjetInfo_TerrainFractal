# -*- coding: utf-8 -*-

from terrain2D import Terrain2D
from abc import ABCMeta, abstractmethod

class GenerationTerrain(metaclass=ABCMeta):
    """Com
    """
    @abstractmethod
    def generate(self, nb_iteration, type_bruit, type_division):
        """
        :return:
        """
        pass


class Gen_2D(GenerationTerrain):
    """

    """
    def generate(self, nb_iteration, type_bruit, type_division):
        #Initialisation
        som_gauche = (0, 0)
        som_droit = (1, 0)
        hauteur = 1
        som_milieu = (0.5, hauteur)

        terrain = Terrain2D(som_gauche, som_milieu, som_droit)

        for i in range(int(nb_iteration)):
            terrain.affine(type_bruit, type_division) # Découpe chaque segments du paysage en deux segments
        terrain.save("new_paysage.gnuplot") #Sauvegarde le paysage dans un fichier texte sous forme de coordonnées successives.

        return



class Gen_3D(GenerationTerrain):
    """

    """
    def generate(self, nb_iteration, type_bruit, type_division):
        pass

