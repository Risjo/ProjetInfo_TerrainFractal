# -*- coding: utf-8 -*-

from terrain2D import Terrain2D
from abc import ABCMeta, abstractmethod

class GenerationTerrain(metaclass=ABCMeta):
    """Classe abstraite pour les générations de terrain en 2D ou en 3D
    """

    @abstractmethod
    def generate(self, nb_iteration, type_bruit, type_division):
        """Créé un terrain en fonction du nombre d'itération, du type de bruit et de la méthode de découpe.
        Le terrain est sauvegardé dans un fichier .gnuplot.
        """
        pass


class Gen_2D(GenerationTerrain):
    """Génération du terrain en 2D.
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
    """Génération du terrain en 3D.
    """

    def generate(self, nb_iteration, type_bruit, type_division):
        pass

