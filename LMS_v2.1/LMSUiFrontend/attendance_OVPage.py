from PyQt6.QtWidgets import QFrame, QGraphicsDropShadowEffect, QTableWidget, QHeaderView, QComboBox, \
    QPushButton, QLabel, QTableWidgetItem, QCheckBox, QMessageBox, QAbstractItemView, QTabWidget
from PyQt6.QtCore import Qt
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
        self.attObVal_tabs = self.findChild(QTabWidget, "attObVal_tabs")
        self.att_rightFrame = self.findChild(QFrame, "rightFrame")
        self.ovTable = self.findChild(QTableWidget, "ovTable")
        self.fillTableBtn = self.findChild(QPushButton, "fillTableBtn")
        self.fillCombo = self.findChild(QComboBox, "fillCombo")
        self.updObBtn = self.findChild(QPushButton, "updObBtn")

        self.attendanceTable = self.findChild(QTableWidget, "attTable")
        self.updAttBtn = self.findChild(QPushButton, "updAttBtn")
        self.labelError = self.findChild(QLabel, "labelAttendanceChanged")
        self.autoComputeCheckBox = self.findChild(QCheckBox, "chckBoxAutoCompute")

        self.gradeSecAttOv = self.findChild(QLabel, "gradeSec_Att")
        self.advAttOv = self.findChild(QLabel, "adv_Att")
        self.syAttOv = self.findChild(QLabel, "sy_Att")
        self.lrn_AttOv = self.findChild(QLabel, "lrnLabel_Att")
        self.name_AttOv = self.findChild(QLabel, "nameLabel_Att")
        self.studentTable_Att = self.findChild(QTableWidget, "studentTable_Att")
        self.lblSelectionAtt = self.findChild(QLabel, "lblSelection")
        self.btnUnselectAtt = self.findChild(QPushButton, "btnUnselect")

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
        for column in range(1, 5):
            self.ovTable.setColumnWidth(column, 50)

        #  set first column to be readonly
        for r in range(self.ovTable.rowCount()):
            item = self.ovTable.item(r, 0)  # behavior statements column
            item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)

        self.ovTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ovTable.horizontalHeader().setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(100, 100, 100); }")

        self.ovTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ovTable.verticalHeader().setStyleSheet("QHeaderView:section{background-color: rgb(255,255,255); \
                                                    border-bottom: 1px solid rgb(200,200,200); border-right: 1px solid rgb(200,200,200);}")
        self.ovTable.cellDoubleClicked.connect(self.attOV_TableActivated)
        self.fillTableBtn.clicked.connect(self.fillOV_Table)
        self.fillTableBtn.setEnabled(False)
        self.fillCombo.setEnabled(False)

        # Attendance table styling
        self.attendanceTable.horizontalHeader().setFixedHeight(55)
        self.attendanceTable.horizontalHeader().setStyleSheet(
            "QHeaderView{ border-bottom: 1px solid rgb(100, 100, 100); }")
        self.attendanceTable.cellDoubleClicked.connect(self.attOV_TableActivated)
        self.attendanceTable.cellClicked.connect(self.attOV_TableClicked)

        #  other initialization
        self.selectedAtt = []
        self.selectedOv = []
        self.btnUnselectAtt.hide()
        self.tableClicked = 0

    def attOV_TableActivated(self, row, column):
        self.tableClicked = 0
        self.labelError.setText("")
        if len(self.selectedAtt) == 0 or len(self.selectedOv) == 0:
            self.showMessage("No Selected Learner", "Please select a learner from the left table",
                             QMessageBox.Icon.Warning)
            # self.attendanceTable.setCurrentItem(None)

    def attOV_TableClicked(self, row, column):
        self.tableClicked += 1
        if self.tableClicked >= 3:
            self.labelError.setText("Double clicked the desired cell to edit")

    def show_AttOvLearner(self, attData, ovData, monthData):  # displaying Learner's name and LRN to the left side table
        if len(attData) != 0:
            self.studentTable_Att.setRowCount(0)
            for i, row in enumerate(attData):
                self.rowcount = self.studentTable_Att.rowCount()
                self.studentTable_Att.insertRow(self.rowcount)

                for column, val in enumerate(row[0:2]):
                    self.studentTable_Att.setItem(i, column, QTableWidgetItem(str(val)))

        monthName = list(monthData[0])
        monthName.pop(0)  # remove monthId
        monthName[-1] = "Total"

        self.attendanceTable.setHorizontalHeaderLabels(["" for _ in range(13)])  # set to empty label first
        self.attendanceTable.setHorizontalHeaderLabels(monthName)

        self.btnUnselectAtt.clicked.connect(lambda: self.clearAttOvSelection())
        self.studentTable_Att.cellClicked.connect(lambda: self.clickedStudentTable_Att(attData, ovData, monthData))

    def clickedStudentTable_Att(self, attData, ovData, monthData):
        if self.studentTable_Att.selectedItems():  # selecting names from studentJHSTable
            try:
                self.attendanceTable.cellChanged.disconnect(self.validateAttendance)
                self.fillTableBtn.setEnabled(False)
                self.fillCombo.setEnabled(False)
            except Exception:
                pass
            self.selected_AttOvNames = []
            for i in self.studentTable_Att.selectedItems():
                self.selected_AttOvNames.append(i.text())

            # selecting data from attendance and ov database corresponding to selected names using filter method
            selectedId = int(self.selected_AttOvNames[0])
            self.selectedAtt = self.getAttendanceToDisplay(attData, monthData, selectedId)
            selectedOvRecord = list(filter(lambda ov: ov[0] == int(self.selected_AttOvNames[0]), ovData))
            self.selectedOv = list(selectedOvRecord[0])

            self.lrn_AttOv.setText(self.selectedAtt[2])
            self.name_AttOv.setText(self.selectedAtt[1])
            self.lblSelectionAtt.setText(f"ID No. {self.selectedAtt[0]} selected")
            self.btnUnselectAtt.show()

            self.displayToAttendanceTable(self.selectedAtt)
            self.displayToOvTable(self.selectedOv)
            self.attendanceTable.cellChanged.connect(self.validateAttendance)
            self.fillTableBtn.setEnabled(True)
            self.fillCombo.setEnabled(True)

    def getAttendanceToDisplay(self, attData: list, monthData: list, selectedId: int) -> list:
        # combining number of school days data and attendance data of selected student
        schoolDays = list(monthData[1])
        schoolDays.pop(0)  # remove monthId

        attendanceSelected = [item for item in attData if item[0] == selectedId]
        selectedAttList = list(attendanceSelected[0])
        for i in range(len(schoolDays)):
            selectedAttList.insert((5 + i), schoolDays[i])

        return selectedAttList

    def displayToAttendanceTable(self, selectedAtt):
        for attRow in range(3):  # display to attendance table
            for attColumn in range(13):
                self.attendanceTable.setItem(attRow, attColumn, QTableWidgetItem(""))
                attItemInt = selectedAtt[(5 + attColumn) + (13 * attRow)]
                if attItemInt is None:
                    self.attendanceTable.setItem(attRow, attColumn, QTableWidgetItem(""))
                else:
                    attItem = QTableWidgetItem(str(attItemInt))
                    self.attendanceTable.setItem(attRow, attColumn, attItem)
                    attItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def displayToOvTable(self, selectedOv):
        for ovRow in range(7):  # display to grades table
            for ovColumn in range(4):
                self.ovTable.setItem(ovRow, ovColumn + 1, QTableWidgetItem(""))
                ovItemStr = selectedOv[(5 + ovColumn) + (4 * ovRow)]
                if ovItemStr is None:
                    self.ovTable.setItem(ovRow, ovColumn + 1, QTableWidgetItem(""))
                else:
                    ovItem = QTableWidgetItem(ovItemStr)
                    self.ovTable.setItem(ovRow, ovColumn + 1, ovItem)
                    ovItem.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def updAttendance(self):
        if len(self.selectedAtt) > 0:
            attendanceData = []
            for attRow in range(3):
                for attColumn in range(13):
                    attendanceItem = self.attendanceTable.item(attRow, attColumn)
                    if attendanceItem.text().strip() == '':
                        attendanceData.append(None)
                    else:
                        attendanceData.append(attendanceItem.text().strip())

            attendanceData.append(self.selectedAtt[0])
            return attendanceData
        else:
            return None

    def updObVal(self):
        if len(self.selectedOv) > 0:
            obValData = []
            validObValList = ["AO", "SO", "RO", "NO"]
            for obValRow in range(7):
                for obValColumn in range(4):
                    obValItem = self.ovTable.item(obValRow, obValColumn + 1)
                    obValData.append(obValItem.text().upper().strip())

            validObVal = True
            for item in obValData:  # checking validity of observe values input
                if not (item in validObValList or item == ''):
                    obValData = [item]
                    validObVal = False
                    break

            if validObVal:
                obValData.append(self.selectedOv[0])
                return tuple(obValData)
            else:
                return obValData

        else:
            return None

    def validateAttendance(self, row, column):  # cell changed signal
        attendanceItem = self.attendanceTable.item(row, column)
        if attendanceItem:
            try:
                attendanceEntry = attendanceItem.text().strip()
                if attendanceEntry.isdigit():
                    attendanceEntry = int(attendanceEntry)
                    if column == 12: return  # do nothing if it is in total column
                    if attendanceEntry <= 31:  # month days should not exceed 31
                        QTableWidgetItem(str(attendanceEntry)).setTextAlignment(Qt.AlignmentFlag.AlignCenter)  # TEST THIS
                        schoolDaysItem = self.attendanceTable.item(0, column)
                        presentDaysItem = self.attendanceTable.item(1, column)
                        absentDaysItem = self.attendanceTable.item(2, column)
                        match row:
                            case 0:  # Typing some values for No of school days
                                presentDaysEmpty = None if presentDaysItem is None else presentDaysItem.text().strip()
                                absentDaysEmpty = None if absentDaysItem is None else absentDaysItem.text().strip()
                                #  condition if no. of present days have value and no. of absent days is empty
                                if presentDaysItem.text().strip() != "" and (
                                        absentDaysEmpty is None or absentDaysEmpty == ""):
                                    presentDaysInt = int(presentDaysItem.text().strip())
                                    if attendanceEntry >= presentDaysInt:
                                        absentDaysValue = attendanceEntry - presentDaysInt
                                        absentDaysValue = QTableWidgetItem(str(absentDaysValue))
                                        self.attendanceTable.setItem(2, column, absentDaysValue)
                                        absentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                    else:
                                        self.showMessage("Error", "No. of present days is greater than no. of school days",
                                                         QMessageBox.Icon.Warning)
                                        self.attendanceTable.setItem(row, column, QTableWidgetItem(""))
                                #  condition if no. of absent days have value and no. of present days is empty
                                elif absentDaysItem.text().strip() != "" and (
                                        presentDaysEmpty is None or presentDaysEmpty == ""):
                                    absentDaysInt = int(absentDaysItem.text().strip())
                                    if attendanceEntry >= absentDaysInt:
                                        presentDaysValue = attendanceEntry - absentDaysInt
                                        presentDaysValue = QTableWidgetItem(str(presentDaysValue))
                                        self.attendanceTable.setItem(1, column, presentDaysValue)
                                        presentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                    else:
                                        self.showMessage("Error", "No. of absent days is greater than no. of school days",
                                                         QMessageBox.Icon.Warning)
                                        self.attendanceTable.setItem(row, column, QTableWidgetItem(""))
                                #  condition if both no. of absent days and no. of present days have value
                                elif absentDaysItem.text().strip() != "" and presentDaysItem.text().strip() != "":
                                    presentDaysInt = int(presentDaysItem.text().strip())
                                    absentDaysInt = int(absentDaysItem.text().strip())
                                    if attendanceEntry != (presentDaysInt + absentDaysInt):
                                        absentDaysValue = attendanceEntry - presentDaysInt
                                        absentDaysValue = QTableWidgetItem(str(absentDaysValue))
                                        self.attendanceTable.setItem(2, column, absentDaysValue)
                                        absentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                        self.showMessage("Update", "No. of absent days has been adjusted",
                                                         QMessageBox.Icon.Information)

                            case 1:  # Typing some values for No of present days
                                schoolDaysEmpty = None if schoolDaysItem is None else schoolDaysItem.text().strip()
                                absentDaysEmpty = None if absentDaysItem is None else absentDaysItem.text().strip()
                                #  condition if no. of school days have value and no. of absent days is empty
                                if schoolDaysItem.text().strip() != "" and (
                                        absentDaysEmpty is None or absentDaysEmpty == ""):
                                    schoolDaysInt = int(schoolDaysItem.text().strip())
                                    if schoolDaysInt >= attendanceEntry:
                                        absentDaysValue = schoolDaysInt - attendanceEntry
                                        absentDaysValue = QTableWidgetItem(str(absentDaysValue))
                                        self.attendanceTable.setItem(2, column, absentDaysValue)
                                        absentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                    else:
                                        self.showMessage("Error", "No. of present days is greater than no. of school days",
                                                         QMessageBox.Icon.Warning)
                                        self.attendanceTable.setItem(row, column, QTableWidgetItem(""))
                                #  condition if no. of absent days have value and no. of school days is empty
                                elif absentDaysItem.text().strip() != "" and (
                                        schoolDaysEmpty is None or schoolDaysEmpty == ""):
                                    absentDaysInt = int(absentDaysItem.text().strip())
                                    schoolDaysValue = attendanceEntry + absentDaysInt
                                    schoolDaysValue = QTableWidgetItem(str(schoolDaysValue))
                                    self.attendanceTable.setItem(0, column, schoolDaysValue)
                                    schoolDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                #  condition if both no. of absent days and no. of school days have value
                                elif absentDaysItem.text().strip() != "" and schoolDaysItem.text().strip() != "":
                                    schoolDaysInt = int(schoolDaysItem.text().strip())
                                    absentDaysInt = int(absentDaysItem.text().strip())
                                    if attendanceEntry != (schoolDaysInt - absentDaysInt):
                                        absentDaysValue = schoolDaysInt - attendanceEntry
                                        absentDaysValue = QTableWidgetItem(str(absentDaysValue))
                                        self.attendanceTable.setItem(2, column, absentDaysValue)
                                        absentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                        self.showMessage("Update", "No. of absent days has been adjusted",
                                                         QMessageBox.Icon.Information)

                            case 2:  # Typing some values for No of absent days
                                schoolDaysEmpty = None if schoolDaysItem is None else schoolDaysItem.text().strip()
                                presentDaysEmpty = None if presentDaysItem is None else presentDaysItem.text().strip()
                                #  condition if no. of school days have value and no. of present days is empty
                                if schoolDaysItem.text().strip() != "" and (
                                        presentDaysEmpty is None or presentDaysEmpty == ""):
                                    schoolDaysInt = int(schoolDaysItem.text().strip())
                                    if schoolDaysInt >= attendanceEntry:
                                        presentDaysValue = schoolDaysInt - attendanceEntry
                                        presentDaysValue = QTableWidgetItem(str(presentDaysValue))
                                        self.attendanceTable.setItem(1, column, presentDaysValue)
                                        presentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                    else:
                                        self.showMessage("Error", "No. of absent days is greater than no. of school days",
                                                         QMessageBox.Icon.Warning)
                                        self.attendanceTable.setItem(row, column, QTableWidgetItem(""))
                                #  condition if no. of present days have value and no. of school days is empty
                                elif presentDaysItem.text().strip() != "" and (
                                        schoolDaysEmpty is None or schoolDaysEmpty == ""):
                                    presentDaysInt = int(presentDaysItem.text().strip())
                                    schoolDaysValue = attendanceEntry + presentDaysInt
                                    schoolDaysValue = QTableWidgetItem(str(schoolDaysValue))
                                    self.attendanceTable.setItem(0, column, schoolDaysValue)
                                    schoolDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                #  condition if both no. of present days and no. of school days have value
                                elif presentDaysItem.text().strip() != "" and schoolDaysItem.text().strip() != "":
                                    schoolDaysInt = int(schoolDaysItem.text().strip())
                                    presentDaysInt = int(presentDaysItem.text().strip())
                                    if attendanceEntry != (schoolDaysInt - presentDaysInt):
                                        presentDaysValue = schoolDaysInt - attendanceEntry
                                        presentDaysValue = QTableWidgetItem(str(presentDaysValue))
                                        self.attendanceTable.setItem(1, column, presentDaysValue)
                                        presentDaysValue.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                                        self.showMessage("Update", "No. of present days has been adjusted",
                                                         QMessageBox.Icon.Information)

                            case _:
                                pass
                    else:
                        self.showMessage("Error",
                                         "Month days should not exceed 31",
                                         QMessageBox.Icon.Warning)
                        self.attendanceTable.setItem(row, column, QTableWidgetItem(""))

                elif attendanceEntry == "":
                    pass

                else:
                    self.showMessage("Error",
                                     f"{attendanceEntry} is not a valid attendance",
                                     QMessageBox.Icon.Warning)
                    self.attendanceTable.setItem(row, column, QTableWidgetItem(""))

            except Exception:
                print("Something went wrong")

    def fillOV_Table(self):
        ovText = self.fillCombo.currentText()
        for r in range(7):
            for c in range(4):
                self.ovTable.setItem(r, c + 1, QTableWidgetItem(""))
                self.ovTable.setItem(r, c + 1, QTableWidgetItem(ovText))

    def clearAttOvSelection(self):
        self.ovTable.clearSelection()
        self.attendanceTable.clearSelection()
        self.studentTable_Att.clearSelection()
        self.selectedAtt = []
        self.selectedOv = []
        self.lblSelectionAtt.setText("No Selection")
        self.btnUnselectAtt.hide()
        self.lrn_AttOv.setText("")
        self.name_AttOv.setText("")
        self.fillTableBtn.setEnabled(False)
        self.fillCombo.setEnabled(False)

        for ovRow in range(7):  # clear ov table
            for ovColumn in range(4):
                self.ovTable.setItem(ovRow, ovColumn + 1, QTableWidgetItem(""))

        for attRow in range(3):  # display to attendance table
            for attColumn in range(13):
                self.attendanceTable.setItem(attRow, attColumn, QTableWidgetItem(""))

    def config_AttOvDisplay(self, classDB):
        self.gradeSecAttOv.setText(f"Grade {classDB[5]} - {classDB[6]}")
        self.advAttOv.setText(f"Adviser: {classDB[7]}")
        self.syAttOv.setText(f"S/Y: {classDB[2]}")

    def showMessage(self, title, message, icon):  # warning message box
        msgBox = QMessageBox(text=message, parent=self)
        msgBox.setWindowTitle(title)
        # icons (QMessageBox.Icon.Question, QMessageBox.Icon.Information,
        # QMessageBox.Icon.Warning, QMessageBox.Icon.Critical)
        msgBox.setIcon(icon)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        msgBox.exec()
