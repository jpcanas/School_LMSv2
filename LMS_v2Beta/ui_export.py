# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_export2SRscDP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import profileDataBase
import classDataBase

import gradesJHSDataBase
import gradesSHSDataBase1
import gradesSHSDataBase2

class Ui_ExpWindow(object):
    def setupUi(self, ExpWindow):
        if ExpWindow.objectName():
            ExpWindow.setObjectName(u"ExpWindow")
        ExpWindow.resize(1135, 540)
        self.centralwidget = QWidget(ExpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 0))
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 100))
        self.frame_6.setMaximumSize(QSize(16777215, 100))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"    border-radius: 0px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 181, 21))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.selectFileOption = QComboBox(self.frame_6)
        self.selectFileOption.addItem("Report Card")            ########### Items for select file option ############
        self.selectFileOption.addItem("Class List")
        self.selectFileOption.setObjectName(u"selectFileOption")
        self.selectFileOption.setGeometry(QRect(40, 60, 281, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        self.selectFileOption.setFont(font1)
        self.selectFileOption.setStyleSheet(u"QComboBox{\n"
"border: 1px solid rgb(26, 191, 164);\n"
"border-radius: 2px;\n"
"}")
        self.selectFileOption.currentIndexChanged.connect(self.selectFunction)  ############### Signal for combobox changed #####
        # self.selectFileOption.setCurrentIndex(0)
        self.verticalLayout.addWidget(self.frame_6)

        self.stackedSide = QStackedWidget(self.frame)
        self.stackedSide.setObjectName(u"stackedSide")
        self.sidePage1 = QWidget()
        self.sidePage1.setObjectName(u"sidePage1")
        self.verticalLayout_2 = QVBoxLayout(self.sidePage1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.rcardFrame = QFrame(self.sidePage1)
        self.rcardFrame.setObjectName(u"rcardFrame")
        self.rcardFrame.setFrameShape(QFrame.StyledPanel)
        self.rcardFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.rcardFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.rcardFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 145))
        self.frame_7.setMaximumSize(QSize(16777215, 145))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"    border-radius: 0px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.selectAll = QRadioButton(self.frame_7)
        self.selectAll.setObjectName(u"selectAll")
        self.selectAll.setGeometry(QRect(20, 10, 161, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.selectAll.setFont(font2)
        self.selectAll.setStyleSheet(u"")
        self.selectFrom = QRadioButton(self.frame_7)
        self.selectFrom.setObjectName(u"selectFrom")
        self.selectFrom.setGeometry(QRect(20, 40, 221, 21))
        self.selectFrom.setFont(font2)
        self.selectOption = QComboBox(self.frame_7)
        self.selectOption.setObjectName(u"selectOption")
        self.selectOption.setGeometry(QRect(40, 70, 291, 31))
        self.selectOption.setFont(font1)
        self.selectOption.setStyleSheet(u"QComboBox{\n"
"border: 1px solid rgb(26, 191, 164);\n"
"border-radius: 2px;\n"
"}")
        self.addBtn = QPushButton(self.frame_7, clicked=lambda:self.addLearner())    ############# Add learner Button #############
        self.addBtn.setObjectName(u"addBtn")
        self.addBtn.setGeometry(QRect(130, 110, 93, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(8)
        font3.setBold(True)
        font3.setWeight(75)
        self.addBtn.setFont(font3)
        self.addBtn.setStyleSheet(u"QPushButton{\n"
"       color: rgb(26, 194, 161);\n"
"       border-radius: 10px;\n"
"       border: 2px solid rgb(191, 191, 191);\n"
"       background-color: rgb(255, 255, 255);}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 194, 161);\n"
"       color: rgb(255, 255, 255);\n"
"       border-radius: 10px;}\n"
"QPushButton:disabled{\n"
"background-color: rgb(200, 200, 200);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 5px;\n"
" border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.clrBtn = QPushButton(self.frame_7)
        self.clrBtn.setObjectName(u"clrBtn")
        self.clrBtn.setGeometry(QRect(240, 110, 93, 28))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setBold(True)
        font4.setWeight(75)
        self.clrBtn.setFont(font4)
        self.clrBtn.setStyleSheet(u"QPushButton{\n"
"       color: rgb(26, 194, 161);\n"
"       border-radius: 10px;\n"
"       border: 2px solid rgb(191, 191, 191);\n"
"       background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 194, 161);\n"
"       color: rgb(255, 255, 255);\n"
"       border-radius: 10px;\n"
"}")

        self.verticalLayout_8.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.rcardFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame{\n"
"    border-radius: 0px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(40, -1, -1, -1)
        self.listWidget_2 = QListWidget(self.frame_4)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setStyleSheet(u"QListWidget{\n"
"border: 1px solid rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"}")

        self.verticalLayout_7.addWidget(self.listWidget_2)


        self.verticalLayout_8.addWidget(self.frame_4)


        self.verticalLayout_2.addWidget(self.rcardFrame)

        self.stackedSide.addWidget(self.sidePage1)
        self.sidePage2 = QWidget()
        self.sidePage2.setObjectName(u"sidePage2")
        self.verticalLayout_5 = QVBoxLayout(self.sidePage2)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.classProfFrame = QFrame(self.sidePage2)
        self.classProfFrame.setObjectName(u"classProfFrame")
        self.classProfFrame.setFrameShape(QFrame.StyledPanel)
        self.classProfFrame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.classProfFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 281, 51))
        self.label_2.setFont(font)
        self.bdayCheck = QCheckBox(self.classProfFrame)
        self.bdayCheck.setObjectName(u"bdayCheck")
        self.bdayCheck.setGeometry(QRect(50, 140, 171, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        self.bdayCheck.setFont(font5)
        self.addressCheck = QCheckBox(self.classProfFrame)
        self.addressCheck.setObjectName(u"addressCheck")
        self.addressCheck.setGeometry(QRect(50, 170, 81, 20))
        self.addressCheck.setFont(font5)
        self.blankCheck = QCheckBox(self.classProfFrame)
        self.blankCheck.setObjectName(u"blankCheck")
        self.blankCheck.setGeometry(QRect(20, 220, 151, 20))
        self.blankCheck.setFont(font5)
        self.label_3 = QLabel(self.classProfFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 270, 261, 41))
        self.label_3.setFont(font5)
        self.title = QLineEdit(self.classProfFrame)
        self.title.setPlaceholderText("Title")     ################### Placeholder Text ##############
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 320, 301, 31))
        self.title.setFont(font5)
        self.title.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid rgb(26, 191, 164);\n"
"border-radius: 3px;\n"
"}")
        self.textEdit = QTextEdit(self.classProfFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 10, 291, 87))

        self.verticalLayout_5.addWidget(self.classProfFrame)

        self.stackedSide.addWidget(self.sidePage2)

        self.verticalLayout.addWidget(self.stackedSide)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"    border-radius: 0px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)

        self.expBtn = QPushButton(self.frame_3, clicked = lambda: self.exportBtn()) ############ Exp Btn ############
        self.expBtn.setObjectName(u"expBtn")
        self.expBtn.setMinimumSize(QSize(150, 35))
        self.expBtn.setMaximumSize(QSize(150, 35))
        self.expBtn.setFont(font)
        self.expBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(26, 191, 164)\n"
"}")

        self.horizontalLayout_2.addWidget(self.expBtn)

        self.cancelBtn = QPushButton(self.frame_3)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setMinimumSize(QSize(150, 35))
        self.cancelBtn.setMaximumSize(QSize(150, 35))
        self.cancelBtn.setFont(font)
        self.cancelBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(26, 191, 164)\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancelBtn)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setMaximumSize(QSize(777, 540))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.fileLabel = QLabel(self.frame_2)
        self.fileLabel.setObjectName(u"fileLabel")
        self.fileLabel.setMinimumSize(QSize(0, 40))
        self.fileLabel.setMaximumSize(QSize(16777215, 40))
        font6 = QFont()
        font6.setFamily(u"Segoe UI Semibold")
        font6.setPointSize(16)
        font6.setBold(True)
        font6.setWeight(75)
        self.fileLabel.setFont(font6)

        self.verticalLayout_3.addWidget(self.fileLabel)

        self.stackedWidget = QStackedWidget(self.frame_2)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"QStackedWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.page1)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cardTempPic = QLabel(self.page1)
        self.cardTempPic.setObjectName(u"cardTempPic")
        self.cardTempPic.setStyleSheet(u"")
        self.cardTempPic.setPixmap(QPixmap(u"icons/tempCard.png"))
        self.cardTempPic.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.cardTempPic)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.verticalLayout_6 = QVBoxLayout(self.page2)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.classListPic = QLabel(self.page2)
        self.classListPic.setObjectName(u"classListPic")
        self.classListPic.setPixmap(QPixmap(u"icons/tempList.jpg"))
        self.classListPic.setScaledContents(True)

        self.verticalLayout_6.addWidget(self.classListPic)

        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.horizontalLayout.addWidget(self.frame_2)

        ExpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExpWindow)

        self.selectAll.toggled.connect(lambda: self.radioState(self.selectAll))     ########### Signals for radio button ####
        self.selectFrom.toggled.connect(lambda: self.radioState(self.selectFrom))

        self.stackedSide.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(ExpWindow)
    # setupUi

    def selectFunction(self, i):

        match i:
            case 0:                     ######### Report Card Index #########
                self.fileLabel.setText("School Report Card")
                self.stackedSide.setCurrentIndex(0)
                self.stackedWidget.setCurrentIndex(0)
            case 1:                     ######## Class Profile ###########
                self.fileLabel.setText("Class List")
                self.stackedSide.setCurrentIndex(1)
                self.stackedWidget.setCurrentIndex(1)
            case _:
                print("Invalid")

######################################### REPORT CARD FUNCTIONS ####################################

    def radioState(self, r):
        if r.isChecked():
            if r.text() == "Select learner from list":   
                self.fewLearner()
            elif r.text() == "Select all learners": 
                self.allLearners()

    def nameListAll(self):      ########### Function for creating new list of names and LRN of all learners #######

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            classData = myClass[0]
            if classData[1] == 'JUNIOR HIGH SCHOOL':
                gradesdata = gradesJHSDataBase.viewGradeJHS()            ##### JHS Grade Data ###########
            else:
                gradesdata = gradesSHSDataBase1.viewGradesem1()        ##### SHS Grade Data ###########
                
        return gradesdata

    def allLearners(self):       ############ Radio button command (select All learners) ##############

        global nameGradeList
                    
        self.selectOption.clear()
        self.selectOption.addItem("-- ALL STUDENTS WERE SELECTED --")
        self.addBtn.setEnabled(False)

        self.listWidget.clear()
        nameGradeList = []

    def fewLearner(self):       ############ Radio button command (select few learners) ##############

        global nameGradeList    
        nameGradeList = []

        grdList = self.nameListAll()
        nameDisplay = []
        for lrnNameOne in grdList:
            nameDisplay.append((f"{(lrnNameOne[0])},    {lrnNameOne[1]}"))

        self.selectOption.clear()
        self.selectOption.addItems(nameDisplay)
        self.addBtn.setEnabled(True)

    def addLearner(self):

        grdList = self.nameListAll()
        optionItem = self.selectOption.currentText()
        optionList = optionItem.split(",",2)
        self.listWidget.addItem(QListWidgetItem(optionItem))
                               
        for lrnNameOne in grdList:
            if optionList[0] == str(lrnNameOne[0]):
                nameGradeList.append(lrnNameOne)        ###### Adding temporary list of selected student #########

    def clrList(self):
        global nameGradeList
        self.listWidget.clear()
        nameGradeList = []

#########################################################################################################
        
    def exportBtn(self):

        if self.selectFileOption.currentIndex() == 0:
            print("Report Card Exported")
        else:
            columnAdd = [self.bdayCheck.isChecked(), self.addressCheck.isChecked(), self.blankCheck.isChecked()]
            print(columnAdd)
            if self.title.text() == "":
                print("blank title")

        # from cardExport import exportCard
        # folderpath = QFileDialog.getExistingDirectory(None, 'Select Folder')

        # if len(folderpath) != 0:
        #     grdList = self.nameListAll()
        #     if self.selectAll.isChecked():                     
        #         exportCard(grdList, folderpath)
                         
        #     elif self.selectFrom.isChecked():       
        #         exportCard(nameGradeList, folderpath)         

        #     self.showMessage("Exported", f"Report Card has been successfully exported\nCheck your directory {folderpath}", QMessageBox.Information)

    def showMessage(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)   ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.exec_()
        
    def retranslateUi(self, ExpWindow):
        ExpWindow.setWindowTitle(QCoreApplication.translate("ExpWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("ExpWindow", u"Select File to export:", None))
        self.selectAll.setText(QCoreApplication.translate("ExpWindow", u"Select all learners", None))
        self.selectFrom.setText(QCoreApplication.translate("ExpWindow", u"Select learner from list", None))
        self.addBtn.setText(QCoreApplication.translate("ExpWindow", u"Add learner", None))
        self.clrBtn.setText(QCoreApplication.translate("ExpWindow", u"Clear List", None))
        self.label_2.setText(QCoreApplication.translate("ExpWindow", u"Select learner's info to add:", None))
        self.bdayCheck.setText(QCoreApplication.translate("ExpWindow", u"Birthdate", None))
        self.addressCheck.setText(QCoreApplication.translate("ExpWindow", u"Address", None))
        self.blankCheck.setText(QCoreApplication.translate("ExpWindow", u"Add Blank Column", None))
        self.label_3.setText(QCoreApplication.translate("ExpWindow", u"Custom Document Title:", None))
        self.textEdit.setHtml(QCoreApplication.translate("ExpWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">This will generate excel file with table of Learner's Name. Addtional column may include on the table by selecting the desired information below.</span></p></body></html>", None))
        self.expBtn.setText(QCoreApplication.translate("ExpWindow", u"Export File", None))
        self.cancelBtn.setText(QCoreApplication.translate("ExpWindow", u"Cancel", None))
        self.fileLabel.setText(QCoreApplication.translate("ExpWindow", u"School Report Card", None))
        self.cardTempPic.setText("")
        self.classListPic.setText("")
    # retranslateUi

