# global imports
from PyQt5 import QtWidgets
from pyqtgraph import mkPen
from numpy import sin, pi, arange
import logging

# relative imports
from .NewPureSignal import Ui_PureSginalDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic

# logger configuration
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("NEW_PURE_SIGNAL")


class Ui_NewPureSignalDialogLogic(Ui_PureSginalDialog):
    def __init__(self):
        log.info("window opened")
        self.y_axis = []
        self.FS: int = 48000
        log.debug("FS:48000 deberia ser almacenada en algun fichero de configuracion y no hardcodeada")
        #@TODO make FS freaded froma  conf file
        self.x_axis = arange(0, 1, 1 / self.FS)
        self.graph_widget = None
        self.plot_window = None

    def setup_binds(self):
        log.info("bind ok")
        self.doubleSpinBoxAmplitude.valueChanged.connect(self.update)
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.doubleSpinBoxPhase.valueChanged.connect(self.update)
        #@TODO make background color readed  freaded from a conf file
        self.PreviewPlot.setBackground(background="w")

    def update(self):
        log.info("plot updated")
        self.y_axis = self.doubleSpinBoxAmplitude.value() * sin(
            2 * pi * self.doubleSpinBoxFrequency.value() * self.x_axis + (self.doubleSpinBoxPhase.value() * 2 * pi))
        self.labelFormula.setText("%.2fsin(2π%.2ft+%.2fπ)" % (
        self.doubleSpinBoxAmplitude.value(), self.doubleSpinBoxFrequency.value(), self.doubleSpinBoxPhase.value()))
        self.PreviewPlot.clear()
        self.PreviewPlot.plot(self.x_axis, self.y_axis, pen=mkPen('b', width=1))

    def generate_plot(self, flag: str = "PURE"):
        log.info("generating final plot")
        self.plot_window = QtWidgets.QWidget()
        self.graph_widget = GraphicWidgetLogic()
        self.graph_widget.setupUi(self.plot_window)
        self.graph_widget.init_binds()
        self.graph_widget.PlotSin(self.doubleSpinBoxAmplitude.value(), self.doubleSpinBoxFrequency.value(),
                                  self.doubleSpinBoxPhase.value(), flag)
        return self.plot_window
