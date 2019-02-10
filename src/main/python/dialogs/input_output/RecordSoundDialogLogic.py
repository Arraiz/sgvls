from .RecordSoundDialog import Ui_RecordSoundDialog
from utils.GraphicWidgetLogic import GraphicWidgetLogic
import pyaudio
from PyQt5 import QtWidgets
from pyqtgraph import mkPen
import wave
import numpy as np
import simpleaudio as sa


class Ui_RecordSoundDialogLogic(Ui_RecordSoundDialog):
    def __init__(self):
        # Default settings
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 1
        self.FS = 48000
        self.RECORD_SECONDS = 2
        self.WAVE_OUTPUT_FILENAME = "record.wav"
        self.x = []
        self.y = []
        self.frames = []
        self.p = 0
        self.amplitude = []
        self.audio=[]

    def setup_binds(self):
        self.graphicsView.setBackground(background="w")
        self.pushButtonRecord.clicked.connect(self.record)
        self.pushButtonPlay.clicked.connect(self.play)
        self.pushButtonSave.clicked.connect(self.saveFile)

    def record(self):

        self.LabelStatus.setText(
            "Recording: "+str(self.RECORD_SECONDS)+" at "+str(self.FS))

        self.p = pyaudio.PyAudio()

        # valores de grabacion del usuario
        self.FS = int(self.doubleSpinBoxFrequency.value())
        self.RECORD_SECONDS = int(self.doubleSpinBoxDuration.value())

        print(str(self.FS) + " " + str(self.RECORD_SECONDS))
        self.frames = []
        self.data = []
        self.amplitude = []
        self.y = []
        stream = self.p.open(format=self.FORMAT,
                             channels=self.CHANNELS,
                             rate=self.FS,
                             input=True,
                             frames_per_buffer=self.CHUNK)

        for i in range(0, int(self.FS / self.CHUNK * self.RECORD_SECONDS)):
            data = stream.read(self.CHUNK)
            self.frames.append(data)

        self.LabelStatus.setText("Record Finished")

        stream.stop_stream()
        stream.close()
        self.p.terminate()

        self.frames = b''.join(self.frames)

        self.amplitude = np.fromstring(self.frames, np.int16)
        self.y = self.amplitude
        duration = len(self.y)/self.FS

        self.x = np.arange(0, duration, 1 / self.FS)

        self.graphicsView.plotItem.clear()
        self.graphicsView.plot(self.x, self.amplitude, pen=mkPen('b', width=1))
        self.graphicsView.setLabel('bottom','Time (s)')
        self.graphicsView.setLabel('left', 'Amplitude')
        self.graphicsView.setLimits(xMin=min(self.x),xMax=max(self.x),yMin=min(self.amplitude),yMax=max(self.amplitude))

    def play(self):
        self.audio=self.amplitude
        # convert to 16-bit data
        self.audio = self.audio.astype(np.int16)
        # start playback
        play_obj = sa.play_buffer(self.audio, 1, 2, self.FS)
        # wait for playback to finish before exiting
        play_obj.wait_done()

    def saveFile(self):
        qfd = QtWidgets.QFileDialog()
        fileName = QtWidgets.QFileDialog.getSaveFileName(qfd, "Save File")

        # print("ruta"+str(fileName))
        # devuelve un array con 2 elementos el primero es la ruta
        wf = wave.open(str(fileName[0]), 'wb')
        wf.setnchannels(self.CHANNELS)
        wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
        wf.setframerate(self.FS)
        wf.writeframes(self.frames)
        wf.close()
        self.LabelStatus.setText("Saved OK.")
    

    def generate_plot(self, flag: str = "PURE"):
        self.plot_window = QtWidgets.QWidget()
        self.plot_window.setWindowTitle('Recorded Signal')
        self.graph_widget = GraphicWidgetLogic()
        self.graph_widget.setupUi(self.plot_window)
        self.graph_widget.freq_label.setText('Recorded Signal')
        flag="DEFAULT"
        self.graph_widget.init_binds()
        self.graph_widget.plotHarmonic(self.x, self.audio)
        return self.plot_window
