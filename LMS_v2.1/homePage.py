from PyQt6.QtWidgets import QFrame, QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

from PyQt6.uic import loadUi
from absPath import resource_path


class Home(QFrame):
    def __init__(self):
        super(Home, self).__init__()
        # Load the UI file
        loadUi(resource_path('ui\\home.ui'), self)

        self.homeWidgets()

    def homeWidgets(self):
        # Initialize widgets inside Home Frame
        self.homeProfileBtn = self.findChild(QPushButton, "homeProfileBtn")  # Home page to Profile Page Button
        self.homeGradesBtn = self.findChild(QPushButton, "homeGradesBtn")  # Home page to Grades Page Button
        self.homeAttendanceBtn = self.findChild(QPushButton, "homeAttendanceBtn")  # Home page to Attendance Page Button
        self.sideFrame = self.findChild(QFrame, "side_frame")

        # Drop shadow effect for sideframe
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(5)
        self.shadowSide.setXOffset(3)
        self.shadowSide.setYOffset(3)
        self.shadowSide.setColor(QColor(200, 200, 200, 255))
        self.sideFrame.setGraphicsEffect(self.shadowSide)
