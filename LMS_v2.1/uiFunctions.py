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
from LMSdataBackend import mainDb_Create, schoolClass_CRUD, profile_CRUD, \
    gradeJHS_CRUD, gradeSHS_CRUD, attendance_CRUD, observedValues_CRUD, \
    schoolDaysPerMonth_CRUD, semesterSubjects_CRUD


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
        mainDb_Create.createDbNames()  # connect and create table if not exist to lms_DbNames
        self.activeDb = mainDb_Create.viewDbNames(1)  # check if there is an active main database
        if len(self.activeDb) > 0:
            activeDbRecord = self.activeDb[0]
            activeDbName = activeDbRecord[1]
            if os.path.isfile(resource_path(f'data\\{activeDbName}.db')):
                self.app_pages.setCurrentWidget(self.registerPage)
                self.fromClassData = schoolClass_CRUD.viewClassData(activeDbName)[0]  # Class data
                self.fromSchoolData = schoolClass_CRUD.viewSchoolData(activeDbName)[0]  # School Data
                self.homeFunction(self.fromSchoolData, self.fromClassData)  # Initialize Home page
                self.profileFunction(self.fromClassData, activeDbName)  # Initialize Profile page
                self.attendance_ov(self.fromClassData, activeDbName)  # Initialize attendance page

                if self.fromClassData[1] == "JUNIOR HIGH SCHOOL":
                    self.jhsGradeFunction(self.fromClassData, activeDbName)
                else:
                    self.shsGradeFunction(self.fromClassData, activeDbName)

                self.app_pages.setCurrentWidget(defaultPage)

        else:
            self.registerFunction()
            self.app_pages.setCurrentWidget(self.registerPage)

    def registerFunction(self):
        # Register page
        self.registerFrame = self.main_ui.findChild(QFrame, "registerPage")
        self.registerLayout = self.main_ui.findChild(QVBoxLayout, "registerPageLayout")
        self.registerMain = Register()
        self.registerLayout.addWidget(self.registerMain)
        self.registerMain.submitEntryBtn.clicked.connect(lambda: saveClass())

        def saveClass():
            classSchoolData = self.registerMain.submitEntry()  # Data from register form
            print(classSchoolData)
            if classSchoolData is not None:
                # creating and adding data to school and class database
                mainDbName = ""
                schoolDataReg = classSchoolData[0]
                classDataReg = classSchoolData[1]
                schoolName_abbrv = schoolDataReg[0].split()
                for initial in schoolName_abbrv:
                    mainDbName += initial[0]

                mainDbName += f"_{classDataReg[1]}_G{classDataReg[4]}_{classDataReg[5]}"
                mainDb_Create.createMainDb(mainDbName)

                # add datas for schoolDaysPerMonth Names
                monthNamesTuple = (classDataReg[2],)  # parameter needed for month names (addDaysPerMonthData)
                schoolDaysList = [None] * 13
                schoolDaysTuple = tuple(
                    schoolDaysList)  # parameter needed for school days (addDaysPerMonthData) default

                schoolClass_CRUD.createSchoolData(mainDbName)
                schoolClass_CRUD.createClassData(mainDbName)
                schoolClass_CRUD.addSchoolData(mainDbName, schoolDataReg)
                schoolClass_CRUD.addClassData(mainDbName, classDataReg)

                schoolDaysPerMonth_CRUD.createDaysPerMonthData(mainDbName)
                schoolDaysPerMonth_CRUD.addDaysPerMonthData(mainDbName, monthNamesTuple)
                schoolDaysPerMonth_CRUD.addDaysPerMonthData(mainDbName, schoolDaysTuple)

                profile_CRUD.createProfileData(mainDbName)
                attendance_CRUD.createAttendanceData(mainDbName)
                observedValues_CRUD.createObValData(mainDbName)
                if classDataReg[0] == "JUNIOR HIGH SCHOOL":
                    gradeJHS_CRUD.createGradesJHSData(mainDbName)
                else:
                    semesterSubjects_CRUD.createSemSubjects(mainDbName)

            self.showMessage("Adding New Class",
                             "You have successfully added new class",
                             QMessageBox.Icon.Information)

            self.checkClassData(self.profilePage)

    def homeFunction(self, schoolDB, classDB):
        # Home Frame from stacked widgets
        self.homeFrame = self.main_ui.findChild(QFrame, "homeMainFrame")
        self.homeLayout = self.main_ui.findChild(QVBoxLayout, "homeMainLayout")
        self.homeMain = Home()
        self.homeLayout.addWidget(self.homeMain)
        self.createNewClassBtn = self.main_ui.findChild(QPushButton, "btnCreateNewClass")

        # Home page buttons inside the home frame
        self.homeMain.homeProfileBtn.clicked.connect(lambda: self.setPage(self.profilePage))
        self.homeMain.homeAttendanceBtn.clicked.connect(lambda: self.setPage(self.attendancePage))

        if classDB[1] == "JUNIOR HIGH SCHOOL":
            self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
        else:
            self.homeMain.homeGradesBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # display class and school info to the page
        self.homeMain.config_HomeDisplay(schoolDB)

        # functionalities
        self.createNewClassBtn.clicked.connect(lambda: self.resetDisplayData())

    def profileFunction(self, classDB, activeDbName):
        # Profile page buttons (Top Bar)
        self.profileHomeBtn = self.profilePage.findChild(QPushButton, "homeBtnProf")
        self.profileGradeBtn = self.profilePage.findChild(QPushButton, "gradesBtnProf")
        self.profileHomeBtn.clicked.connect(lambda: self.setPage(self.homePage))

        # Profile Page Frame from stacked widgets
        self.profileFrame = self.main_ui.findChild(QFrame, "profMainFrame")
        self.profileLayout = self.main_ui.findChild(QVBoxLayout, "profileMainLayout")
        self.profileMain = Profile()
        self.profileLayout.addWidget(self.profileMain)
        self.profileMain.save_updateBtn.clicked.connect(lambda: saveUpdateLearner())
        self.profileMain.delLearnerBtn.clicked.connect(lambda: deleteLearner())

        if classDB[1] == "JUNIOR HIGH SCHOOL":
            self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeJHSPage))
            self.profileMain.status.addItems(["Enrolled", "Pending", "Incomplete", "Dropped"])
        else:
            shsStatus = ["Enrolled (1st and 2nd sem)", "Enrolled 1st Sem, No 2nd Sem", "No 1st Sem, Enrolled 2nd Sem", "Pending", "Incomplete", "Dropped"]
            self.profileMain.status.addItems(shsStatus)
            self.profileGradeBtn.clicked.connect(lambda: self.setPage(self.gradeSHSPage))

        # displaying learner's profile from database including class info
        self.profileMain.config_ProfileDisplay(classDB)
        fromProfileData = profile_CRUD.viewProfileData(activeDbName)
        self.profileMain.show_learner(fromProfileData)

        def saveUpdateLearner():
            formEntries = self.profileMain.save_update_learner()
            if type(formEntries) == list:
                if len(formEntries) != 0:
                    fromSem1Subjects = semesterSubjects_CRUD.viewSemSubjects(activeDbName, 1)  # check for sem1 subjects
                    if formEntries[1]:  # Adding New Learner to profile
                        addedID = profile_CRUD.addProfileData(activeDbName, formEntries[0])
                        fromProfile_Add = profile_CRUD.viewProfileData(activeDbName)
                        self.profileMain.show_learner(fromProfile_Add)

                        #  adding blank entries with id to Attendance, grades, and observed values
                        attendance_CRUD.addAttendanceData(activeDbName, addedID)
                        observedValues_CRUD.addObValData(activeDbName, addedID)
                        fromDaysPerMonthData = schoolDaysPerMonth_CRUD.viewDaysPerMonthData(activeDbName)
                        fromAttendanceData = attendance_CRUD.viewAttendanceData(activeDbName)
                        fromObValData = observedValues_CRUD.viewObValData(activeDbName)
                        self.attendOV_Main.show_AttOvLearner(fromAttendanceData, fromObValData, fromDaysPerMonthData)

                        if classDB[1] == "JUNIOR HIGH SCHOOL":
                            gradeJHS_CRUD.addGradesJHSData(activeDbName, addedID)
                        else:
                            sem1SubjectCount = len(semesterSubjects_CRUD.viewSemSubjects(activeDbName, 1))
                            sem2SubjectCount = len(semesterSubjects_CRUD.viewSemSubjects(activeDbName, 2))
                            if sem1SubjectCount > 0:
                                gradeSHS_CRUD.addOneGradesSHSData(activeDbName, addedID, sem1SubjectCount, 1)
                                if len(fromSem1Subjects) > 0:
                                    fromSem1GradesSHSData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
                                    fromSem2GradesSHSData = []
                                    self.gradeSHSMain.show_shsLearners(fromSem1GradesSHSData, fromSem2GradesSHSData)

                            if sem2SubjectCount > 0:
                                gradeSHS_CRUD.addOneGradesSHSData(activeDbName, addedID, sem2SubjectCount, 2)

                        self.showMessage("Adding New Learner",
                                         "You have successfully added a new learner",
                                         QMessageBox.Icon.Information)

                    else:  # Editing existing learner
                        profile_CRUD.updateProfileData(activeDbName, formEntries[0])
                        fromProfile_Edit = profile_CRUD.viewProfileData(activeDbName)
                        editMsg = f"ID No. {formEntries[0][14]} has been edited successfully"
                        self.profileMain.show_learner(fromProfile_Edit)
                        self.showMessage("Edit Learner",
                                         editMsg,
                                         QMessageBox.Icon.Information)

            elif type(formEntries) == str:
                self.showMessage("Error",
                                 formEntries,
                                 QMessageBox.Icon.Warning)

        def msgBoxBtnClick(i):  # callback function for warning message box (delete learner)
            if i.text() == "&Yes":
                learnerID = self.profileMain.delete_learner()
                if learnerID > 0:
                    profile_CRUD.deleteProfileData(activeDbName, learnerID)  # delete profile data
                    attendance_CRUD.deleteAttData(activeDbName, learnerID)  # delete attendance data
                    observedValues_CRUD.deleteObValData(activeDbName, learnerID)  # delete observed values data

                    if classDB[1] == "JUNIOR HIGH SCHOOL":
                        gradeJHS_CRUD.deleteGradesJHSData(activeDbName, learnerID)  # delete JHS grade data
                    else:
                        sem1SubjectCount = len(semesterSubjects_CRUD.viewSemSubjects(activeDbName, 1))
                        sem2SubjectCount = len(semesterSubjects_CRUD.viewSemSubjects(activeDbName, 2))
                        if sem1SubjectCount > 0:
                            gradeSHS_CRUD.deleteGradesSHSData(activeDbName, learnerID, 1)

                        if sem2SubjectCount > 0:
                            gradeSHS_CRUD.deleteGradesSHSData(activeDbName, learnerID, 2)

                    fromProfile_Del = profile_CRUD.viewProfileData(activeDbName)
                    self.profileMain.show_learner(fromProfile_Del)

        def deleteLearner():
            msgDelBox = QMessageBox(text="Are you sure you want to delete the selected learner?"
                                         "\nThis will also delete corresponding grade, attendance and observed values data"
                                         "\nand cannot be undone",
                                    parent=self.main_ui)
            msgDelBox.setWindowTitle("Delete Learner")
            msgDelBox.setIcon(QMessageBox.Icon.Critical)
            msgDelBox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            msgDelBox.buttonClicked.connect(msgBoxBtnClick)
            msgDelBox.exec()

    def jhsGradeFunction(self, classDB, activeDbName):
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
        self.gradeJHSMain.updGradeJHSBtn.clicked.connect(lambda: updateJHSGrade())

        # displaying class info and learner's Name and LRN to JHS Grade Page
        self.gradeJHSMain.config_jhsGradeDisplay(classDB)
        fromGradesJHSData = gradeJHS_CRUD.viewGradesJHSData(activeDbName)
        self.gradeJHSMain.show_jhsLearner(fromGradesJHSData)

        def updateJHSGrade():
            jhsTableEntries = self.gradeJHSMain.updJHSGrade()
            if jhsTableEntries is not None:
                if len(jhsTableEntries) > 1:
                    gradeJHS_CRUD.updateGradesJHSData(activeDbName, jhsTableEntries)
                    fromGradesJHSUpdt = gradeJHS_CRUD.viewGradesJHSData(activeDbName)
                    gradeJHSSelected = [item for item in fromGradesJHSUpdt if item[0] == jhsTableEntries[-1]]
                    self.gradeJHSMain.displayToJHSGradeTable(gradeJHSSelected[0])
                    self.gradeJHSMain.show_jhsLearner(fromGradesJHSUpdt)
                    self.showMessage("Successful",
                                     f"ID No. {jhsTableEntries[-1]} grades has been successfully updated",
                                     QMessageBox.Icon.Information)
                else:
                    self.showMessage("Invalid Grade",
                                     f"Error: {jhsTableEntries[0]} is not a valid grade",
                                     QMessageBox.Icon.Warning)
            else:
                self.showMessage("No Selected Learner",
                                 "Please select learner from the left side table",
                                 QMessageBox.Icon.Warning)

    def shsGradeFunction(self, classDB, activeDbName):
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
        self.gradeSHSMain.saveSubSHSBtn.clicked.connect(lambda: saveSubjects())
        self.gradeSHSMain.updGradeSHSBtn.clicked.connect(lambda: updateSHSGrades())

        # displaying class info and learner's Name and LRN to JHS Grade Page
        self.gradeSHSMain.config_shsGradeDisplay(classDB)
        fromSem1Subjects = semesterSubjects_CRUD.viewSemSubjects(activeDbName, 1)
        fromSem2Subjects = semesterSubjects_CRUD.viewSemSubjects(activeDbName, 2)
        self.gradeSHSMain.initializeSem1Pages(fromSem1Subjects)
        self.gradeSHSMain.initializeSem2Pages(fromSem2Subjects)

        # if sem1 subjects has data show table of learners (left side) #### TO EDIT CONDITION
        if len(fromSem1Subjects) > 0 and len(fromSem2Subjects) == 0:
            fromSem1GradesSHSData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
            fromSem2GradesSHSData = []
            self.gradeSHSMain.show_shsLearners(fromSem1GradesSHSData, fromSem2GradesSHSData)
        elif len(fromSem1Subjects) > 0 and len(fromSem2Subjects) > 0:
            fromSem1GradesSHSData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
            fromSem2GradesSHSData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 2)
            self.gradeSHSMain.show_shsLearners(fromSem1GradesSHSData, fromSem2GradesSHSData)

        def saveSubjects():
            semSubjectReturn = self.gradeSHSMain.shsSaveSubject(fromSem1Subjects)
            if type(semSubjectReturn) == list:
                semester = semSubjectReturn[0]
                subjectCount = len(semSubjectReturn)
                profileData = profile_CRUD.viewProfileData(activeDbName)
                if semester == 1:
                    semesterSubjects_CRUD.addSemSubjects(activeDbName, semSubjectReturn)
                    gradeSHS_CRUD.createGradesSHSData(activeDbName, subjectCount, 1)
                    if len(profileData) > 0:
                        gradeSHS_CRUD.addManyGradesSHSData(activeDbName, profileData, subjectCount, 1)
                        self.gradeSHSMain.shsStackedWidgetSem1.setCurrentIndex(1)
                        sem1GradesData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
                        sem2GradesData = []
                        self.gradeSHSMain.show_shsLearners(sem1GradesData, sem2GradesData)

                        sem1SubjectsUpdt = semesterSubjects_CRUD.viewSemSubjects(activeDbName, 1)
                        self.gradeSHSMain.initializeSem1Pages(sem1SubjectsUpdt)
                else:
                    semesterSubjects_CRUD.addSemSubjects(activeDbName, semSubjectReturn)
                    gradeSHS_CRUD.createGradesSHSData(activeDbName, subjectCount, 2)
                    if len(profileData) > 0:
                        gradeSHS_CRUD.addManyGradesSHSData(activeDbName, profileData, subjectCount, 2)
                        self.gradeSHSMain.shsStackedWidgetSem2.setCurrentIndex(1)
                        sem1GradesData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
                        sem2GradesData = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 2)
                        self.gradeSHSMain.show_shsLearners(sem1GradesData, sem2GradesData)

                        sem1SubjectsUpdt = semesterSubjects_CRUD.viewSemSubjects(activeDbName, 2)
                        self.gradeSHSMain.initializeSem2Pages(sem1SubjectsUpdt)
                        self.gradeSHSMain.saveSubSHSBtn.hide()
                        self.gradeSHSMain.updGradeSHSBtn.show()

                self.showMessage("Save subject successful",
                                 f"You have successfully save SHS subjects for semester {semester[-1]}",
                                 QMessageBox.Icon.Information)
            else:
                self.showMessage("Cannot save subjects",
                                 f"{semSubjectReturn}",
                                 QMessageBox.Icon.Warning)

        def updateSHSGrades():
            shsGradesEntries = self.gradeSHSMain.updSHSGrade()
            if shsGradesEntries is not None:
                sem = shsGradesEntries[-1]
                if len(shsGradesEntries) > 1:
                    gradeSHS_CRUD.updateGradesSHSData(activeDbName, shsGradesEntries)
                    if sem == 1:
                        sem1GradesSHSDataUpdt = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 1)
                        gradeSHSSelected = [item for item in sem1GradesSHSDataUpdt if item[0] == shsGradesEntries[-2]][0]
                        self.gradeSHSMain.showSem1GradeTable(gradeSHSSelected)
                        self.gradeSHSMain.show_shsLearners(sem1GradesSHSDataUpdt, fromSem2GradesSHSData)
                    else:
                        sem2GradesSHSDataUpdt = gradeSHS_CRUD.viewGradesSHSData(activeDbName, 2)
                        gradeSHSSelected = [item for item in sem2GradesSHSDataUpdt if item[0] == shsGradesEntries[-2]][0]
                        self.gradeSHSMain.showSem2GradeTable(gradeSHSSelected)
                        self.gradeSHSMain.show_shsLearners(fromSem1GradesSHSData, sem2GradesSHSDataUpdt)

                    self.showMessage("Successful",
                                     f"{gradeSHSSelected[1]} grades has been successfully updated",
                                     QMessageBox.Icon.Information)
                else:
                    self.showMessage("Invalid Grade",
                                     f"Error: {shsGradesEntries[0]} is not a valid grade",
                                     QMessageBox.Icon.Warning)
            else:
                self.showMessage("No Selected Learner",
                                 "Please select learner from the left side table",
                                 QMessageBox.Icon.Warning)

    def attendance_ov(self, classDB, activeDbName):
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
        self.attendOV_Main.updObBtn.clicked.connect(lambda: updateObVal())
        self.attendOV_Main.updAttBtn.clicked.connect(lambda: updateAttendance())

        # displaying class info and learner's Name and LRN to Attendance OV Grade Page
        self.attendOV_Main.config_AttOvDisplay(classDB)
        fromDaysPerMonthData = schoolDaysPerMonth_CRUD.viewDaysPerMonthData(activeDbName)
        fromAttendanceData = attendance_CRUD.viewAttendanceData(activeDbName)
        fromObValData = observedValues_CRUD.viewObValData(activeDbName)
        self.attendOV_Main.show_AttOvLearner(fromAttendanceData, fromObValData, fromDaysPerMonthData)

        def updateAttendance():
            attEntries = self.attendOV_Main.updAttendance()
            if attEntries is not None:
                schoolDaysData = attEntries[0:13]
                presAbsData = attEntries[13:]
                schoolDaysPerMonth_CRUD.updateDaysPerMonthData(activeDbName, schoolDaysData, 2)
                attendance_CRUD.updateAttendanceData(activeDbName, presAbsData)

                fromAttendanceUpdt = attendance_CRUD.viewAttendanceData(activeDbName)
                fromMonthDataUpdt = schoolDaysPerMonth_CRUD.viewDaysPerMonthData(activeDbName)

                r = self.attendOV_Main.studentTable_Att.currentRow()
                attList = self.attendOV_Main.getAttendanceToDisplay(fromAttendanceUpdt, fromMonthDataUpdt, presAbsData[-1])
                self.attendOV_Main.displayToAttendanceTable(attList)
                self.attendOV_Main.show_AttOvLearner(fromAttendanceUpdt, fromObValData, fromMonthDataUpdt)
                self.attendOV_Main.studentTable_Att.selectRow(r)

                self.showMessage("Successful",
                                 f"ID No. Attendance has been successfully updated",
                                 QMessageBox.Icon.Information)

        def updateObVal():
            obValEntries = self.attendOV_Main.updObVal()
            if obValEntries is not None:
                if len(obValEntries) > 1:
                    observedValues_CRUD.updateObValData(activeDbName, obValEntries)
                    fromObValDataUpdt = observedValues_CRUD.viewObValData(activeDbName)
                    obValList = [item for item in fromObValDataUpdt if item[0] == obValEntries[-1]]
                    self.attendOV_Main.displayToOvTable(obValList[0])
                    r = self.attendOV_Main.studentTable_Att.currentRow()
                    self.attendOV_Main.show_AttOvLearner(fromAttendanceData, fromObValDataUpdt, fromDaysPerMonthData)
                    self.attendOV_Main.studentTable_Att.selectRow(r)

                    self.showMessage("Successful",
                                     f"ID No. {obValEntries[-1]} Observed Values has been successfully updated",
                                     QMessageBox.Icon.Information)
                else:
                    self.showMessage("Invalid Input",
                                     f"Error: {obValEntries[0]} is not a valid observed values",
                                     QMessageBox.Icon.Warning)
            else:
                self.showMessage("No Selected Learner",
                                 "Please select a learner from the left table",
                                 QMessageBox.Icon.Warning)

    def resetDisplayData(self):
        # add message box for creating new class
        if len(self.activeDb) > 0:
            activeDbRecord = self.activeDb[0]
            mainDb_Create.updateDbNamesStatus(0, activeDbRecord[0])  # set the current database to be inactive
            # reset the data display in every page
            self.profileMain.cancel_save()
            self.profileMain.profile_Table.clearContents()
            self.gradeJHSMain.clearJHSSelection()
            self.gradeJHSMain.studentJHSTable.clearContents()
            self.attendOV_Main.studentTable_Att.clearContents()
            self.attendOV_Main.clearAttOvSelection()
            # add SHS reset data here

            self.checkClassData(self.homePage)

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
