from PyQt5 import QtWidgets
from pyqtgraph import mkPen
from numpy import sin, pi, arange,random
import logging

# relative imports
from .NewNoiseDialog import Ui_NoiseSignalDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic

# logger configuration
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("NEW_NOISE_SIGNAL")


#buf in lsignal amplitude in pure in
#not zoom in abajo window

class Ui_NewNoiseDialogLogic(Ui_NoiseSignalDialog):
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
        # @TODO make background color readed  freaded from a conf file
        self.whiteRadio.clicked.connect(self.update)
        self.pinkRadio.clicked.connect(self.update)
        self.brownRadio.clicked.connect(self.update)
        self.PreviewPlot.setBackground(background="w")


    def update(self):
        log.info("plot updated")
        if self.whiteRadio.isChecked():
            log.debug("white selected")
            self.white_noise()
        elif self.pinkRadio.isChecked():
            log.debug("pink selected")
        elif self.brownRadio.isChecked():
            log.debug("brown selected")


    def white_noise(self):
        self.y_axis=3*random.randn(self.FS)
        self.PreviewPlot.clear()
        self.PreviewPlot.plot(self.x_axis, self.y_axis, pen=mkPen('b', width=1))


    def generate_plot(self, flag: str = "PURE"):
        log.info("generating final plot")
        self.plot_window = QtWidgets.QWidget()
        title = 'White Noise'
        self.plot_window.setWindowTitle(title)
        self.graph_widget = GraphicWidgetLogic()
        self.graph_widget.setupUi(self.plot_window)
        self.graph_widget.freq_label.setText(title)
        flag="DEFAULT"
        self.graph_widget.init_binds()
        self.graph_widget.plot_white_noise()
        return self.plot_window