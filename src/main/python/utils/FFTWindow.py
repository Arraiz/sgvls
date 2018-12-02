# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/FFTWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWindowFFT(object):
    def setupUi(self, PlotWindowFFT):
        PlotWindowFFT.setObjectName("PlotWindowFFT")
        PlotWindowFFT.resize(849, 530)
        self.gridLayout = QtWidgets.QGridLayout(PlotWindowFFT)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.FFTplotView = PlotWidget(PlotWindowFFT)
        self.FFTplotView.setObjectName("FFTplotView")
        self.verticalLayout.addWidget(self.FFTplotView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PlotWindowFFT)
        QtCore.QMetaObject.connectSlotsByName(PlotWindowFFT)

    def retranslateUi(self, PlotWindowFFT):
        _translate = QtCore.QCoreApplication.translate
        PlotWindowFFT.setWindowTitle(_translate("PlotWindowFFT", "FFTwindow"))

from pyqtgraph import PlotWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PlotWindowFFT = QtWidgets.QWidget()
    ui = Ui_PlotWindowFFT()
    ui.setupUi(PlotWindowFFT)
    PlotWindowFFT.show()
    sys.exit(app.exec_())

