# ===============================================================================
# By: June P. Canas
# Project made with: Qt Designer and PySide2
# v: 1.0.2
# ===============================================================

## ==> GUI FILE
from mainWindow import *
import profileDataBase
import classDataBase

## ==> GLOBALS

GLOBAL_STATE = 0

class UIFunctions(MainWindow):

    ## ==> MAXIMIZE RESTORE FUNCTION
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()

            # SET GLOBAL TO 1
            GLOBAL_STATE = 1

            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.modernLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 0px;")
            self.ui.maxBtn.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.modernLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.mainFrame.setStyleSheet("background-color: rgb(255, 255, 255);border-radius: 10px;")
            self.ui.maxBtn.setToolTip("Maximize")

    # ==> UI DEFINITIONS
    def uiDefinitions(self):

        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # SET DROPSHADOW WINDOW 
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        # APPLY DROPSHADOW TO FRAME
        self.ui.mainFrame.setGraphicsEffect(self.shadow)

        # MAXIMIZE / RESTORE
        self.ui.maxBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # MINIMIZE
        self.ui.minBtn.clicked.connect(lambda: self.showMinimized())

        # CLOSE
        self.ui.closeBtn.clicked.connect(lambda: self.close())

        # ==> CREATE SIZE GRIP TO RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.gripFrame)
        self.sizegrip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px}")
        self.sizegrip.setToolTip("Resize Window")  

    def resetDisplay(self):
        self.ui.homeSection.depDisplay.setText("<DEPARTMENT>")
        self.ui.homeSection.shDisplay.setText(f"School Head:")
        self.ui.homeSection.syDisplay.setText(f"School Year:")
        self.ui.homeSection.advDisplay.setText(f"Adviser:")
        self.ui.homeSection.semDisplay.setText("")
        self.ui.homeSection.gradeSecDisplay.setText(f"Grade & Section")
        self.ui.homeSection.strandDisplay.setText("")

        self.ui.homeSection.depCombo.setEnabled(True)
        self.ui.homeSection.depCombo.setCurrentText("-- select --")
        self.ui.homeSection.syEntry.setEnabled(True)
        self.ui.homeSection.syEntry.setText("")
        self.ui.homeSection.sectionEntry.setEnabled(True)
        self.ui.homeSection.sectionEntry.setText("")
        self.ui.homeSection.gradeCombo.setEnabled(True)
        self.ui.homeSection.shEntry.setText("")
        self.ui.homeSection.advEntry.setText("")
        self.ui.homeSection.strandCombo.setEnabled(True)

        self.ui.homeSection.profBtn0.setEnabled(False)
        self.ui.homeSection.gradeBtn0.setEnabled(False)
        self.ui.homeSection.attendBtn0.setEnabled(False)

    def homeFunctions(self):            ######### (HOME PAGE FUNCTIONALITIES PAGING BUTTONS ) ###############

        self.ui.homeSection.profBtn0.clicked.connect(lambda: self.setPage(self.ui.profilePage))     ####### SET PAGE from HOME To PROFILE #####
        self.ui.homeSection.attendBtn0.clicked.connect(lambda: self.setPage(self.ui.attendPage))    ####### SET PAGE from HOME To ATTENDANCE #####
        self.ui.homeSection.saveClassBtn.clicked.connect(lambda: self.saveClass())
        self.ui.homeSection.upClassBtn.clicked.connect(lambda: self.ui.homeSection.updateClass(self.displayClass))
        self.ui.homeSection.delAllBtn.clicked.connect(lambda: self.ui.homeSection.delAllRecords(self.displayClass))
        self.ui.homeSection.openSF1Btn.clicked.connect(lambda: self.ui.homeSection.openFile(self.delContentDB))

    def profileFunctions(self):            ######### PROFILE PAGE FUNCTIONALITIES and BUTTONS #######

        self.ui.homeBtnProf.clicked.connect(lambda: self.setPage(self.ui.home))                     ####### SET PAGE from PROFILE To HOME #####
        
        self.ui.profSection.showLearner()
        self.ui.profSection.saveBtn.clicked.connect(lambda: self.saveLearner())
        self.ui.profSection.clrEntryBtn.clicked.connect(lambda: self.ui.profSection.clearEntry())
        self.ui.profSection.updateBtn.clicked.connect(lambda: self.ui.profSection.updateProfile(self.ui.gJHSSection.showJHS_Info, \
                                                    self.ui.gSHSSection.showSHS_Info, self.ui.attOVSection.showAttOV_Info, self.showMessage, QMessageBox.Information))
        self.ui.profSection.delBtn.clicked.connect(lambda: self.ui.profSection.delProfile(self.ui.gJHSSection.showJHS_Info, \
                                                    self.ui.gSHSSection.showSHS_Info, self.ui.attOVSection.showAttOV_Info, self.showMessage, QMessageBox.Information))

    def jhsGradeFunctions(self,myclass):           ########## JHS GRADE PAGE FUNCTIONALITIES and BUTTONS  ###########

        self.ui.homeBtnJHS.clicked.connect(lambda: self.setPage(self.ui.home))                      ####### SET PAGE from JHS GRADE To HOME #####
        self.ui.prevBtnJHS.clicked.connect(lambda: self.setPage(self.ui.profilePage))               ####### SET PAGE from JHS GRADE To PROFILE #####
        self.ui.attendBtnJHS.clicked.connect(lambda: self.setPage(self.ui.attendPage))              ####### SET PAGE from JHS GRADE To ATTENDANCE #####

        self.ui.gJHSSection.gradeSecJHS.setText(f"  Grade {myclass[4]} - {myclass[5]}")         ########### Display Class Info to JHS Page ######
        self.ui.gJHSSection.advJHS.setText(f"Adviser: {myclass[6]}")
        self.ui.gJHSSection.syJHS.setText(f"School Year: {myclass[2]}")

        self.ui.gJHSSection.showJHS_Info()                                                          ########### Display learner's name to JHS Page (tablewidget) ###### 

    def shsGradeFunctions(self,myclass):           ########## SHS GRADE PAGE FUNCTIONALITIES and BUTTONS  ###########

        self.ui.homeBtnSHS.clicked.connect(lambda: self.setPage(self.ui.home))                      ####### SET PAGE from SHS GRADE To HOME #####
        self.ui.prevBtnSHS.clicked.connect(lambda: self.setPage(self.ui.profilePage))               ####### SET PAGE from SHS GRADE To PROFILE #####
        self.ui.attendBtnSHS.clicked.connect(lambda: self.setPage(self.ui.attendPage))              ####### SET PAGE from SHS GRADE To ATTENDANCE #####

        self.ui.gSHSSection.gradeSecSHS.setText(f"  Grade {myclass[4]} - {myclass[5]}")         ########### Display Class Info to SHS Page ######
        self.ui.gSHSSection.strand.setText(myclass[7])
        self.ui.gSHSSection.advSHS.setText(f"Adviser: {myclass[6]}")
        self.ui.gSHSSection.sySHS.setText(f"School Year: {myclass[2]}")

        self.ui.gSHSSection.showSHS_Info()                                                      ########### Display learner's name to SHS Page (tablewidget) ###### 

    def attendanceOV(self,myclass):                ########## (ATTENDANCE PAGE PAGING BUTTONS ) ###############

        self.ui.homeBtnAttend.clicked.connect(lambda: self.setPage(self.ui.home))                   ####### SET PAGE from ATTENDANCE To HOME #####

        self.ui.attOVSection.gradeSecAttOb.setText(f"  Grade {myclass[4]} - {myclass[5]}")
        self.ui.attOVSection.advAttOb.setText(f"Adviser: {myclass[6]}")
        self.ui.attOVSection.syAttOb.setText(f"School Year: {myclass[2]}")

        self.ui.attOVSection.showAttOV_Info()                     ########### Display learner's name to Attendance and OV (tablewidget) ######
        self.ui.attOVSection.monthDisplay()

        
    ## RETURN STATUS IF WINDOWS IS MAXIMIZE OR RESTAURED
    def returnStatus():
        return GLOBAL_STATE

