from PyQt5 import QtCore, QtGui, QtWidgets
import sounddevice as sd
from RecordWindow import Ui_Dialog

class Ui_RecordWindowLogic(Ui_Dialog):
    def __init__(self, RecordWindowLogic):
        Ui_Dialog.__init__(self)