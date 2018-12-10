from PyQt5 import QtCore, QtGui, QtWidgets
from .NewSquareDialog import Ui_NewSquareDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic
from pyqtgraph import mkPen
from numpy import arange, pi
from scipy.signal import square


class Ui_NewSuareDialogLogic(Ui_NewSquareDialog):
    def __init__(self, NewSignalDialogLogic):
        Ui_NewSquareDialog.__init__(self)
        self.FS = 48000
        self.x = arange(0, 1, 1/self.FS)
        self.y = []
        self.plot = 0

    def setupBinds(self):
        self.doubleSpinBoxAmplitude.valueChanged.connect(self.update)
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.plot = self.PreviewPlot.plotItem
        self.plot.vb.setBackgroundColor("w")

    def update(self):
        self.y = self.doubleSpinBoxAmplitude.value()*square(2*pi*self.doubleSpinBoxFrequency.value()*self.x)
        self.plot.clear()
        self.plot.plot(self.x, self.y, pen=mkPen('b', width=1.5))

    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = GraphicWidgetLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initializeBinds()
        self.ui.plotSquare(self.doubleSpinBoxAmplitude.value(), self.doubleSpinBoxFrequency.value())
        return self.PlotWindow
