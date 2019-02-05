from PyQt5 import QtWidgets
from pyqtgraph import mkPen
from numpy import arange, pi, cos, sin
from scipy.signal import square

import logging

from utils.GraphicWidgetLogic import GraphicWidgetLogic
from .HarmonicSynthesisWidget import Ui_FreeHarmSynthWidget

# logger configuration
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("NEW HARMONIC SIGNAL")


class UiHarmonicSynthesisLogic(Ui_FreeHarmSynthWidget):
    def __init__(self):
        log.info("window opened")
        self.y_axis = []
        self.FS: int = 48000
        log.debug("FS:48000 deberia ser almacenada en algun fichero de configuracion y no hardcodeada")
        # @TODO make FS freaded froma  conf file
        self.x_axis = arange(0, 1, 1 / self.FS)
        self.graph_widget = None
        self.plot_window = None
        self.plot = 0
        self.freq_bias: float = 0.01

    def setup_binds(self):

        self.PlotPreview.setBackground(background="w")

        self.FreqVSlider.valueChanged.connect(self.update)
        self.FreqSpinBox.valueChanged.connect(self.update)

        self.FreqVSlider_2.valueChanged.connect(self.update)
        self.FreqSpinBox_2.valueChanged.connect(self.update)

        self.FreqVSlider_3.valueChanged.connect(self.update)
        self.FreqSpinBox_3.valueChanged.connect(self.update)

        self.FreqVSlider_4.valueChanged.connect(self.update)
        self.FreqSpinBox_4.valueChanged.connect(self.update)

        self.FreqVSlider_5.valueChanged.connect(self.update)
        self.FreqSpinBox_5.valueChanged.connect(self.update)

        self.FreqVSlider_6.valueChanged.connect(self.update)
        self.FreqSpinBox_6.valueChanged.connect(self.update)

        self.FreqVSlider_7.valueChanged.connect(self.update)
        self.FreqSpinBox_7.valueChanged.connect(self.update)

        self.FreqVSlider_8.valueChanged.connect(self.update)
        self.FreqSpinBox_8.valueChanged.connect(self.update)

        self.FreqVSlider_9.valueChanged.connect(self.update)
        self.FreqSpinBox_9.valueChanged.connect(self.update)

        self.FreqVSlider_10.valueChanged.connect(self.update)
        self.FreqSpinBox_10.valueChanged.connect(self.update)

        self.pushButtonPlot.clicked.connect(self.generate_plot)
        log.info("binds ok")

    def update(self):
        """THE FORMULA TO RULE THE WORRRRLDDDDD"""
        self.PlotPreview.clear()
        self.y_axis = (self.freq_bias * self.FreqVSlider.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox.value())) + (self.freq_bias * self.FreqVSlider_2.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_2.value())) + (self.freq_bias * self.FreqVSlider_3.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_3.value())) + (self.freq_bias * self.FreqVSlider_4.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_4.value())) + (self.freq_bias * self.FreqVSlider_5.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_5.value())) + (self.freq_bias * self.FreqVSlider_6.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_6.value())) + (self.freq_bias * self.FreqVSlider_7.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_7.value())) + (self.freq_bias * self.FreqVSlider_8.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_8.value())) + (self.freq_bias * self.FreqVSlider_9.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_9.value())) + (self.freq_bias * self.FreqVSlider_10.value() * cos(
            2 * pi * self.x_axis * self.FreqSpinBox_10.value()))
        self.PlotPreview.plotItem.plot(self.x_axis, self.y_axis, pen=mkPen('r', width=1))

    def generate_plot(self):
        self.plot_window = QtWidgets.QWidget()
        self.graph_widget = GraphicWidgetLogic()
        self.graph_widget.setupUi(self.plot_window)
        self.graph_widget.init_binds()
        title='Freqs: '+str(
            self.FreqSpinBox.value())+','+str(
            self.FreqSpinBox_2.value())+','+str(
            self.FreqSpinBox_3.value())+','+str(
            self.FreqSpinBox_4.value())+','+str(
            self.FreqSpinBox_5.value())+','+str(
            self.FreqSpinBox_6.value())+','+str(
            self.FreqSpinBox_7.value())+','+str(
            self.FreqSpinBox_8.value())+','+str(
            self.FreqSpinBox_9.value())+','+str(
            self.FreqSpinBox_10.value())

        self.graph_widget.freq_label.setText(title)
        self.graph_widget.plotHarmonic(self.x_axis, self.y_axis)
        return self.plot_window
