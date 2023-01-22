# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gradesJHSGHElFo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QIntValidator)
from PySide2.QtWidgets import *

import classDataBase
import profileDataBase
import gradesJHSDataBase

class Ui_gradesJHSsection(object):
    def setupUi(self, gradesJHSsection):
        if gradesJHSsection.objectName():
            gradesJHSsection.setObjectName(u"gradesJHSsection")
        gradesJHSsection.resize(1146, 784)
        gradesJHSsection.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(235, 235, 235);\n"
"}")
        self.horizontalLayout = QHBoxLayout(gradesJHSsection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(gradesJHSsection)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(395, 0))
        self.frame.setMaximumSize(QSize(395, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 140))
        self.frame_4.setMaximumSize(QSize(16777215, 140))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gradeSecJHS = QLabel(self.frame_4)
        self.gradeSecJHS.setObjectName(u"gradeSecJHS")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gradeSecJHS.setFont(font)
        self.gradeSecJHS.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(67, 156, 250);\n"
"    border-radius: 10px;\n"
"	color: rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.gradeSecJHS)

        self.advJHS = QLabel(self.frame_4)
        self.advJHS.setObjectName(u"advJHS")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.advJHS.setFont(font1)

        self.verticalLayout.addWidget(self.advJHS)

        self.syJHS = QLabel(self.frame_4)
        self.syJHS.setObjectName(u"syJHS")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.syJHS.setFont(font2)

        self.verticalLayout.addWidget(self.syJHS)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 95))
        self.frame_3.setMaximumSize(QSize(16777215, 95))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_3)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(14)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lrn_JHS = QLabel(self.frame_3)
        self.lrn_JHS.setObjectName(u"lrn_JHS")
        self.lrn_JHS.setMinimumSize(QSize(0, 30))
        self.lrn_JHS.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lrn_JHS.setFont(font4)
        self.lrn_JHS.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lrn_JHS)

        self.name_JHS = QLabel(self.frame_3)
        self.name_JHS.setObjectName(u"name_JHS")
        self.name_JHS.setMinimumSize(QSize(0, 30))
        self.name_JHS.setMaximumSize(QSize(16777215, 30))
        self.name_JHS.setFont(font4)
        self.name_JHS.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_JHS)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        font5.setItalic(True)
        self.label_6.setFont(font5)

        self.verticalLayout_2.addWidget(self.label_6)

        self.studentJHSTable = QTableWidget(self.frame)
        if (self.studentJHSTable.columnCount() < 2):
            self.studentJHSTable.setColumnCount(2)
        self.brush = QBrush(QColor(67, 156, 250, 255))
        self.brush.setStyle(Qt.SolidPattern)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        __qtablewidgetitem.setForeground(self.brush);
        self.studentJHSTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        __qtablewidgetitem1.setForeground(self.brush);
        self.studentJHSTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.studentJHSTable.setObjectName(u"studentJHSTable")
        fontstudent = QFont()
        fontstudent.setFamily(u"Segoe UI")
        fontstudent.setPointSize(10)
        self.studentJHSTable.setFont(fontstudent)
        self.studentJHSTable.setStyleSheet(u"QTableWidget{border: none;\n"
"	background-color: rgb(255, 255, 255);}\n"
"QFrame{background-color:  rgb(255, 255, 255); border-radius: 15px;\n"	
"    border: none;}\n"
"QTableView::item:selected  {color: rgb(255, 255, 255);\n"
"	background-color: rgb(67, 156, 250);}\n"
"QScrollBar:vertical {border: none;\n"         
"            background: rgb(255, 255, 255);\n"
"            width: 20px;\n"
"            margin: 26px 6px 26px 6px;}\n"
"        QScrollBar::handle:vertical {\n"
"            background: lightgray;\n"
"            min-height: 26px;}\n"
"        QScrollBar::add-line:vertical {\n"
"            background: rgb(255, 255, 255);\n"
"            height: 26px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;}\n"
"        QScrollBar::sub-line:vertical {\n"
"            background: rgb(255, 255, 255);\n"
"            height: 26px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;}\n"
"        QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"            width: 26px;\n"
"            height: 26px;\n"
"            background: rgb(255, 255, 255);}\n"
"QScrollBar::up-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowUp.png\");}\n"
"QScrollBar::down-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowDown.png\");}\n"
"")
        self.studentJHSTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.studentJHSTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.studentJHSTable.horizontalHeader().setStretchLastSection(True)
        self.studentJHSTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.studentJHSTable)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 0, 12, 0)

        self.updGradeJHS = QPushButton(self.frame_5, clicked = lambda: self.updateJHSgrds())  ########################### update grades function connect ################
        self.updGradeJHS.setObjectName(u"updGradeJHS")
        self.updGradeJHS.setMinimumSize(QSize(0, 30))
        self.updGradeJHS.setFont(font2)
        self.updGradeJHS.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.updGradeJHS)

        self.clrGradeJHS = QPushButton(self.frame_5)
        self.clrGradeJHS.setObjectName(u"clrGradeJHS")
        self.clrGradeJHS.setMinimumSize(QSize(0, 30))
        self.clrGradeJHS.setFont(font2)
        self.clrGradeJHS.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.clrGradeJHS)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(gradesJHSsection)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(235, 235, 235);\n"
"    border: solid;\n"
"	border-width: 2px 2px 2px 2px;\n"
"	border-color: rgb(26, 194, 161);\n"
"	border-radius: 10px\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 50))
        self.label_7.setMaximumSize(QSize(16777215, 50))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(26, 194, 161);\n"
"    border-radius: 10px;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gradeJHSTable = QTableWidget(self.frame_6)
        if (self.gradeJHSTable.columnCount() < 6):
            self.gradeJHSTable.setColumnCount(6)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        __qtablewidgetitem6.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        __qtablewidgetitem7.setForeground(brush1);
        self.gradeJHSTable.setHorizontalHeaderItem(5, __qtablewidgetitem7)
        if (self.gradeJHSTable.rowCount() < 13):
            self.gradeJHSTable.setRowCount(13)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(4, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(5, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(6, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(7, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font2);
        self.gradeJHSTable.setVerticalHeaderItem(8, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font2);
        self.gradeJHSTable.setVerticalHeaderItem(9, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font2);
        self.gradeJHSTable.setVerticalHeaderItem(10, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font2);
        self.gradeJHSTable.setVerticalHeaderItem(11, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font4);
        self.gradeJHSTable.setVerticalHeaderItem(12, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.gradeJHSTable.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        self.gradeJHSTable.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.gradeJHSTable.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem24.setFont(font2);
        self.gradeJHSTable.setItem(0, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.gradeJHSTable.setItem(0, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.gradeJHSTable.setItem(0, 5, __qtablewidgetitem26)
        self.gradeJHSTable.setObjectName(u"gradeJHSTable")
        fontgrade = QFont()
        fontgrade.setFamily(u"Segoe UI Semibold")
        fontgrade.setPointSize(11)
        self.gradeJHSTable.setFont(fontgrade)
        # self.gradeJHSTable.setTextAlignment(Qt.AlignCenter);
        self.gradeJHSTable.setStyleSheet(u"QHeaderView:section{\n"
"	background-color: rgb(26, 191, 164);\n"
"border: 1px solid rgb(255, 255, 255);}\n"
"QTableCornerButton:section{\n"
" image: url(\"c:/LMS_appVer2/icons/subject.png\");\n"
"border: 1px solid rgb(26, 191, 164);\n"
"background-color: rgb(255, 255, 255);}\n"
"QTableView::item:selected  {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(67, 156, 250);}\n"
"QScrollArea{background-color: rgb(255, 255, 255);}\n"
"   QScrollBar:horizontal{border: none;\n"  
"         background: rgb(255, 255, 255);\n"
"         height: 18px;\n"
"         margin: 5px 26px 5px 26px;}\n"
"   QScrollBar::handle:horizontal {\n"
"         background: lightgray;\n"
"         min-width: 20px;}\n"
"   QScrollBar::add-line:horizontal {\n"
"            background:rgb(255, 255, 255);\n"
"            width: 20px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;}\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: rgb(255, 255, 255);\n"
"            width: 20px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;}\n"
"        QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {\n"         
"            width: 26px;\n"
"            height: 26px;\n"
"            background: none;}\n"
"QScrollBar::left-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowLeft.png\");}\n"
"QScrollBar::right-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowRight.png\");}\n"
"")
        self.gradeJHSTable.setColumnWidth(0,80)  ###################################### Column width (grades table)#######################
        self.gradeJHSTable.setColumnWidth(1,80)
        self.gradeJHSTable.setColumnWidth(2,80)
        self.gradeJHSTable.setColumnWidth(3,80)
       
        # delegate = Delegate()
        # for col in range(5):
        #     self.gradeJHSTable.setItemDelegateForColumn(col, delegate)   ######################### Validator for tablewidget to enter Int Value only ##########

        self.studentJHSTable.verticalHeader().setDefaultSectionSize(44)

        self.gradeJHSTable.horizontalHeader().setStretchLastSection(True)
        self.gradeJHSTable.verticalHeader().setVisible(True)
        self.gradeJHSTable.verticalHeader().setMinimumSectionSize(22)
        self.gradeJHSTable.verticalHeader().setDefaultSectionSize(44)

        self.gradeJHSTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch);  
        self.gradeJHSTable.verticalHeader().setStyleSheet("QHeaderView:section{background-color: rgb(255,255,255); \
                                                            border-bottom: 1px solid rgb(200,200,200); border-right: 1px solid rgb(200,200,200);}")

        self.horizontalLayout_3.addWidget(self.gradeJHSTable)

        self.verticalLayout_3.addWidget(self.frame_6)

        self.horizontalLayout.addWidget(self.frame_2)

        self.retranslateUi(gradesJHSsection)

        QMetaObject.connectSlotsByName(gradesJHSsection)
    # setupUi
        self.studentJHSTable.cellClicked.connect(lambda: self.clickedJHSTable())   ####### Signal for clicking cell in table widget ##################
    
    ################################################## FUNCTIONS ################################
    def clickedJHSTable(self):

        learner = profileDataBase.viewstudentData()
        ldata = gradesJHSDataBase.viewGradeJHS()
        global studentinfo
        failColor = QBrush(QColor(255, 100, 0, 255))  #### Orange ####
        failColor.setStyle(Qt.SolidPattern)
        averageList = []

        if len(learner) != 0: 
            select_list = []
            self.lrn_JHS.setText("")
            self.name_JHS.setText("")

            for item in self.studentJHSTable.selectedItems():
                select_list.append(item.text())

            self.lrn_JHS.setText(select_list[0])
            self.name_JHS.setText(select_list[1])

            for s in ldata:
                studentinfo = list(s)
                if select_list[0] == studentinfo[2]:
                    break

            for graderow in range(12):               ############# Display selected info Grades to table ##################
                for gradecolumn in range(4):
                    jhsItem = QTableWidgetItem(studentinfo[(5 + gradecolumn)+(5*graderow)])
                    self.gradeJHSTable.setItem(graderow, gradecolumn, QTableWidgetItem(""))
                    self.gradeJHSTable.setItem(graderow, gradecolumn, jhsItem)
                    jhsItem.setTextAlignment(Qt.AlignCenter)

            for genCol in range(6):
                self.gradeJHSTable.setItem(12, genCol, QTableWidgetItem(""))

            for finrow in range(8):
                aveText = studentinfo[ 9 +(5*finrow)]
                finalItem = QTableWidgetItem(aveText)
                self.gradeJHSTable.setItem(finrow, 4, QTableWidgetItem(""))
                self.gradeJHSTable.setItem(finrow, 4, finalItem)
                finalItem.setForeground(self.brush)
                finalItem.setTextAlignment(Qt.AlignCenter)
                averageList.append(aveText)

                self.showRemarks(finrow, aveText, failColor)

            self.genAve(averageList)          

    def showJHS_Info(self):

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:

            learner = profileDataBase.viewstudentData()
            # classData = myClass[0]
            if len(learner) != 0:    
                self.studentJHSTable.setRowCount(0)
                for i, lrn_Name in enumerate(learner):
                    table_name = []  
                    table_name.append(lrn_Name[1])  ############# append LRN to temporary table name list ########

                    if lrn_Name[4] == "" or lrn_Name[4] == " ":
                        midname = "-"
                    else:
                        midname = lrn_Name[4].strip()

                    nameJHS = str(f"{lrn_Name[2]}, {lrn_Name[3]} {midname[0]}. {lrn_Name[5]}")
                    table_name.append(nameJHS) ############# append name to temporary table name list ########

                    self.rowcount = self.studentJHSTable.rowCount() 
                    self.studentJHSTable.insertRow(self.rowcount)    ########### Adding Row to table ############

                    for column, val in enumerate(tuple(table_name)):
                        self.studentJHSTable.setItem(i, column, QTableWidgetItem(val))  
            
        else:
            print("No JHS Grade Data Available")

    def updateJHSgrds(self):
        gData = gradesJHSDataBase.viewGradeJHS()
        grdList = []
        try:
            for subrow in range(12):     
                for subcol in range(4):
                    if subrow == 7:
                        continue
                    grdData = self.gradeJHSTable.item(subrow,subcol)
                    grdList.append(grdData.text())

            checkLetter = True

            for m in grdList:                       ################ Check if entry contain letters or symbols ######
                if not(m.isdigit() or m == ''):
                    self.showMessage("Error","Letters and symbols are not accepted\nPlease type integer value", QMessageBox.Warning)
                    print(f'invalid {m}')
                    checkLetter = False
                    break  

            if checkLetter:

                for genCol in range(6):
                    self.gradeJHSTable.setItem(12, genCol, QTableWidgetItem(""))

                gradesJHSDataBase.updJHSGrade(grdList, studentinfo[0])
                self.showMapeh(studentinfo[0])   ########## compute mapeh final grade #######
                self.showFinalJHS(studentinfo[0]) ########## compute final grade on each subject #######
                self.clickedJHSTable()      ##### Refresh Display on table ###########    
                self.showMessage("Grades Update","Grades has been updated successfully", QMessageBox.Information)   
        except:  
            self.showMessage("Error","No learner selected", QMessageBox.Warning)

    def showMapeh(self, myId):   ################# compute and update mapeh grade ############
        mapehAve = []   
        for mapehcol in range(4):
            mapehComp = []
            mapehBox = self.gradeJHSTable.item(7, mapehcol)       ######### item for mapeh (1st to 4th) ########
            for mapehrow in range(8,12):
                mapehFin = self.gradeJHSTable.item(mapehrow,mapehcol)   ######### item iteration for music, arts, pe and health ########
                mapehComp.append(mapehFin.text())                       ######### List for music, arts, pe and health entry ########
            
            if all(m for m in mapehComp): 
                total = int(mapehComp[0]) + int(mapehComp[1]) + int(mapehComp[2]) + int(mapehComp[3])  
                ave = total/len(mapehComp)
                mapehAve.append(round(ave))

            else:
                mapehAve.append("")
                if mapehBox.text() != "":
                    self.gradeJHSTable.setItem(7, mapehcol, QTableWidgetItem(""))

        gradesJHSDataBase.updMapehGrade(mapehAve, myId)

        # if not(all(k for k in mapehAve)):   
        #     self.showMessage("MAPEH Grade","MAPEH grade will be automatically computed if\nMusic, Arts, PE, and Health have entries", QMessageBox.Information)       
        # else:
            
    def showFinalJHS(self, myId):    ######### compute and update final grade in database #############
        finalAve = []
        for finalrow in range(12):
            finalComp = []
            for finalcol in range(4):
                subjectFinal = self.gradeJHSTable.item(finalrow, finalcol)
                finalComp.append(subjectFinal.text())

            if all(f for f in finalComp):
                totalfin = int(finalComp[0]) + int(finalComp[1]) + int(finalComp[2]) + int(finalComp[3])  
                avefin = totalfin/len(finalComp)
                finalAve.append(round(avefin))
            else:
                finalAve.append("") 

        gradesJHSDataBase.updJHSFinal(finalAve, myId)

    def showRemarks(self, remarkRow, averageItem, color):
 
        failColor = QBrush(QColor(255, 100, 0, 255))  #### Orange ####
        failColor.setStyle(Qt.SolidPattern)
       
        passItem = QTableWidgetItem("Passed")
        failItem = QTableWidgetItem("Failed")

        if averageItem != "":
            if int(averageItem) >= 75:
                self.gradeJHSTable.setItem(remarkRow, 5, QTableWidgetItem(""))
                self.gradeJHSTable.setItem(remarkRow, 5, passItem)
                passItem.setTextAlignment(Qt.AlignCenter)
            else:
                self.gradeJHSTable.setItem(remarkRow, 5, QTableWidgetItem(""))
                self.gradeJHSTable.setItem(remarkRow, 5, failItem)
                failItem.setTextAlignment(Qt.AlignCenter)
                failItem.setForeground(color)
        else:
            self.gradeJHSTable.setItem(remarkRow, 5, QTableWidgetItem(""))

    def genAve(self, average):

        if all(k for k in average):    ########## show general average on tablewidget ####### 
            sum_digit = 0
            for x in average:
                sum_digit = (sum_digit + int(x))

            aveGen = (sum_digit/len(average))
            aveItem = QTableWidgetItem(str(aveGen))
            self.gradeJHSTable.setItem(12, 4, QTableWidgetItem(""))
            self.gradeJHSTable.setItem(12, 4, aveItem)
            aveItem.setTextAlignment(Qt.AlignCenter)
            aveItem.setFont(QFont("Segoe UI Semibold", 16, QFont.Bold))
            aveItem.setForeground(self.brush)
        else:
            self.gradeJHSTable.setItem(12, 4, QTableWidgetItem(""))

    def showMessage(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)   ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.exec_()

    def retranslateUi(self, gradesJHSsection):
        gradesJHSsection.setWindowTitle(QCoreApplication.translate("gradesJHSsection", u"Frame", None))
        self.gradeSecJHS.setText(QCoreApplication.translate("gradesJHSsection", u" Grade and Section", None))
        self.advJHS.setText(QCoreApplication.translate("gradesJHSsection", u"Adviser", None))
        self.syJHS.setText(QCoreApplication.translate("gradesJHSsection", u"School Year", None))
        self.label.setText(QCoreApplication.translate("gradesJHSsection", u"LRN:", None))
        self.label_2.setText(QCoreApplication.translate("gradesJHSsection", u"Name:", None))
        self.lrn_JHS.setText("")
        self.name_JHS.setText("")
        self.label_6.setText(QCoreApplication.translate("gradesJHSsection", u"  Select learner from the table", None))
        ___qtablewidgetitem = self.studentJHSTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("gradesJHSsection", u"LRN", None));
        ___qtablewidgetitem1 = self.studentJHSTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("gradesJHSsection", u"Name", None));
        self.updGradeJHS.setText(QCoreApplication.translate("gradesJHSsection", u"Update Grades", None))
        self.clrGradeJHS.setText(QCoreApplication.translate("gradesJHSsection", u"Clear Grades", None))
        self.label_7.setText(QCoreApplication.translate("gradesJHSsection", u"REPORT ON LEARNING PROGRESS AND ACHIEVEMENT", None))
        ___qtablewidgetitem2 = self.gradeJHSTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("gradesJHSsection", u"Q1", None));
        ___qtablewidgetitem3 = self.gradeJHSTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("gradesJHSsection", u"Q2", None));
        ___qtablewidgetitem4 = self.gradeJHSTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("gradesJHSsection", u"Q3", None));
        ___qtablewidgetitem5 = self.gradeJHSTable.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("gradesJHSsection", u"Q4", None));
        ___qtablewidgetitem6 = self.gradeJHSTable.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("gradesJHSsection", u"FINAL GRADE", None));
        ___qtablewidgetitem7 = self.gradeJHSTable.horizontalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("gradesJHSsection", u"REMARKS", None));
        ___qtablewidgetitem8 = self.gradeJHSTable.verticalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("gradesJHSsection", u"  Filipino", None));
        ___qtablewidgetitem9 = self.gradeJHSTable.verticalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("gradesJHSsection", u"  English", None));
        ___qtablewidgetitem10 = self.gradeJHSTable.verticalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("gradesJHSsection", u"  Mathematics", None));
        ___qtablewidgetitem11 = self.gradeJHSTable.verticalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("gradesJHSsection", u"  Science", None));
        ___qtablewidgetitem12 = self.gradeJHSTable.verticalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("gradesJHSsection", u"  Araling Panlipunan", None));
        ___qtablewidgetitem13 = self.gradeJHSTable.verticalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("gradesJHSsection", u"  Edukasyon sa Pagpapatao", None));
        ___qtablewidgetitem14 = self.gradeJHSTable.verticalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("gradesJHSsection", u"  Technology and Livelihood Education", None));
        ___qtablewidgetitem15 = self.gradeJHSTable.verticalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("gradesJHSsection", u"  MAPEH", None));
        ___qtablewidgetitem16 = self.gradeJHSTable.verticalHeaderItem(8)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("gradesJHSsection", u"     - Music", None));
        ___qtablewidgetitem17 = self.gradeJHSTable.verticalHeaderItem(9)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("gradesJHSsection", u"     - Arts", None));
        ___qtablewidgetitem18 = self.gradeJHSTable.verticalHeaderItem(10)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("gradesJHSsection", u"     - P.E.", None));
        ___qtablewidgetitem19 = self.gradeJHSTable.verticalHeaderItem(11)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("gradesJHSsection", u"     - Health", None));
        ___qtablewidgetitem20 = self.gradeJHSTable.verticalHeaderItem(12)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("gradesJHSsection", u"    GENERAL AVERAGE", None));

        __sortingEnabled = self.gradeJHSTable.isSortingEnabled()
        self.gradeJHSTable.setSortingEnabled(False)
        self.gradeJHSTable.setSortingEnabled(__sortingEnabled)

    # retranslateUi

# class Delegate(QStyledItemDelegate):
#     def createEditor(self, parent, option, index):
#         editor = super().createEditor(parent, option, index)
#         if isinstance(editor, QLineEdit):
#             validator = QIntValidator(0, 100, editor)
#             editor.setValidator(validator)

#         return editor

