from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtCore import Qt,QUrl
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow,QDialog

from PyQt5 import uic
import sys
#import requests

import logging


from main_ui import Ui_MainWindow


#MD Place here your custom imports
from dialogs.pure.NewPureSignalLogic import Ui_NewPureSignalDialogLogic
from dialogs.periodic.NewSquareDialogLogic import UiNewSuareDialogLogic
from dialogs.periodic.NewSawtoothDialogLogic import UiNewSawtoothDialogLogic
from dialogs.harmonic_synthesis.HarmonicSynthesisWidgetLogic import UiHarmonicSynthesisLogic
from dialogs.noise.NewNoiseDialogLogic import Ui_NewNoiseDialogLogic
#logger configuration
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger("MAIN")


class AppContext(ApplicationContext):
    def run(self):
        stylesheet = self.get_resource('styles.qss')
        self.app.setStyleSheet(open(stylesheet).read())
        self.window.show()
        return self.app.exec_()

    @cached_property
    def window(self):
        return MainWindow()


class MainWindow(QMainWindow):
    def __init__(self):
        self.windows = []
        self.plotWindows = []
        self.FS = 48000
        self.window = None
        self.windows = []
        self.interface = None
        # ^ global variables go here
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_menu()

    def initialize_menu(self):
        """ ALL top menu functions go here """
        self.ui.actionNew.triggered.connect(self.open_pure_signal_dialog)
        self.ui.actionSquare.triggered.connect(self.open_square_signal_dialog)
        self.ui.actionSawtooth.triggered.connect(self.open_saw_signal_dialog)
        #MD change this name to Free Harmonic Synthesis
        self.ui.actionFree.triggered.connect(self.open_hs_signal_dialog)
        self.ui.actionWhite.triggered.connect(self.open_noise_signal_dialog)
        log.info("header menu ok")

    """DIALOGS PLACED HERE"""

    def open_test_dialog(self):
        self.window = QDialog()
        self.window.show()

    def open_pure_signal_dialog(self):
        log.info("pure opened")
        self.window = QDialog()
        self.interface = Ui_NewPureSignalDialogLogic()
        self.interface.setupUi(self.window)
        self.interface.setup_binds()
        self.interface.buttonBox.accepted.connect(self.open_plot_and_close_window)
        log.info("window added to list")
        self.windows.append(self.window)
        self.windows[len(self.windows) - 1].show()
        self.windows[len(self.windows) - 1].activateWindow()
        self.windows[len(self.windows) - 1].raise_()
        # @TODO delete windows from list when 'ok' or 'cancel' buttons are pressed

    def open_square_signal_dialog(self):
        log.info("square opened")
        self.window = QDialog()
        self.interface = UiNewSuareDialogLogic()
        self.interface.setupUi(self.window)
        self.interface.setup_binds()
        self.interface.buttonBox.accepted.connect(self.open_plot_and_close_window)
        log.info("window added to list")
        self.windows.append(self.window)
        self.windows[len(self.windows) - 1].show()
        self.windows[len(self.windows) - 1].activateWindow()
        self.windows[len(self.windows) - 1].raise_()
        # @TODO delete windows from list when 'ok' or 'cancel' buttons are pressed

    def open_saw_signal_dialog(self):
        log.info("saw opened")
        self.window = QDialog()
        self.interface = UiNewSawtoothDialogLogic()
        self.interface.setupUi(self.window)
        self.interface.setup_binds()
        self.interface.buttonBox.accepted.connect(self.open_plot_and_close_window)
        log.info("window added to list")
        self.windows.append(self.window)
        self.windows[len(self.windows) - 1].show()
        self.windows[len(self.windows) - 1].activateWindow()
        self.windows[len(self.windows) - 1].raise_()
        # @TODO delete windows from list when 'ok' or 'cancel' buttons are pressed


    def open_hs_signal_dialog(self):
        log.info("harmonic synthesis opened")
        self.window = QDialog()
        self.interface = UiHarmonicSynthesisLogic()
        self.interface.setupUi(self.window)
        self.interface.setup_binds()
        self.interface.pushButtonPlot.clicked.connect(self.open_plot_and_close_window)
        log.info("window added to list")
        self.windows.append(self.window)
        self.windows[len(self.windows) - 1].show()
        self.windows[len(self.windows) - 1].activateWindow()
        self.windows[len(self.windows) - 1].raise_()
        # @TODO delete windows from list when 'ok' or 'cancel' buttons are pressed

    def open_noise_signal_dialog(self):
        log.info("noise dialog opened")
        self.window = QDialog()
        self.interface = Ui_NewNoiseDialogLogic()
        self.interface.setupUi(self.window)
        self.interface.setup_binds()
        self.interface.buttonBox.accepted.connect(self.open_plot_and_close_window)
        log.info("window added to list")
        self.windows.append(self.window)
        self.windows[len(self.windows) - 1].show()
        self.windows[len(self.windows) - 1].activateWindow()
        self.windows[len(self.windows) - 1].raise_()
        # @TODO delete windows from list when 'ok' or 'cancel' buttons are pressed


    def open_plot_and_close_window(self):
        log.info("plot window added to list")
        plot_window = self.interface.generate_plot()
        self.plotWindows.append(plot_window)
        self.plotWindows[len(self.plotWindows) - 1].show()
        self.plotWindows[len(self.plotWindows) - 1].activateWindow()
        self.plotWindows[len(self.plotWindows) - 1].raise_()
        self.window.hide()


    """LIVE WINDOW MONITOR GO HERE"""




if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
