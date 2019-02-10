from .LoadFileDialog import Ui_LoadFile
from PyQt5 import QtWidgets
from scipy.io import wavfile
from pyqtgraph import mkPen
from numpy import arange, sin, pi, linspace
import sounddevice as sd


class LoadFileDialogLogic(Ui_LoadFile):

    def __init__(self, LoadFileDialogLogic):
        Ui_LoadFile.__init__(self)
        self.x = []
        self.y = []
        self.fs = 0
        self.data = []

    def setupBinds(self):
        self.pushButtonLoad.clicked.connect(self.openFileDialog)
        self.lineEdit.returnPressed.connect(self.openFileDialog)
        self.pushButtonPlay.clicked.connect(self.play)
        self.plot.setBackground(background="w")

    def play(self):
        sd.play(self.data, self.fs)

    def openFileDialog(self):
        self._audio_file = None
        qfd = QtWidgets.QFileDialog()
        filter = "wav(*.wav)"
        self._audio_file = QtWidgets.QFileDialog.getOpenFileName(
            qfd, "Select a file", "", filter)[0]
        print(str(self._audio_file))

        if(len(str(self._audio_file)) > 4):
            # check if file is not empty
            self.lineEdit.setText(str(self._audio_file))
            # open file
            fs, data = wavfile.read(str(self._audio_file))

            self.fs = fs
            self.data = data

            self.x = arange(0, len(data)/fs, 1/fs)
            self.plot.plotItem.clear()
            self.plot.plot(self.x, data, pen=mkPen('b', width=1))


        # def generatePlot(self):
        #     self.PlotWindow = QtWidgets.QWidget()
        #     self.ui = GraphicWidgetLogic(self)
        #     self.ui.setupUi(self.PlotWindow)
        #     self.ui.initializeBinds()
        #     self.ui.PlotSin(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrequency.value(),self.doubleSpinBoxPhase.value(),"PURE")
        #     return self.PlotWindow