from PyQt6.QtWidgets import QDialog, QPushButton, QLineEdit, QRadioButton, QComboBox, QListWidget, QFileDialog
from PyQt6 import uic
import sys

from absPath import resource_path

from LMSdataBackend import schoolClass_CRUD
from LMSdataBackend import gradeJHS_CRUD
from LMSdataBackend import gradeSHS_CRUD
from LMSdataBackend import mainDb_Create
from LMSdataBackend import cardExcelExport


class CardExportWindow(QDialog):
    def __init__(self, parent=None):
        super(CardExportWindow, self).__init__(parent)
        uic.loadUi(resource_path('ui\\cardExportDialog.ui'), self)
        self.setWindowTitle("Export to excel card")

        # Initialize widgets
        self.btnFilePath = self.findChild(QPushButton, "btnFilePath")
        self.txtFilePath = self.findChild(QLineEdit, "txtFilePath")
        self.radioBtnSelectAl = self.findChild(QRadioButton, "radioBtnSelectAl")
        self.radioBtnSelectFew = self.findChild(QRadioButton, "radioBtnSelectFew")
        self.expBtn = self.findChild(QPushButton, "expBtn")

        self.activeClass = mainDb_Create.viewDbNames(1)[0]
        self.className = self.activeClass[1]
        self.classData = schoolClass_CRUD.viewClassData(self.className)[0]
        self.gradesData = []

        # Events
        self.btnFilePath.clicked.connect(self.openFilePath)
        self.expBtn.clicked.connect(self.exportCard)

    def openFilePath(self):
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory to save"))
        self.txtFilePath.setText(folder)

    def getGrades(self):
        if self.classData[1] == 'JUNIOR HIGH SCHOOL':
            self.gradesData = gradeJHS_CRUD.viewGradesJHSData(self.className)
        else:
            shsGradesSem1 = gradeSHS_CRUD.viewGradesSHSData(self.className, 1)
            shsGradesSem2 = gradeSHS_CRUD.viewGradesSHSData(self.className, 2)
            self.gradesData = self.joinSem1Sem2Data(shsGradesSem1, shsGradesSem2)

        return self.gradesData

    def joinSem1Sem2Data(self, sem1Grade, sem2Grade):
        sem1GradesBasic = []
        sem2GradesBasic = []
        for s in sem1Grade:
            sList = list(s)
            sTuple = tuple(sList[:5])
            sem1GradesBasic.append(sTuple)
        for r in sem2Grade:
            rList = list(r)
            rTuple = tuple(rList[:5])
            sem2GradesBasic.append(rTuple)

        sem1Set = set(sem1GradesBasic)
        sem2Set = set(sem2GradesBasic)
        sem1sem2Datas = list(sem1Set.union(sem2Set))
        sem1sem2Sorted = sorted(sem1sem2Datas, key=lambda item: item[1])

        return sem1sem2Sorted

    def exportCard(self):
        if self.txtFilePath.text().strip() != "":
            folderPath = self.txtFilePath.text().strip()
            print("Exporting...")
            v = cardExcelExport.ReportCardExport()
            v.exportCard(self.getGrades(), folderPath)
            print("Done. Check directory")
        else:
            print("Please select directory")

