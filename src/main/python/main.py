from fbs_runtime.application_context import ApplicationContext, cached_property
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QMainWindow

import sys
import logging

from main_ui import Ui_MainWindow
from dialogs.pure.NewPureSignalLogic import Ui_NewPureSignalDialogLogic

# logger configuration
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
        self.ui.actionNew.triggered.connect(self.open_pure_signal_dialog)
        log.info("header menu ok")

    """DIALOGS"""

    def open_test_dialog(self):
        self.window = QtWidgets.QDialog()
        self.window.show()

    def open_pure_signal_dialog(self):
        log.info("pure opened")
        self.window = QtWidgets.QDialog()
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

    def open_plot_and_close_window(self):
        log.info("plot window added to list")
        plot_window = self.interface.generate_plot()
        self.plotWindows.append(plot_window)
        self.plotWindows[len(self.plotWindows) - 1].show()
        self.plotWindows[len(self.plotWindows) - 1].activateWindow()
        self.plotWindows[len(self.plotWindows) - 1].raise_()
        self.window.hide()


if __name__ == '__main__':
    appctxt = AppContext()
    exit_code = appctxt.run()
    sys.exit(exit_code)
