# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/GraphicWidget.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GraphicWindow(object):
    def setupUi(self, GraphicWindow):
        GraphicWindow.setObjectName("GraphicWindow")
        GraphicWindow.resize(937, 546)
        self.verticalLayout = QtWidgets.QVBoxLayout(GraphicWindow)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.freq_label = QtWidgets.QLabel(GraphicWindow)
        self.freq_label.setText("")
        self.freq_label.setAlignment(QtCore.Qt.AlignCenter)
        self.freq_label.setObjectName("freq_label")
        self.verticalLayout.addWidget(self.freq_label)
        self.pushButtonPlay = QtWidgets.QPushButton(GraphicWindow)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.verticalLayout.addWidget(self.pushButtonPlay)
        self.pushButton = QtWidgets.QPushButton(GraphicWindow)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.graphicsView = GraphicsLayoutWidget(GraphicWindow)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)

        self.retranslateUi(GraphicWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphicWindow)

    def retranslateUi(self, GraphicWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphicWindow.setWindowTitle(_translate("GraphicWindow", "GraphicWindow"))
        self.pushButtonPlay.setText(_translate("GraphicWindow", "Play"))
        self.pushButton.setText(_translate("GraphicWindow", "View Spectrum"))

from pyqtgraph import GraphicsLayoutWidget
