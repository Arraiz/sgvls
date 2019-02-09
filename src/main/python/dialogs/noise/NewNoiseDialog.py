# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/NewNoiseDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NoiseSignalDialog(object):
    def setupUi(self, NoiseSignalDialog):
        NoiseSignalDialog.setObjectName("NoiseSignalDialog")
        NoiseSignalDialog.resize(592, 572)
        NoiseSignalDialog.setSizeGripEnabled(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(NoiseSignalDialog)
        self.buttonBox.setGeometry(QtCore.QRect(370, 540, 221, 41))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.PreviewPlot = PlotWidget(NoiseSignalDialog)
        self.PreviewPlot.setGeometry(QtCore.QRect(0, 0, 591, 281))
        self.PreviewPlot.setObjectName("PreviewPlot")
        self.descriptionLabel = QtWidgets.QLabel(NoiseSignalDialog)
        self.descriptionLabel.setGeometry(QtCore.QRect(40, 290, 531, 16))
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.groupBox = QtWidgets.QGroupBox(NoiseSignalDialog)
        self.groupBox.setGeometry(QtCore.QRect(80, 320, 191, 181))
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.whiteRadio = QtWidgets.QRadioButton(self.groupBox)
        self.whiteRadio.setChecked(True)
        self.whiteRadio.setObjectName("whiteRadio")
        self.verticalLayout.addWidget(self.whiteRadio)
        self.pinkRadio = QtWidgets.QRadioButton(self.groupBox)
        self.pinkRadio.setObjectName("pinkRadio")
        self.verticalLayout.addWidget(self.pinkRadio)
        self.brownRadio = QtWidgets.QRadioButton(self.groupBox)
        self.brownRadio.setObjectName("brownRadio")
        self.verticalLayout.addWidget(self.brownRadio)

        self.retranslateUi(NoiseSignalDialog)
        self.buttonBox.accepted.connect(NoiseSignalDialog.accept)
        self.buttonBox.rejected.connect(NoiseSignalDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NoiseSignalDialog)

    def retranslateUi(self, NoiseSignalDialog):
        _translate = QtCore.QCoreApplication.translate
        NoiseSignalDialog.setWindowTitle(_translate("NoiseSignalDialog", "Noise Signal"))
        self.descriptionLabel.setText(_translate("NoiseSignalDialog", "This dialog will generate random noise with zero mean a bla blah blah"))
        self.groupBox.setTitle(_translate("NoiseSignalDialog", "Noise type"))
        self.whiteRadio.setText(_translate("NoiseSignalDialog", "Genetate white noise"))
        self.pinkRadio.setText(_translate("NoiseSignalDialog", "Genetate pink noise"))
        self.brownRadio.setText(_translate("NoiseSignalDialog", "Genetate brown noise"))

from pyqtgraph import PlotWidget
