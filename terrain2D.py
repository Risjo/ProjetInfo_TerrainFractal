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

    def trouve_sommet_max(self):
        """Retourne le sommet ayant la plus haute altitude.
        """
        som_max = self.liste_sommets
        som = self.liste_sommets
        while som is not None:
            if som.h > som_max.h :
                som_max = som
            som = som.next
        return som_max

    def save(self, nom_fichier):
        """sauvegarde l'état actuel du paysage dans le fichier texte nom_fichier.
        """

        with open(nom_fichier, 'w') as f:
            som = self.liste_sommets
            while som is not None:
                f.write(str(som))
                f.write("\n")
                som = som.next

    def __str__(self):
        string = ""
        som = self.liste_sommets
        while som is not None :
            string+= str(som) + "\n"
            som = som.next
        return string

if __name__ == "__main__":
    terrain = Terrain2D((0,0), (1,2), (2,1))

    print(terrain)

    print("Sommet le plus haut : " + str(terrain.trouve_sommet_max()))

    print("On affine le terrain...")
    terrain.affine(1,1)

    print(terrain)

    print("Sommet le plus haut : " + str(terrain.trouve_sommet_max()))