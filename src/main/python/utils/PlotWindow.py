# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/PlotWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PlotWindow(object):
    def setupUi(self, PlotWindow):
        PlotWindow.setObjectName("PlotWindow")
        PlotWindow.resize(849, 530)
        self.gridLayout = QtWidgets.QGridLayout(PlotWindow)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlotView = PlotWidget(PlotWindow)
        self.PlotView.setObjectName("PlotView")
        self.verticalLayout.addWidget(self.PlotView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonAddSignal = QtWidgets.QPushButton(PlotWindow)
        self.pushButtonAddSignal.setObjectName("pushButtonAddSignal")
        self.horizontalLayout.addWidget(self.pushButtonAddSignal)
        self.pushButtonViewFFT = QtWidgets.QPushButton(PlotWindow)
        self.pushButtonViewFFT.setObjectName("pushButtonViewFFT")
        self.horizontalLayout.addWidget(self.pushButtonViewFFT)
        self.pushButtonExportCSV = QtWidgets.QPushButton(PlotWindow)
        self.pushButtonExportCSV.setObjectName("pushButtonExportCSV")
        self.horizontalLayout.addWidget(self.pushButtonExportCSV)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(PlotWindow)
        QtCore.QMetaObject.connectSlotsByName(PlotWindow)

    def retranslateUi(self, PlotWindow):
        _translate = QtCore.QCoreApplication.translate
        PlotWindow.setWindowTitle(_translate("PlotWindow", "PlotWindow"))
        self.pushButtonAddSignal.setText(_translate("PlotWindow", "Add Signal"))
        self.pushButtonViewFFT.setText(_translate("PlotWindow", "View FFT"))
        self.pushButtonExportCSV.setText(_translate("PlotWindow", "Export CSV"))

from pyqtgraph import PlotWidget
