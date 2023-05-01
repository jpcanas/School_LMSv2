from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QLineEdit, QListWidget, QComboBox, QStackedWidget, \
     QGraphicsDropShadowEffect, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QColor
import json

from PyQt6.uic import loadUi
from absPath import resource_path


class GradesSHS(QFrame):
    def __init__(self):
        super(GradesSHS, self).__init__()
        # Load UI file
        loadUi(resource_path('ui\\gradesSHS.ui'), self)
        self.shs_main_widgets()

    def shs_main_widgets(self):
        # Initialize widgets inside SHS Grades Frame (Main)
        self.shs_table_frame = self.findChild(QFrame, "shsGradeTable")
        self.shs_stacked = self.findChild(QStackedWidget, "shs_stackedWidget")
        self.shsSemTitle = self.findChild(QLabel, "semTitle")

        # Drop shadow effect for sideframe and main table
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(15)
        self.shadowSide.setXOffset(0)
        self.shadowSide.setYOffset(0)
        self.shadowSide.setColor(QColor(100, 100, 100, 255))
        self.shs_table_frame.setGraphicsEffect(self.shadowSide)

        # shs Pages Initialization
        self.sem1_widgets()
        self.sem2_widgets()
        self.shs_subject_widgets()
        self.shsSetPage(1, None)

    def sem1_widgets(self):  # First sem page widgets initialization
        self.sem1Table = self.findChild(QTableWidget, "sem1SubTable")
        self.sem1_editSubject = self.findChild(QPushButton, "sem1EditSubject")
        self.sem2PageBtn = self.findChild(QPushButton, "sem2PageBtn")

        self.sem1Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.sem1Table.setColumnWidth(1, 80)
        self.sem1Table.setColumnWidth(2, 80)
        self.sem1Table.setColumnWidth(3, 100)
        self.sem1Table.horizontalHeader().setFixedHeight(60)

        self.sem2PageBtn.clicked.connect(lambda: self.shsSetPage(2, None))
        self.sem1_editSubject.clicked.connect(lambda: self.shsSetPage(0, 0))

    def sem2_widgets(self):  # Second sem page widgets initialization
        self.sem2Table = self.findChild(QTableWidget, "sem2SubTable")
        self.sem2_editSubject = self.findChild(QPushButton, "sem2EditSubject")
        self.sem1PageBtn = self.findChild(QPushButton, "sem1PageBtn")

        self.sem2Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.sem2Table.setColumnWidth(1, 80)
        self.sem2Table.setColumnWidth(2, 80)
        self.sem2Table.setColumnWidth(3, 100)
        self.sem2Table.horizontalHeader().setFixedHeight(60)

        self.sem1PageBtn.clicked.connect(lambda: self.shsSetPage(1, None))
        self.sem2_editSubject.clicked.connect(lambda: self.shsSetPage(0, 1))

    def shs_subject_widgets(self):  # SHS subjects page widgets initialization
        with open("shsSubjects.json", "r") as file:  # Load shs subjects from json data
            subjects_dict = json.load(file)
        subjectList = list(subjects_dict.values())

        self.selectSubFrame = self.findChild(QFrame, "select_sub_frame")
        self.selectSubCombo = self.findChild(QComboBox, "subjectCombo")
        self.typeSubBtn = self.findChild(QPushButton, "typeSubBtn")
        self.typeSubFrame = self.findChild(QFrame, "type_sub_frame")
        self.subEntry = self.findChild(QLineEdit, "subjectEntry")
        self.selectSubBtn = self.findChild(QPushButton, "selectSubBtn")
        self.shs_subjectStacked = self.findChild(QStackedWidget, "shs_subjectStacked")
        self.typeSubFrame.hide()

        # sem1 subject page
        self.addSubBtnSem1 = self.findChild(QPushButton, "addSubBtnSem1")
        self.delRowBtnSem1 = self.findChild(QPushButton, "delRowBtnSem1")
        self.saveSubBtnSem1 = self.findChild(QPushButton, "saveSubBtnSem1")
        self.clrSubBtnSem1 = self.findChild(QPushButton, "clrSubBtnSem1")
        self.sem1subjectList = self.findChild(QListWidget, "sem1subjectList")
        # sem2 subject page
        self.addSubBtnSem2 = self.findChild(QPushButton, "addSubBtnSem2")
        self.delRowBtnSem2 = self.findChild(QPushButton, "delRowBtnSem2")
        self.saveSubBtnSem2 = self.findChild(QPushButton, "saveSubBtnSem2")
        self.clrSubBtnSem2 = self.findChild(QPushButton, "clrSubBtnSem2")
        self.sem2subjectList = self.findChild(QListWidget, "sem2subjectList")

        self.selectSubCombo.addItems(subjectList)
        self.typeSubBtn.clicked.connect(lambda: self.typeSelectOption())
        self.selectSubBtn.clicked.connect(lambda: self.typeSelectOption())
        self.saveSubBtnSem1.clicked.connect(lambda: self.shsSaveSubject(1))
        self.saveSubBtnSem2.clicked.connect(lambda: self.shsSaveSubject(2))

    def shsSetPage(self, pageIndex, subjectSem):  # Function for setting page in shs stacked widget
        self.shs_stacked.setCurrentIndex(pageIndex)
        if self.shs_stacked.currentIndex() == 0:
            self.shsSemTitle.setText("Add/Edit SHS Subjects")
            self.shs_subjectStacked.setCurrentIndex(subjectSem)
        elif self.shs_stacked.currentIndex() == 1:
            self.shsSemTitle.setText("1st Semester")
        else:
            self.shsSemTitle.setText("2nd Semester")

    def shsSaveSubject(self, semIndex):  # saving shs subjects functionality (1st and 2nd Sem)
        self.shs_stacked.setCurrentIndex(semIndex)
        if semIndex == 1:
            self.shsSemTitle.setText("1st Semester")
        else:
            self.shsSemTitle.setText("2nd Semester")

    def typeSelectOption(self):  # showing/hiding select or type subject frame
        if self.typeSubFrame.isHidden():
            self.typeSubFrame.show()
            self.selectSubFrame.hide()
        else:
            self.typeSubFrame.hide()
            self.selectSubFrame.show()
