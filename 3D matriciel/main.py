from random import random
class Paysage(object):
    def __init__(self,iteration):
        assert iteration > 0
        self.matrice = [[0]*(2**iteration+1)]*(2**iteration+1)
        self.iteration= iteration
    def generer(self):
        for i in range(self.iteration):
            for j in range(i):
                for k in range(i):
                    bruit = (2*random()-1)/2**i
                    self.matrice[1+j*2**(self.iteration-i)][1+k*-2**(self.iteration-i)]=bruit+self.matrice[j][k-2**(self.iteration-i)]+self.matrice[j-2**(self.iteration-i)][k]+self.matrice[j-2**(self.iteration-i)][k]+self.matrice[j-2**(self.iteration-i)][k-2**(self.iteration-i)]

