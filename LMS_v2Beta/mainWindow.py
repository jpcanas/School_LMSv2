# ===============================================================================
# By: June P. Canas
# Project made with: Qt Designer and PySide2
# v: 1.0.2
# ===============================================================

import sys
import platform
import os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

# GUI FILE
from ui_mainWindow import Ui_MainWindow

# IMPORT FUNCTIONS
from ui_functions import *
### IMPORT DATABASES #####
import classDataBase
import profileDataBase
import gradesJHSDataBase
import shsSubject
import gradesSHSDataBase1
import gradesSHSDataBase2
import ovDataBase
import attDataBase

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # MOVE WINDOW
        def moveWindow(event):
            # RESTORE BEFORE MOVE
            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            # IF LEFT CLICK MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # SET TITLE BAR
        self.ui.titleBar.mouseMoveEvent = moveWindow
        ################# Make/Connect Class Data Base #################
        classDataBase.classData()

        #### Default Display Page
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

        ## ==> SET UI DEFINITIONS
        UIFunctions.uiDefinitions(self)

        UIFunctions.homeFunctions(self)    ######### (HOME PAGE FUNCTIONALITIES PAGING BUTTONS) ###############
        UIFunctions.profileFunctions(self) ######### PROFILE PAGE FUNCTIONALITIES and BUTTONS #######
        self.displayClass()

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()

     ###### Set Current Page Function #############################
    def setPage(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)

    ################ SAVING CLASS DATA AND DISPLAY TO INFO TO ALL PAGE ################################

    def saveClass(self): 

        myClass = classDataBase.viewDataclass()
        if len(myClass) == 0:

            classCondition = self.ui.homeSection.depCombo.currentText() == "-- select --" or self.ui.homeSection.syEntry.text() == "" or self.ui.homeSection.syEntry.text().isspace()\
                            or self.ui.homeSection.shEntry.text() == "" or self.ui.homeSection.shEntry.text().isspace()\
                            or self.ui.homeSection.sectionEntry.text() == "" or self.ui.homeSection.sectionEntry.text().isspace()\
                            or self.ui.homeSection.advEntry.text() == "" or self.ui.homeSection.advEntry.text().isspace()

            if  classCondition:
                self.showMessage("Incomplete Info","Please fill-up the required fields", QMessageBox.Warning)
            else:
                classDataBase.addClassRec(self.ui.homeSection.depCombo.currentText(), self.ui.homeSection.syEntry.text(), self.ui.homeSection.shEntry.text().upper(), self.ui.homeSection.gradeCombo.currentText(),\
                                           self.ui.homeSection.sectionEntry.text().upper(), self.ui.homeSection.advEntry.text().upper(), self.ui.homeSection.strandCombo.currentText(), self.ui.homeSection.semCombo.currentText()) 
                
                profileDataBase.studentData()                                           ########## Database for Learner's Profile #########
                ovDataBase.values_data()                                                ########## Database for observe values #########
                attDataBase.month_data()                                                ########## Database for Month #########
                attDataBase.insertMonth("Month1","Month2","Month3","Month4","Month5","Month6","Month7","Month8","Month9","Month10","Month11","Month12") 
                attDataBase.att_data()                                                  ########## Database for attendance #########
                
                if self.ui.homeSection.depCombo.currentText() == "JUNIOR HIGH SCHOOL":
                    gradesJHSDataBase.gradesDataJHS()                                   ########## Database for JHS Grades ################
                else:
                    shsSubject.subj_SHS()                                               ########## Creating database shs subjects #########
                    gradesSHSDataBase1.gradesDataSem1()                                 ########## Database for SHS Grades ################
                    gradesSHSDataBase2.gradesDataSem2()

                self.displayClass()
                self.showMessage("Class Created","Class has been created", QMessageBox.Information) 
        else:
            self.showMessage("Error","Class data has an existing entry", QMessageBox.Warning)

    def displayClass(self):

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            classData = myClass[0]

            ############# HOME CLASS INFO DISPLAY #############################
            self.ui.homeSection.depDisplay.setText(classData[1])
            self.ui.homeSection.shDisplay.setText(f"School Head: {classData[3]}")
            self.ui.homeSection.syDisplay.setText(f"School Year: {classData[2]}")
            self.ui.homeSection.advDisplay.setText(f"Adviser: {classData[6]}")
            self.ui.homeSection.semDisplay.setText(classData[8])
            self.ui.homeSection.gradeSecDisplay.setText(f"Grade {classData[4]} - {classData[5]}")
            self.ui.homeSection.strandDisplay.setText(classData[7])

            self.ui.homeSection.depCombo.setCurrentText(classData[1])
            self.ui.homeSection.depCombo.setEnabled(False)
            self.ui.homeSection.syEntry.setText(classData[2])
            self.ui.homeSection.syEntry.setEnabled(False)
            self.ui.homeSection.sectionEntry.setText(classData[5])
            self.ui.homeSection.sectionEntry.setEnabled(False)
            self.ui.homeSection.gradeCombo.addItem(classData[4])
            self.ui.homeSection.gradeCombo.setEnabled(False)
            self.ui.homeSection.shEntry.setText(classData[3])
            self.ui.homeSection.advEntry.setText(classData[6])
            self.ui.homeSection.strandCombo.setEnabled(False)

            self.ui.homeSection.profBtn0.setEnabled(True)
            self.ui.homeSection.gradeBtn0.setEnabled(True)
            self.ui.homeSection.attendBtn0.setEnabled(True)

            if classData[1] == "SENIOR HIGH SCHOOL":

                self.ui.homeSection.gradeBtn0.clicked.connect(lambda: self.setPage(self.ui.gradeSHSPage))   ### Home Section Page to (SHS Grade Page)
                self.ui.gradesBtnProf.clicked.connect(lambda: self.setPage(self.ui.gradeSHSPage))           ### Profile Section Page to (SHS Grade Page)
                self.ui.prevBtnAttend.clicked.connect(lambda: self.setPage(self.ui.gradeSHSPage))           ### Attendance Section Page to (SHS Grade Page)

                self.ui.homeSection.strandCombo.addItems(["General Academic Strand","TVL - BPP, BNC & Dressmaking"])
                self.ui.homeSection.strandCombo.setCurrentText(classData[7])
                self.ui.homeSection.semCombo.addItems(["1st Semester","2nd Semester"])
                self.ui.homeSection.semCombo.setCurrentText(classData[8])

                UIFunctions.shsGradeFunctions(self,classData)         ########## SHS GRADE PAGE FUNCTIONALITIES and BUTTONS  ###########

            else:
                self.ui.homeSection.gradeBtn0.clicked.connect(lambda: self.setPage(self.ui.gradeJHSPage))   ### Home Section Page to (JHS Grade Page)
                self.ui.gradesBtnProf.clicked.connect(lambda: self.setPage(self.ui.gradeJHSPage))           ### Profile Section Page to (JHS Grade Page)
                self.ui.prevBtnAttend.clicked.connect(lambda: self.setPage(self.ui.gradeJHSPage))           ### Attendance Section Page to (JHS Grade Page)

                UIFunctions.jhsGradeFunctions(self,classData)          ########## JHS GRADE PAGE FUNCTIONALITIES and BUTTONS  ###########                                                

            ############ PROFILE CLASS INFO DISPLAY #########################
            self.ui.profSection.depLabel.setText(classData[1])
            self.ui.profSection.syLabel.setText(f"S/Y: {classData[2]}")
            self.ui.profSection.gradeSectionLabel.setText(f"Grade {classData[4]} - {classData[5]}")
            self.ui.profSection.strandLabel.setText(classData[7])
            self.ui.profSection.adviserLabel.setText(classData[6])
            self.ui.profSection.semLabel.setText(classData[8])

            UIFunctions.attendanceOV(self,classData)          ########## ATTENDANCE and OV PAGE FUNCTIONALITIES and BUTTONS  ########### 
        else:
            UIFunctions.resetDisplay(self)
    
    def saveLearner(self):

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            classData = myClass[0]

            addressAll = self.ui.profSection.brgyEntry.text() + ', ' + self.ui.profSection.munEntry.text() + ', ' + self.ui.profSection.provEntry.text()
            dob = self.ui.profSection.monthCombo.currentText() + ' ' + self.ui.profSection.dateEntry.text() + ' ' +  self.ui.profSection.yearEntry.text()
            lastName = self.ui.profSection.l_nameEntry.text()
            firstName = self.ui.profSection.f_nameEntry.text()
            middleName = self.ui.profSection.m_nameEntry.text()
            mother = self.ui.profSection.motherEntry.text()
            father = self.ui.profSection.fatherEntry.text()
            guardian = self.ui.profSection.guardianEntry.text()

            if lastName == "" or firstName == "" or self.ui.profSection.lrn_entry.text() == "":                   
                self.showMessage("Required field missing","Please fill-up LRN, Last Name and First Name", QMessageBox.Warning)
            else:
                ########################## ADDING ENTRIES TO PROFILE DATABASE ########################################################
                profileDataBase.addStdRec(self.ui.profSection.lrn_entry.text(),lastName.upper(),firstName.upper(),middleName.upper(),self.ui.profSection.n_ExtEntry.text(),\
                    self.ui.profSection.sexComboBox.currentText(), self.ui.profSection.ageEntry.text(), addressAll.upper(),dob.upper(),mother.upper(),father.upper(),\
                    guardian.upper(), self.ui.profSection.modalCombo.currentText(), self.ui.profSection.eligCombo.currentText())

                self.ui.profSection.showLearner()                    ############ Adding Learner's data to tableWidget row ##########

                if middleName == "":
                    middleInitial = ""
                else:
                    middleInitial = middleName[0].upper()

                name = str(f"{lastName.upper()}, {firstName.upper()} {middleInitial}. {self.ui.profSection.n_ExtEntry.text()}")

                ovDataBase.insert_values(name, self.ui.profSection.lrn_entry.text(),\
                '','','','','','','','','','','','','','','','','','','','','','','','','','','','')  ############### Observe Values SECTION (Adding Entry) ###########

                attDataBase.insert_att(name, self.ui.profSection.lrn_entry.text(),\
                '','','','','','','','','','','','','','','','','','','','','','','','','','',\
                '','','','','','','','','','','','','')                                   ############### Attendance SECTION (Adding Entry) ###########
 
                self.ui.attOVSection.showAttOV_Info()

                if classData[1] == "JUNIOR HIGH SCHOOL":    ############### JHS Grades SECTION (Adding Entry) ###########################

                    gradesJHSDataBase.insertGradeJHS(name, self.ui.profSection.lrn_entry.text(), self.ui.profSection.sexComboBox.currentText(), self.ui.profSection.ageEntry.text(),\
                            '','','','','','','','','','','','','','','','','','','','',\
                            '','','','','','','','','','','','','','','','','','','','',\
                            '','','','','','','','','','','','','','','','','','','','')

                    self.ui.gJHSSection.showJHS_Info()

                else:                                       ############### SHS Grades SECTION (Adding Entry) ###########################
            
                    gradesSHSDataBase1.insertGradeSem1(name, self.ui.profSection.lrn_entry.text(), self.ui.profSection.sexComboBox.currentText(), self.ui.profSection.ageEntry.text(),\
                            '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','')

                    gradesSHSDataBase2.insertGradeSem2(name, self.ui.profSection.lrn_entry.text(), self.ui.profSection.sexComboBox.currentText(), self.ui.profSection.ageEntry.text(),\
                            '','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','')

                    self.ui.gSHSSection.showSHS_Info()

                self.ui.profSection.clearEntry()                      ########### Clear entries (Profile Section) #######################
                self.showMessage("Add Learner","Learner has been successfully added to class", QMessageBox.Information)

    def delContentDB(self):

        myClass = classDataBase.viewDataclass()
        classData = myClass[0]
        profileDataBase.deleteALLStdRec()
        ovDataBase.deleteALLvalues()
        attDataBase.delete_AllAtt()

        if classData[1] == "JUNIOR HIGH SCHOOL":
            gradesJHSDataBase.deleteALLGradeJHS()   
        else:
            gradesSHSDataBase1.deleteALLGradesem1()
            gradesSHSDataBase2.deleteALLGradesem2()
        
    # APP EVENTS
    #######################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def showMessage(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)   ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())