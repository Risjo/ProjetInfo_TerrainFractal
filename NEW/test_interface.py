# -*- coding: utf-8 -*-

from interface import Ui_MainWindow
import sys
from PyQt4 import QtGui, QtCore
from matplotlib import cm
from matplotlib.figure import Figure
from paysage import *
from trace import trace
from numpy import array
# from point import Point
# from facette import Facette
#from cours_eau import CoursEau
from matplotlib.pyplot import show

class MonAppli(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ecopainter = QtGui.QPainter()
        self.trois_D = False
        self.nb_iter = 0
        self.fraction = 0.5
        self.puiss = 1
        self.terrain = None
        self.figure2D = self.figure3D = Figure() #figsize=(width, height), dpi=dpi
        self.cours_eau = None

        # Configuration de l'interface utilisateur.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        QtCore.QObject.connect(self.ui.actionQuitter, QtCore.SIGNAL("triggered()"), self.quit)
        QtCore.QObject.connect(self.ui.Iterations,QtCore.SIGNAL("valueChanged(int)"), self.nbIter)
        self.ui.bruit_lin.toggled.connect(self.bruitLin)
        self.ui.bruit_quadra.toggled.connect(self.bruitQua)
        self.ui.bruit_racine.toggled.connect(self.bruitRac)
        QtCore.QObject.connect(self.ui.val_fraction,QtCore.SIGNAL("valueChanged(double)"),self.frac)
        self.ui.deuxD.toggled.connect(self.deuxDim)
        self.ui.troisD.toggled.connect(self.troisDim)
        QtCore.QObject.connect(self.ui.generer_bouton,QtCore.SIGNAL("clicked()"),self.generer)

        QtCore.QObject.connect(self.ui.val_fraction, QtCore.SIGNAL("valueChanged(double)"), self.change_val_doubleSpin)
        QtCore.QObject.connect(self.ui.Fraction, QtCore.SIGNAL("valueChanged(int)"), self.change_position_slider)

        QtCore.QObject.connect(self.ui.ajouter_cours_bouton,QtCore.SIGNAL("clicked()"),self.ajoute_cours)


    def change_position_slider(self, path):
        self.ui.val_fraction.setValue(path/100)

    def change_val_doubleSpin(self, path):
        self.ui.Fraction.setSliderPosition(path*100)

    def nbIter(self, path):
        self.nb_iter = path

    def bruitLin(self):
        self.puiss = 1

    def bruitQua(self):
        self.puiss = 2

    def bruitRac(self):
        self.puiss = 1/2.

    def frac(self, path):
        self.fraction = path

    def deuxDim(self, path):
        if path:
            self.trois_D = False
        else:
            self.trois_D = True


    def troisDim(self):
        pass

    def ajoute_cours(self):
        if self.terrain is None :
            pass
        else :
            self.terrain.ajoute_cours_eau()
            cours = self.terrain.cours_eau[-1].points
            for i in range(len(cours)):
                cours[i] = (cours[i].x, cours[i].y)
            X, Y = array(cours).T
            self.ui.matplotlib.axes.plot(X,Y,'b-', linewidth=2.0)
            self.ui.matplotlib.draw()


    def generer(self):
        if self.trois_D :
            p1 = Point(0,0,0)
            p2 = Point(1,0,0)
            p3 = Point(1,1,0)
            p4 = Point(0,1,0)
            base = Facette([p1, p2, p3, p4])
            self.terrain = Paysage(base)
        else :
            p1 = Point(0,0)
            p2 = Point(1,0)
            base = Facette([p1, p2])
            self.terrain = Paysage(base)


        for i in range(self.nb_iter):
            self.terrain.itere(self.puiss, self.fraction)

        X, Y, Z = trace(self.terrain)

        self.ui.matplotlib.axes.clear()

        if len(Z) < 1 : #2D
            self.axes2D = self.figure2D.add_subplot(111)
            self.ui.matplotlib.axes.plot(X,Y,'r-')
            self.ui.matplotlib.axes.hold(True)
            self.ui.matplotlib.draw()
        else : #3D
            self.axes2D = None
            self.axes3D = self.figure3D.gca(projection='3d') #self.axes = self.figure.add_subplot(111, projection='3d')
            self.axes3D.set_axis_off()
            self.axes3D.plot_surface(X, Y, Z, cmap=cm.ocean) #ou terrain
            show()
            self.ui.matplotlib.draw()



    def quit(self):
        exit(0)



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    sys.exit(app.exec_())