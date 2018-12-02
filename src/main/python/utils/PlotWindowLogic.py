import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from .PlotWindow import Ui_PlotWindow
from .FFTWindowLogic import FFTWindowLogic
from numpy import sin, cos, fft, arange, pi, savetxt
from scipy import signal
from scipy.signal import square, sawtooth, gausspulse

from pyqtgraph import LinearRegionItem, SignalProxy
from pyqtgraph import mkPen


class PlotWindowLogic(Ui_PlotWindow):
    def __init__(self, PlotWindowLogic):
        Ui_PlotWindow.__init__(self)

    def initBindings(self):
        # self.pushButtonAddSignal.clicked.connect(self.addSignal)
        self.pushButtonViewFFT.clicked.connect(self.showFFT)
        self.pushButtonExportCSV.clicked.connect(self.exportDataset)
        self.FFTwindow = None


   




    def PlotSin(self, amp, freq, phase):

        self.Fs = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*sin(2 * pi * freq * self.x + (phase*pi))
        self.plot = self.PlotView.plotItem
        self.vBox = self.plot.vb
        self.vBox.setLimits(xMin=-0, yMin=-2, xMax=1.3, yMax=2)
        self.vBox.setBackgroundColor("w")
        # self.vBox.setBackgroundColor("white")
        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        self.plot.plot(self.x, self.y, pen=mkPen('b', width=1),
                       name=str(amp)+"Sin(2π"+str(freq)+"+"+str(phase))
        proxy = SignalProxy(self.plot.scene().sigMouseMoved, rateLimit=60, slot=self.MouseMoved)

    def MouseMoved(self):
        pass


    def plotSawtooth(self, amp, freq):
        self.Fs: int = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*sawtooth(2*pi*freq*self.x)
        self.plot = self.PlotView.plotItem
        self.vBox = self.plot.vb
        self.vBox.setLimits(xMin=-0, yMin=-2, xMax=1.3, yMax=2)
        self.vBox.setBackgroundColor("w")

        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        self.plot.plot(self.x, self.y, pen=mkPen('b', width=1),
                       name=str(amp)+"Sawtooth(2π"+str(freq))

    def plotSquare(self, amp, freq):
        self.Fs: int = 48000
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*square(2*pi*freq*self.x)
        self.plot = self.PlotView.plotItem
        self.vBox = self.plot.vb
        self.vBox.setLimits(xMin=-0, yMin=-2, xMax=1.3, yMax=2)
        self.vBox.setBackgroundColor("w")

        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        self.plot.plot(self.x, self.y, pen=mkPen('b', width=1),
                    name=str(amp)+"Sawtooth(2π"+str(freq))

    def plotGpulse(self, amp, freq):
        self.Fs: int = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*gausspulse((self.x,freq))
        self.plot = self.PlotView.plotItem
        self.vBox = self.plot.vb
        self.vBox.setLimits(xMin=-0, yMin=-2, xMax=1.3, yMax=2)
        self.vBox.setBackgroundColor("w")

        self.plot.addLegend()
        self.plot.showGrid(x=True, y=True)
        self.plot.plot(self.x, self.y, pen=mkPen('b', width=1),
                    name=str(amp)+"Gaussian Pulse(2π"+str(freq))

    # def addSignal(self):
    #     # abre un nuevo dialogo
    #     self.AddSignalWindow = QtWidgets.QDialog()
    #     self.ui = Ui_AddSignalDialog()
    #     self.ui.setupUi(self.AddSignalWindow)
    #     self.AddSignalWindow.show()
    #     self.AddSignalWindow.activateWindow()
    #     self.AddSignalWindow.raise_
    #     self.AddSignalWindow.accepted.connect(self.Addplot)

    # def Addplot(self):
    #     amp = self.ui.horizontalSliderAmplitude.value()
    #     freq = self.ui.horizontalSliderFrequency.value()
    #     phase = self.ui.horizontalSliderPhase.value()
    #     func = 'Sin'
    #     self.y = self.y+(amp/10)*sin(2*pi*freq*self.x+phase*pi)
    #     if(self.ui.radioButtonCos.isChecked() == True):
    #         self.y = self.y+(amp/10)*cos(2*pi*freq*self.x+phase*pi)
    #         func = 'Cos'

    #     self.plot.clearPlots()
    #     self.plot.plot(self.x, self.y, pen='r', name=str(
    #         amp/10)+' ('+func+' 2π '+str(freq)+'*t)')

    def showFFT(self):
        self.FFTwindow = QtWidgets.QWidget()
        self.ui = FFTWindowLogic(self, self.y, self.Fs)
        self.ui.setupUi(self.FFTwindow)
        self.ui.PlotFFT()
        self.FFTwindow.activateWindow()
        self.FFTwindow.show()
        self.FFTwindow.raise_()


    def exportDataset(self):
        savetxt('file.csv',[self.x,self.y],delimiter=",")
