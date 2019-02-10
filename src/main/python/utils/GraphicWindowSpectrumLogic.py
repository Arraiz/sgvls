from .GraphicWindowSpectrum import Ui_GraphicWindowSpectrum
from pyqtgraph import SignalProxy, LinearRegionItem, InfiniteLine
from pyqtgraph.Point import Point
from numpy import sin, cos, fft, arange, pi, savetxt, linspace, zeros
from scipy import signal
from scipy.signal import square, sawtooth, gausspulse
from scipy import fftpack
from pyqtgraph import mkPen, setConfigOption

from PyQt5 import QtCore



class GraphicWidgetLogicSpectrumLogic (Ui_GraphicWindowSpectrum):
    def __init__(self):
        Ui_GraphicWindowSpectrum.__init__(self)
        self.FS = 48000
        self.x = 0
        self.y = 0

    # se inicializa el sistema de visualizado avanzado
    def init_binds(self):
        # añadir plots

        setConfigOption('leftButtonPan', False)
        self.x = 0
        self.y = 0

        self.zoomedPlot = self.graphicsView.addPlot(row=1, col=0)
        self.fullPlot = self.graphicsView.addPlot(row=2, col=0)


        self.graphicsView.setBackground(background="w")
        self.penB = mkPen('b')
        self.penR = mkPen('r')
        self.region = LinearRegionItem()
        self.region.setZValue(1)

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

        self.fullPlot.setLabel('left','Amplitude')
        self.fullPlot.setLabel('bottom', 'Frecuency (Hz)')

        self.zoomedPlot.setLabel('bottom','Frecuency (Hz)')
        self.zoomedPlot.setLabel('left', 'Amplitude')

        self.fullPlot.setMouseEnabled(False,False)
        self.zoomedPlot.setMouseEnabled(True,False)

        # self.zoomedPlot.setXRange(0, self.FS/2, padding=0)
    def updateRegion(self, window, viewRange):
        rgn = viewRange[0]
        self.region.setRegion(rgn)

    def update(self):
        self.region.setZValue(10)
        self.region.setBounds([0,self.FS/2])
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

    def plotFFTfromPureSignal(self, freqValue):

        # para este caso no calculamos nada simplemente hardcodeamos todo

        xf = arange(0, 2000, 0.01)
        yf = zeros(len(xf))

        self.fullPlot.plot(xf, yf, pen=self.penR)
        self.zoomedPlot.plot(xf, yf, pen=self.penB)

        # self.zoomedPlot.setXRange(0, max(xf), padding=0)
        # self.fullPlot.setXRange(0, max(yf), padding=0)
        #
        # self.zoomedPlot.vb.setLimits(xMin=min(xf), xMax=max(xf), yMin=min(yf) - 1, yMax=max(yf) + 1)
        # self.fullPlot.vb.setLimits(xMin=min(xf), xMax=max(xf), yMin=min(yf) - 1, yMax=max(yf) + 1)

    # con el flag decidiremos que tipo de FFT plotear
    def PlotFFT(self, xArray, yArray, flag="DEFAULT", amplitude=0):
        self.x = xArray
        self.y = yArray
        if(flag == 'DEFAULT'):

            yf = fftpack.fft(yArray)
            xf = linspace(0.0, 1.0 / (2.0 * (1/self.FS)), int(self.FS / 2))
            self.fullPlot.plot(xf, 2.0/self.FS * abs(yf[:self.FS//2]),pen=self.penR,fillLevel=0)
            self.zoomedPlot.plot(xf, 2.0/self.FS * abs(yf[:self.FS//2]), pen=self.penB)

            self.zoomedPlot.setXRange(0, max(xf), padding=0)
            self.fullPlot.setXRange(0, max(xf), padding=0)
            # #
            self.zoomedPlot.vb.setLimits(xMin=min(xf), xMax=max(xf), yMin=0, yMax=int(max(abs(yf)))*1.5)
            self.fullPlot.vb.setLimits(xMin=min(xf), xMax=max(xf), yMin=0, yMax=int(max(abs(yf)))*1.5)


