from PyQt6.QtWidgets import QFrame, QLabel, QPushButton, QLineEdit, QListWidget, QComboBox, QStackedWidget, \
    QGraphicsDropShadowEffect, QTableWidget, QHeaderView, QTableWidgetItem, QTabWidget, QWidget, QHBoxLayout, \
    QApplication
from PyQt6.QtGui import QColor
from PyQt6.QtCore import pyqtSignal, Qt
import json

from PyQt6.uic import loadUi
from absPath import resource_path
from LMSdataBackend import shsSubjects_CRUD


class GradesSHS(QFrame):
    def __init__(self):
        super(GradesSHS, self).__init__()
        # Load UI file
        loadUi(resource_path('ui\\gradesSHS.ui'), self)
        self.shs_main_widgets()

    def shs_main_widgets(self):
        self.shsSideFrame = self.findChild(QFrame, "shsSideFrame")
        self.lblGradeSecSHS = self.findChild(QLabel, "lblGradeSecSHS")
        self.lblStrand = self.findChild(QLabel, "lblStrand")
        self.lblAdvSHS = self.findChild(QLabel, "lblAdvSHS")
        self.lblSchoolYearSHS = self.findChild(QLabel, "lblSchoolYearSHS")
        self.lrnLabelSHS = self.findChild(QLabel, "lrnLabelSHS")
        self.nameLabelSHS = self.findChild(QLabel, "nameLabelSHS")
        self.studentTableSHS = self.findChild(QTableWidget, "studentTableSHS")
        self.lblSelectionSHS = self.findChild(QLabel, "lblSelection")
        self.btnUnselectSHS = self.findChild(QPushButton, "btnUnselect")

        self.shsGradeFrame = self.findChild(QFrame, "shsGradeFrame")
        self.shsTabWidget = self.findChild(QTabWidget, "shsTabWidget")

        self.shsStackedWidgetSem1 = self.findChild(QStackedWidget, "shsStackedWidgetSem1")
        self.shsStackedWidgetSem2 = self.findChild(QStackedWidget, "shsStackedWidgetSem2")

        #  bottom widgets initialization
        self.saveSubSHSBtn = self.findChild(QPushButton, "saveSubSHSBtn")
        self.updGradeSHSBtn = self.findChild(QPushButton, "updGradeSHSBtn")

        # Drop shadow effect for sideFrame and main table
        self.shadowSide = QGraphicsDropShadowEffect()
        self.shadowSide.setBlurRadius(15)
        self.shadowSide.setXOffset(0)
        self.shadowSide.setYOffset(0)
        self.shadowSide.setColor(QColor(100, 100, 100, 255))
        self.shsGradeFrame.setGraphicsEffect(self.shadowSide)

        # Other initialization
        self.shsTabWidget.currentChanged.connect(self.onSemTabChanged)
        self.shsTabWidget.setCurrentIndex(0)
        self.btnUnselectSHS.hide()
        self.selected_shsNames = []
        self.selectedRow = -1
        self.selectedShsSem1Record = []
        self.selectedShsSem2Record = []
        self.sem1Grades = []
        self.sem2Grades = []
        self.sem1SubjectCount = 0
        self.sem2SubjectCount = 0

    # <editor-fold desc="Initializing 1st and 2nd semester widgets">
    def initializeSem1Pages(self, sem1SubjectData):
        #  sem1 widgets initialization
        if len(sem1SubjectData) == 0:  # adding shs subjects page
            self.shsStackedWidgetSem1.setCurrentIndex(0)
            self.subjectComboSem1 = self.findChild(QComboBox, "subjectComboSem1")
            self.addSubBtnSem1 = self.findChild(QPushButton, "addSubBtnSem1")
            self.subjSem1TableWidget = self.findChild(QTableWidget, "subjSem1TableWidget")
            self.addSubBtnSem1.clicked.connect(lambda: self.addSem1SubjectsToTable())

            self.subjSem1TableWidget.horizontalHeader().setFixedHeight(50)
            self.subjSem1TableWidget.setColumnWidth(0, 80)
            self.subjSem1TableWidget.setColumnWidth(1, 100)
            self.subjSem1TableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
            self.subjectComboSem1.addItems(self.loadSHSSubjects())
            self.saveSubSHSBtn.show()
            self.updGradeSHSBtn.hide()
        else:
            self.shsStackedWidgetSem1.setCurrentIndex(1)
            self.sem1GradesTable = self.findChild(QTableWidget, "sem1GradesTable")  # main shs Grades
            self.sem1GradesTable.horizontalHeader().setFixedHeight(50)
            self.sem1GradesTable.setColumnWidth(1, 70)
            self.sem1GradesTable.setColumnWidth(2, 70)
            self.sem1GradesTable.setColumnWidth(3, 100)
            self.sem1GradesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            self.sem1GradesTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # noinspection PyTypeChecker
            self.loadSubjectsToTable(sem1SubjectData, self.sem1GradesTable)
            self.sem1SubjectCount = len(sem1SubjectData)
            self.saveSubSHSBtn.hide()
            self.updGradeSHSBtn.show()

    def initializeSem2Pages(self, sem2SubjectData):
        #  sem2 widgets initialization
        if len(sem2SubjectData) == 0:  # adding shs subjects page
            self.shsStackedWidgetSem2.setCurrentIndex(0)
            self.subjectComboSem2 = self.findChild(QComboBox, "subjectComboSem2")
            self.addSubBtnSem2 = self.findChild(QPushButton, "addSubBtnSem2")
            self.subjSem2TableWidget = self.findChild(QTableWidget, "subjSem2TableWidget")
            self.addSubBtnSem2.clicked.connect(lambda: self.addSem2SubjectsToTable())

            self.subjSem2TableWidget.horizontalHeader().setFixedHeight(50)
            self.subjSem2TableWidget.setColumnWidth(0, 80)
            self.subjSem2TableWidget.setColumnWidth(1, 100)
            self.subjSem2TableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
            self.subjectComboSem2.addItems(self.loadSHSSubjects())

        else:
            self.shsStackedWidgetSem2.setCurrentIndex(1)
            self.sem2GradesTable = self.findChild(QTableWidget, "sem2GradesTable")  # main shs Grades
            self.sem2GradesTable.horizontalHeader().setFixedHeight(50)
            self.sem2GradesTable.setColumnWidth(1, 70)
            self.sem2GradesTable.setColumnWidth(2, 70)
            self.sem2GradesTable.setColumnWidth(3, 100)
            self.sem2GradesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
            self.sem2GradesTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            # noinspection PyTypeChecker
            self.loadSubjectsToTable(sem2SubjectData, self.sem2GradesTable)
            self.sem2SubjectCount = len(sem2SubjectData)

    def loadSubjectsToTable(self, subjectData: list, subjectTable: QTableWidget):
        subjectTable.setRowCount(0)
        for i, row in enumerate(subjectData):
            rowcount = subjectTable.rowCount()
            subjectTable.insertRow(rowcount)

            subjectItem = f"   {row[2]}"
            subjectTable.setItem(i, 0, QTableWidgetItem(subjectItem))

        rowcount = subjectTable.rowCount()
        subjectTable.insertRow(rowcount)
        subjectTable.setItem(rowcount, 0, QTableWidgetItem("   AVERAGE:"))

    ...

    # </editor-fold>

    def loadSHSSubjects(self) -> list:
        shsSubjectsDropDown = ["-- ADD CUSTOM SUBJECT --"]
        shsSubjData = shsSubjects_CRUD.viewSubjectsShs()
        for subject in shsSubjData:
            shsSubjectsDropDown.append(subject[2])

        return shsSubjectsDropDown

    # <editor-fold desc="1st semester adding and editing subjects">
    def addSem1SubjectsToTable(self):
        subjectName = self.subjectComboSem1.currentText()
        if subjectName != "":
            rowPosition = self.subjSem1TableWidget.rowCount()
            self.subjSem1TableWidget.insertRow(rowPosition)
            actionButtons = ActionButtonsWidget()
            if subjectName != "-- ADD CUSTOM SUBJECT --":
                subjectDatas = \
                    list(filter(lambda subject: subject[2] == subjectName, shsSubjects_CRUD.viewSubjectsShs()))[0]
                subjectCategory = subjectDatas[1]
                subjectDatasItem = QTableWidgetItem(subjectCategory)
                subjectCatItem = QTableWidgetItem(subjectName)  # set item to readonly initially
                subjectDatasItem.setFlags(subjectDatasItem.flags() & ~Qt.ItemFlag.ItemIsEditable)
                subjectCatItem.setFlags(subjectCatItem.flags() & ~Qt.ItemFlag.ItemIsEditable)

                self.subjSem1TableWidget.setCellWidget(rowPosition, 0, actionButtons)
                self.subjSem1TableWidget.setItem(rowPosition, 1, subjectDatasItem)
                self.subjSem1TableWidget.setItem(rowPosition, 2, subjectCatItem)
            else:
                actionButtons.btnActionEdit.hide()
                actionButtons.btnActionDelete.hide()
                actionButtons.btnActionDone.show()
                self.subjSem1TableWidget.setCellWidget(rowPosition, 0, actionButtons)
                self.subjSem1TableWidget.setItem(rowPosition, 1, QTableWidgetItem(""))
                self.subjSem1TableWidget.setItem(rowPosition, 2, QTableWidgetItem("[Type Subject Name here]"))

                self.editSem1SubjTableRow(actionButtons, rowPosition)  # instantly enter in edit mode

            actionButtons.deleteClicked.connect(lambda: self.deleteSem1SubjTableRow(actionButtons))
            actionButtons.editClicked.connect(lambda: self.editSem1SubjTableRow(actionButtons))
            actionButtons.doneEditClicked.connect(lambda: self.doneEditSem1SubjTableRow(actionButtons))

    def deleteSem1SubjTableRow(self, actionButtons):
        subjRow = self.subjSem1TableWidget.indexAt(actionButtons.pos()).row()
        if subjRow >= 0:
            self.subjSem1TableWidget.removeRow(subjRow)

    def editSem1SubjTableRow(self, actionButtons, blankRow=None):
        if blankRow is None:
            subjRow = self.subjSem1TableWidget.indexAt(actionButtons.pos()).row()
        else:
            subjRow = blankRow
        for col in range(self.subjSem1TableWidget.columnCount()):
            item = self.subjSem1TableWidget.item(subjRow, col)
            if item:
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.subjSem1TableWidget.setCurrentCell(subjRow, 2)

        QApplication.processEvents()  # enter edit mode when cell is selected
        self.subjSem1TableWidget.edit(self.subjSem1TableWidget.currentIndex())

    def doneEditSem1SubjTableRow(self, actionButtons):
        subjRow = self.subjSem1TableWidget.indexAt(actionButtons.pos()).row()
        for col in range(self.subjSem1TableWidget.columnCount()):
            item = self.subjSem1TableWidget.item(subjRow, col)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.subjSem1TableWidget.clearSelection()

    ...

    # </editor-fold>

    # <editor-fold desc="2nd semester adding and editing subjects">
    def addSem2SubjectsToTable(self):
        subjectName = self.subjectComboSem2.currentText()
        if subjectName != "":
            rowPosition = self.subjSem2TableWidget.rowCount()
            self.subjSem2TableWidget.insertRow(rowPosition)
            actionButtons = ActionButtonsWidget()
            if subjectName != "-- ADD CUSTOM SUBJECT --":
                subjectDatas = \
                    list(filter(lambda subject: subject[2] == subjectName, shsSubjects_CRUD.viewSubjectsShs()))[0]
                subjectCategory = subjectDatas[1]
                subjectDatasItem = QTableWidgetItem(subjectCategory)
                subjectCatItem = QTableWidgetItem(subjectName)  # set item to readonly initially
                subjectDatasItem.setFlags(subjectDatasItem.flags() & ~Qt.ItemFlag.ItemIsEditable)
                subjectCatItem.setFlags(subjectCatItem.flags() & ~Qt.ItemFlag.ItemIsEditable)

                self.subjSem2TableWidget.setCellWidget(rowPosition, 0, actionButtons)
                self.subjSem2TableWidget.setItem(rowPosition, 1, subjectDatasItem)
                self.subjSem2TableWidget.setItem(rowPosition, 2, subjectCatItem)
            else:
                actionButtons.btnActionEdit.hide()
                actionButtons.btnActionDelete.hide()
                actionButtons.btnActionDone.show()
                self.subjSem2TableWidget.setCellWidget(rowPosition, 0, actionButtons)
                self.subjSem2TableWidget.setItem(rowPosition, 1, QTableWidgetItem(""))
                self.subjSem2TableWidget.setItem(rowPosition, 2, QTableWidgetItem("[Type Subject Name here]"))

                self.editSem2SubjTableRow(actionButtons, rowPosition)  # instantly enter in edit mode

            actionButtons.deleteClicked.connect(lambda: self.deleteSem2SubjTableRow(actionButtons))
            actionButtons.editClicked.connect(lambda: self.editSem2SubjTableRow(actionButtons))
            actionButtons.doneEditClicked.connect(lambda: self.doneEditSem2SubjTableRow(actionButtons))

    def deleteSem2SubjTableRow(self, actionButtons):
        subjRow = self.subjSem2TableWidget.indexAt(actionButtons.pos()).row()
        if subjRow >= 0:
            self.subjSem2TableWidget.removeRow(subjRow)

    def editSem2SubjTableRow(self, actionButtons, blankRow=None):
        if blankRow is None:
            subjRow = self.subjSem2TableWidget.indexAt(actionButtons.pos()).row()
        else:
            subjRow = blankRow
        for col in range(self.subjSem2TableWidget.columnCount()):
            item = self.subjSem2TableWidget.item(subjRow, col)
            if item:
                item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.subjSem2TableWidget.setCurrentCell(subjRow, 2)

        QApplication.processEvents()  # enter edit mode when cell is selected
        self.subjSem2TableWidget.edit(self.subjSem2TableWidget.currentIndex())

    def doneEditSem2SubjTableRow(self, actionButtons):
        subjRow = self.subjSem2TableWidget.indexAt(actionButtons.pos()).row()
        for col in range(self.subjSem2TableWidget.columnCount()):
            item = self.subjSem2TableWidget.item(subjRow, col)
            if item:
                item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.subjSem2TableWidget.clearSelection()

    ...

    # </editor-fold>

    # <editor-fold desc="Saving subjects button functionality">
    def shsSaveSubject(self, fromSem1Subjects):  # saving shs subjects functionality (1st and 2nd Sem)m1
        if self.shsTabWidget.currentIndex() == 0 and self.shsStackedWidgetSem1.currentIndex() == 0:
            # noinspection PyTypeChecker
            sem1SubjectStatus = self.checkAndCollectSubject(self.subjSem1TableWidget, 1)
            return sem1SubjectStatus

        elif self.shsTabWidget.currentIndex() == 1 and self.shsStackedWidgetSem2.currentIndex() == 0:
            if len(fromSem1Subjects) == 0:
                sem2SubjectStatus = "Please add some subjects first on 1st Semester before proceeding with 2nd Semester"
            else:
                # noinspection PyTypeChecker
                sem2SubjectStatus = self.checkAndCollectSubject(self.subjSem2TableWidget, 2)

            return sem2SubjectStatus

    def checkAndCollectSubject(self, subjectTableWidget, sem) -> list | str:
        tableRowCount = subjectTableWidget.rowCount()
        if tableRowCount > 0:
            # checking if all entries on table are done editing (all items are not editable)
            isDoneEditing = True
            for row in range(tableRowCount):
                item = subjectTableWidget.item(row, 2)
                if item.flags() & Qt.ItemFlag.ItemIsEditable:
                    isDoneEditing = False
                    break

            if isDoneEditing:  # return list of tuple (category and subject name) - perfect case
                semSubjectList = []  # list of semSubject
                for subjectRow in range(tableRowCount):
                    semSubject = []  # list of subjectCat and Subject Name (will be converted to tuple)
                    for subjectColumn in range(2):
                        subjectItem = subjectTableWidget.item(subjectRow, subjectColumn + 1)
                        if subjectColumn == 0:  # subject category set to uppercase
                            semSubject.append(subjectItem.text().upper().strip())
                        else:
                            semSubject.append(subjectItem.text().strip())

                    semSubject.append(sem)
                    semSubjectList.append(tuple(semSubject))
                # checking if there are subjects that are custom (then add to shs Subject database)
                subjectListDataBase = shsSubjects_CRUD.viewSubjNameAndCat()
                for subjEntry in semSubjectList:
                    subjEntryCompare = list(subjEntry)
                    subjEntryCompare.pop()  # remove the sem for it to compare with database
                    subjectNotInDB = not (tuple(subjEntryCompare) in subjectListDataBase)
                    if subjectNotInDB:
                        customSubject = subjEntryCompare
                        customSubject.append("User-Defined")
                        print(f"custom subject {customSubject}")
                        shsSubjects_CRUD.addSubjectsShs(tuple(customSubject))

                return semSubjectList
            else:
                return "Some subject/s are not yet done editing"
        else:
            return "Empty subject. Add some SHS subjects"

    ...

    # </editor-fold>

    # <editor-fold desc="Clicking learner on table EVENTS">

    def shsLearnerToTable(self, semGrades):
        self.studentTableSHS.setRowCount(0)
        for i, row in enumerate(semGrades):
            self.rowcount = self.studentTableSHS.rowCount()
            self.studentTableSHS.insertRow(self.rowcount)

            for column, val in enumerate(row[0:2]):
                self.studentTableSHS.setItem(i, column, QTableWidgetItem(str(val)))

    def show_shsLearners(self, shsSem1GradesData, shsSem2GradesData):
        self.sem1Grades = shsSem1GradesData
        self.sem2Grades = shsSem2GradesData
        if len(self.sem1Grades) > 0 or len(self.sem2Grades) > 0:
            if self.shsTabWidget.currentIndex() == 0:
                self.shsLearnerToTable(self.sem1Grades)
            else:
                self.shsLearnerToTable(self.sem2Grades)

            self.btnUnselectSHS.clicked.connect(lambda: self.clearShsSelection())
            self.studentTableSHS.cellClicked.connect(lambda: self.clickedShsLearner_table())

    def clickedShsLearner_table(self):
        if self.studentTableSHS.selectedItems():  # selecting names from studentJHSTable
            self.selected_shsNames = []
            for i in self.studentTableSHS.selectedItems():
                self.selected_shsNames.append(i.text())

            self.selectedShsSem1Record = list(filter(lambda gShs: gShs[0] == int(self.selected_shsNames[0]), self.sem1Grades))
            if len(self.selectedShsSem1Record) > 0:
                self.showSem1GradeTable(self.selectedShsSem1Record[0])
                self.selectedLearnerSHS = list(self.selectedShsSem1Record[0])
                self.lrnLabelSHS.setText(self.selectedLearnerSHS[2])
                self.nameLabelSHS.setText(self.selectedLearnerSHS[1])
                self.lblSelectionSHS.setText(f"ID No. {self.selectedLearnerSHS[0]} selected")
                self.btnUnselectSHS.show()
                row = self.getRowBasedOnSelectedItem(self.selectedLearnerSHS[0])
                self.selectedRow = row

            if len(self.sem2Grades) > 0 and len(self.sem1Grades) > 0:
                self.selectedShsSem2Record = list(filter(lambda gShs: gShs[0] == int(self.selected_shsNames[0]), self.sem2Grades))
                if len(self.selectedShsSem2Record) > 0:
                    self.showSem2GradeTable(self.selectedShsSem2Record[0])
                    self.selectedLearnerSHS = list(self.selectedShsSem2Record[0])
                    self.lrnLabelSHS.setText(self.selectedLearnerSHS[2])
                    self.nameLabelSHS.setText(self.selectedLearnerSHS[1])
                    self.lblSelectionSHS.setText(f"ID No. {self.selectedLearnerSHS[0]} selected")
                    self.btnUnselectSHS.show()
                    row = self.getRowBasedOnSelectedItem(self.selectedLearnerSHS[0])
                    self.selectedRow = row


    def showSem1GradeTable(self, sem1GradesSelectedData):
        rowTableCount = self.sem1GradesTable.rowCount()
        for gradeRow in range(rowTableCount):  # display to grades table
            for gradeColumn in range(3):
                self.sem1GradesTable.setItem(gradeRow, gradeColumn+1, QTableWidgetItem(""))
                shsItemInt = sem1GradesSelectedData[(6 + gradeColumn) + (3 * gradeRow)]
                if shsItemInt is None:
                    self.sem1GradesTable.setItem(gradeRow, gradeColumn+1, QTableWidgetItem(""))
                else:
                    shsItem = QTableWidgetItem(str(shsItemInt))
                    self.sem1GradesTable.setItem(gradeRow, gradeColumn+1, shsItem)
                    shsItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def showSem2GradeTable(self, sem2GradesSelectedData):
        rowTableCount = self.sem2GradesTable.rowCount()
        for gradeRow in range(rowTableCount):  # display to grades table
            for gradeColumn in range(3):
                self.sem2GradesTable.setItem(gradeRow, gradeColumn + 1, QTableWidgetItem(""))
                shsItemInt = sem2GradesSelectedData[(6 + gradeColumn) + (3 * gradeRow)]
                if shsItemInt is None:
                    self.sem2GradesTable.setItem(gradeRow, gradeColumn + 1, QTableWidgetItem(""))
                else:
                    shsItem = QTableWidgetItem(str(shsItemInt))
                    self.sem2GradesTable.setItem(gradeRow, gradeColumn + 1, shsItem)
                    shsItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
    ...

    # </editor-fold>

    def updSHSGrade(self):
        if self.shsTabWidget.currentIndex() == 0 and self.shsStackedWidgetSem1.currentIndex() == 1:
            return self.getSemGradesToUpdate(self.selectedShsSem1Record, self.sem1GradesTable, 1)

        elif self.shsTabWidget.currentIndex() == 1 and self.shsStackedWidgetSem2.currentIndex() == 1:
            return self.getSemGradesToUpdate(self.selectedShsSem2Record, self.sem2GradesTable, 2)

    def getSemGradesToUpdate(self, selectedSemGrade, semGradeTable, sem):
        if len(selectedSemGrade) > 0:
            selectedGradeSem = selectedSemGrade[0]
            rowCount = semGradeTable.rowCount()
            gSHSTableDataSem = []
            for tableRow in range(rowCount-1):  # excluding the quarter average
                for tableColumn in range(2):
                    tableItem = semGradeTable.item(tableRow, tableColumn+1)
                    gSHSTableDataSem.append(tableItem.text().strip())  # remove whitespace

            validGrade = True
            for gSHSTableItem in gSHSTableDataSem:
                if not (gSHSTableItem.isdigit() or gSHSTableItem == ''):
                    gSHSTableDataSem = [gSHSTableItem]  # append the error grade to list
                    validGrade = False
                    break

            if validGrade:
                gSHSTableDataSem.append(rowCount)  # append table row count
                gSHSTableDataSem.append(selectedGradeSem[0])  # append selected SHS ID
                gSHSTableDataSem.append(sem)  # append semester
                return tuple(gSHSTableDataSem)
            else:
                return gSHSTableDataSem

        else:
            print("enter no selection")
            return None

    def onSemTabChanged(self, tabIndex):
        if tabIndex == 0:
            if self.shsStackedWidgetSem1.currentIndex() == 0:
                self.saveSubSHSBtn.show()
                self.updGradeSHSBtn.hide()
            else:
                self.saveSubSHSBtn.hide()
                self.updGradeSHSBtn.show()

                if len(self.sem1Grades) > 0:
                    self.shsLearnerToTable(self.sem1Grades)
                else:
                    self.studentTableSHS.clearContents()
                    self.studentTableSHS.setRowCount(0)

                if len(self.selectedShsSem1Record) > 0:
                    selectedLearner = self.selectedShsSem1Record[0]
                    row = self.getRowBasedOnSelectedItem(selectedLearner[0])
                    self.studentTableSHS.selectRow(row)
                    self.selectedRow = row
                else:
                    self.clearShsSelection()

        elif tabIndex == 1:
            self.shsLearnerToTable(self.sem1Grades)
            if self.shsStackedWidgetSem2.currentIndex() == 0:
                self.saveSubSHSBtn.show()
                self.updGradeSHSBtn.hide()
            else:
                self.saveSubSHSBtn.hide()
                self.updGradeSHSBtn.show()

                if len(self.sem2Grades) > 0:
                    self.shsLearnerToTable(self.sem2Grades)
                else:
                    self.studentTableSHS.clearContents()
                    self.studentTableSHS.setRowCount(0)

                if len(self.selectedShsSem2Record) > 0:
                    selectedLearner = self.selectedShsSem1Record[0]
                    row = self.getRowBasedOnSelectedItem(selectedLearner[0])
                    self.studentTableSHS.selectRow(row)
                    self.selectedRow = row
                else:
                    self.clearShsSelection()

    def getRowBasedOnSelectedItem(self, learnerId):
        selectedRow = -1
        for row in range(self.studentTableSHS.rowCount()):
            idItem = self.studentTableSHS.item(row, 0)
            if idItem is not None and int(idItem.text()) == learnerId:
                selectedRow = row
                break

        return selectedRow

    def clearShsSelection(self):
        self.studentTableSHS.clearSelection()
        self.selectedRow = -1
        self.btnUnselectSHS.hide()
        self.selectedShsSem1Record.clear()
        self.selectedShsSem2Record.clear()
        self.lrnLabelSHS.setText("")
        self.nameLabelSHS.setText("")
        self.lblSelectionSHS.setText("No Selection")

        for gradeRowSem1 in range(self.sem1GradesTable.rowCount()):
            for gradeColumnSem1 in range(3):
                self.sem1GradesTable.setItem(gradeRowSem1, gradeColumnSem1+1, QTableWidgetItem(""))

        if self.sem2SubjectCount > 0:
            for gradeRowSem2 in range(self.sem2GradesTable.rowCount()):
                for gradeColumnSem2 in range(3):
                    self.sem2GradesTable.setItem(gradeRowSem2, gradeColumnSem2 + 1, QTableWidgetItem(""))

    def config_shsGradeDisplay(self, classDB):
        self.lblGradeSecSHS.setText(f"Grade {classDB[5]} - {classDB[6]}")
        self.lblStrand.setText(classDB[8])
        self.lblAdvSHS.setText(f"Adviser: {classDB[7]}")
        self.lblSchoolYearSHS.setText(f"S/Y: {classDB[2]}")


# <editor-fold desc="ActionButtonsWidget Class">
class ActionButtonsWidget(QWidget):
    # Custom signals when buttons are clicked
    deleteClicked = pyqtSignal()
    editClicked = pyqtSignal()
    doneEditClicked = pyqtSignal()

    def __init__(self):
        super(ActionButtonsWidget, self).__init__()
        # Load UI file
        loadUi(resource_path('ui\\actionButtons.ui'), self)

        self.btnActionEdit = self.findChild(QPushButton, "btnActionEdit")
        self.btnActionDelete = self.findChild(QPushButton, "btnActionDelete")
        self.btnActionDone = self.findChild(QPushButton, "btnActionDone")

        self.btnActionEdit.clicked.connect(self.onEditClicked)
        self.btnActionDelete.clicked.connect(self.onDeleteClicked)
        self.btnActionDone.clicked.connect(self.onDoneClicked)

        self.btnActionDone.hide()

    def onDeleteClicked(self):
        # Emit the deleteClicked signal when the delete button is clicked
        self.deleteClicked.emit()

    def onEditClicked(self):
        self.btnActionEdit.hide()
        self.btnActionDelete.hide()
        self.btnActionDone.show()

        self.editClicked.emit()

    def onDoneClicked(self):
        self.btnActionEdit.show()
        self.btnActionDelete.show()
        self.btnActionDone.hide()

        self.doneEditClicked.emit()


...
# </editor-fold>
