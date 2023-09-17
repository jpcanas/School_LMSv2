from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QTableWidget, QHeaderView, \
    QTableWidgetItem, QLabel, QPushButton
from PyQt6.QtCore import Qt
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
        self.jhsGradeTable_frame = self.findChild(QFrame, "jhsGradeTable")
        self.jhsGradeTable = self.findChild(QTableWidget, "gradeJHSTable")
        self.updGradeJHSBtn = self.findChild(QPushButton, "updGradeJHS")
        self.clrGradeJHSBtn = self.findChild(QPushButton, "clrGradeJHS")

        self.gradeSecJHS = self.findChild(QLabel, "gradeSecJHS")
        self.advJHS = self.findChild(QLabel, "advJHS")
        self.syJHS = self.findChild(QLabel, "syJHS")
        self.lrn_JHS = self.findChild(QLabel, "lrn_JHS")
        self.name_JHS = self.findChild(QLabel, "name_JHS")
        self.studentJHSTable = self.findChild(QTableWidget, "studentJHSTable")
        self.lblSelection = self.findChild(QLabel, "lblSelection")
        self.btnUnselect = self.findChild(QPushButton, "btnUnselect")

        # Drop shadow effect for side frame and main table
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(15)
        self.shadowSide.setXOffset(0)
        self.shadowSide.setYOffset(0)
        self.shadowSide.setColor(QColor(100, 100, 100, 255))
        self.jhsGradeTable_frame.setGraphicsEffect(self.shadowSide)

        # Styling jhs table widget
        self.jhsGradeTable.horizontalHeader().setFixedHeight(50)
        self.jhsGradeTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # self.jhsGradeTable.verticalHeader().setStyleSheet("QHeaderView::section:vertical{background-color: rgb(255,255,255); \ "
        #                                               "border-bottom: 1px solid rgb(230,230,230);}")
        for i in range(5):
            if i == 4:
                self.jhsGradeTable.setColumnWidth(i, 120)
            else:
                self.jhsGradeTable.setColumnWidth(i, 70)

        #  other initialization
        self.selectedLearnerJHS = []
        self.selectedRow = -1
        self.btnUnselect.hide()

    def show_jhsLearner(self, jhsGradeData):  # displaying Learner's name and LRN to the left side table
        if len(jhsGradeData) != 0:
            self.studentJHSTable.setRowCount(0)
            for i, row in enumerate(jhsGradeData):
                self.rowcount = self.studentJHSTable.rowCount()
                self.studentJHSTable.insertRow(self.rowcount)

                for column, val in enumerate(row[0:2]):
                    self.studentJHSTable.setItem(i, column, QTableWidgetItem(str(val)))

        self.btnUnselect.clicked.connect(lambda: self.clearJHSSelection())
        self.studentJHSTable.cellClicked.connect(lambda: self.clickedJHSLearner_table(jhsGradeData))

    def clickedJHSLearner_table(self, jhsGradeData):
        if self.studentJHSTable.selectedItems():  # selecting names from studentJHSTable
            self.selected_jhsNames = []
            for i in self.studentJHSTable.selectedItems():
                self.selected_jhsNames.append(i.text())

            # selecting data from jhs database corresponding to selected names using filter method
            selectedJhsRecord = list(filter(lambda gJhs: gJhs[0] == int(self.selected_jhsNames[0]), jhsGradeData))

            self.selectedLearnerJHS = list(selectedJhsRecord[0])
            self.lrn_JHS.setText(self.selectedLearnerJHS[2])
            self.name_JHS.setText(self.selectedLearnerJHS[1])
            self.lblSelection.setText(f"ID No. {self.selectedLearnerJHS[0]} selected")
            self.btnUnselect.show()
            self.selectedRow = self.getRowBasedOnSelectedItem(self.selectedLearnerJHS[0])

            self.displayToJHSGradeTable(self.selectedLearnerJHS)

    def displayToJHSGradeTable(self, selectedLearnerJHS):  # displaying grade to the right side table
        for gradeRow in range(13):  # display to grades table
            for gradeColumn in range(5):
                self.jhsGradeTable.setItem(gradeRow, gradeColumn, QTableWidgetItem(""))
                jhsItemInt = selectedLearnerJHS[(6 + gradeColumn) + (5 * gradeRow)]
                if jhsItemInt is None:
                    self.jhsGradeTable.setItem(gradeRow, gradeColumn, QTableWidgetItem(""))
                else:
                    jhsItem = QTableWidgetItem(str(jhsItemInt))
                    self.jhsGradeTable.setItem(gradeRow, gradeColumn, jhsItem)
                    jhsItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            # show remarks
            if gradeRow < 8:
                finalGrade = selectedLearnerJHS[10 + (gradeRow * 5)]
                if finalGrade is not None:
                    remarks = QTableWidgetItem("PASSED" if finalGrade >= 75.0 else "FAILED")
                    self.jhsGradeTable.setItem(gradeRow, 5, remarks)
                    remarks.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                else:
                    self.jhsGradeTable.setItem(gradeRow, 5, QTableWidgetItem(""))

    def updJHSGrade(self):
        if len(self.selectedLearnerJHS) != 0:
            gJHSTableData = []  # initialize gJHSTableData list
            for tableRow in range(12):
                for tableColumn in range(4):  # (Q1 to Q4) excluding final grade
                    if tableRow == 7:  # skip MAPEH row
                        continue
                    tableItem = self.jhsGradeTable.item(tableRow, tableColumn)
                    gJHSTableData.append(tableItem.text().strip())  # remove whitespace
            validGrade = True
            for gJHSTableItem in gJHSTableData:
                if not (gJHSTableItem.isdigit() or gJHSTableItem == ''):
                    gJHSTableData = [gJHSTableItem]  # append the error grade to list
                    validGrade = False
                    break

            if validGrade:
                gJHSTableData.append(self.selectedLearnerJHS[0])  # append selected JHS ID
                return tuple(gJHSTableData)
            else:
                return gJHSTableData
        else:
            return None

    def getRowBasedOnSelectedItem(self, learnerId):
        selectedRow = -1
        for row in range(self.studentJHSTable.rowCount()):
            idItem = self.studentJHSTable.item(row, 0)
            if idItem is not None and int(idItem.text()) == learnerId:
                selectedRow = row
                break

        return selectedRow

    def clearJHSSelection(self):
        self.studentJHSTable.clearSelection()
        self.jhsGradeTable.clearSelection()
        self.selectedLearnerJHS = []
        self.lblSelection.setText("No Selection")
        self.btnUnselect.hide()
        self.lrn_JHS.setText("")
        self.name_JHS.setText("")
        for gradeRow in range(13):  # clear grades table -> alternative  clearContents() removes all items
            for gradeColumn in range(6):
                self.jhsGradeTable.setItem(gradeRow, gradeColumn, QTableWidgetItem(""))

    def config_jhsGradeDisplay(self, classDB):
        self.gradeSecJHS.setText(f"Grade {classDB[5]} - {classDB[6]}")
        self.advJHS.setText(f"Adviser: {classDB[7]}")
        self.syJHS.setText(f"S/Y: {classDB[2]}")
