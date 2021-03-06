# -*- coding: utf-8 -*-
from numpy import *
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

        self.filsinfg= None
        self.filsinfd= None
        self.filssupg= None
        self.filssupd= None

    def generer_millieu(self):
        bruit = (2*random() - 1)*(1/self.taille)
        moyenne = (self.somminfd+self.somminfg+self.sommsupg+self.sommsupd)/4
        self.millieu = bruit+moyenne

    def generer_arrete_g(self):
        if self.voisingauche == None:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg)/3
            self.arrg=bruit+moyenne
        else:
           self.arrg= self.voisingauche.arrd

    def generer_arrete_d(self):
        if self.voisindroite == None:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfd+self.sommsupd)/3
            self.arrd = bruit+moyenne
        else:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.millieu+self.somminfg+self.sommsupg+self.voisindroite.millieu)/4
            self.arrsud = bruit+moyenne

    def generer_arrete_superieure(self):
        if self.voisinhaut == None:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.millieu+self.sommsupg+self.sommsupd)/3
            self.arrsup = bruit+moyenne
        else:
            self.arrsup= self.voisinhaut.arrinf

    def generer_arrete_inferieure(self):

        if self.voisinbas != None:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.somminfd+ self.somminfg+ self.voisinbas.milieu+self.millieu)/4
            self.arrinf= bruit+moyenne

        else:
            bruit= (2*random() - 1)*(1/self.taille)
            moyenne = (self.millieu+self.sommsupg+self.sommsupd)/3
            self.arrinf=bruit+moyenne

    def generer_contour(self):
        self.generer_arrete_g()
        self.generer_arrete_d()
        self.generer_arrete_superieure()
        self.generer_arrete_inferieure()

    def __str__(self):
        matrice= full((3,3),0)
        matrice[0][0]  =self.sommsupg
        matrice[0][1] = self.arrsup
        matrice[0][2] = self.sommsupd
        matrice[1][0] = self.arrg
        matrice[1][1] = self.millieu
        matrice[1][2] = self.arrd
        matrice[2][0] = self.somminfg
        matrice[2][1] = self.arrinf
        matrice[2][2] = self.somminfd
        return str(matrice)


    def diviser(self):
        self.filsinfd= Chunk(self.millieu,self.arrd,self.arrinf,self.somminfd,self.taille+1)
        self.filsinfg= Chunk(self.arrg, self.millieu,self.somminfg,self.arrinf,self.taille+1)
        self.filssupd= Chunk(self.arrsup, self.sommsupd,self.millieu,self.arrd,self.taille+1)
        self.filssupg= Chunk(self.sommsupg, self.arrsup,self.arrg,self.millieu,self.taille+1)

        self.filsinfd.voisingauche = self.filsinfg
        self.filsinfg.voisindroite = self.filsinfd
        self.filssupd.voisingauche = self.filssupg
        self.filssupg.voisindroite = self.filssupd

        self.filssupd.voisinbas = self.filsinfd
        self.filssupg.voisinbas = self.filsinfg
        self.filsinfd.voisinhaut = self.filssupd
        self.filsinfg.voisinhaut = self.filssupg

        if self.voisinhaut != None:
            self.filssupg.voisinhaut = self.voisinhaut.filsinfg
            self.voisinhaut.filsinfg.voisinbas = self.filssupg.voisinhaut
            self.filssupd.voisinhaut = self.voisinhaut.filsinfd
            self.voisinhaut.filsinfd.voisinbas = self.filssupd.voisinhaut

        if self.voisingauche != None:
            self.filssupg.voisingauche = self.voisingauche.filssupd
            self.voisingauche.filssupd.voisindroite = self.filssupg
            self.filsinfg.voisingauche = self.voisingauche.filsinfd
            self.voisingauche.filssupd.voisindroite = self.somminfg