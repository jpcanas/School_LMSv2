from PyQt6.QtWidgets import QDialog, QPushButton, QLineEdit, QRadioButton, QComboBox, QListWidget, QFileDialog, QMessageBox
from PyQt6 import uic
import sys
import time
import os
from absPath import resource_path

from LMSdataBackend import schoolClass_CRUD
from LMSdataBackend import gradeJHS_CRUD
from LMSdataBackend import gradeSHS_CRUD
from LMSdataBackend import mainDb_Create
from LMSdataBackend import cardExcelExport

from LMSUiFrontend import loadingWindow


class CardExportWindow(QDialog):
    def __init__(self, parent=None):
        super(CardExportWindow, self).__init__(parent)
        uic.loadUi(resource_path('ui\\cardExportDialog.ui'), self)
        self.setWindowTitle("Export to excel card")

        # Initialize widgets
        self.btnFilePath = self.findChild(QPushButton, "btnFilePath")
        self.txtFilePath = self.findChild(QLineEdit, "txtFilePath")
        self.radioBtnSelectAll = self.findChild(QRadioButton, "radioBtnSelectAll")
        self.radioBtnSelectFew = self.findChild(QRadioButton, "radioBtnSelectFew")
        self.expBtn = self.findChild(QPushButton, "expBtn")

        self.activeClass = mainDb_Create.viewDbNames(1)[0]
        self.className = self.activeClass[1]
        self.classData = schoolClass_CRUD.viewClassData(self.className)[0]
        self.gradesData = []

        # Events
        self.btnFilePath.clicked.connect(self.openFilePath)
        self.expBtn.clicked.connect(self.exportCard)
        self.radioBtnSelectAll.toggled.connect(lambda: self.radioState(self.radioBtnSelectAll))
        self.radioBtnSelectFew.toggled.connect(lambda: self.radioState(self.radioBtnSelectFew))

    def radioState(self, r):
        if r.isChecked() and r.text() == "SELECT ALL LEARNERS":
            print("all selected")
        elif r.isChecked() and r.text() == "SELECT LEARNERS FROM LIST":
            print("few selected")

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

    def checkTemplate(self):
        jhsTemplate = resource_path("templates\\card_temp_JHSver2.xlsx")
        shsTemplate = resource_path("templates\\card_temp_SHSver2.xlsx")
        if os.path.exists(jhsTemplate) and os.path.exists(shsTemplate):
            return True
        else:
            return False

    def exportCard(self):
        filePath = self.txtFilePath.text().strip()
        if filePath != "" and self.checkTemplate():
            if os.path.exists(filePath) and os.path.isdir(filePath):
                self.loading = loadingWindow.LoadingWindow(filePath, self.getGrades())
                self.loading.show()
                self.loading.doneLoading.connect(lambda: self.close())
                self.loading.processLoading()
                self.expBtn.setEnabled(False)
                self.btnFilePath.setEnabled(False)
            else:
                self.showMessage("Not Valid Path", "The selected folder is not valid", QMessageBox.Icon.Warning)

        elif filePath == "":
            self.showMessage("No Directory", "Please select a directory/folder to save", QMessageBox.Icon.Warning)
        elif not self.checkTemplate():
            self.showMessage("No Template", "Excel template does not found or has been moved.", QMessageBox.Icon.Warning)

    def showMessage(self, title, message, icon):  # warning message box
        msgBox = QMessageBox(text=message, parent=self)
        msgBox.setWindowTitle(title)
        # icons (QMessageBox.Icon.Question, QMessageBox.Icon.Information,
        # QMessageBox.Icon.Warning, QMessageBox.Icon.Critical)
        msgBox.setIcon(icon)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        msgBox.exec()

