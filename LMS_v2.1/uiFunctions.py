from PyQt6.QtWidgets import QWidget, QPushButton, QFrame, QStackedWidget, QVBoxLayout, QSizeGrip, \
    QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor

from profilePage import Profile
from homePage import Home
from gradesJHSPage import GradesJHS
from gradesSHSPage import GradesSHS
from attendance_OVPage import AttendanceOV


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

        # Default page to show up
        self.app_pages.setCurrentWidget(self.homePage)
        self.homeFunction()
        self.profileFunction()
        # self.jhsGradeFunction()
        self.shsGradeFunction()
        self.attendance_ov()

    def registerFunction(self):
        # Register page
        pass

    def homeFunction(self):
        # Home Frame from stacked widgets
        self.homeFrame = self.main_ui.findChild(QFrame, "homeMainFrame")
        self.homeLayout = self.main_ui.findChild(QVBoxLayout, "homeMainLayout")
        self.homeMain = Home()
        self.homeLayout.addWidget(self.homeMain)

        # Home page buttons inside the home frame
        self.homeMain.homeProfileBtn.clicked.connect(lambda: self.setPage(self.profilePage))
        # self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))
        self.homeMain.homeAttendanceBtn.clicked.connect(lambda: self.setPage(self.attendancePage))

    def profileFunction(self):
        # Profile page buttons (Top Bar)
        self.profileHomeBtn = self.profilePage.findChild(QPushButton, "homeBtnProf")
        self.profileGradeBtn = self.profilePage.findChild(QPushButton, "gradesBtnProf")
        self.profileHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        # self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # Profile Page Frame from stacked widgets
        self.profileFrame = self.main_ui.findChild(QFrame, "profMainFrame")
        self.profileLayout = self.main_ui.findChild(QVBoxLayout, "profileMainLayout")
        self.profileMain = Profile()
        self.profileLayout.addWidget(self.profileMain)

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

    def attendance_ov(self):
        # Attendance and Observed Values page buttons
        self.attendHomeBtn = self.attendancePage.findChild(QPushButton, "homeBtnAttend")
        self.attendGradeBtn = self.attendancePage.findChild(QPushButton, "prevBtnAttend")
        self.attendHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))
        # self.attendGradeBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        self.attendGradeBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # Attendance and Observed Values Page Frame from stacked widgets
        self.attendFrame = self.main_ui.findChild(QFrame, "attendMainFrame")
        self.attendFrameLayout = self.main_ui.findChild(QVBoxLayout, "attendMainLayout")
        self.attendOV_Main = AttendanceOV()
        self.attendFrameLayout.addWidget(self.attendOV_Main)

    def setPage(self, page):
        self.app_pages.setCurrentWidget(page)
