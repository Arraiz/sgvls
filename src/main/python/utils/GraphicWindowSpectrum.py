# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/GraphicWidgetSpectrum.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphicWindowSpectrum(object):
    def setupUi(self, GraphicWindow):
        GraphicWindow.setObjectName("GraphicWindow")
        GraphicWindow.resize(935, 567)
        self.verticalLayout = QtWidgets.QVBoxLayout(GraphicWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView = GraphicsLayoutWidget(GraphicWindow)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(GraphicWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphicWindow)

    def retranslateUi(self, GraphicWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphicWindow.setWindowTitle(_translate("GraphicWindow", "GraphicWindow"))

from pyqtgraph import GraphicsLayoutWidget
