from PyQt6.QtWidgets import QFrame, QPushButton, QGraphicsDropShadowEffect, QLabel, QComboBox
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
        self.homeOVBtn = self.findChild(QPushButton, "homeOVBtn")  # Home page to Observed Values Page Button
        self.sideFrame = self.findChild(QFrame, "side_frame")
        self.lblSchoolName = self.findChild(QLabel, "school_name")

        self.lblHomeDepartment = self.findChild(QLabel, "lblHomeDepartment")
        self.lblHomeGradeSectionSY = self.findChild(QLabel, "lblHomeGradeSectionSY")
        self.lblHomeAdviser = self.findChild(QLabel, "lblHomeAdviser")
        self.createNewClassBtn = self.findChild(QPushButton, "btnCreateNewClass")

        self.lblLearnerCount = self.findChild(QLabel, "lblLearnerCount")

        self.btnOpenPrevClass = self.findChild(QPushButton, "btnOpenPrevClass")
        self.prevClassComboBox = self.findChild(QComboBox, "prevClassComboBox")

        self.btnExportCard = self.findChild(QPushButton, "btnExportCard")

        # Drop shadow effect for sideframe
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(5)
        self.shadowSide.setXOffset(3)
        self.shadowSide.setYOffset(3)
        self.shadowSide.setColor(QColor(200, 200, 200, 255))
        self.sideFrame.setGraphicsEffect(self.shadowSide)

    def config_HomeDisplay(self, schoolDB, classDB):
        self.lblSchoolName.setText(schoolDB[1])
        self.lblHomeDepartment.setText(f"{classDB[1]} DEPARTMENT")
        self.lblHomeGradeSectionSY.setText(f"Grade {classDB[5]} - {classDB[6]} {classDB[2]}")
        self.lblHomeAdviser.setText(classDB[7])

