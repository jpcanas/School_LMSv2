from PyQt6.QtWidgets import QFrame, QPushButton, QDateEdit, QLabel, QTableWidget, QTableWidgetItem, QGraphicsDropShadowEffect
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
        self.birthdate = self.findChild(QDateEdit, "birthdate")
        self.save_updateBtn = self.findChild(QPushButton, "save_updateBtn")
        self.addLearnerBtn = self.findChild(QPushButton, "addLearnerBtn")
        self.cancelSaveBtn = self.findChild(QPushButton, "cancelSave")

        # Table section widgets initialization (Right side)
        self.profile_Table = self.findChild(QTableWidget, "tableWidget")
        self.selectionBtnFrame = self.findChild(QFrame, "selectionBtns")
        self.editLearnerBtn = self.findChild(QPushButton, "updateBtn")
        self.delLearnerBtn = self.findChild(QPushButton, "delBtn")
        self.cancelEditBtn = self.findChild(QPushButton, "cancelEdit")
        self.table_notif = self.findChild(QLabel, "table_notif")

        # Buttons connect to functions/ Table_init call
        self.cancelSaveBtn.clicked.connect(lambda: self.cancel_save())
        self.addLearnerBtn.clicked.connect(lambda: self.add_learner())
        self.save_updateBtn.clicked.connect(lambda: self.save_update_learner())
        self.cancelEditBtn.clicked.connect(lambda: self.cancel_edit())
        self.table_init()
        self.show_learner()

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.profileDisplay.setGraphicsEffect(self.shadow)

        # Other initializations
        self.sidebar.hide()
        # self.add_learner_mode = False
        # self.edit_learner_mode = False

    def table_init(self):
        # Setting table header column width
        self.profile_Table.setColumnWidth(0, 30)  # ID
        self.profile_Table.setColumnWidth(2, 220)  # Last Name
        self.profile_Table.setColumnWidth(3, 220)  # First Name
        self.profile_Table.setColumnWidth(4, 220)  # Middle Name
        self.profile_Table.setColumnWidth(5, 150)  # Name Ext
        self.profile_Table.setColumnWidth(6, 100)   # Sex
        self.profile_Table.setColumnWidth(7, 70)  # Age
        self.profile_Table.setColumnWidth(8, 300)  # Address
        self.profile_Table.setColumnWidth(9, 230)  # Date of Birth
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
        # self.profile_Table.clicked.connect(self.tableCLicked)

        self.selectionBtnFrame.hide()

    # BUTTONS FUNCTIONALITY --------------------------------------------------
    def add_learner(self):
        self.sidebar.show()
        self.selectionBtnFrame.hide()  # hide edit and delete button
        self.addLearnerBtn.setEnabled(False)
        self.profile_Table.clearSelection()


    def edit_learner(self):
        self.sidebar.show()
        self.editLearnerBtn.setEnabled(False)

    def save_update_learner(self):
        self.sidebar.hide()
        # self.selectionBtnFrame.show()
        self.addLearnerBtn.setEnabled(True)

    def cancel_save(self):
        self.sidebar.hide()
        # self.selectionBtnFrame.hide()
        self.addLearnerBtn.setEnabled(True)

    def cancel_edit(self):
        self.addLearnerBtn.setEnabled(True)
        self.profile_Table.clearSelection()
        self.selectionBtnFrame.hide()  # hide edit and delete button
        self.table_notif.setText("No learner selected")

    # ---------------------------------------------------------------------
    def show_learner(self):
        # Sample Data from database
        samp_data = [(1, "112635201202", "Targaryen", "Rhaenyra", "Velaryon", "", "Female", 21, "Del Pillar, Dragonstone, Westeros",
                      "August 21, 2002", "Rhaenys Velaryon", "Viserys Targaryen", "", "Face-to-Face", "Enrolled"),
                     (2, "112302125420", "Snow", "John", "Stark", "Jr.", "Male", 22, "Castaneda, Winterfell, Westeros",
                      "April 08, 2001", "Catelyn Stark", "Eddard Stark", "", "Face-to-Face", "Pending")]
        if len(samp_data) != 0:
            self.profile_Table.setRowCount(0)
            for i, row in enumerate(samp_data):
                self.rowcount = self.profile_Table.rowCount()
                self.profile_Table.insertRow(self.rowcount)

                for column, val in enumerate(row):
                    self.profile_Table.setItem(i, column, QTableWidgetItem(str(val)))

    def clickedTableItem(self):
        self.selectionBtnFrame.show()
        self.sidebar.hide()
        self.addLearnerBtn.setEnabled(False)

        if self.profile_Table.selectedItems():
            for i in self.profile_Table.selectedItems():
                print(i.text())

            id_no = self.profile_Table.selectedItems()[0].text()
            self.table_notif.setText(f"ID No. {id_no}, selected")














