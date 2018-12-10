# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewSawtoothDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewSawtoothDialog(object):
    def setupUi(self, NewSawtoothDialog):
        NewSawtoothDialog.setObjectName("NewSawtoothDialog")
        NewSawtoothDialog.resize(402, 488)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewSawtoothDialog.sizePolicy().hasHeightForWidth())
        NewSawtoothDialog.setSizePolicy(sizePolicy)
        NewSawtoothDialog.setMinimumSize(QtCore.QSize(402, 488))
        NewSawtoothDialog.setMaximumSize(QtCore.QSize(402, 488))
        NewSawtoothDialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewSawtoothDialog)
        self.buttonBox.setGeometry(QtCore.QRect(180, 450, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.line = QtWidgets.QFrame(NewSawtoothDialog)
        self.line.setGeometry(QtCore.QRect(0, 270, 401, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(NewSawtoothDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 290, 381, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelAmplitude = QtWidgets.QLabel(self.layoutWidget)
        self.labelAmplitude.setObjectName("labelAmplitude")
        self.horizontalLayout.addWidget(self.labelAmplitude)
        self.doubleSpinBoxAmplitude = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxAmplitude.setMaximum(1.1)
        self.doubleSpinBoxAmplitude.setSingleStep(0.1)
        self.doubleSpinBoxAmplitude.setProperty("value", 1.0)
        self.doubleSpinBoxAmplitude.setObjectName("doubleSpinBoxAmplitude")
        self.horizontalLayout.addWidget(self.doubleSpinBoxAmplitude)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelFrequency = QtWidgets.QLabel(self.layoutWidget)
        self.labelFrequency.setObjectName("labelFrequency")
        self.horizontalLayout_2.addWidget(self.labelFrequency)
        self.doubleSpinBoxFrequency = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFrequency.setMaximum(20000.0)
        self.doubleSpinBoxFrequency.setProperty("value", 50.0)
        self.doubleSpinBoxFrequency.setObjectName("doubleSpinBoxFrequency")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxFrequency)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.PreviewPlot = PlotWidget(NewSawtoothDialog)
        self.PreviewPlot.setGeometry(QtCore.QRect(0, 0, 401, 261))
        self.PreviewPlot.setObjectName("PreviewPlot")

        self.retranslateUi(NewSawtoothDialog)
        self.buttonBox.accepted.connect(NewSawtoothDialog.accept)
        self.buttonBox.rejected.connect(NewSawtoothDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewSawtoothDialog)

    def retranslateUi(self, NewSawtoothDialog):
        _translate = QtCore.QCoreApplication.translate
        NewSawtoothDialog.setWindowTitle(_translate("NewSawtoothDialog", "Periodic Known Signal-Sawtooth"))
        self.labelAmplitude.setText(_translate("NewSawtoothDialog", "Amplitude (A)"))
        self.labelFrequency.setText(_translate("NewSawtoothDialog", "Frequency (Fo)"))

from pyqtgraph import PlotWidget
