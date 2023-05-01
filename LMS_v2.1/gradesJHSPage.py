from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QColor

from PyQt6.uic import loadUi
from absPath import resource_path


class GradesJHS(QFrame):
    def __init__(self):
        super(GradesJHS, self).__init__()
        # Load UI file
        loadUi(resource_path('ui\\gradesJHS.ui'), self)
        self.grades_jhs_widgets()

    def grades_jhs_widgets(self):
        # Initialize widgets inside JHS Grades Frame
        self.jhs_side_frame = self.findChild(QFrame, "jhsSideFrame")
        self.jhs_table_frame = self.findChild(QFrame, "jhsGradeTable")
        self.jhs_table = self.findChild(QTableWidget, "gradeJHSTable")

        # Drop shadow effect for sideframe and main table
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(15)
        self.shadowSide.setXOffset(0)
        self.shadowSide.setYOffset(0)
        self.shadowSide.setColor(QColor(100, 100, 100, 255))
        self.jhs_table_frame.setGraphicsEffect(self.shadowSide)

        # Styling jhs table widget
        self.jhs_table.horizontalHeader().setFixedHeight(50)
        self.jhs_table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.jhs_table.verticalHeader().setStyleSheet("QHeaderView::section:vertical{background-color: rgb(255,255,255); \ "
                                                      "border-bottom: 1px solid rgb(230,230,230);}")
        for i in range(5):
            if i == 4:
                self.jhs_table.setColumnWidth(i, 120)
            else:
                self.jhs_table.setColumnWidth(i, 70)





