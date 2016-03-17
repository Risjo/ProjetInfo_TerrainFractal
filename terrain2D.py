# -*- coding: utf-8 -*-
from sommet2D import Sommet2D


class Terrain2D(object):
    """Classe représentant un terrain en 2D. Le-dit terrain peut-être "affiné", c'est-à-dire que l'on peut itérer dessus
    pour avoir à partir d'un terrain donné, le même avec une itération de découpage en plus. De plus, une méthode permet
    de le sauvegarder dans un fichier.
    """

    def __init__(self, som_gauche, som_milieu, som_droit):
        """Génére un terrain en 2D à partir de trois sommets : som_gauche, som_milieu et som_droit.
        """

        self.liste_sommets = Sommet2D([som_gauche, som_milieu, som_droit])

    def affine(self, bruit, division):
        """Découpe chaque segment du paysage en créant un nouveau sommet entre chaque sommet.
        """

        som = self.liste_sommets
        while som is not None and som.next is not None:
            som.creer_sommet(bruit, division)
            som = som.next.next

    def save(self, nom_fichier):
        """sauvegarde l'état actuel du paysage dans le fichier texte nom_fichier.
        """

        with open(nom_fichier, 'w') as f:
            som = self.liste_sommets
            while som is not None:
                f.write(str(som))
                f.write("\n")
                som = som.next

    def __str__(self): #TODO
        string = ""
        for sommet in self.liste_sommets:
            string+= str(sommet) +"\n"
        return string

if __name__ == "__main__":
    #TODO
    print("tests à faire")