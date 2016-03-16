# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class CreationCiel(metaclass=ABCMeta):
    """

    """
    @abstractmethod
    def creer(self, type_ciel, paysage):
        """
        :return:
        """
        pass


class Cree_2D(CreationCiel):
    """

    """
    def creer(self, paysage):
        pass



class Cree_3D(CreationCiel):
    """

    """
    def creer(self, paysage):
        pass


