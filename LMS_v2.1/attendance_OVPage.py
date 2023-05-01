from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QTableWidget, QHeaderView
from PyQt6.QtGui import QColor

from PyQt6.uic import loadUi
from absPath import resource_path


class AttendanceOV(QFrame):
    def __init__(self):
        super(AttendanceOV, self).__init__()
        # Load UI file
        loadUi(resource_path('ui\\attendanceOV.ui'), self)
        self.attendanceOV_widgets()

    def attendanceOV_widgets(self):
        # Initialize widgets inside Attendance and OV Frame
        self.att_rightFrame = self.findChild(QFrame, "rightFrame")
        self.ovTable = self.findChild(QTableWidget, "ovTable")
        self.attendanceTable = self.findChild(QTableWidget, "attTable")

        # Drop shadow effect for right frame and main tables
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(15)
        self.shadowSide.setXOffset(0)
        self.shadowSide.setYOffset(0)
        self.shadowSide.setColor(QColor(100, 100, 100, 255))
        self.att_rightFrame.setGraphicsEffect(self.shadowSide)

        # Observe values table styling
        for i in range(4):
            self.ovTable.setColumnWidth(i, 60)

        self.ovTable.horizontalHeader().setFixedHeight(50)
        self.ovTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ovTable.horizontalHeader().setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(100, 100, 100); }")

        self.ovTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ovTable.verticalHeader().setStyleSheet("QHeaderView:section{background-color: rgb(255,255,255); \
                                                    border-bottom: 1px solid rgb(200,200,200); border-right: 1px solid rgb(200,200,200);}")

        # Attendance table styling
        self.attendanceTable.horizontalHeader().setFixedHeight(50)
        self.attendanceTable.horizontalHeader().setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(100, 100, 100); }")