from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt6.QtCore import Qt
from PyQt6 import QtGui
from PyQt6 import uic
import sys

from absPath import resource_path
from uiFunctions import UIFunctions


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi(resource_path('ui\\ui_mainWindow.ui'), self)

        self.setWindowTitle("MNHS Learner Management System")
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        self.main_functions = UIFunctions(self)

        self.header = self.findChild(QFrame, "title_InputFrame")

        # initialize mouse position
        self.mousePos = None

        # self.initWidgetsUI()
        self.show()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        # Check if the mouse is pressed within the header frame
        if event.button() == Qt.MouseButton.LeftButton and self.header.geometry().contains(event.pos()):
            # Capture the mouse position on mouse press
            self.mousePos = event.globalPosition().toPoint()
            event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent) -> None:
        # Move the window on mouse drag
        if event.buttons() == Qt.MouseButton.LeftButton and self.mousePos is not None:
            self.move(self.pos() + event.globalPosition().toPoint() - self.mousePos)
            self.mousePos = event.globalPosition().toPoint()
            event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
