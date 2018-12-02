from .GraphicWidget import Ui_GraphicWindow
from .GraphicWindowSpectrumLogic import GraphicWidgetLogicSpectrumLogic
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import SignalProxy, LinearRegionItem, InfiniteLine
from pyqtgraph.Point import Point
from numpy import sin, cos, fft, arange, pi, savetxt
from scipy import signal
from scipy.signal import square, sawtooth, gausspulse
from pyqtgraph import mkPen, setConfigOption

from PyQt5 import QtCore

import sounddevice as sd


class GraphicWidgetLogic (Ui_GraphicWindow):
    def __init__(self, GraphicWidgetLogic):
        Ui_GraphicWindow.__init__(self)
        self.FS = 48000
        self.x = 0
        self.y = 0
        self.freq = 0
        self.amp = 0
        self.flag = "PURE"

    # se inicializa el sistema de visualizado avanzado
    def initializeBinds(self):
        # añadir plots

        self.pushButtonPlay.clicked.connect(self.play)
        self.pushButton.clicked.connect(self.showFFT)
        setConfigOption('leftButtonPan', False)
        self.x = 0
        self.y = 0

        self.zoomedPlot = self.graphicsView.addPlot(row=1, col=0)
        self.fullPlot = self.graphicsView.addPlot(row=2, col=0)

        
        self.graphicsView.setBackground(background="w")
        # self.zoomedPlot.vb.setBackgroundColor("w")
        # self.fullPlot.vb.setBackgroundColor("w")
        self.penB = mkPen('b')
        self.penR = mkPen('r')
        self.region = LinearRegionItem()
        self.region.setZValue(10)

        self.vb = self.zoomedPlot.vb
        self.region.setRegion([1000, 2000])

        self.fullPlot.addItem(self.region, ignoreBounds=True)
        # pg.dbg()
        self.zoomedPlot.setAutoVisible(y=True)

        self.vLine = InfiniteLine(angle=90, movable=False)
        self.hLine = InfiniteLine(angle=0, movable=False)
        self.zoomedPlot.addItem(self.vLine, ignoreBounds=True)
        self.zoomedPlot.addItem(self.hLine, ignoreBounds=True)

        # signal para capturar evento de raton
        # proxy = SignalProxy(self.zoomedPlot.scene().sigMouseMoved, rateLimit=60, slot=self.mouseMoved)

        self.zoomedPlot.scene().sigMouseMoved.connect(self.mouseMoved)
        self.region.sigRegionChanged.connect(self.update)

        self.zoomedPlot.sigRangeChanged.connect(self.updateRegion)

    def play(self):
        sd.play(self.y, self.FS, blocking=True)

    def showFFT(self):
        self.FFTwindow = QtWidgets.QWidget()
        self.ui = GraphicWidgetLogicSpectrumLogic(self)
        self.ui.setupUi(self.FFTwindow)
        self.ui.initializeBinds()

        self.ui.PlotFFT(self.x, self.y,self.flag,self.amp)
        
        self.FFTwindow.activateWindow()
        self.FFTwindow.show()
        self.FFTwindow.raise_()

    def updateRegion(self, window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)

    def update(self):
        self.region.setZValue(10)
        minX, maxX = self.region.getRegion()
        self.zoomedPlot.setXRange(minX, maxX, padding=0)

    def mouseMoved(self, evt):
        pos = Point(evt.x(), evt.y())
        if self.zoomedPlot.sceneBoundingRect().contains(pos):
            mousePoint = self.vb.mapSceneToView(pos)
            index = float(evt.x())
        #   if index > 0 :
            # self.dataLabel.setText("<span style='font-size: 12pt'>x=%0.1f,   <span style='color: red'>y1=%0.1f</span>,   <span style='color: green'>y2=%0.1f</span>" % int(index), self.x[index], self.y[index])
            self.vLine.setPos(mousePoint.x())
            self.hLine.setPos(mousePoint.y())

    def PlotSin(self, amp, freq, phase, flag="PURE"):
        print(self.flag)
        self.flag = flag
        self.amp = amp
        self.freq = freq

        self.x = arange(0, 1, 1/self.FS)
        self.y = (amp/10)*sin(2 * pi * freq * self.x + (phase*pi))

        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

    def plotSawtooth(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*sawtooth(2*pi*freq*self.x)
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

    def plotSquare(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*square(2*pi*freq*self.x)
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

    def plotGpulse(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1/self.Fs)
        self.y = (amp/10)*gausspulse((self.x, freq))
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

    def plotHarmonic(self, x_array, y_array):
        self.x = x_array
        self.y = y_array
        self.fullPlot.plot(x_array, y_array, pen=self.penR)
        self.zoomedPlot.plot(x_array, y_array, pen=self.penB)

   
