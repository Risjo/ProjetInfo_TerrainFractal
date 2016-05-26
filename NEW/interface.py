# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test interface.ui'
#
# Created: Thu May 19 13:24:04 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(760,666)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.generer_bouton = QtGui.QPushButton(self.centralwidget)
        self.generer_bouton.setGeometry(QtCore.QRect(30, 560, 141, 31))
        self.generer_bouton.setObjectName(_fromUtf8("generer_bouton"))
        self.Fraction = QtGui.QSlider(self.centralwidget)
        self.Fraction.setGeometry(QtCore.QRect(500, 570, 171, 22))
        self.Fraction.setMaximum(100)
        self.Fraction.setValue(50)
        self.Fraction.setOrientation(QtCore.Qt.Horizontal)
        self.Fraction.setObjectName(_fromUtf8("Fraction"))
        self.Iterations = QtGui.QSpinBox(self.centralwidget)
        self.Iterations.setGeometry(QtCore.QRect(130, 530, 41, 22))
        self.Iterations.setObjectName(_fromUtf8("Iterations"))
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(210, 530, 111, 80))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.Dimensions = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.Dimensions.setMargin(0)
        self.Dimensions.setObjectName(_fromUtf8("Dimensions"))
        self.nb_dim_terrain = QtGui.QLabel(self.verticalLayoutWidget)
        self.nb_dim_terrain.setLineWidth(1)
        self.nb_dim_terrain.setTextFormat(QtCore.Qt.RichText)
        self.nb_dim_terrain.setObjectName(_fromUtf8("nb_dim_terrain"))
        self.Dimensions.addWidget(self.nb_dim_terrain)
        self.deuxD = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.deuxD.setObjectName(_fromUtf8("deuxD"))
        self.deuxD.setChecked(True)
        self.Dimensions.addWidget(self.deuxD)
        self.troisD = QtGui.QRadioButton(self.verticalLayoutWidget)
        self.troisD.setObjectName(_fromUtf8("troisD"))
        self.Dimensions.addWidget(self.troisD)
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(360, 530, 160, 84))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.type_bruit = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.type_bruit.setObjectName(_fromUtf8("type_bruit"))
        self.verticalLayout_2.addWidget(self.type_bruit)
        self.bruit_lin = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.bruit_lin.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bruit_lin.setObjectName(_fromUtf8("bruit_lin"))
        self.bruit_lin.setChecked(True)
        self.verticalLayout_2.addWidget(self.bruit_lin)
        self.bruit_racine = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.bruit_racine.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bruit_racine.setObjectName(_fromUtf8("bruit_racine"))
        self.verticalLayout_2.addWidget(self.bruit_racine)
        self.bruit_quadra = QtGui.QRadioButton(self.verticalLayoutWidget_2)
        self.bruit_quadra.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.bruit_quadra.setObjectName(_fromUtf8("bruit_quadra"))
        self.verticalLayout_2.addWidget(self.bruit_quadra)
        self.nb_iteration = QtGui.QLabel(self.centralwidget)
        self.nb_iteration.setGeometry(QtCore.QRect(30, 530, 101, 20))
        self.nb_iteration.setObjectName(_fromUtf8("nb_iteration"))
        self.val_frac = QtGui.QLabel(self.centralwidget)
        self.val_frac.setGeometry(QtCore.QRect(510, 550, 71, 16))
        self.val_frac.setObjectName(_fromUtf8("val_frac"))
        self.val_fraction = QtGui.QDoubleSpinBox(self.centralwidget)
        self.val_fraction.setGeometry(QtCore.QRect(590, 540, 51, 31))
        self.val_fraction.setObjectName(_fromUtf8("val_fraction"))
        self.val_fraction.setSingleStep(0.01)
        self.val_fraction.setValue(0.5)
        self.val_fraction.setMaximum(1.)
        self.val_fraction.setMinimum(0.)
        self.ajouter_cours_bouton = QtGui.QPushButton(self.centralwidget)
        self.ajouter_cours_bouton.setGeometry(QtCore.QRect(40, 600, 121, 23))
        self.ajouter_cours_bouton.setObjectName(_fromUtf8("ajouter_cours_bouton"))
        self.ajouter_cours_bouton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Génère un cours d'eau à partir du point le plus haut du terrain. Le cours s'arrête dès que le terrain remonte.</p><p>Uniquement en 2D.</p></body></html>", None))
        self.matplotlib = MatplotlibWidget(self.centralwidget)
        self.matplotlib.setGeometry(QtCore.QRect(9, 9, 741, 501))
        self.matplotlib.setObjectName(_fromUtf8("matplotlib"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName(_fromUtf8("menuFichier"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setObjectName(_fromUtf8("actionOuvrir"))
        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setObjectName(_fromUtf8("actionQuitter"))
        self.actionAjouter_Ciel = QtGui.QAction(MainWindow)
        self.actionAjouter_Ciel.setObjectName(_fromUtf8("actionAjouter_Ciel"))
        self.actionAjouter_cours_d_eau = QtGui.QAction(MainWindow)
        self.actionAjouter_cours_d_eau.setObjectName(_fromUtf8("actionAjouter_cours_d_eau"))
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionQuitter)
        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.troisD, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.val_frac.setDisabled)
        QtCore.QObject.connect(self.troisD, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.Fraction.setDisabled)
        QtCore.QObject.connect(self.troisD, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.val_fraction.setDisabled)
        QtCore.QObject.connect(self.troisD, QtCore.SIGNAL(_fromUtf8("toggled(bool)")), self.ajouter_cours_bouton.setDisabled)
        QtCore.QObject.connect(self.Fraction, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.val_fraction.clear)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Génération de terrain fractal", None))
        self.generer_bouton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Lance la génération du terrain.</p></body></html>", None))
        self.generer_bouton.setText(_translate("MainWindow", "Générer", None))
        self.nb_dim_terrain.setToolTip(_translate("MainWindow", "<html><head/><body><p>Indique si l\'on désire générer un terrain en deux dimensions ou en trois dimensions.</p></body></html>", None))
        self.nb_dim_terrain.setText(_translate("MainWindow", "Dimension du terrain :", None))
        self.deuxD.setText(_translate("MainWindow", "2D", None))
        self.troisD.setText(_translate("MainWindow", "3D", None))
        self.type_bruit.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pour la génération de terrain en 2D. Indique si le bruit généré (valeur aléatoire) dépend directement de la longueur du segment concerné (bruit linéaire) ou s\'il dépend du carré ou de la racine de cette longueur.</p></body></html>", None))
        self.type_bruit.setText(_translate("MainWindow", "Type de bruit :", None))
        self.bruit_lin.setText(_translate("MainWindow", "bruit linéaire", None))
        self.bruit_racine.setText(_translate("MainWindow", "bruit racine", None))
        self.bruit_quadra.setText(_translate("MainWindow", "bruit quadratique", None))
        self.nb_iteration.setToolTip(_translate("MainWindow", "<html><head/><body><p>Ce nombre correspond au nombre de fois chaque partie du terrain est redécoupée. </p><p>Plus ce nombre est grand, meilleur sera la définition.</p><p> Attention cependant, un nombre trop grand demandera beaucoup de temps de calcul.</p></body></html>", None))
        self.nb_iteration.setText(_translate("MainWindow", "Nombre d\'itérations:", None))
        self.val_frac.setToolTip(_translate("MainWindow", "<html><head/><body><p>Pour la génération en 2D, à chaque itération, chaque segment est découpé en deux.</p><p>La valeur de la fraction indique où cette découpe à lieu (0.5 correspondant au mileu du segment).</p></body></html>", None))
        self.val_frac.setText(_translate("MainWindow", "Valeur fraction:", None))
        self.ajouter_cours_bouton.setText(_translate("MainWindow", "Ajouter cours d\'eau", None))
        self.menuFichier.setTitle(_translate("MainWindow", "Fichier", None))
        self.actionOuvrir.setText(_translate("MainWindow", "Ouvrir", None))
        self.actionOuvrir.setShortcut(_translate("MainWindow", "Ctrl+O", None))
        self.actionQuitter.setText(_translate("MainWindow", "Quitter", None))
        self.actionQuitter.setShortcut(_translate("MainWindow", "Ctrl+Q", None))


from matplotlibwidget import MatplotlibWidget
