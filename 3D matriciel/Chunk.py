from random import *
class Chunk(object):
    def __init__(self,sommsupg, sommsupd,somminfg,somminfd,taille):
        self.sommsupg = sommsupg
        self.sommsupd = sommsupd
        self.somminfg = somminfg
        self.somminfd = somminfd
        self.millieu = None
        self.arrg = None
        self.arrd = None
        self.arrsup = None
        self.arrinf = None
        self.taille= taille
        self.voisinhaut= None
        self.voisinbas= None
        self.voisingauche=None
        self.voisindroite=None

    def generermillieu(self):
        bruit= (2*random.int - 1)*(1/self.taille)
        moyenne = (self.somminfd+self.somminfg+self.sommsupg+self.sommsupd)/4
        self.millieu= bruit+moyenne

    def generer_arrete_g(self):
        if self.voisingauche= None:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg)/3
            self.arrg=bruit+moyenne
        else:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg+self.voisingauche.milieu)/4
            self.arrg=bruit+moyenne
    def generer_arrete_d(self):
        if self.voisindroite= None:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfd+self.sommsupd)/3
            self.arrg=bruit+moyenne
        else:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg+self.voisingauche.milieu)/4
            self.arrg=bruit+moyenne
    def generer_arrete_d(self):
        if self.voisindroite= None:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfd+self.sommsupd)/3
            self.arrg=bruit+moyenne
        else:
            bruit= (2*random.int - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg+self.voisingauche.milieu)/4
            self.arrg=bruit+moyenne