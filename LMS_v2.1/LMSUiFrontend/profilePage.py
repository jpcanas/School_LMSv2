from PyQt6.QtWidgets import QFrame, QPushButton, QDateEdit, QLabel, QTableWidget, QTableWidgetItem, \
    QGraphicsDropShadowEffect, QLineEdit, QComboBox, QSpinBox, QAbstractItemView
from PyQt6.QtCore import QDate
from datetime import datetime
from PyQt6.QtGui import QColor

from PyQt6.uic import loadUi
from absPath import resource_path


class Profile(QFrame):
    def __init__(self):
        super(Profile, self).__init__()
        # Load the UI file
        loadUi(resource_path('ui\\profile.ui'), self)
        self.profileWidgets()

    def profileWidgets(self):
        # Form section widgets initialization (Left Side)
        self.profileDisplay = self.findChild(QFrame, "disProfFrame")
        self.sidebar = self.findChild(QFrame, "inputProfFrame")
        self.lrn = self.findChild(QLineEdit, "lrn_entry")
        self.lastName = self.findChild(QLineEdit, "l_nameEntry")
        self.firstName = self.findChild(QLineEdit, "f_nameEntry")
        self.middleName = self.findChild(QLineEdit, "m_nameEntry")
        self.name_ext = self.findChild(QComboBox, "nameExtCombo")
        self.birthdate = self.findChild(QDateEdit, "birthdate")
        self.sex = self.findChild(QComboBox, "sexComboBox")
        self.age = self.findChild(QSpinBox, "ageSpinBox")
        self.brgy = self.findChild(QLineEdit, "brgyEntry")
        self.municipal = self.findChild(QLineEdit, "munEntry")
        self.province = self.findChild(QLineEdit, "provEntry")
        self.mother = self.findChild(QLineEdit, "motherEntry")
        self.father = self.findChild(QLineEdit, "fatherEntry")
        self.guardian = self.findChild(QLineEdit, "guardianEntry")
        self.modality = self.findChild(QComboBox, "modalCombo")
        self.status = self.findChild(QComboBox, "statusCombo")
        self.save_updateBtn = self.findChild(QPushButton, "save_updateBtn")
        self.cancelSaveBtn = self.findChild(QPushButton, "cancelSave")

        # Table section widgets initialization (Right side)
        self.profile_Table = self.findChild(QTableWidget, "tableWidget")
        self.departmentLabel = self.findChild(QLabel, "depLabel")
        self.gradeSectionLabel = self.findChild(QLabel, "gradeSectionLabel")
        self.adviserLabel = self.findChild(QLabel, "adviserLabel")
        self.syLabel = self.findChild(QLabel, "syLabel")
        self.strandLabel = self.findChild(QLabel, "strandLabel")
        self.semLabel = self.findChild(QLabel, "semLabel")
        self.selectionBtnFrame = self.findChild(QFrame, "selectionBtns")
        self.addLearnerBtn = self.findChild(QPushButton, "addLearnerBtn")
        self.editLearnerBtn = self.findChild(QPushButton, "updateBtn")
        self.delLearnerBtn = self.findChild(QPushButton, "delBtn")
        self.cancelEditBtn = self.findChild(QPushButton, "cancelEdit")
        self.table_notif = self.findChild(QLabel, "table_notif")

        # Buttons below learner's form
        # save_update_learner() will be executed to uiFunctions.py (profileFunction)
        self.cancelSaveBtn.clicked.connect(lambda: self.cancel_save())
        # Buttons below table
        self.addLearnerBtn.clicked.connect(lambda: self.add_learner())
        self.editLearnerBtn.clicked.connect(lambda: self.edit_learner())
        self.cancelEditBtn.clicked.connect(lambda: self.cancel_edit())

        self.table_init()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.profileDisplay.setGraphicsEffect(self.shadow)

        # Other initializations
        self.sidebar.hide()
        self.selectionBtnFrame.hide()
        self.selected_learner = []

    def table_init(self):
        # Setting table header column width
        self.profile_Table.setColumnWidth(0, 30)  # ID
        self.profile_Table.setColumnWidth(2, 220)  # Last Name
        self.profile_Table.setColumnWidth(3, 220)  # First Name
        self.profile_Table.setColumnWidth(4, 220)  # Middle Name
        self.profile_Table.setColumnWidth(5, 150)  # Name Ext
        self.profile_Table.setColumnWidth(6, 230)  # Date of Birth
        self.profile_Table.setColumnWidth(7, 100)  # Sex
        self.profile_Table.setColumnWidth(8, 70)  # Age
        self.profile_Table.setColumnWidth(9, 300)  # Address
        self.profile_Table.setColumnWidth(10, 260)  # Mother's Name
        self.profile_Table.setColumnWidth(11, 260)  # Father's Name
        self.profile_Table.setColumnWidth(12, 260)  # Name of Guardian
        self.profile_Table.setColumnWidth(13, 260)  # Modality
        self.profile_Table.setColumnWidth(14, 240)  # Status

        # Table Header initialize
        self.table_header = self.profile_Table.horizontalHeader()
        self.table_header.setFixedHeight(40)

        # Table clicked signals
        self.profile_Table.cellClicked.connect(lambda: self.clickedTableItem())

    # BUTTONS FUNCTIONALITY (Below Learner's Form - Left side)--------------------------------------------------
    def save_update_learner(self):
        self.profileForm_list = []
        dob = self.birthdate.date().toPyDate().strftime("%B %d, %Y")
        if self.name_ext.currentText() == "-- N/A --":
            nameExtension = ""
        else:
            nameExtension = self.name_ext.currentText()

        completeAdd = f"{self.brgy.text().capitalize()}, {self.municipal.text().capitalize()}, " \
                      f"{self.province.text().capitalize()}"

        self.profile_entry = [self.lrn.text(), self.lastName.text().capitalize(),
                              self.firstName.text().capitalize(), self.middleName.text().capitalize(),
                              nameExtension, dob, self.sex.currentText(), str(self.age.value()),
                              completeAdd, self.mother.text().capitalize(),
                              self.father.text().capitalize(), self.guardian.text().capitalize(),
                              self.modality.currentText(), self.status.currentText()]
        self.profile_required_ent = [self.lrn.text(), self.lastName.text(), self.firstName.text(), dob,
                                     self.sex.currentText(), self.modality.currentText(), self.status.currentText()]

        if len(self.selected_learner) == 0:  # if there is no current selected learner from the table (Add New Mode)
            print("No current selection - Adding New learner")
            # Checking if required entries are not blank and remove whitespace
            if all(required_Entry.strip() for required_Entry in self.profile_required_ent):
                self.profileForm_list.append(tuple(self.profile_entry))
                self.profileForm_list.append(True)  # Adding bool True for "add mode", False for "update mode"
                self.sidebar.hide()
                self.addLearnerBtn.setEnabled(True)
                self.clearProfileEntries()
                return self.profileForm_list
            else:
                print("Missing required field for adding new learner")
                return self.profileForm_list
        else:  # a learner has been selected from the table (Update Mode)
            print("There is selection")
            # Checking if required entries are not blank and remove whitespace
            if all(required_Entry.strip() for required_Entry in self.profile_required_ent):
                self.profile_entry.append(int(self.selected_learner[0]))  # adding selected id to the profile entries
                self.profileForm_list.append(tuple(self.profile_entry))
                self.profileForm_list.append(False)  # Adding bool True for "add mode", False for "update mode"
                self.cancel_save()
                return self.profileForm_list
            else:
                print("Missing required field for updating learner's info")
                return self.profileForm_list

    def cancel_save(self):
        self.sidebar.hide()
        self.addLearnerBtn.show()
        self.cancelEditBtn.show()
        self.cancel_edit()

    # BUTTONS FUNCTIONALITY (Below Learner's Table)--------------------------------------------------
    def add_learner(self):
        self.sidebar.show()
        self.selectionBtnFrame.hide()  # hide edit and delete button
        self.addLearnerBtn.setEnabled(False)
        self.profile_Table.clearSelection()
        self.selected_learner = []
        self.save_updateBtn.setText("Save Learner")

    def delete_learner(self):
        selectedLearner = self.selected_learner
        if len(selectedLearner) != 0:
            self.cancel_edit()
            return int(selectedLearner[0])
        else:
            return 0

    def edit_learner(self):
        self.sidebar.show()
        self.addLearnerBtn.hide()
        self.cancelEditBtn.hide()
        self.editLearnerBtn.setEnabled(False)
        self.save_updateBtn.setText("Update Learner")

    def cancel_edit(self):  # Cancel button below table
        self.addLearnerBtn.setEnabled(True)
        self.editLearnerBtn.setEnabled(True)
        self.profile_Table.clearSelection()
        self.selected_learner = []
        self.selectionBtnFrame.hide()  # hide edit and delete button
        self.table_notif.setText("No learner selected")
        self.clearProfileEntries()

    # ---------------------------------------------------------------------
    def show_learner(self, learnerData):  # displaying learner's profile data to table
        if len(learnerData) != 0:
            self.profile_Table.setRowCount(0)
            for i, row in enumerate(learnerData):
                self.rowcount = self.profile_Table.rowCount()
                self.profile_Table.insertRow(self.rowcount)

                for column, val in enumerate(row):
                    self.profile_Table.setItem(i, column, QTableWidgetItem(str(val)))
        # else:
        #     self.profile_Table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)

    def clickedTableItem(self):
        if len(self.selected_learner) == 0:  # No current selected learner from the table
            self.selectionBtnFrame.show()
            self.sidebar.hide()
            self.addLearnerBtn.setEnabled(False)

        if self.profile_Table.selectedItems():
            self.selected_learner = []  # Clear the previous selected learner if any
            for i in self.profile_Table.selectedItems():
                self.selected_learner.append(i.text())

            id_no = self.profile_Table.selectedItems()[0].text()
            self.table_notif.setText(f"ID No. {id_no}, selected")
            self.selection_to_Entries(self.selected_learner)
            # print(self.selected_learner)

    def selection_to_Entries(self, selectedLearner):  # Copying selected learner from table to entries
        self.lrn.setText(selectedLearner[1])
        self.lastName.setText(selectedLearner[2])
        self.firstName.setText(selectedLearner[3])
        self.middleName.setText(selectedLearner[4])

        if self.selected_learner[5] == "":  # If name extension column is blank
            self.name_ext.setCurrentIndex(0)
        else:
            self.name_ext.setCurrentText(self.selected_learner[5])

        dateObj = datetime.strptime(self.selected_learner[6], "%B %d, %Y").date()
        pyqtDate = QDate(dateObj.year, dateObj.month, dateObj.day)
        self.birthdate.setDate(pyqtDate)

        self.sex.setCurrentText(selectedLearner[7])
        self.age.setValue(int(selectedLearner[8]))

        splitAddress = selectedLearner[9].rsplit(", ", 2)
        self.brgy.setText(splitAddress[0])
        self.municipal.setText(splitAddress[1])
        self.province.setText(splitAddress[2])

        self.mother.setText(selectedLearner[10])
        self.father.setText(selectedLearner[11])
        self.guardian.setText(selectedLearner[12])
        self.modality.setCurrentText(selectedLearner[13])
        self.status.setCurrentText(selectedLearner[14])

    def clearProfileEntries(self):
        self.lrn.clear()
        self.lastName.clear()
        self.firstName.clear()
        self.middleName.clear()
        self.name_ext.setCurrentIndex(0)
        self.mother.clear()
        self.father.clear()
        self.guardian.clear()

    def config_ProfileDisplay(self, classDB):  # display class info to profile page
        self.departmentLabel.setText(classDB[1])
        self.gradeSectionLabel.setText(f"Grade {classDB[5]} - {classDB[6].upper()}")
        self.adviserLabel.setText(classDB[7].upper())
        self.syLabel.setText(f"School Year: {classDB[2]}")
        self.strandLabel.setText(classDB[8])
