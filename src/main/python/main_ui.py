# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(433, 207)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 40, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 433, 22))
        self.menubar.setObjectName("menubar")
        self.menuSignal_Visualizer = QtWidgets.QMenu(self.menubar)
        self.menuSignal_Visualizer.setObjectName("menuSignal_Visualizer")
        self.menuGenerate = QtWidgets.QMenu(self.menubar)
        self.menuGenerate.setObjectName("menuGenerate")
        self.menuPeriodic_Known_Signal = QtWidgets.QMenu(self.menuGenerate)
        self.menuPeriodic_Known_Signal.setObjectName("menuPeriodic_Known_Signal")
        self.menuHarmonic_Synteshis = QtWidgets.QMenu(self.menuGenerate)
        self.menuHarmonic_Synteshis.setObjectName("menuHarmonic_Synteshis")
        self.menuPure_Tone = QtWidgets.QMenu(self.menuGenerate)
        self.menuPure_Tone.setObjectName("menuPure_Tone")
        self.menuNoise = QtWidgets.QMenu(self.menuGenerate)
        self.menuNoise.setObjectName("menuNoise")
        self.menuOther = QtWidgets.QMenu(self.menubar)
        self.menuOther.setObjectName("menuOther")
        self.menuAnalisys = QtWidgets.QMenu(self.menubar)
        self.menuAnalisys.setObjectName("menuAnalisys")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSine = QtWidgets.QAction(MainWindow)
        self.actionSine.setObjectName("actionSine")
        self.actionCosine = QtWidgets.QAction(MainWindow)
        self.actionCosine.setObjectName("actionCosine")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionLoad_Signal = QtWidgets.QAction(MainWindow)
        self.actionLoad_Signal.setObjectName("actionLoad_Signal")
        self.actionRecord_Signal = QtWidgets.QAction(MainWindow)
        self.actionRecord_Signal.setObjectName("actionRecord_Signal")
        self.actionSin = QtWidgets.QAction(MainWindow)
        self.actionSin.setObjectName("actionSin")
        self.actionCos = QtWidgets.QAction(MainWindow)
        self.actionCos.setObjectName("actionCos")
        self.actionSawtooth = QtWidgets.QAction(MainWindow)
        self.actionSawtooth.setObjectName("actionSawtooth")
        self.actionRosenbert = QtWidgets.QAction(MainWindow)
        self.actionRosenbert.setObjectName("actionRosenbert")
        self.actionSquare = QtWidgets.QAction(MainWindow)
        self.actionSquare.setObjectName("actionSquare")
        self.actionFree = QtWidgets.QAction(MainWindow)
        self.actionFree.setObjectName("actionFree")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionWhite = QtWidgets.QAction(MainWindow)
        self.actionWhite.setObjectName("actionWhite")
        self.actionPink = QtWidgets.QAction(MainWindow)
        self.actionPink.setObjectName("actionPink")
        self.actionPeriodic = QtWidgets.QAction(MainWindow)
        self.actionPeriodic.setObjectName("actionPeriodic")
        self.actionLoad = QtWidgets.QAction(MainWindow)
        self.actionLoad.setObjectName("actionLoad")
        self.actionRecord = QtWidgets.QAction(MainWindow)
        self.actionRecord.setObjectName("actionRecord")
        self.actionSpectrogram = QtWidgets.QAction(MainWindow)
        self.actionSpectrogram.setObjectName("actionSpectrogram")
        self.menuSignal_Visualizer.addSeparator()
        self.menuSignal_Visualizer.addAction(self.actionExit)
        self.menuPeriodic_Known_Signal.addAction(self.actionSawtooth)
        self.menuPeriodic_Known_Signal.addAction(self.actionRosenbert)
        self.menuPeriodic_Known_Signal.addAction(self.actionSquare)
        self.menuHarmonic_Synteshis.addAction(self.actionFree)
        self.menuHarmonic_Synteshis.addAction(self.actionPeriodic)
        self.menuPure_Tone.addAction(self.actionNew)
        self.menuNoise.addAction(self.actionWhite)
        self.menuNoise.addAction(self.actionPink)
        self.menuGenerate.addAction(self.menuPure_Tone.menuAction())
        self.menuGenerate.addAction(self.menuPeriodic_Known_Signal.menuAction())
        self.menuGenerate.addAction(self.menuHarmonic_Synteshis.menuAction())
        self.menuGenerate.addAction(self.menuNoise.menuAction())
        self.menuGenerate.addSeparator()
        self.menuOther.addAction(self.actionLoad)
        self.menuOther.addAction(self.actionRecord)
        self.menuAnalisys.addAction(self.actionSpectrogram)
        self.menubar.addAction(self.menuSignal_Visualizer.menuAction())
        self.menubar.addAction(self.menuGenerate.menuAction())
        self.menubar.addAction(self.menuOther.menuAction())
        self.menubar.addAction(self.menuAnalisys.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Signal BETA-LIZER"))
        self.menuSignal_Visualizer.setTitle(_translate("MainWindow", "Signal Visualizer"))
        self.menuGenerate.setTitle(_translate("MainWindow", "Generate"))
        self.menuPeriodic_Known_Signal.setTitle(_translate("MainWindow", "Periodic Known Signal"))
        self.menuHarmonic_Synteshis.setTitle(_translate("MainWindow", "Harmonic Synteshis"))
        self.menuPure_Tone.setTitle(_translate("MainWindow", "Pure Tone"))
        self.menuNoise.setTitle(_translate("MainWindow", "Noise"))
        self.menuOther.setTitle(_translate("MainWindow", "Input/Output"))
        self.menuAnalisys.setTitle(_translate("MainWindow", "Analyze"))
        self.actionSine.setText(_translate("MainWindow", "Sine"))
        self.actionCosine.setText(_translate("MainWindow", "Cosine"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionLoad_Signal.setText(_translate("MainWindow", "Load Signal"))
        self.actionRecord_Signal.setText(_translate("MainWindow", "Record Signal"))
        self.actionSin.setText(_translate("MainWindow", "Sin"))
        self.actionCos.setText(_translate("MainWindow", "Cos"))
        self.actionSawtooth.setText(_translate("MainWindow", "Sawtooth"))
        self.actionRosenbert.setText(_translate("MainWindow", "Rosenbert"))
        self.actionSquare.setText(_translate("MainWindow", "Square"))
        self.actionFree.setText(_translate("MainWindow", "Free"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionWhite.setText(_translate("MainWindow", "White"))
        self.actionPink.setText(_translate("MainWindow", "Pink"))
        self.actionPeriodic.setText(_translate("MainWindow", "Periodic"))
        self.actionLoad.setText(_translate("MainWindow", "Load"))
        self.actionRecord.setText(_translate("MainWindow", "Record"))
        self.actionSpectrogram.setText(_translate("MainWindow", "Spectrogram"))

