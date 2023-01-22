# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_gradesSHSZKmWvm.ui'
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
import shsSubject
import gradesSHSDataBase1
import gradesSHSDataBase2

class Ui_gradesSHSsection(object):
    def setupUi(self, gradesSHSsection):
        if gradesSHSsection.objectName():
            gradesSHSsection.setObjectName(u"gradesSHSsection")
        gradesSHSsection.resize(1103, 799)
        self.horizontalLayout = QHBoxLayout(gradesSHSsection)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(gradesSHSsection)
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
        self.frame_4.setMaximumSize(QSize(16777215, 170))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gradeSecSHS = QLabel(self.frame_4)
        self.gradeSecSHS.setObjectName(u"gradeSecSHS")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gradeSecSHS.setFont(font)
        self.gradeSecSHS.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(67, 156, 250);\n"
"    border-radius: 10px;\n"
"	color: rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.gradeSecSHS)

        self.strand = QLabel(self.frame_4)
        self.strand.setObjectName(u"strand")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.strand.setFont(font1)
        self.strand.setStyleSheet(u"QLabel{\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.verticalLayout.addWidget(self.strand)

        self.advSHS = QLabel(self.frame_4)
        self.advSHS.setObjectName(u"advSHS")
        self.advSHS.setFont(font1)

        self.verticalLayout.addWidget(self.advSHS)

        self.sySHS = QLabel(self.frame_4)
        self.sySHS.setObjectName(u"sySHS")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.sySHS.setFont(font2)

        self.verticalLayout.addWidget(self.sySHS)

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

        self.lrn_SHS = QLabel(self.frame_3)
        self.lrn_SHS.setObjectName(u"lrn_SHS")
        self.lrn_SHS.setMinimumSize(QSize(0, 30))
        self.lrn_SHS.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lrn_SHS.setFont(font4)
        self.lrn_SHS.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lrn_SHS)

        self.name_SHS = QLabel(self.frame_3)
        self.name_SHS.setObjectName(u"name_SHS")
        self.name_SHS.setMinimumSize(QSize(0, 30))
        self.name_SHS.setMaximumSize(QSize(16777215, 30))
        self.name_SHS.setFont(font4)
        self.name_SHS.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_SHS)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        font5.setItalic(True)
        self.label_6.setFont(font5)

        self.verticalLayout_2.addWidget(self.label_6)

        self.studentSHSTable = QTableWidget(self.frame)
        if (self.studentSHSTable.columnCount() < 2):
            self.studentSHSTable.setColumnCount(2)
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
        self.studentSHSTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        __qtablewidgetitem1.setForeground(self.brush);
        self.studentSHSTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.studentSHSTable.setObjectName(u"studentSHSTable")
        self.studentSHSTable.setStyleSheet(u"QTableWidget{border: none;\n"
"	background-color: rgb(255, 255, 255);}\n"
"QFrame{background-color:  rgb(255, 255, 255);\n"	
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
        self.studentSHSTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.studentSHSTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.studentSHSTable.horizontalHeader().setStretchLastSection(True)
        self.studentSHSTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.studentSHSTable)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 50))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 0, 12, 0)
        self.updGradeSHS = QPushButton(self.frame_5, clicked = lambda: self.updateSHSgrds())
        self.updGradeSHS.setObjectName(u"updGradeSHS")
        self.updGradeSHS.setMinimumSize(QSize(0, 30))
        self.updGradeSHS.setFont(font2)
        self.updGradeSHS.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);}\n"
"QPushButton:focus{background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;}")

        self.horizontalLayout_2.addWidget(self.updGradeSHS)

        self.clrGradeSHS = QPushButton(self.frame_5, clicked=lambda:self.clrFunction()) ########## clear function ############
        self.clrGradeSHS.setObjectName(u"clrGradeSHS")
        self.clrGradeSHS.setMinimumSize(QSize(0, 30))
        self.clrGradeSHS.setFont(font2)
        self.clrGradeSHS.setStyleSheet(u"QPushButton{\n"
"       color: rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"       border: 2px solid rgb(67, 156, 250);\n"
"       background-color: rgb(255, 255, 255);}\n"
"QPushButton:focus{background-color: rgb(67, 156, 250);\n"
"       color: rgb(255, 255, 255);\n"
"       border-radius: 10px;}")

        self.horizontalLayout_2.addWidget(self.clrGradeSHS)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(gradesSHSsection)
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
        self.verticalLayout_3.setContentsMargins(9, 5, -1, 5)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(26, 194, 161);\n"
"    border-radius: 10px;\n"
"	color: rgb(255,255,255);\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_7)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 90))
        self.frame_7.setMaximumSize(QSize(16777215, 90))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(170, 0))
        self.frame_8.setMaximumSize(QSize(170, 16777215))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 6, 10, 6)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(9)
        font7.setBold(False)
        font7.setWeight(50)
        self.label_4.setFont(font7)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.label_4)

        self.semLabel = QLabel(self.frame_8)
        self.semLabel.setObjectName(u"semLabel")
        font8 = QFont()
        font8.setFamily(u"Segoe UI Semibold")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.semLabel.setFont(font8)
        self.semLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_5.addWidget(self.semLabel)


        self.horizontalLayout_4.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_9)
        self.verticalLayout_4.setSpacing(3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.subj_area = { 99:"-- ADD BLANK ROW --",0:"21st Century Literature from the Philippines and the World", 1:"Contemporary Philippine Arts from the Regions", 
                        2: "Disaster Readiness and Risk Reduction", 3:"Earth and Life Science", 4: "Earth Science", 5: "General Mathematics",
                        6: "Introduction to the Philosophy of Human Person", 7: "Komunikasyon at Pananaliksik sa Wika at Kulturang Pilipino",
                        8: "Media and Information Literacy", 9: "Oral Communication in Context", 10: "Pagbasa at Pagsusuri ng iba't ibang Teksto tungo sa Pananaliksik",
                        11: "Personal Development", 12: "Physical Education and Health (G11)", 13: "Physical Education and Health (G12)", 
                        14: "Physical Science", 15: "Reading and Writing Skills", 16: "Statistics and Probability", 17: "Understanding Culture, Society and Politics",
                        18: "Empowerment Technologies", 19: "English for Academic and Professional Purposes", 20: "Entrepreneurship", 
                        21: "Filipino sa Piling Larangan (Akademik)", 22: "Filipino sa Piling Larangan (TechVoc)", 23: "Inquiries, Investigation and Immersion",
                        24: "Practical Research 1", 25: "Practical Research 2", 26: "Applied Economics", 27: "Organizational Management",
                        28: "Community Engagement, Solidarity and Citizenship", 29: "Creative Nonfiction", 30: "Creative Writing",
                        31: "Introduction of World Religions and Belief System", 32: "Malikhaing Pagsulat", 33: "Philippine Politics and Governance",
                        34: "Trends, Networks, and Critical Thinking in the 21st Century"}

        self.subjectCombo = QComboBox(self.frame_9)
        self.subjectCombo.setObjectName(u"subjectCombo")
        self.subjectCombo.setMinimumSize(QSize(0, 30))
        self.subjectCombo.setMaximumSize(QSize(16777215, 30))
        self.subjectCombo.setStyleSheet(u"QComboBox{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(26, 194, 161);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")    
        self.subjectCombo.setFont(font7)                ##############
        a = list(self.subj_area.values())               ############## values #######
        self.subjectCombo.addItems(a)

        self.verticalLayout_4.addWidget(self.subjectCombo)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(0, 30))
        self.frame_10.setMaximumSize(QSize(16777215, 30))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)

        self.addSubBtn = QPushButton(self.frame_10, clicked=lambda: self.addSub())  ########### connect function #################
        self.addSubBtn.setObjectName(u"addSubBtn")
        self.addSubBtn.setMinimumSize(QSize(100, 30))
        self.addSubBtn.setMaximumSize(QSize(100, 16777215))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.addSubBtn.setFont(font9)
        self.addSubBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 194, 161);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(191, 191, 191);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 194, 161);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(200, 200, 200);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 5px;\n"
" border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.addSubBtn)

        self.delRowBtn = QPushButton(self.frame_10, clicked = lambda: self.delSub())  ################## delete row #############
        self.delRowBtn.setObjectName(u"delRowBtn")
        self.delRowBtn.setMinimumSize(QSize(120, 30))
        self.delRowBtn.setMaximumSize(QSize(120, 16777215))
        self.delRowBtn.setFont(font9)
        self.delRowBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 194, 161);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(191, 191, 191);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 194, 161);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(200, 200, 200);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 5px;\n"
" border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.delRowBtn)

        self.saveSubBtn = QPushButton(self.frame_10, clicked=lambda: self.saveTable()) ############ connect the save subject function #################
        self.saveSubBtn.setObjectName(u"saveSubBtn")
        self.saveSubBtn.setMinimumSize(QSize(155, 30))
        self.saveSubBtn.setMaximumSize(QSize(155, 16777215))
        self.saveSubBtn.setFont(font9)
        self.saveSubBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(26, 194, 161);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(191, 191, 191);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 194, 161);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(200, 200, 200);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 5px;\n"
" border: 1px solid rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_5.addWidget(self.saveSubBtn)  
        self.resetBtn = QPushButton(self.frame_10, clicked=lambda: self.resetSub())  ############# connect the reset function ###########
        self.resetBtn.setObjectName(u"resetBtn")
        self.resetBtn.setMinimumSize(QSize(100, 30))
        self.resetBtn.setMaximumSize(QSize(100, 16777215))
        self.resetBtn.setFont(font9)
        self.resetBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_5.addWidget(self.resetBtn)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.horizontalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_7)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_6)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.sem1 = QWidget()
        self.sem1.setObjectName(u"sem1")
        self.sem1.setStyleSheet(u"")
        self.verticalLayout_6 = QVBoxLayout(self.sem1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.sem1SubTable = QTableWidget(self.sem1)
        if (self.sem1SubTable.columnCount() < 4):
            self.sem1SubTable.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.sem1SubTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        brush1 = QBrush(QColor(26, 191, 164, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setForeground(brush1);
        self.sem1SubTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setForeground(brush1);
        self.sem1SubTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setForeground(brush1);
        self.sem1SubTable.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.sem1SubTable.setObjectName(u"sem1SubTable")
        fontTable = QFont()
        fontTable.setFamily(u"Segoe UI Semibold")  ######################## Font for table widget #####################################
        fontTable.setPointSize(11)
        self.sem1SubTable.setFont(fontTable)
        self.sem1SubTable.setStyleSheet(u"QTableWidget{border: none;\n"
"       background-color: rgb(255, 255, 255);}\n"
"QFrame{background-color:  rgb(255, 255, 255);\n"     
"    border: none;}\n"
"QTableView::item:selected  {color: rgb(255, 255, 255);\n"    
"       background-color: rgb(67, 156, 250);}\n"
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

        self.verticalLayout_6.addWidget(self.sem1SubTable)

        self.frame_11 = QFrame(self.sem1)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setMaximumSize(QSize(16777215, 30))
        self.frame_11.setLayoutDirection(Qt.RightToLeft)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.frame_16 = QFrame(self.frame_11)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        avefont = QFont()
        avefont.setFamily(u"Segoe UI Semibold")
        avefont.setPointSize(13)
        avefont.setBold(True)
        avefont.setWeight(75)

        self.genAve1 = QLabel(self.frame_16)
        self.genAve1.setObjectName(u"genAve1")
        self.genAve1.setMinimumSize(QSize(140, 0))
        self.genAve1.setMaximumSize(QSize(140, 16777215))
        self.genAve1.setFont(avefont)
        self.genAve1.setStyleSheet(u"QLabel{\n"
"color: rgb(67, 156, 250);\n"
"}")
        self.genAve1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.genAve1)

        self.genSem1Label = QLabel(self.frame_16)
        self.genSem1Label.setObjectName(u"genSem1Label")
        font10 = QFont()
        font10.setFamily(u"Segoe UI Semibold")
        font10.setPointSize(9)
        font10.setBold(True)
        font10.setItalic(True)
        font10.setWeight(75)
        self.genSem1Label.setFont(font10)
        self.genSem1Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.genSem1Label)


        self.horizontalLayout_6.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_11)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.sem2Btn = QPushButton(self.frame_15, clicked = lambda: self.sempage(self.sem2))  #################### set page ####################
        self.sem2Btn.setObjectName(u"sem2Btn")
        self.sem2Btn.setMinimumSize(QSize(185, 30))
        self.sem2Btn.setMaximumSize(QSize(185, 16777215))
        self.sem2Btn.setFont(font9)
        self.sem2Btn.setLayoutDirection(Qt.RightToLeft)
        self.sem2Btn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(26, 194, 161);\n"
"	background-color: rgb(255, 255, 255);}\n"
"QPushButton:focus{background-color: rgb(26, 194, 161);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;}")

        self.horizontalLayout_9.addWidget(self.sem2Btn)

        self.horizontalLayout_6.addWidget(self.frame_15)

        self.verticalLayout_6.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.sem1)
        self.sem2 = QWidget()
        self.sem2.setObjectName(u"sem2")
        self.verticalLayout_7 = QVBoxLayout(self.sem2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.sem2SubTable = QTableWidget(self.sem2)
        if (self.sem2SubTable.columnCount() < 4):
            self.sem2SubTable.setColumnCount(4)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.sem2SubTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        __qtablewidgetitem7.setForeground(brush1);
        self.sem2SubTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font4);
        __qtablewidgetitem8.setForeground(brush1);
        self.sem2SubTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        __qtablewidgetitem9.setForeground(brush1);
        self.sem2SubTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.NoBrush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)

        self.sem2SubTable.setObjectName(u"sem2SubTable")
        self.sem2SubTable.setFont(fontTable)
        self.sem2SubTable.setStyleSheet(u"QTableWidget{border: none;\n"
"       background-color: rgb(255, 255, 255);}\n"
"QFrame{background-color:  rgb(255, 255, 255);\n"    
"    border: none;}\n"
"QTableView::item:selected  {color: rgb(255, 255, 255);\n"
"       background-color: rgb(67, 156, 250);}\n"
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
        self.verticalLayout_7.addWidget(self.sem2SubTable)

        self.frame_12 = QFrame(self.sem2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 30))
        self.frame_12.setMaximumSize(QSize(16777215, 30))
        self.frame_12.setLayoutDirection(Qt.RightToLeft)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.frame_12)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.genAve2 = QLabel(self.frame_14)
        self.genAve2.setObjectName(u"genAve2")
        self.genAve2.setMinimumSize(QSize(140, 0))
        self.genAve2.setMaximumSize(QSize(140, 16777215))
        self.genAve2.setFont(avefont)
        self.genAve2.setStyleSheet(u"QLabel{\n"
"color: rgb(67, 156, 250);\n"
"}")
        self.genAve2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.genAve2)

        self.genSem2Label = QLabel(self.frame_14)
        self.genSem2Label.setObjectName(u"genSem2Label")
        self.genSem2Label.setFont(font10)
        self.genSem2Label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.genSem2Label)

        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sem1Btn = QPushButton(self.frame_13, clicked = lambda: self.sempage(self.sem1))  ########################### set page #################
        self.sem1Btn.setObjectName(u"sem1Btn")
        self.sem1Btn.setMinimumSize(QSize(170, 30))
        self.sem1Btn.setMaximumSize(QSize(170, 16777215))
        self.sem1Btn.setFont(font9)
        self.sem1Btn.setLayoutDirection(Qt.RightToLeft)
        self.sem1Btn.setStyleSheet(u"QPushButton{\n"
"       color: rgb(0, 0, 0);\n"
"       border-radius: 10px;\n"
"       border: 2px solid rgb(26, 194, 161);\n"
"       background-color: rgb(255, 255, 255);}\n"
"QPushButton:focus{background-color: rgb(26, 194, 161);\n"
"       color: rgb(255, 255, 255);\n"
"       border-radius: 10px;}")

        self.sem1SubTable.setColumnWidth(0,350)  ###################################### Column width (grades table) SEM 1 #######################
        self.sem1SubTable.setColumnWidth(1,90)
        self.sem1SubTable.setColumnWidth(2,90)
        self.sem1SubTable.setColumnWidth(3,130)
        self.header1 = self.sem1SubTable.horizontalHeader()
        self.header1.setSectionResizeMode(0,QHeaderView.Stretch)
        self.header1.setFixedHeight(60)
        self.header1.setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(222, 222, 222); }")
                      
        self.sem1SubTable.verticalHeader().setMinimumSectionSize(22)
        self.sem1SubTable.verticalHeader().setDefaultSectionSize(44)

        self.sem2SubTable.setColumnWidth(0,350)  ###################################### Column width (grades table) SEM 2 #######################
        self.sem2SubTable.setColumnWidth(1,90)
        self.sem2SubTable.setColumnWidth(2,90)
        self.sem2SubTable.setColumnWidth(3,130)
        self.header2 = self.sem2SubTable.horizontalHeader()
        self.header2.setSectionResizeMode(0,QHeaderView.Stretch)
        self.header2.setFixedHeight(60)
        self.header2.setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(222, 222, 222); }")

        self.sem2SubTable.verticalHeader().setMinimumSectionSize(22)
        self.sem2SubTable.verticalHeader().setDefaultSectionSize(44)

        self.horizontalLayout_8.addWidget(self.sem1Btn)

        self.horizontalLayout_7.addWidget(self.frame_13)

        self.verticalLayout_7.addWidget(self.frame_12)
        self.stackedWidget.addWidget(self.sem2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.frame_2)


        self.retranslateUi(gradesSHSsection)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(gradesSHSsection)
    # setupUi

        self.studentSHSTable.cellClicked.connect(lambda: self.clickedSHSTable())   ####### Signal for clicking cell in table widget ##################
                
############################### Functions for adding and deleting row in table widget + (SAVE ALL SUBJECT AND RESET BUTTONS)###########################
    def addSub(self):
        viewSub = shsSubject.viewSubjSHS()
        if self.stackedWidget.currentIndex() == 0:    ################ FUNCTION FOR ADD SUBJECT BUTTON #########################
            self.addRow(self.sem1SubTable)
        else:
            self.addRow(self.sem2SubTable)

    def delSub(self):                                 ############## FUNCTION FOR DELETE LAST ROW BUTTON ####################
        viewSub = shsSubject.viewSubjSHS()
        if self.stackedWidget.currentIndex() == 0:
            self.delRow(self.sem1SubTable) 
        else:
            self.delRow(self.sem2SubTable)     

    def addRow(self,subTable):
        
        rowcount = subTable.rowCount() 
        subTable.insertRow(rowcount)    ########### Adding Row to table #########
        rowTotal = subTable.rowCount()
 
        if self.subjectCombo.currentText() == "-- ADD BLANK ROW --":
            pass
        else:
            subTable.setItem((rowTotal-1), 0, QTableWidgetItem(self.subjectCombo.currentText()))

    def delRow(self,subTableDel):
        if subTableDel.rowCount() != 0:
            subTableDel.removeRow(subTableDel.rowCount()-1)
    
    def saveTable(self):                              ################# FUNCTION FOR SAVE ALL SUBJECTS BUTTON ######################
        viewSub = shsSubject.viewSubjSHS()

        if self.stackedWidget.currentIndex() == 0 and len(viewSub) == 0:
            self.saveSub(self.sem1SubTable,1)
            self.showMessage("Save Subjects","First Semester Subjects has been save", None, QMessageBox.Information)            

        elif self.stackedWidget.currentIndex() == 1:
            if len(viewSub) == 1:
                self.saveSub(self.sem2SubTable,2)
                self.showMessage("Save Subjects","Second Semester Subjects has been save", None, QMessageBox.Information)
            else:
                self.showMessage("No 1st Sem subjects","You must add and save subjects on first semester before\nadding subjects on second semester", None, QMessageBox.Information)            

    def saveSub(self, table, semNum):

        subjectNum = table.rowCount()
        subList = [semNum]
        if subjectNum != 0 and subjectNum <= 15:
            for subrow in range(subjectNum):
                subjectData = table.item(subrow,0)
                subList.append(subjectData.text())

            for blank in range(15-subjectNum):
                subList.append("")

            shsSubject.insertSubjSHS(tuple(subList))
            self.addSubBtn.setEnabled(False)
            self.delRowBtn.setEnabled(False)
            self.saveSubBtn.setEnabled(False)

        else:
            self.showMessage("No Subjects","You didn't add subject on the table \nor the table exceed the maximum slot(15 subjects max)", QMessageBox.Warning)

    def resetSub(self):
        viewSub = shsSubject.viewSubjSHS()
        sem1data = gradesSHSDataBase1.viewGradesem1()

        blnkGrade = []
        blnkFinal = []

        for blank in range(30):
            blnkGrade.append("")
        for emp in range(15):
            blnkFinal.append("")

        for s in range(len(sem1data)):
            gradesSHSDataBase1.updSem1Grade(blnkGrade, s)
            gradesSHSDataBase1.updSem1Final(blnkFinal, s)
            gradesSHSDataBase2.updSem2Grade(blnkGrade, s)
            gradesSHSDataBase2.updSem2Final(blnkFinal, s)

        def msgbtn(i):
            if i.text() == "OK":
                shsSubject.deleteSubjSHS(1)
                shsSubject.deleteSubjSHS(2)
                self.displaySubjects()

                self.addSubBtn.setEnabled(True)
                self.delRowBtn.setEnabled(True)
                self.saveSubBtn.setEnabled(True)

        if len(viewSub) != 0:
            self.showMessage("Reset Subjects","First and Second Semester subjects will be removed including the learner's grade\nClick Ok to continue", msgbtn, QMessageBox.Information)
            
    def displaySubjects(self):

        viewSub = shsSubject.viewSubjSHS()

        if len(viewSub) >= 1:
            self.sem1SubTable.setRowCount(0)
            for row, sub in enumerate(viewSub[0][1:]):   ###### Iteration (subject database) skipping the first loop (id) ########
                if sub != '':
                    self.sem1SubTable.insertRow(self.sem1SubTable.rowCount())
                    self.sem1SubTable.setItem((row), 0, QTableWidgetItem(sub))
                else:
                    break

            self.addSubBtn.setEnabled(False)
            self.delRowBtn.setEnabled(False)
            self.saveSubBtn.setEnabled(False)

        if len(viewSub) == 2:
            self.sem2SubTable.setRowCount(0)
            for row, sub in enumerate(viewSub[1][1:]):   ###### Iteration (subject database) skipping the first loop (id) ########
                if sub != '':
                    self.sem2SubTable.insertRow(self.sem2SubTable.rowCount())
                    self.sem2SubTable.setItem((row), 0, QTableWidgetItem(sub))
                else:
                    break

        if len(viewSub) == 0: 
            self.sem1SubTable.setRowCount(0)
            self.sem2SubTable.setRowCount(0)


 #######################################################################################################################################

    def sempage(self,sempage):
        self.stackedWidget.setCurrentWidget(sempage)
        viewSub = shsSubject.viewSubjSHS()

        try:
            self.clickedSHSTable()
        except:
            print("no learner selected")
        
        if self.stackedWidget.currentIndex() == 0:
            self.semLabel.setText("1st Semester")
            if len(viewSub) == 1:
                self.addSubBtn.setEnabled(False)
                self.delRowBtn.setEnabled(False)
                self.saveSubBtn.setEnabled(False)

        else:
            self.semLabel.setText("2nd Semester") 
            if len(viewSub) == 2:
                self.addSubBtn.setEnabled(False)
                self.delRowBtn.setEnabled(False)
                self.saveSubBtn.setEnabled(False)
            else:
                self.addSubBtn.setEnabled(True)
                self.delRowBtn.setEnabled(True)
                self.saveSubBtn.setEnabled(True)

    def displayToTable(self, selectItem, gradeData, table, aveLabel):

        for s in gradeData:
            studentinfo = list(s)
            if selectItem[0] == studentinfo[2]:
                break

        if table.rowCount() != 0:
            for graderow in range(table.rowCount()):               ############# Display selected info Grades to table ##################
                for gradecolumn in range(1,3):
                    shsItem = QTableWidgetItem(studentinfo[(4 + gradecolumn)+(3*graderow)])
                    table.setItem(graderow, gradecolumn, QTableWidgetItem(""))
                    table.setItem(graderow, gradecolumn, shsItem)
                    shsItem.setTextAlignment(Qt.AlignCenter)

                shsFinal = QTableWidgetItem(studentinfo[(7)+(3*graderow)])
                table.setItem(graderow, 3, QTableWidgetItem(""))
                table.setItem(graderow, 3, shsFinal)
                shsFinal.setTextAlignment(Qt.AlignCenter)
                shsFinal.setForeground(self.brush)

        self.showGenAve(table, aveLabel)  ############ Showing general average ##############

    def clickedSHSTable(self):   ############ event function for clicking learner on the table ###############

        global sem1data
        global sem2data
        viewSub = shsSubject.viewSubjSHS()
        learner = profileDataBase.viewstudentData()
        sem1data = gradesSHSDataBase1.viewGradesem1()
        sem2data = gradesSHSDataBase2.viewGradesem2()
        global select_list

        if len(learner) != 0: 
            select_list = []
            self.lrn_SHS.setText("")
            self.name_SHS.setText("")

            for item in self.studentSHSTable.selectedItems():
                select_list.append(item.text())

            self.lrn_SHS.setText(select_list[0])
            self.name_SHS.setText(select_list[1])

            if self.stackedWidget.currentIndex() == 0 and len(viewSub) >= 1:
                self.displayToTable(select_list, sem1data, self.sem1SubTable, self.genAve1) 
            elif self.stackedWidget.currentIndex() == 1 and len(viewSub) == 2:
                self.displayToTable(select_list, sem2data, self.sem2SubTable, self.genAve2)
            else:
                pass

    def showSHS_Info(self):  ############################ function on showing learner and lrn on table ###################

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:

            learner = profileDataBase.viewstudentData()
            if len(learner) != 0:    
                self.studentSHSTable.setRowCount(0)
                for i, lrn_Name in enumerate(learner):
                    table_name = []  
                    table_name.append(lrn_Name[1])  ############# append LRN to temporary table name list ########

                    if lrn_Name[4] == "" or lrn_Name[4] == " ":
                        midname = "-"
                    else:
                        midname = lrn_Name[4].strip()

                    nameSHS = str(f"{lrn_Name[2]}, {lrn_Name[3]} {midname[0]}. {lrn_Name[5]}")
                    table_name.append(nameSHS) ############# append name to temporary table name list ########

                    self.rowcount = self.studentSHSTable.rowCount() 
                    self.studentSHSTable.insertRow(self.rowcount)    ########### Adding Row to table ############

                    for column, val in enumerate(tuple(table_name)):
                        self.studentSHSTable.setItem(i, column, QTableWidgetItem(val))

            self.displaySubjects()      ######################## Displaying subjects on table ##########################  
            
        else:
            print("No JHS Grade Data Available")

    def updateSHSgrds(self):                            ################### function for update grade button ###################
        
        sem1Function = gradesSHSDataBase1.updSem1Grade
        sem2Function = gradesSHSDataBase2.updSem2Grade
        sem1Final = gradesSHSDataBase1.updSem1Final
        sem2Final = gradesSHSDataBase2.updSem2Final

        try:
            if self.stackedWidget.currentIndex() == 0:
                self.updateTemp(self.sem1SubTable, sem1data, sem1Function)
                self.showFinal(sem1data, sem1Final, self.sem1SubTable)
                self.showGenAve(self.sem1SubTable, self.genAve1)
                self.showMessage("Update Grades","First Sem Grade has been updated", None, QMessageBox.Information)
            elif self.stackedWidget.currentIndex() == 1:
                self.updateTemp(self.sem2SubTable, sem2data, sem2Function)
                self.showFinal(sem2data, sem2Final, self.sem2SubTable)
                self.showGenAve(self.sem2SubTable, self.genAve2)
                self.showMessage("Update Grades","Second Sem Grade has been updated", None, QMessageBox.Information)
        except:  
            self.showMessage("Error","No learner selected", None, QMessageBox.Warning)
        
    def updateTemp(self, tableGrade, semdata, updFunction):
        
        semRow = tableGrade.rowCount()
        grdList = []

        if semRow  != 0 and semRow  <= 15:
            for subrow in range(semRow):
                for subcol in range(1,3):
                    subjectData = tableGrade.item(subrow,subcol)
                    grdList.append(subjectData.text())

            for blank in range(30-len(grdList)):
                grdList.append("")

            for s in semdata:
                studentinfo = list(s)
                if select_list[0] == studentinfo[2]:
                    break

            checkLetter = True

            for m in grdList:                       ################ Check if entry contain letters or symbols ######
                if not(m.isdigit() or m == ''):
                    errMsg = (f"{m} is invalid\nLetters and symbols are not accepted as input grade\nPlease type integer value")   
                    self.showMessage("Error",errMsg, None, QMessageBox.Warning)
                    checkLetter = False
                    self.clickedSHSTable()  ####### Refresh display table #########
                    break  

            if checkLetter:
                updFunction(grdList, studentinfo[0])     ################# Update data grades #######################
        
    def showFinal(self, semdata, updFinal, tablefinal):
        try:
            finalRow = tablefinal.rowCount()
            grdList = []
            finalList = []                               ############ list of final grade ###############

            if finalRow != 0 and finalRow <= 15:
                for subrow in range(finalRow):
                    for subcol in range(1,3):
                        subjectData = tablefinal.item(subrow,subcol)
                        grdList.append(subjectData.text())                ###print(grdList)

                    if all(v for v in grdList):        ################ Check if both quarter have grade entries ########
                        ave = (int(grdList[0]) + int(grdList[1]))/len(grdList)
                        finalList.append(round(ave))
                    else:
                        finalList.append("")
                        
                    grdList = []

                for blank in range(15-len(finalList)):                  #print(finalList)         
                    finalList.append("")

                for s in semdata:       ############## selecting corresponding id to selected student on table ##########
                    studentinfo = list(s)
                    if select_list[0] == studentinfo[2]:
                        break

                updFinal(finalList, studentinfo[0])  ############## updating final grade ################## 

                for row in range(finalRow):          ############### displaying final grade to table ########
                    shsFinalItem = QTableWidgetItem(str(finalList[row]))
                    tablefinal.setItem(row, 3, QTableWidgetItem(""))
                    tablefinal.setItem(row, 3, shsFinalItem)
                    shsFinalItem.setTextAlignment(Qt.AlignCenter)
                    shsFinalItem.setForeground(self.brush)
                    
        except:
            print("No learner selected")

    def showGenAve(self, table, aveLabel):
        genAveList = []
        tableRow = table.rowCount()
        for row in range(tableRow):
            aveData = table.item(row, 3)
            genAveList.append(aveData.text()) 

        if all(g for g in genAveList):
            aveSum = 0
            for aveInt in genAveList:
                aveSum += int(aveInt)
                genAve = aveSum/tableRow

            aveLabel.setText(str(genAve))
        else:
            aveLabel.setText("-")

    def clrFunction(self):
        if self.stackedWidget.currentIndex() == 0:
            sem1Row = self.sem1SubTable.rowCount()
            for col in range(1,4):
                for row in range(sem1Row):
                    self.sem1SubTable.setItem(row, col, QTableWidgetItem(""))
            self.genAve1.setText("-")
         
        elif self.stackedWidget.currentIndex() == 1:
            sem2Row = self.sem2SubTable.rowCount()
            for col in range(1,4):
                for row in range(sem2Row):
                    self.sem2SubTable.setItem(row, col, QTableWidgetItem(""))
            self.genAve2.setText("-")
   
    def showMessage(self, title,  message, callback, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)  ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(callback)
        msg.exec_()

    def retranslateUi(self, gradesSHSsection):
        gradesSHSsection.setWindowTitle(QCoreApplication.translate("gradesSHSsection", u"Frame", None))
        self.gradeSecSHS.setText(QCoreApplication.translate("gradesSHSsection", u"Grade and Section", None))
        self.strand.setText(QCoreApplication.translate("gradesSHSsection", u"Strand", None))
        self.advSHS.setText(QCoreApplication.translate("gradesSHSsection", u"Adviser: ", None))
        self.sySHS.setText(QCoreApplication.translate("gradesSHSsection", u"School Year", None))
        self.label.setText(QCoreApplication.translate("gradesSHSsection", u"LRN:", None))
        self.label_2.setText(QCoreApplication.translate("gradesSHSsection", u"Name:", None))
        self.lrn_SHS.setText("")
        self.name_SHS.setText("")
        self.label_6.setText(QCoreApplication.translate("gradesSHSsection", u"  Select learner from the table", None))
        ___qtablewidgetitem = self.studentSHSTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("gradesSHSsection", u"LRN", None));
        ___qtablewidgetitem1 = self.studentSHSTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("gradesSHSsection", u"Name", None));
        self.updGradeSHS.setText(QCoreApplication.translate("gradesSHSsection", u"Update Grades", None))
        self.clrGradeSHS.setText(QCoreApplication.translate("gradesSHSsection", u"Clear Grades", None))
        self.label_7.setText(QCoreApplication.translate("gradesSHSsection", u"REPORT ON LEARNING PROGRESS AND ACHIEVEMENT", None))
        self.label_4.setText(QCoreApplication.translate("gradesSHSsection", u"Select Subject", None))
        self.semLabel.setText(QCoreApplication.translate("gradesSHSsection", u"1st semester", None))
        self.addSubBtn.setText(QCoreApplication.translate("gradesSHSsection", u"Add subject", None))
        self.delRowBtn.setText(QCoreApplication.translate("gradesSHSsection", u"Delete last row", None))
        self.saveSubBtn.setText(QCoreApplication.translate("gradesSHSsection", u"SAVE ALL SUBJECTS", None))
        self.resetBtn.setText(QCoreApplication.translate("gradesSHSsection", u"RESET", None))
        ___qtablewidgetitem2 = self.sem1SubTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("gradesSHSsection", u"SUBJECTS", None));
        ___qtablewidgetitem3 = self.sem1SubTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("gradesSHSsection", u"Q1", None));
        ___qtablewidgetitem4 = self.sem1SubTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("gradesSHSsection", u"Q2", None));
        ___qtablewidgetitem5 = self.sem1SubTable.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("gradesSHSsection", u"Final Grade", None));
        self.genAve1.setText(QCoreApplication.translate("gradesSHSsection", u"-", None))
        self.genSem1Label.setText(QCoreApplication.translate("gradesSHSsection", u"General Average for sem 1:", None))
        self.sem2Btn.setText(QCoreApplication.translate("gradesSHSsection", u"Proceed to 2nd Sem Page", None))
        ___qtablewidgetitem6 = self.sem2SubTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("gradesSHSsection", u"SUBJECTS", None));
        ___qtablewidgetitem7 = self.sem2SubTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("gradesSHSsection", u"Q3", None));
        ___qtablewidgetitem8 = self.sem2SubTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("gradesSHSsection", u"Q4", None));
        ___qtablewidgetitem9 = self.sem2SubTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("gradesSHSsection", u"Final Grade", None));
        self.genAve2.setText(QCoreApplication.translate("gradesSHSsection", u"-", None))
        self.genSem2Label.setText(QCoreApplication.translate("gradesSHSsection", u"General Average for sem 2:", None))
        self.sem1Btn.setText(QCoreApplication.translate("gradesSHSsection", u"Back to 1st Sem Page", None))

    # retranslateUi

