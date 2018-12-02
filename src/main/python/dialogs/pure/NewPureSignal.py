# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/NewPureSignal.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PureSginalDialog(object):
    def setupUi(self, PureSginalDialog):
        PureSginalDialog.setObjectName("PureSginalDialog")
        PureSginalDialog.resize(591, 573)
        self.buttonBox = QtWidgets.QDialogButtonBox(PureSginalDialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 540, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.PreviewPlot = PlotWidget(PureSginalDialog)
        self.PreviewPlot.setGeometry(QtCore.QRect(0, 0, 591, 281))
        self.PreviewPlot.setObjectName("PreviewPlot")
        self.layoutWidget = QtWidgets.QWidget(PureSginalDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 290, 271, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.doubleSpinBoxAmplitude = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxAmplitude.setMaximum(1.0)
        self.doubleSpinBoxAmplitude.setSingleStep(0.1)
        self.doubleSpinBoxAmplitude.setObjectName("doubleSpinBoxAmplitude")
        self.horizontalLayout_3.addWidget(self.doubleSpinBoxAmplitude)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.doubleSpinBoxFrequency = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxFrequency.setMaximum(20000.0)
        self.doubleSpinBoxFrequency.setSingleStep(1.0)
        self.doubleSpinBoxFrequency.setObjectName("doubleSpinBoxFrequency")
        self.horizontalLayout_2.addWidget(self.doubleSpinBoxFrequency)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.doubleSpinBoxPhase = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.doubleSpinBoxPhase.setMaximum(1.0)
        self.doubleSpinBoxPhase.setSingleStep(0.1)
        self.doubleSpinBoxPhase.setObjectName("doubleSpinBoxPhase")
        self.horizontalLayout.addWidget(self.doubleSpinBoxPhase)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.labelFormula = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.labelFormula.setFont(font)
        self.labelFormula.setText("")
        self.labelFormula.setAlignment(QtCore.Qt.AlignCenter)
        self.labelFormula.setObjectName("labelFormula")
        self.horizontalLayout_4.addWidget(self.labelFormula)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(PureSginalDialog)
        self.buttonBox.accepted.connect(PureSginalDialog.accept)
        self.buttonBox.rejected.connect(PureSginalDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(PureSginalDialog)

    def retranslateUi(self, PureSginalDialog):
        _translate = QtCore.QCoreApplication.translate
        PureSginalDialog.setWindowTitle(_translate("PureSginalDialog", "Pure Signal"))
        self.label.setText(_translate("PureSginalDialog", "Amplitude"))
        self.label_2.setText(_translate("PureSginalDialog", "Frequency"))
        self.label_3.setText(_translate("PureSginalDialog", "Phase"))

from pyqtgraph import PlotWidget
