from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QSizeGrip, \
    QGraphicsDropShadowEffect, QMessageBox
from PyQt6.QtGui import QColor
from absPath import resource_path
import os

# UI python file
from LMSUiFrontend.registerPage import Register
from LMSUiFrontend.profilePage import Profile
from LMSUiFrontend.homePage import Home
from LMSUiFrontend.gradesJHSPage import GradesJHS
from LMSUiFrontend.gradesSHSPage import GradesSHS
from LMSUiFrontend.attendance_OVPage import AttendanceOV

# backend database file
from LMSdataBackend import schoolClass_db, profile_db


class UIFunctions:
    def __init__(self, mainUI: QWidget):
        # Initialize the Main window and its functionality
        self.main_ui = mainUI
        self.close_btn = self.main_ui.findChild(QPushButton, "closeBtn")
        self.min_btn = self.main_ui.findChild(QPushButton, "minBtn")
        self.max_btn = self.main_ui.findChild(QPushButton, "maxBtn")

        self.close_btn.clicked.connect(lambda: self.main_ui.close())
        self.min_btn.clicked.connect(lambda: self.main_ui.showMinimized())
        self.max_btn.clicked.connect(lambda: self.maximize_window())

        self.header = self.main_ui.findChild(QFrame, "title_InputFrame")
        self.main_frame = self.main_ui.findChild(QFrame, "mainFrame")
        self.mainFrameLayout = self.main_ui.findChild(QVBoxLayout, "modernLayout")

        # Initialize widgets, shadows and sizegrip  on mainwindow
        self.initWidgetsUI()

        # initialize mouse position
        self.mousePos = None

    def maximize_window(self):
        if self.main_ui.isMaximized():
            self.main_ui.showNormal()
            self.mainFrameLayout.setContentsMargins(10, 10, 10, 10)
            self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
            self.max_btn.setToolTip("Maximize")
        else:
            self.main_ui.showMaximized()
            self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
            self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 0px;")
            self.max_btn.setToolTip("Restore")

    def initWidgetsUI(self):
        # Create size grip frame and functionality
        self.size_grip_Frame = self.main_ui.findChild(QFrame, "gripFrame")
        self.size_grip = QSizeGrip(self.size_grip_Frame)
        self.size_grip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 8px}")

        # Drop shadow effect
        self.shadow = QGraphicsDropShadowEffect(self.main_ui)
        self.shadow.setBlurRadius(25)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.main_frame.setGraphicsEffect(self.shadow)

        # Stacked Widgets pages
        self.app_pages = self.main_ui.findChild(QStackedWidget, "stackedWidget")
        self.registerPage = self.app_pages.findChild(QWidget, "registerClass")
        self.homePage = self.app_pages.findChild(QWidget, "home")
        self.profilePage = self.app_pages.findChild(QWidget, "profilePage")
        self.gradeJHSPage = self.app_pages.findChild(QWidget, "gradeJHSPage")
        self.gradeSHSPage = self.app_pages.findChild(QWidget, "gradeSHSPage")
        self.attendancePage = self.app_pages.findChild(QWidget, "attendPage")

        self.checkClassData(self.homePage)

    def checkClassData(self, defaultPage):  # Check if class database exist
        if os.path.isfile(resource_path('data\\classData.db')):
            self.fromClassData = schoolClass_db.viewClassData()[0]  # Class data
            self.fromSchoolData = schoolClass_db.viewSchoolData()[0]  # School Data
            self.homeFunction(self.fromClassData)  # Initialize Home page
            self.profileFunction(self.fromClassData)  # Initialize Profile page
            self.attendance_ov(self.fromClassData)  # Initialize attendance page
            if self.fromClassData[1] == "JUNIOR HIGH SCHOOL":
                self.jhsGradeFunction()
            else:
                self.shsGradeFunction()

            self.app_pages.setCurrentWidget(defaultPage)
            self.profileMain.config_ClassDisplay(self.fromClassData)
            self.homeMain.config_HomeDisplay(self.fromSchoolData)

        else:
            self.registerFunction()
            self.app_pages.setCurrentWidget(self.registerPage)

    def registerFunction(self):
        # Register page
        self.registerFrame = self.main_ui.findChild(QFrame, "registerPage")
        self.registerLayout = self.main_ui.findChild(QVBoxLayout, "registerPageLayout")
        self.registerMain = Register()
        self.registerLayout.addWidget(self.registerMain)
        self.registerMain.submitEntryBtn.clicked.connect(lambda:  saveClass())

        def saveClass():
            classSchoolData = self.registerMain.submitEntry(self.main_ui)  # Data from register form
            if classSchoolData is not None:
                # creating and adding data to school and class database
                schoolClass_db.createSchoolData()
                schoolClass_db.createClassData()
                schoolClass_db.addSchoolData(classSchoolData[0])
                schoolClass_db.addClassData(classSchoolData[1])
                profile_db.createProfileData()

                self.checkClassData(self.profilePage)

    def homeFunction(self, classDB):
        # Home Frame from stacked widgets
        self.homeFrame = self.main_ui.findChild(QFrame, "homeMainFrame")
        self.homeLayout = self.main_ui.findChild(QVBoxLayout, "homeMainLayout")
        self.homeMain = Home()
        self.homeLayout.addWidget(self.homeMain)

        # Home page buttons inside the home frame
        self.homeMain.homeProfileBtn.clicked.connect(lambda: self.setPage(self.profilePage))
        self.homeMain.homeAttendanceBtn.clicked.connect(lambda: self.setPage(self.attendancePage))

        if classDB[1] == "JUNIOR HIGH SCHOOL":
            self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        else:
            self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

    def profileFunction(self, classDB):
        # Profile page buttons (Top Bar)
        self.profileHomeBtn = self.profilePage.findChild(QPushButton, "homeBtnProf")
        self.profileGradeBtn = self.profilePage.findChild(QPushButton, "gradesBtnProf")
        self.profileHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        if classDB[1] == "JUNIOR HIGH SCHOOL":
            self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        else:
            self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # Profile Page Frame from stacked widgets
        self.profileFrame = self.main_ui.findChild(QFrame, "profMainFrame")
        self.profileLayout = self.main_ui.findChild(QVBoxLayout, "profileMainLayout")
        self.profileMain = Profile()
        self.profileLayout.addWidget(self.profileMain)
        self.profileMain.save_updateBtn.clicked.connect(lambda: saveUpdateLearner())
        self.profileMain.delLearnerBtn.clicked.connect(lambda: deleteLearner())

        fromProfileData = profile_db.viewProfileData()  # displaying learner's profile from database
        self.profileMain.show_learner(fromProfileData)

        def saveUpdateLearner():
            formEntries = self.profileMain.save_update_learner()
            if len(formEntries) != 0:
                if formEntries[1]:  # Adding New Learner
                    profile_db.addProfileData(formEntries[0])
                    fromProfile_Add = profile_db.viewProfileData()
                    self.profileMain.show_learner(fromProfile_Add)
                    self.showMessage("Adding New Learner",
                                     "You have successfully added a new learner",
                                     QMessageBox.Icon.Information)
                else:  # Editing existing learner
                    profile_db.updateProfileData(formEntries[0])
                    fromProfile_Edit = profile_db.viewProfileData()
                    print(formEntries[0])
                    editMsg = f"ID No. {formEntries[0][14]} has been edited successfully"
                    self.profileMain.show_learner(fromProfile_Edit)
                    self.showMessage("Edit Learner",
                                     editMsg,
                                     QMessageBox.Icon.Information)
            else:
                print("Something went wrong, No return entries")

        def msgBoxBtnClick(i):  # callback function for warning message box (delete learner)
            if i.text() == "&Yes":
                learnerID = self.profileMain.delete_learner()
                if learnerID > 0:
                    profile_db.deleteProfileData(learnerID)
                    fromProfile_Del = profile_db.viewProfileData()
                    self.profileMain.show_learner(fromProfile_Del)

        def deleteLearner():
            msgDelBox = QMessageBox(text="Are you sure you want to delete the selected learner?",
                                    parent=self.main_ui)
            msgDelBox.setWindowTitle("Delete Learner")
            msgDelBox.setIcon(QMessageBox.Icon.Warning)
            msgDelBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msgDelBox.buttonClicked.connect(msgBoxBtnClick)
            msgDelBox.exec()

    def jhsGradeFunction(self):
        # JHS grades page buttons
        self.jhsHomeBtn = self.gradeJHSPage.findChild(QPushButton, "homeBtnJHS")
        self.jhsProfileBtn = self.gradeJHSPage.findChild(QPushButton, "prevBtnJHS")
        self.jhsAttendanceBtn = self.gradeJHSPage.findChild(QPushButton, "attendBtnJHS")
        self.jhsHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        self.jhsProfileBtn.clicked.connect(lambda: self.setPage(self.profilePage))
        self.jhsAttendanceBtn.clicked.connect(lambda: self.setPage(self.attendancePage))

        # JHS Grades Page Frame from stacked widgets
        self.gradesJHSFrame = self.main_ui.findChild(QFrame, "gJHSMainFrame")
        self.gradesJHSLayout = self.main_ui.findChild(QVBoxLayout, "gradesJHSLayout")
        self.gradeJHSMain = GradesJHS()
        self.gradesJHSLayout.addWidget(self.gradeJHSMain)

    def shsGradeFunction(self):
        # SHS grades page buttons
        self.shsHomeBtn = self.gradeSHSPage.findChild(QPushButton, "homeBtnSHS")
        self.shsProfileBtn = self.gradeSHSPage.findChild(QPushButton, "prevBtnSHS")
        self.shsAttendanceBtn = self.gradeSHSPage.findChild(QPushButton, "attendBtnSHS")
        self.shsHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        self.shsProfileBtn.clicked.connect(lambda: self.setPage(self.profilePage))
        self.shsAttendanceBtn.clicked.connect(lambda: self.setPage(self.attendancePage))

        # SHS Grades Page Frame from stacked widgets
        self.gradesSHSFrame = self.main_ui.findChild(QFrame, "gSHSMainFrame")
        self.gradesSHSLayout = self.main_ui.findChild(QVBoxLayout, "gradesSHSLayout")
        self.gradeSHSMain = GradesSHS()
        self.gradesSHSLayout.addWidget(self.gradeSHSMain)

    def attendance_ov(self, classDB):
        # Attendance and Observed Values page buttons
        self.attendHomeBtn = self.attendancePage.findChild(QPushButton, "homeBtnAttend")
        self.attendGradeBtn = self.attendancePage.findChild(QPushButton, "prevBtnAttend")
        self.attendHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        if classDB[1] == "JUNIOR HIGH SCHOOL":
            self.attendGradeBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        else:
            self.attendGradeBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # Attendance and Observed Values Page Frame from stacked widgets
        self.attendFrame = self.main_ui.findChild(QFrame, "attendMainFrame")
        self.attendFrameLayout = self.main_ui.findChild(QVBoxLayout, "attendMainLayout")
        self.attendOV_Main = AttendanceOV()
        self.attendFrameLayout.addWidget(self.attendOV_Main)

    def setPage(self, page):
        self.app_pages.setCurrentWidget(page)

    def showMessage(self, title, message, icon):  # warning message box
        msgBox = QMessageBox(text=message, parent=self.main_ui)
        msgBox.setWindowTitle(title)
        # icons (QMessageBox.Icon.Question, QMessageBox.Icon.Information,
        # QMessageBox.Icon.Warning, QMessageBox.Icon.Critical)
        msgBox.setIcon(icon)
        msgBox.setDefaultButton(QMessageBox.StandardButton.Ok)
        msgBox.exec()
