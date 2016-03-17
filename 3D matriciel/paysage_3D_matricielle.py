# -*- coding: utf-8 -*-

from Chunk import Chunk
from numpy import full

class Paysage(object):
    def __init__(self,sommsupg,sommsupd,somminfg,somminfd):
        self.root = Chunk(sommsupg,sommsupd,somminfg,somminfd,1)
        self.terrain = [[self.root]]

    def developper(self):
        taille = len(self.terrain)
        nouveauterrain = [[None]*(2*taille)]*(2*taille)
        for i in range (0,taille):
            for j in range(0, taille):
                self.terrain[i][j].diviser()
                nouveauterrain[i*2][j*2] = self.terrain[i][j].filssupg
                nouveauterrain[i*2][j*2+1] = self.terrain[i][j].filssupd
                nouveauterrain[i*2+1][j*2] = self.terrain[i][j].filsinfg
                nouveauterrain[i*2+1][j*2+1] = self.terrain[i][j].filsinfd
        self.terrain = nouveauterrain

    def generer_nouveaux_millieux(self):
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain)):
                self.terrain[i][j].generer_millieu()

    def generer_nouveaux_contours(self):
        for i in range(len(self.terrain)):
            for j in range(len(self.terrain)):
                self.terrain[i][j].generer_contour()


    def creer_la_matrice(self):
        taille = len(self.terrain)
        matrice = full((taille*2+1,taille*2+1),None)
        for i in range(taille):
            for j in range(taille):
                matrice[i*2][j*2]=self.terrain[i][j].sommsupg
                matrice[i*2][j*2+1]=self.terrain[i][j].arrsup
                matrice[i*2+1][j*2]= self.terrain[i][j].arrg
                matrice[i*2+1][j*2+1]= self.terrain[i][j].millieu
            matrice[i*2][taille*2]= self.terrain[i][j].sommsupd
            matrice[i*2+1][taille*2]= self.terrain[i][j].arrd
        for k in range(taille):
            matrice[2*taille][2*k] = self.terrain[taille-1][k].somminfg
            matrice[2*taille][2*k+1] = self.terrain[taille-1][k].arrinf
        matrice[2*taille][2*taille] = self.terrain[taille-1][taille-1].somminfd
        return matrice
