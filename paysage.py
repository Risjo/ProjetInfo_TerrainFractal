# -*- coding: utf-8 -*-

from generation_terrain import *
from creer_ciel import *
from ajoute_cours_eau import *
from abc import ABCMeta, abstractmethod

class Paysage(object):
    """

    """

    def __init__(self, dimension, nb_iteration, type_bruit, type_division):
        """

        :return:
        """
        if dimension == '2D':
            self.__terrain = Gen_2D().generate(nb_iteration, type_bruit, type_division)
            self.__cree_ciel = Cree_2D()
            self.__aj_cours = Ajoute_2D()

        else : #dimension == '3D'
            self.__terrain = Gen_3D().generate(type_bruit, type_division)
            self.__cree_ciel = Cree_3D()
            self.__aj_cours = Ajoute_3D()


    def genere_decors(self):
        """

        :return:
        """
        self.__cree_ciel.creer(self.__terrain)
        self.__aj_cours.ajoute(self.__terrain)

    def __str__(self):
        """

        :return:
        """
        pass
