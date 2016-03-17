# -*- coding: utf-8 -*-

from Chunk import Chunk

class Paysage(object):
    def __init__(self,sommsupg,sommsupd,somminfg,somminfd):
        self.root = Chunk(sommsupg,sommsupd,somminfg,somminfd,0)
        self.terrain = [[self.root]]

    def develloper(self):
        taille = len(self.terrain)
        nouveauterrain = [[]*(2*taille)]*(2*taille)
        for i in taille:
            for j in taille:
                self.terrain[i][j].creerfils
                nouveauterrain[i*2][j*2] = self.terrain[i][j].filssupg
                nouveauterrain[i*2][j*2+1] = self.terrain[i][j].filssupd
                nouveauterrain[i*2+1][j*2] = self.terrain[i][j].filsinfg
                nouveauterrain[i*2+1][j*2+1] = self.terrain[i][j].filsinfd
        self.terrain = nouveauterrain

    def creer_la_matrice(self):
        taille = len(self.terrain)
        matrice = [[]*(2*(taille+1)+1)]*(2*(taille+1)+1)
        for i in range(taille):
            for j in range(taille):
                matrice[i*2][j*2] = self.terrain[i][j].sommsupg
                matrice[i*2][j*2+1] = self.terrain[i][j].arrsup
                matrice[i*2+1][j*2] = self.terrain[i][j].arrg
                matrice[i*2+1][j*2+1] = self.terrain[i][j].millieu
            matrice[i*2][j*2+2] = self.terrain[i][j].sommsupd
            matrice[i*2+1][j*2+2] = self.terrain[i][j].arrd
        for k in range(taille):
            matrice[2*taille+2][taille] = self.terrain[taille][k].somminfg
            matrice[2*taille+2][taille+1] = self.terrain[taille][k].arrinf
        matrice[2*taille+2][2*taille+2] = self.terrain[taille][taille].somminfd
        return matrice
