from .GraphicWidget import Ui_GraphicWindow
from .GraphicWindowSpectrumLogic import GraphicWidgetLogicSpectrumLogic
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import SignalProxy, LinearRegionItem, InfiniteLine
from pyqtgraph.Point import Point
import numpy as np
from numpy import sin, cos, fft, arange, pi, savetxt,random,array,int16
from scipy import signal
from scipy.signal import square, sawtooth, gausspulse
import pyqtgraph as pg
from pyqtgraph import mkPen, setConfigOption
import simpleaudio as sa
#import pyaudio




class GraphicWidgetLogic(Ui_GraphicWindow):
    def __init__(self):
        self.FS = 48000
        self.x = 0
        self.y = 0
        self.freq = 0
        self.amp = 0
        self.flag = "DEFAULT"



    # se inicializa el sistema de visualizado avanzado
    def init_binds(self):
        # añadir plots
        self.pushButtonPlay.clicked.connect(self.play)
        self.pushButton.clicked.connect(self.show_fft)
        # pg.setConfigOptions(useOpenGL=True)
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
        self.region.setRegion([0, 1])

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
        self.fullPlot.setMouseEnabled(False,False)


        self.fullPlot.setLabel('bottom','Time (s)')
        self.fullPlot.setLabel('left', 'Amplitude')

        self.zoomedPlot.setLabel('bottom','Time (s) ')
        self.zoomedPlot.setLabel('left', 'Amplitude')


    def play(self):
        pass
        audio=self.y
        if(self.y.dtype != 'int16'):
            audio *= 32767 / np.max(np.abs(audio))
        # convert to 16-bit data
        audio = audio.astype(np.int16)
        # start playback
        play_obj = sa.play_buffer(audio, 1, 2, self.FS)
        # wait for playback to finish before exiting
        play_obj.wait_done()

    def show_fft(self,title="undefined"):

        self.FFTwindow = QtWidgets.QWidget()
        # self.FFTwindow.setWindowTitle(title)
        self.ui = GraphicWidgetLogicSpectrumLogic()
        self.ui.setupUi(self.FFTwindow)
        self.ui.init_binds()

        self.ui.PlotFFT(self.x, self.y, self.flag, self.amp)

        self.FFTwindow.activateWindow()
        self.FFTwindow.show()
        self.FFTwindow.raise_()

    def updateRegion(self, window, viewRange):
        rgn = viewRange[0]

        self.region.setRegion(rgn)

    def update(self):
        self.region.setZValue(10)

        minX, maxX = self.region.getRegion()
        if minX < 0:
            minX = 0
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
        self.flag = flag
        self.amp = amp
        self.freq = freq

        self.x = arange(0, 1, 1 / self.FS)
        self.y = (amp ) * sin(2 * pi * freq * self.x + (phase * pi))

        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)

        self.zoomedPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))

    def plotSawtooth(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1 / self.Fs)
        self.y = (amp ) * sawtooth(2 * pi * freq * self.x)
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)

        self.zoomedPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))

    def plotSquare(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1 / self.Fs)
        self.y = (amp ) * square(2 * pi * freq * self.x)
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)

        self.zoomedPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))

    def plotGpulse(self, amp, freq):
        self.amp = amp
        self.freq = freq
        self.Fs: int = 44100
        self.x = arange(0, 1, 1 / self.Fs)
        self.y = (amp / 10) * gausspulse((self.x, freq))
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)

        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)

        self.zoomedPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))

    def plotHarmonic(self, x_array, y_array):
        self.x = x_array
        self.y = y_array
        self.fullPlot.plot(x_array, y_array, pen=self.penR)
        self.zoomedPlot.plot(x_array, y_array, pen=self.penB)

        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)

        self.zoomedPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.y),yMax=max(self.y))

    def plot_white_noise(self):
        self.x = self.x = arange(0, 1, 1 / self.FS)
        self.y=3*random.randn(self.FS)
        self.fullPlot.plot(self.x, self.y, pen=self.penR)
        self.zoomedPlot.plot(self.x, self.y, pen=self.penB)
        self.zoomedPlot.setXRange(0,max(self.x),padding=0)
        self.fullPlot.setXRange(0, max(self.x), padding=0)
        self.zoomedPlot.vb.setLimits(xMin=-0.1,xMax=1,yMin=min(self.y),yMax=max(self.y))
        self.fullPlot.vb.setLimits(xMin=-0.1,xMax=1,yMin=min(self.y)-0.1,yMax=max(self.y))


