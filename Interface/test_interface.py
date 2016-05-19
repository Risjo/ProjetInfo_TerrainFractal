# -*- coding: utf-8 -*-

from interface import Ui_MainWindow
import sys
from PyQt4 import QtGui, QtCore
from paysage import Paysage

class MonAppli(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ecopainter = QtGui.QPainter()

        # Configuration de l'interface utilisateur.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # self.ui.bouton_gen.clicked.connect(self.generer)

        # self.ui.conteneur.paintEvent = self.drawecosysteme



        # palette = QtGui.QPalette()
        # pixmap = QtGui.QPixmap("arrierPlan.png")
        # palette.setBrush(QtGui.QPalette.Background,QtGui.QBrush(pixmap))
        # self.setPalette(palette)
        # # Configuration du modèle
        # self.generer()



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    sys.exit(app.exec_())