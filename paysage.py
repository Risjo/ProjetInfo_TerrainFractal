# -*- coding: utf-8 -*-

from generation_terrain import *
from creer_ciel import *
from ajoute_cours_eau import *
from abc import ABCMeta, abstractmethod

class Paysage(object):
    """
    Génération de terrain et ajout de décors (cours d'eau, ciel)
    """

    def __init__(self, dimension, nb_iteration, type_bruit, type_division):
        """
        Constructeur du terrain. Appelle les bonnes classes en fonction de si l'on souhaite un terrain en 2D ou en 3D,
        du nombre d'itérations, du type de bruit et de la méthode de division.
        Le terrain en lui-même est stocké dans self.__terrain.
        Le cours d'eau est dans self.__cours_eau et le ciel dans self.__ciel.
        """
        if dimension == '2D':
            self.__terrain = Gen_2D().generate(nb_iteration, type_bruit, type_division)
            self.__cree_ciel = Cree_2D()
            self.__aj_cours = Ajoute_2D()

        else : #dimension == '3D'
            self.__terrain = Gen_3D().generate(type_bruit, type_division)
            self.__cree_ciel = Cree_3D()
            self.__aj_cours = Ajoute_3D()

        self.__cours_eau = None
        self.__ciel = None


    def genere_decors(self):
        """
        Ajoute un ciel et un cours d'eau au terrain actuel.
        """
        self.__cree_ciel.creer(self.__terrain)
        self.__aj_cours.ajoute(self.__terrain)

    def __str__(self):
        # TODO
        """
        :return:
        """
        pass

if __name__ == "__main__":
    #TODO
    print("tests à faire")