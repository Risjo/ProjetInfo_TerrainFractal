class Paysage(object):
    def __init__(self,iteration):
        assert iteration > 0
        self.matrice = [[0]*(2**iteration+1)]*(2**iteration+1)
        self.iteration= iteration
    def generer(self):
