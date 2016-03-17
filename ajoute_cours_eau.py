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

    def ajoute(self, paysage):
        pass



class Ajoute_3D(AjouteCoursEau):
    """Ajoute le cours d'eau à un terrain en 3D.
    """

    def ajoute(self, paysage):
        pass


