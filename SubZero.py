import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QTextEdit
from PyQt5.QtCore import QThread, pyqtSignal, pyqtSlot
import speech_recognition as sr
from googletrans import Translator
import time


class AudioProcessor(QThread):
    audioText = pyqtSignal(str)

    def __init__(self, source, speech, target):
        super().__init__()
        self.source = source
        self.speech = speech
        self.target = target

    def run(self):
        r = sr.Recognizer()
        mic = sr.Microphone(device_index=self.source)
        translator = Translator()
        last_time = time.time()
        while True:
            with mic as source:
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language=self.speech)
                self.audioText.emit(text)
                if time.time() - last_time > 5:
                    self.audioText.emit("")
                    last_time = time.time()
                if text:
                    translation = translator.translate(text, dest=self.target).text
                    self.audioText.emit(translation)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                pass


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Speech to Text'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        sourceLabel = QLabel('Audio Input Source', self)
        sourceLabel.move(20, 20)
        self.sourceCombo = QComboBox(self)
        self.sourceCombo.move(150, 20)
        self.sourceCombo.addItem('Default')
        for i, name in enumerate(sr.Microphone.list_microphone_names()):
            self.sourceCombo.addItem(name)

        speechLabel = QLabel('Speech Language', self)
        speechLabel.move(20, 60)
        self.speechCombo = QComboBox(self)
        self.speechCombo.move(150, 60)
        self.speechCombo.addItem('English')
        self.speechCombo.addItem('Russian')

        targetLabel = QLabel('Translation Language', self)
        targetLabel.move(20, 100)
        self.targetCombo = QComboBox(self)
        self.targetCombo.move(150, 100)
        self.targetCombo.addItem('English')
        self.targetCombo.addItem('Russian')

        self.textEdit = QTextEdit(self)
        self.textEdit.move(20, 140)
        self.textEdit.resize(560, 200)
        self.textEdit.setReadOnly(True)

        self.startButton = QPushButton('Start', self)
        self.startButton.move(500, 60)

