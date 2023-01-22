# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_OpenFilefxCudq.ui'
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

import openSF1

class Ui_openFileWindow(object):
    def setupUi(self, openFileWindow):
        if openFileWindow.objectName():
            openFileWindow.setObjectName(u"openFileWindow")
        openFileWindow.resize(920, 500)
        openFileWindow.setMinimumSize(QSize(920, 500))
        openFileWindow.setMaximumSize(QSize(920, 500))
        self.centralwidget = QWidget(openFileWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.notValidPage = QWidget()
        self.notValidPage.setObjectName(u"notValidPage")
        self.horizontalLayout_2 = QHBoxLayout(self.notValidPage)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.notValidFrame = QFrame(self.notValidPage)
        self.notValidFrame.setObjectName(u"notValidFrame")
        self.notValidFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 5px;\n"
"}")
        self.notValidFrame.setFrameShape(QFrame.StyledPanel)
        self.notValidFrame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.notValidFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 10, 431, 71))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.notValidFrame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 30, 101, 81))
        self.label_3.setPixmap(QPixmap(u"icons/error.png"))
        self.label_3.setScaledContents(True)
        self.label_4 = QLabel(self.notValidFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(170, 50, 381, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(20)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_4.setFont(font1)
        self.textEdit = QTextEdit(self.notValidFrame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 140, 831, 241))

        self.okBtn = QPushButton(self.notValidFrame)
        self.okBtn.setObjectName(u"okBtn")
        self.okBtn.setGeometry(QRect(380, 430, 151, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.okBtn.setFont(font2)

        self.horizontalLayout_2.addWidget(self.notValidFrame)

        self.stackedWidget.addWidget(self.notValidPage)
        self.validFrame = QWidget()
        self.validFrame.setObjectName(u"validFrame")
        self.horizontalLayout_3 = QHBoxLayout(self.validFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.validFrame_2 = QFrame(self.validFrame)
        self.validFrame_2.setObjectName(u"validFrame_2")
        self.validFrame_2.setStyleSheet(u"")
        self.validFrame_2.setFrameShape(QFrame.StyledPanel)
        self.validFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.validFrame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame = QFrame(self.validFrame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(350, 0))
        self.frame.setMaximumSize(QSize(350, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.learnerDisplay = QTableWidget(self.frame)
        if (self.learnerDisplay.columnCount() < 2):
            self.learnerDisplay.setColumnCount(2)
        brush = QBrush(QColor(67, 156, 250, 255))
        brush.setStyle(Qt.SolidPattern)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setForeground(brush);
        self.learnerDisplay.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font3);
        __qtablewidgetitem1.setForeground(brush);
        self.learnerDisplay.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.learnerDisplay.setObjectName(u"learnerDisplay")
        self.learnerDisplay.setStyleSheet(u"QTableWidget{\n"
"border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QFrame{\n"
"	background-color:  rgb(255, 255, 255);\n"
"	border-radius: 15px;\n"
"    border: none;\n"
"}\n"
"\n"
"QTableView::item:selected  {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(67, 156, 250);\n"
"}\n"
"\n"
"")
        self.learnerDisplay.setSelectionMode(QAbstractItemView.SingleSelection)
        self.learnerDisplay.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.learnerDisplay.horizontalHeader().setStretchLastSection(True)
        self.learnerDisplay.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.learnerDisplay)


        self.horizontalLayout_4.addWidget(self.frame)

        self.frame_2 = QFrame(self.validFrame_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.textBrowser = QTextBrowser(self.frame_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 55))
        self.textBrowser.setMaximumSize(QSize(16777215, 55))

        self.verticalLayout_2.addWidget(self.textBrowser)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamily(u"Microsoft Sans Serif")
        font4.setPointSize(16)
        font4.setBold(False)
        font4.setWeight(50)
        self.label.setFont(font4)

        self.verticalLayout_2.addWidget(self.label)

        self.department = QLabel(self.frame_2)
        self.department.setObjectName(u"department")
        self.department.setFont(font4)

        self.verticalLayout_2.addWidget(self.department)

        self.schoolName = QLabel(self.frame_2)
        self.schoolName.setObjectName(u"schoolName")
        self.schoolName.setMinimumSize(QSize(0, 40))
        self.schoolName.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamily(u"Microsoft Sans Serif")
        font5.setPointSize(10)
        self.schoolName.setFont(font5)

        self.verticalLayout_2.addWidget(self.schoolName)

        self.schoolID = QLabel(self.frame_2)
        self.schoolID.setObjectName(u"schoolID")
        self.schoolID.setMinimumSize(QSize(0, 40))
        self.schoolID.setMaximumSize(QSize(16777215, 40))
        self.schoolID.setFont(font5)

        self.verticalLayout_2.addWidget(self.schoolID)

        self.schoolYear = QLabel(self.frame_2)
        self.schoolYear.setObjectName(u"schoolYear")
        self.schoolYear.setMinimumSize(QSize(0, 40))
        self.schoolYear.setMaximumSize(QSize(16777215, 40))
        self.schoolYear.setFont(font5)

        self.verticalLayout_2.addWidget(self.schoolYear)

        self.gradeSection = QLabel(self.frame_2)
        self.gradeSection.setObjectName(u"gradeSection")
        self.gradeSection.setMinimumSize(QSize(0, 40))
        self.gradeSection.setMaximumSize(QSize(16777215, 40))
        self.gradeSection.setFont(font5)

        self.verticalLayout_2.addWidget(self.gradeSection)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 0, 0);\n"
"}")

        self.verticalLayout_2.addWidget(self.label_6)

        self.textBrowser_2 = QTextBrowser(self.frame_2)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(0, 55))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 55))

        self.verticalLayout_2.addWidget(self.textBrowser_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 70))
        self.frame_3.setMaximumSize(QSize(16777215, 70))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.copyBtn = QPushButton(self.frame_3)
        self.copyBtn.setObjectName(u"copyBtn")
        self.copyBtn.setGeometry(QRect(80, 20, 171, 41))
        font6 = QFont()
        font6.setPointSize(10)
        self.copyBtn.setFont(font6)
        self.copyBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")
        self.cancelBtn = QPushButton(self.frame_3)
        self.cancelBtn.setObjectName(u"cancelBtn")
        self.cancelBtn.setGeometry(QRect(270, 20, 171, 41))
        self.cancelBtn.setFont(font6)
        self.cancelBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.verticalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.frame_2)


        self.horizontalLayout_3.addWidget(self.validFrame_2)

        self.stackedWidget.addWidget(self.validFrame)

        self.horizontalLayout.addWidget(self.stackedWidget)

        openFileWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(openFileWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(openFileWindow)
    # setupUi

    def sf1Checker(self, sf1path):
        
        import xlrd
        sf1book =  xlrd.open_workbook(sf1path)  
        sf1_sheet = sf1book.sheet_by_index(0) 

        validXLS = "notValidSF1"

        try:
            if sf1_sheet.cell_value(6,0) != "":                             #### JHS checker ########  
                if len(str(int(sf1_sheet.cell_value(6,0)))) == 12:
                    validXLS = "validJHS"

            elif sf1_sheet.cell_value(19,0) != "":                          #### SHS checker ######## 
                if len(str(int(sf1_sheet.cell_value(19,0)))) == 12:
                    validXLS = "validSHS"
            else:
                pass
        except:
            print("some value of lrn is not a number")

        return  validXLS

    def showSF1JHS_Data(self, sf1path):
        
        studentListJHS = openSF1.learnerJHS_SF1(sf1path)
        depInfoList = openSF1.depInfoJHS_SF1(sf1path)
        
        self.department.setText("JUNIOR HIGH SCHOOL")
        self.schoolName.setText("School Name: MANTALISAY NATIONAL HIGH SCHOOL")
        self.schoolID.setText("School ID: 309711")
        self.schoolYear.setText(f"School Year: {depInfoList[0]}")
        self.gradeSection.setText(f"Grade {depInfoList[1]} - {depInfoList[2]}")

        for row, student in enumerate(studentListJHS):
            lrn = student[0]
            gradesName = student[1] + ', ' + student[2] 
    
            self.rowcount = self.learnerDisplay.rowCount() 
            self.learnerDisplay.insertRow(self.rowcount)    ########### Adding Row to table ############

            self.learnerDisplay.setItem(row, 0, QTableWidgetItem(lrn))
            self.learnerDisplay.setItem(row, 1, QTableWidgetItem(gradesName))

    def showSF1SHS_Data(self, sf1path):

        studentListSHS = openSF1.learnerSHS_SF1(sf1path)
        depInfoListSHS = openSF1.depInfoSHS_SF1(sf1path)

        self.department.setText("SENIOR HIGH SCHOOL")
        self.schoolName.setText("School Name: MANTALISAY NATIONAL HIGH SCHOOL")
        self.schoolID.setText("School ID: 309711")
        self.schoolYear.setText(f"School Year: {depInfoListSHS[0]}")
        self.gradeSection.setText(f"{depInfoListSHS[1]} - {depInfoListSHS[2]}")

        for row, student in enumerate(studentListSHS):
            lrn = student[0]
            gradesName = student[1] + ', ' + student[2] 
    
            self.rowcount = self.learnerDisplay.rowCount() 
            self.learnerDisplay.insertRow(self.rowcount)    ########### Adding Row to table ############

            self.learnerDisplay.setItem(row, 0, QTableWidgetItem(lrn))
            self.learnerDisplay.setItem(row, 1, QTableWidgetItem(gradesName))

    def copyFunction(self, closeWindow, sf1path):

        # self.showMessage()

        if self.sf1Checker(sf1path) == "validJHS":  ########### checking supported excel file ##########
            studentListJHS = openSF1.learnerJHS_SF1(sf1path)  
            self.sftoDB(studentListJHS, True)             ####### Junior High ######
        elif self.sf1Checker(sf1path) == "validSHS":
            studentListSHS = openSF1.learnerSHS_SF1(sf1path)
            self.sftoDB(studentListSHS, False)              ####### Senior High #####
        else:
            pass
  
        closeWindow()

    def sftoDB(self, sf1List, jhsDefault):

        import profileDataBase
        import gradesJHSDataBase
        import gradesSHSDataBase1
        import gradesSHSDataBase2
        import ovDataBase
        import attDataBase
  
        for student in sf1List:

            grd_mdname = student[3].strip()
            gradesName = (f"{student[1]}, {student[2]} {grd_mdname[0]}.")

            profileDataBase.addStdRec(student[0], student[1], student[2], student[3], student[4],\
                    student[5], student[6], student[7], student[8], student[9], student[10],\
                    student[11], student[12], student[13])    

            attDataBase.insert_att(gradesName, student[0],\
                    '','','','','','','','','','','','','','','','','','','','','','','','','','',\
                    '','','','','','','','','','','','','')  
                                      
            ovDataBase.insert_values(gradesName, student[0],\
                    '','','','','','','','','','','','','','','','','','','','','','','','','','','','')

            if jhsDefault:

                gradesJHSDataBase.insertGradeJHS(gradesName, student[0], student[5], student[6],\
                '','','','','','','','','','','','','','','','','','','','',\
                '','','','','','','','','','','','','','','','','','','','',\
                '','','','','','','','','','','','','','','','','','','','')
            else:

                gradesSHSDataBase1.insertGradeSem1(gradesName, student[0], student[5], student[6],\
                '','','','','','','','','','','','','','','','','','','','','','','','','','',\
                '','','','','','','','','','','','','','','','','','','')

                gradesSHSDataBase2.insertGradeSem2(gradesName, student[0], student[5], student[6],\
                '','','','','','','','','','','','','','','','','','','','','','','','','','',\
                '','','','','','','','','','','','','','','','','','','')

        print("done importing sf1")

    def showMessage(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)   ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.exec_()

    def retranslateUi(self, openFileWindow):
        openFileWindow.setWindowTitle(QCoreApplication.translate("openFileWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("openFileWindow", u"Unsupported SF1 format", None))
        self.textEdit.setHtml(QCoreApplication.translate("openFileWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Sorry, the selected SF1 file is not supported</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size"
                        ":11pt;\">Possible Reasons:</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">1. School Form 1 downloaded from DepEd LIS has been updated and the app cannot extract the data from it. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">2. The selected SF1 file has been modified. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">3. File is corrupted</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px; font-size:10pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">(</span><span style=\" font-size:10pt; font-style:italic;\">If file has been modified, edited or corrupted, try to download new SF1 from DepEd LIS</span><span style=\" font-size:10pt;\">)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.okBtn.setText(QCoreApplication.translate("openFileWindow", u"OK", None))
        ___qtablewidgetitem = self.learnerDisplay.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("openFileWindow", u"LRN", None));
        ___qtablewidgetitem1 = self.learnerDisplay.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("openFileWindow", u"Name", None));
        self.textBrowser.setHtml(QCoreApplication.translate("openFileWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-style:italic;\">The following information has been found. Kindly check first before copying to LMS app</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("openFileWindow", u"School Form 1 (SF1) School Register", None))
        self.department.setText(QCoreApplication.translate("openFileWindow", u"<Department>", None))
        self.schoolName.setText(QCoreApplication.translate("openFileWindow", u"School Name:", None))
        self.schoolID.setText(QCoreApplication.translate("openFileWindow", u"School ID:", None))
        self.schoolYear.setText(QCoreApplication.translate("openFileWindow", u"School Year:", None))
        self.gradeSection.setText(QCoreApplication.translate("openFileWindow", u"Grade & Section:", None))
        self.label_6.setText(QCoreApplication.translate("openFileWindow", u"Important Note:", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("openFileWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-style:italic;\">Copying Learner's Information from SF1 will overwrite the existing data on LMS app</span></p></body></html>", None))
        self.copyBtn.setText(QCoreApplication.translate("openFileWindow", u"Copy ", None))
        self.cancelBtn.setText(QCoreApplication.translate("openFileWindow", u"Cancel ", None))
    # retranslateUi

     # def openSF1(self):
 #        sf1_excel = QFileDialog.getOpenFileName(None, "Open File", "", "Excel 97-2003 Workbook (*.xls)")
 #        print(str(sf1_excel))
        # open_File.learnerJHS_SF1(sf1_excel)
        
        #     myClass = classDataBase.viewDataclass()
    #     if len(myClass) != 0: 
            # myClassData = myClass[0]              Excel 97-2003 Workbook (*.xls)
            # sf1_excel = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)")
            # print(str(sf1_excel))
            # file_ext = pathlib.Path(sf1_excel).suffix
                                        
        #         if file_ext == '.xls':

        #         if class_impDep[1] == 'JUNIOR HIGH SCHOOL':
        #             open_File.learnerJHS_SF1(sf1_excel)
        #             display_studentData()
        #         else:
        #             msg = ''' Please check and update the First Name and Middle name entries of learner
        #                       Data maybe incorrect because the program separates first name and middle name through the spaces between them in the SF1'''
                                                                          
        #             open_File.learnerSHS_SF1(sf1_excel)
        #             display_studentData()
        #             messagebox.showinfo("SHS data",msg)

        #                 elif file_ext == '.zip':
        #                     print(file_ext) 
        #                 else:
        #                     pass
                        
        #     except Exception as ex:
        #         messagebox.showwarning("Error","Unsupported file or\n Some data cannot read by the program")
        #         print(ex)
        # else:
        #     messagebox.showerror("No info","No class data found\nPlease fill up the class info and then click save info")
