from PyQt5 import QtCore, QtGui, QtWidgets
from .NewPureSignal import Ui_PureSginalDialog
from plot.PlotWindowLogic import PlotWindowLogic
from plot.GraphicWidgetLogic import GraphicWidgetLogic
from pyqtgraph import mkPen
from numpy import arange,sin, pi

class Ui_NewPureSignalDialogLogic(Ui_PureSginalDialog):
    def __init__(self, Ui_NewPureSignalDialogLogic):
        Ui_PureSginalDialog.__init__(self)
        self.FS = 48000
        self.x=arange(0,1,1/self.FS)
        self.y=[]
        self.plot=0

    def setupBinds(self):
        self.doubleSpinBoxAmplitude.valueChanged.connect(self.update)
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.doubleSpinBoxPhase.valueChanged.connect(self.update)
        self.PreviewPlot.setBackground(background="w")
        self.plot = self.PreviewPlot.plotItem
        

    
    def update(self):
        self.y=self.doubleSpinBoxAmplitude.value()*sin(2*pi*self.doubleSpinBoxFrequency.value()*self.x+(self.doubleSpinBoxPhase.value()*2*pi))
        self.labelFormula.setText("%.2fsin(2π%.2ft+%.2fπ)"%(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrequency.value(),self.doubleSpinBoxPhase.value()))
        self.plot.clear()
        self.plot.plot(self.x,self.y,pen=mkPen('b', width=1))
        
    #generamos el plot
    # def GeneratePlot(self):
    #     self.PlotWindow = QtWidgets.QWidget()
    #     self.ui = PlotWindowLogic(self)
    #     self.ui.setupUi(self.PlotWindow)
    #     self.ui.initBindings()
    #     self.ui.PlotSin(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrequency.value(),self.doubleSpinBoxPhase.value())
    #     return self.PlotWindow

    def GeneratePlot(self):
        self.PlotWindow = QtWidgets.QWidget()
        self.ui = GraphicWidgetLogic(self)
        self.ui.setupUi(self.PlotWindow)
        self.ui.initializeBinds()
        self.ui.PlotSin(self.doubleSpinBoxAmplitude.value(),self.doubleSpinBoxFrequency.value(),self.doubleSpinBoxPhase.value(),"PURE")
        return self.PlotWindow