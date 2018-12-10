from PyQt5 import QtCore, QtGui, QtWidgets
from .NewSawtoothDialog import Ui_NewSawtoothDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic
from pyqtgraph import mkPen
from numpy import arange, pi
from scipy.signal import sawtooth

class Ui_NewSawtoothDialogLogic(Ui_NewSawtoothDialog):
    def __init__(self, NewSignalDialogLogic):
        Ui_NewSawtoothDialog.__init__(self)
        self.FS = 48000
        self.x=arange(0,1,1/self.FS)
        self.y=[]
        self.plot=0

    def setupBinds(self):
        self.doubleSpinBoxAmplitude.valueChanged.connect(self.update)
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.plot = self.PreviewPlot.plotItem
        self.plot.vb.setBackgroundColor("w")

    def update(self):
        self.y=self.doubleSpinBoxAmplitude.value()*sawtooth(2*pi*self.doubleSpinBoxFrequency.value()*self.x)
        self.plot.clear()
        self.plot.plot(self.x,self.y,pen=mkPen('b', width=1.5))

    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = GraphicWidgetLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initializeBinds()
        self.ui.plotSawtooth(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrequency.value())
        return self.PlotWindow