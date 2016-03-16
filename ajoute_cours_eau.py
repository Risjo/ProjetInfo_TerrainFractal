# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class AjouteCoursEau(metaclass=ABCMeta):
    """

    """
    @abstractmethod
    def ajoute(self, paysage):
        """
        :return:
        """
        pass


class Ajoute_2D(AjouteCoursEau):
    """

    """
    def ajoute(self, paysage):
        pass



class Ajoute_3D(AjouteCoursEau):
    """

    """
    def ajoute(self, paysage):
        pass


