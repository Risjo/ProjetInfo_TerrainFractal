# -*- coding: utf-8 -*-


#Initialisation

class Paysage:
    def __init__(self,som_gauche,som_milieu,som_droit):
        self.liste_sommets = [som_gauche,som_milieu,som_droit]
        self.liste_triangles = [Segment(som_gauche,som_milieu),Segment(som_milieu,som_droit)]

    def ajoutersommets(self):
        nouvliste_triangles = []
        for triangle in self.liste_triangles:
            (nouvsommet,triangle1,triangle2,triangle3)= triangle.creer_sommet()
            nouvliste_triangles += [triangle1,triangle2,triangle3]
            self.liste_sommets.append(nouvsommet)
        self.liste_triangles = nouvliste_triangles
        return True

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

def main():
    nbre_coupe = input("Combien d'itération voulez-vous effectuer ? ")

    for i in range(int(nbre_coupe)):
        paysage.ajoutersommet()
    paysage.save("paysage.gnuplot")

    return True