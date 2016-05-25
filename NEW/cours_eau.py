# -*- coding: utf-8 -*-

class CoursEau():

    def __init__(self, start, paysage):
        self.points = [start]
        self.paysage = paysage

    def coule(self):

        if self.points[0].est_3D :
            pass

        else : #2D
            tolerance = 0.0001
            point_act = self.points[-1]
            vois1, vois2 = self.paysage.trouve_voisins(point_act)
            if point_act.y > vois1.y - tolerance and point_act.y > vois2.y - tolerance:
                if point_act.y - vois1.y > point_act.y - vois2.y :
                    self.points.append(vois1)
                else:
                    self.points.append(vois2)
                self.coule()
            elif point_act.y > vois1.y - tolerance:
                self.points.append(vois1)
                self.coule()
            elif point_act.y > vois2.y - tolerance:
                self.points.append(vois2)
                self.coule()

    def __str__(self):
        return str([str(p) for p in self.points])