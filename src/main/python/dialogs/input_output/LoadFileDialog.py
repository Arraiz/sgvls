# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/LoadFileDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadFile(object):
    def setupUi(self, LoadFile):
        LoadFile.setObjectName("LoadFile")
        LoadFile.resize(816, 385)
        self.gridLayout_2 = QtWidgets.QGridLayout(LoadFile)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(LoadFile)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonLoad = QtWidgets.QPushButton(LoadFile)
        self.pushButtonLoad.setObjectName("pushButtonLoad")
        self.horizontalLayout.addWidget(self.pushButtonLoad)
        self.pushButtonPlay = QtWidgets.QPushButton(LoadFile)
        self.pushButtonPlay.setObjectName("pushButtonPlay")
        self.horizontalLayout.addWidget(self.pushButtonPlay)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.plot = PlotWidget(LoadFile)
        self.plot.setObjectName("plot")
        self.gridLayout.addWidget(self.plot, 1, 0, 1, 1)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(LoadFile)
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        self.gridLayout.addWidget(self.buttonBox_2, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(LoadFile)
        self.buttonBox_2.accepted.connect(LoadFile.close)
        self.buttonBox_2.rejected.connect(LoadFile.close)
        QtCore.QMetaObject.connectSlotsByName(LoadFile)

    def retranslateUi(self, LoadFile):
        _translate = QtCore.QCoreApplication.translate
        LoadFile.setWindowTitle(_translate("LoadFile", "Load File Window"))
        self.pushButtonLoad.setText(_translate("LoadFile", "Load"))
        self.pushButtonPlay.setText(_translate("LoadFile", "Play"))

from pyqtgraph import PlotWidget
