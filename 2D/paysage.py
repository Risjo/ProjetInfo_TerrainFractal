from segment import Segment


class Paysage:
    def __init__(self,som_gauche,som_milieu,som_droit):
        self.liste_sommets = [som_gauche,som_milieu,som_droit]
        self.liste_segments = [Segment(som_gauche,som_milieu),Segment(som_milieu,som_droit)]

    def affine(self,fraction=1/2):
        self.update_liste_sommets(fraction)
        self.update_liste_segements()

    def update_liste_sommets(self,fraction):
        self.liste_sommets = []
        for seg in self.liste_segments:
            self.liste_sommets += [seg.som1,seg.creer_sommet(fraction)]
        self.liste_sommets.append(self.liste_segments[-1].som2)

    def update_liste_segements(self):
        self.liste_segments = []
        for i in range(len(self.liste_sommets)-1):
            self.liste_segments.append(Segment(self.liste_sommets[i],self.liste_sommets[i+1]))

    def __str__(self):
        string = ""
        for sommet in self.liste_sommets:
            string+= str(sommet) +"\n"
        return string

    def save(self, nom_fichier):
        with open(nom_fichier, 'w') as f:
            for som in self.liste_sommets:
                f.write(str(som))
                f.write("\n")