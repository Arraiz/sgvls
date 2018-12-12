from PyQt5 import QtWidgets
from .NewSawtoothDialog import Ui_NewSawtoothDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic
from pyqtgraph import mkPen
from numpy import arange, pi
from scipy.signal import sawtooth

import logging

# logger configuration
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("NEW SAW SIGNAL")


class UiNewSawtoothDialogLogic(Ui_NewSawtoothDialog):
    def __init__(self):
        log.info("window opened")
        self.y_axis = []
        self.FS: int = 48000
        log.debug("FS:48000 deberia ser almacenada en algun fichero de configuracion y no hardcodeada")
        # @TODO make FS freaded froma  conf file
        self.x_axis = arange(0, 1, 1 / self.FS)
        self.graph_widget = None
        self.plot_window = None

    def setup_binds(self):
        self.doubleSpinBoxAmplitude.valueChanged.connect(self.update)
        self.doubleSpinBoxFrequency.valueChanged.connect(self.update)
        self.PreviewPlot.setBackground(background="w")

    def update(self):
        self.y_axis = self.doubleSpinBoxAmplitude.value() * sawtooth(
            2 * pi * self.doubleSpinBoxFrequency.value() * self.x_axis)
        self.PreviewPlot.clear()
        self.PreviewPlot.plot(self.x_axis, self.y_axis, pen=mkPen('b', width=1.5))

    def generate_plot(self):
        self.plot_window = QtWidgets.QWidget()
        self.graph_widget = GraphicWidgetLogic()
        self.graph_widget.setupUi(self.plot_window)
        self.graph_widget.init_binds()
        self.graph_widget.plotSawtooth(self.doubleSpinBoxAmplitude.value(), self.doubleSpinBoxFrequency.value())
        return self.plot_window
