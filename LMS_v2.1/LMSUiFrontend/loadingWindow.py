from PyQt6.QtWidgets import QDialog, QLabel, QFrame, QGraphicsDropShadowEffect
from PyQt6.QtGui import QMovie, QColor
from PyQt6.QtCore import QThread, QTimer, pyqtSignal, Qt
from PyQt6 import uic
import sys

from absPath import resource_path
from LMSdataBackend import cardExcelExport


class LoadingWindow(QDialog):
    doneLoading = pyqtSignal()

    def __init__(self, path, grades, parent=None):
        super(LoadingWindow, self).__init__(parent)
        self.path = path
        self.grades = grades
        uic.loadUi(resource_path('ui\\loadingDialog.ui'), self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.loadingFrame = self.findChild(QFrame, "loadingFrame")
        self.gifPlaceholder = self.findChild(QLabel, "gifPlaceholder")
        self.loadingMsg = self.findChild(QLabel, "loadingMsg")

        # Loading GIF
        self.loading = QMovie(resource_path('assets\\rolling.gif'))
        self.checked = QMovie(resource_path('assets\\check.gif'))

        self.exportThread = ExportThread(self.path, self.grades)

        # Drop shadow effect for sideframe
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(5)
        self.shadowSide.setXOffset(3)
        self.shadowSide.setYOffset(3)
        self.shadowSide.setColor(QColor(200, 200, 200, 255))
        self.loadingFrame.setGraphicsEffect(self.shadowSide)

    def processLoading(self):
        self.gifPlaceholder.setMovie(self.loading)
        self.loadingMsg.setText("Generating Excel file...")
        self.loading.start()

        self.exportThread.finished.connect(self.processDone)
        self.exportThread.finished.connect(self.exportThread.deleteLater)
        self.exportThread.start()

    def processDone(self):
        self.loading.stop()
        self.gifPlaceholder.setMovie(self.checked)
        self.checked.start()
        self.loadingMsg.setText("Done Exporting\n Check Directory")
        QTimer.singleShot(3000, self.quitLoading)

    def quitLoading(self):
        self.checked.stop()
        self.doneLoading.emit()
        self.close()


class ExportThread(QThread):
    def __init__(self, path, grades):
        super().__init__()
        self.path = path
        self.grades = grades

    def run(self) -> None:
        v = cardExcelExport.ReportCardExport()
        v.exportCard(self.grades, self.path)
