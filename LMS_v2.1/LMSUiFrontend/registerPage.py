from PyQt6.QtWidgets import QFrame, QPushButton, QStackedWidget, QLineEdit, QComboBox, QSpinBox, QLabel, QMessageBox

from PyQt6.uic import loadUi
from absPath import resource_path


class Register(QFrame):
    def __init__(self):
        super(Register, self).__init__()
        # Load the UI file
        loadUi(resource_path('ui\\register.ui'), self)

        self.registerWidgets()

    def registerWidgets(self):
        # Initialize widgets inside Home Frame
        self.entryFormStacked = self.findChild(QStackedWidget, "entryFormStacked")
        self.entryFormStacked.setCurrentIndex(0)
        # depEd entry entry form
        self.schoolName = self.findChild(QLineEdit, "schoolName")
        self.schoolID = self.findChild(QLineEdit, "school_id")
        self.district = self.findChild(QLineEdit, "district")
        self.division = self.findChild(QLineEdit, "division")
        self.region = self.findChild(QComboBox, "region")
        # school form entry
        self.department = self.findChild(QComboBox, "depCombo")
        self.schoolYear = self.findChild(QSpinBox, "school_year")
        self.schoolYear_to = self.findChild(QSpinBox, "school_year_to")
        self.school_head = self.findChild(QLineEdit, "shEntry")
        self.grade = self.findChild(QComboBox, "gradeCombo")
        self.section = self.findChild(QLineEdit, "sectionEntry")
        self.adviser = self.findChild(QLineEdit, "advEntry")
        self.strandLabel = self.findChild(QLabel, "strandLabel")
        self.strand = self.findChild(QComboBox, "strandCombo")
        self.semLabel = self.findChild(QLabel, "semLabel")
        self.sem = self.findChild(QComboBox, "semCombo")
        self.reg_message = self.findChild(QLabel, "reg_message")
        self.submitEntryBtn = self.findChild(QPushButton, "submitEntryBtn")
        self.nextPageBtn = self.findChild(QPushButton, "nextPageBtn")
        self.backBtn = self.findChild(QPushButton, "backPageBtn")
        self.backBtn.hide()
        self.submitEntryBtn.hide()
        self.strandLabel.hide()
        self.strand.hide()
        self.semLabel.hide()
        self.sem.hide()

        self.department.addItem("-- select --")
        self.department.addItem("JUNIOR HIGH SCHOOL", ['7', '8', '9', '10'])
        self.department.addItem("SENIOR HIGH SCHOOL", ['11', '12'])
        self.department.activated.connect(self.depGrade)
        self.schoolYear.valueChanged.connect(lambda: self.schoolYear_change())
        self.schoolYear_to.setValue((self.schoolYear.value() + 1))
        self.nextPageBtn.clicked.connect(lambda: self.nextPage())
        self.backBtn.clicked.connect(lambda: self.backPage())

    def depGrade(self, index):  # Signals for department combobox
        dep = self.department.itemData(index)
        self.grade.clear()
        if dep:
            self.grade.addItems(dep)
            if self.department.currentIndex() == 2:
                self.strandLabel.show()
                self.strand.show()
                self.semLabel.show()
                self.sem.show()
            else:
                self.strandLabel.hide()
                self.strand.hide()
                self.semLabel.hide()
                self.sem.hide()

    def schoolYear_change(self):  # Signal for school year change
        self.schoolYear_to.setValue((self.schoolYear.value() + 1))

    def nextPage(self):
        if self.entryFormStacked.currentIndex() == 0:
            self.entryFormStacked.setCurrentIndex(1)
            self.backBtn.show()
            self.submitEntryBtn.show()
            self.nextPageBtn.hide()

    def backPage(self):
        if self.entryFormStacked.currentIndex() == 1:
            self.entryFormStacked.setCurrentIndex(0)
            self.backBtn.hide()
            self.submitEntryBtn.hide()
            self.nextPageBtn.show()

    def submitEntry(self, mainWindow):  # returns a list of tuples (school entries)
        self.register_list = []
        school_Entries = [self.schoolName.text().upper(), self.schoolID.text(), self.district.text().upper(),
                          self.division.text().upper(), self.region.currentText()]
        # Checking if entries are not blank and remove whitespace
        if all(school_Entry.strip() for school_Entry in school_Entries):
            school_valid_entries = []
            for entry in school_Entries:
                school_valid_entries.append(entry.strip())
            self.register_list.append(tuple(school_valid_entries))
        else:
            self.reg_message.setText("Incomplete Information. Click back and fill up the missing entry")
            return None

        if self.department.currentIndex() != 0:
            sy = f"{self.schoolYear.value()}-{self.schoolYear_to.value()}"
            class_Entries = [self.department.currentText(), sy, self.school_head.text().upper(),
                             self.grade.currentText(), self.section.text().upper(), self.adviser.text().upper()]
            # Checking if entries are not blank and remove whitespace
            if all(class_Entry.strip() for class_Entry in class_Entries):
                class_valid_entries = []
                for entry in class_Entries:
                    class_valid_entries.append(entry.strip())

                if self.department.currentIndex() == 1:
                    class_valid_entries.extend(["", ""])
                else:
                    class_valid_entries.extend([self.strand.currentText(), self.sem.currentText()])

                self.register_list.append(tuple(class_valid_entries))

            else:
                self.reg_message.setText("All fields are required. Please fill up missing information")
                return None
        else:
            self.reg_message.setText("Please Select Department")
            return None

        self.infoMessage(mainWindow, "You have successfully registered your class\n"
                                     "You can now manually add or import learner's information")
        self.reg_message.setText("")
        self.clearClassEntries()
        return self.register_list

    def infoMessage(self, mainWindow, message):  # warning message box
        msg_w = QMessageBox(text=message, parent=mainWindow)
        msg_w.setWindowTitle("Successful Registration")
        msg_w.setIcon(QMessageBox.Icon.Information)
        msg_w.setDefaultButton(QMessageBox.StandardButton.Ok)
        msg_w.exec()

    def clearClassEntries(self):
        self.schoolName.clear()
        self.schoolID.clear()
        self.district.clear()
        self.division.clear()
        self.department.setCurrentIndex(0)
        self.school_head.clear()
        self.grade.clear()
        self.section.clear()
        self.adviser.clear()
