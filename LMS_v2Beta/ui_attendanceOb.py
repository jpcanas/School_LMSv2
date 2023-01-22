# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_attendanceObJIDGiD.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, QDate, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import classDataBase
import profileDataBase
import ovDataBase
import attDataBase

class Ui_attendanceOVFrame(object):
    def setupUi(self, attendanceOVFrame):
        if attendanceOVFrame.objectName():
            attendanceOVFrame.setObjectName(u"attendanceOVFrame")
        attendanceOVFrame.resize(1144, 783)
        self.horizontalLayout = QHBoxLayout(attendanceOVFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftframe = QFrame(attendanceOVFrame)
        self.leftframe.setObjectName(u"leftframe")
        self.leftframe.setMinimumSize(QSize(395, 0))
        self.leftframe.setMaximumSize(QSize(395, 16777215))
        self.leftframe.setFrameShape(QFrame.StyledPanel)
        self.leftframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.leftframe)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 140))
        self.frame_4.setMaximumSize(QSize(16777215, 170))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gradeSecAttOb = QLabel(self.frame_4)
        self.gradeSecAttOb.setObjectName(u"gradeSecAttOb")
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.gradeSecAttOb.setFont(font)
        self.gradeSecAttOb.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(67, 156, 250);\n"
"    border-radius: 10px;\n"
"	color: rgb(255,255,255);\n"
"}")

        self.verticalLayout.addWidget(self.gradeSecAttOb)

        self.advAttOb = QLabel(self.frame_4)
        self.advAttOb.setObjectName(u"advAttOb")
        font1 = QFont()
        font1.setFamily(u"Segoe UI Semibold")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.advAttOb.setFont(font1)

        self.verticalLayout.addWidget(self.advAttOb)

        self.syAttOb = QLabel(self.frame_4)
        self.syAttOb.setObjectName(u"syAttOb")
        font2 = QFont()
        font2.setFamily(u"Segoe UI Semibold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.syAttOb.setFont(font2)

        self.verticalLayout.addWidget(self.syAttOb)

        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.leftframe)
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

        self.lrn_AttOb = QLabel(self.frame_3)
        self.lrn_AttOb.setObjectName(u"lrn_AttOb")
        self.lrn_AttOb.setMinimumSize(QSize(0, 30))
        self.lrn_AttOb.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Segoe UI Semibold")
        font4.setPointSize(11)
        font4.setBold(True)
        font4.setWeight(75)
        self.lrn_AttOb.setFont(font4)
        self.lrn_AttOb.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lrn_AttOb)

        self.name_AttOb = QLabel(self.frame_3)
        self.name_AttOb.setObjectName(u"name_AttOb")
        self.name_AttOb.setMinimumSize(QSize(0, 30))
        self.name_AttOb.setMaximumSize(QSize(16777215, 30))
        self.name_AttOb.setFont(font4)
        self.name_AttOb.setStyleSheet(u"QLabel{\n"
"border-radius: 10px;\n"
"border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name_AttOb)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.label_6 = QLabel(self.leftframe)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(9)
        font5.setItalic(True)
        self.label_6.setFont(font5)

        self.verticalLayout_2.addWidget(self.label_6)

        self.studentAttObTable = QTableWidget(self.leftframe)
        if (self.studentAttObTable.columnCount() < 2):
            self.studentAttObTable.setColumnCount(2)
        brush = QBrush(QColor(67, 156, 250, 255))
        brush.setStyle(Qt.SolidPattern)
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(10)
        font6.setBold(True)
        font6.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        __qtablewidgetitem.setForeground(brush);
        self.studentAttObTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        __qtablewidgetitem1.setForeground(brush);
        self.studentAttObTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.studentAttObTable.setObjectName(u"studentAttObTable")
        self.studentAttObTable.setStyleSheet(u"QTableWidget{border: none;\n"
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
        self.studentAttObTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.studentAttObTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.studentAttObTable.horizontalHeader().setStretchLastSection(True)
        self.studentAttObTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.studentAttObTable)

        self.frame_5 = QFrame(self.leftframe)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 35))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(12, 0, 12, 0)

        self.delAllBtn = QPushButton(self.frame_5, clicked = lambda: self.clearEntry())  ############### Clear Entry Function #############
        self.delAllBtn.setObjectName(u"delAllBtn")
        self.delAllBtn.setMinimumSize(QSize(150, 30))
        self.delAllBtn.setMaximumSize(QSize(150, 30))
        self.delAllBtn.setFont(font2)
        self.delAllBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.delAllBtn)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.leftframe)

        self.rightFrame = QFrame(attendanceOVFrame)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setStyleSheet(u"")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.ovFrame = QFrame(self.rightFrame)
        self.ovFrame.setObjectName(u"ovFrame")
        self.ovFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(235, 235, 235);\n"
"    border: none;\n"
"}")
        self.ovFrame.setFrameShape(QFrame.StyledPanel)
        self.ovFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.ovFrame)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.ovFrame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 40))
        self.label_7.setMaximumSize(QSize(16777215, 40))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255,255,255);\n"
"    border-radius: 10px;\n"
"	color: rgb(67, 156, 250);\n"
"	border: 1px solid rgb(67, 156, 250);\n"
"}\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_7)

        self.frame = QFrame(self.ovFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(8, 5, 8, 0)
        self.obTable = QTableWidget(self.frame)
        if (self.obTable.columnCount() < 5):
            self.obTable.setColumnCount(5)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        __qtablewidgetitem2.setForeground(brush1);
        self.obTable.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        __qtablewidgetitem3.setForeground(brush1);
        self.obTable.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        __qtablewidgetitem4.setForeground(brush1);
        self.obTable.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        __qtablewidgetitem5.setForeground(brush1);
        self.obTable.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        __qtablewidgetitem6.setForeground(brush1);
        self.obTable.setHorizontalHeaderItem(4, __qtablewidgetitem6)
        if (self.obTable.rowCount() < 7):
            self.obTable.setRowCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.obTable.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.obTable.setVerticalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font4);
        self.obTable.setVerticalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.obTable.setVerticalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font4);
        self.obTable.setVerticalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font4);
        self.obTable.setVerticalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.obTable.setVerticalHeaderItem(6, __qtablewidgetitem13)
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(10)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font7);
        self.obTable.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font7);
        self.obTable.setItem(1, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font7);
        self.obTable.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font7);
        self.obTable.setItem(3, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font7);
        self.obTable.setItem(4, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font7);
        self.obTable.setItem(5, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font7);
        self.obTable.setItem(6, 0, __qtablewidgetitem20)
        self.obTable.setObjectName(u"obTable")
        self.obTable.setStyleSheet(u"QTableWidget{\n"
"border: none;\n"
"}\n"
"QHeaderView:section{\n"
"	background-color: rgb(67, 156, 250);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTableView::item:selected  {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(67, 156, 250);\n"
"}\n"
"QScrollArea{background-color: rgb(255, 255, 255);}\n" 
"QScrollBar:vertical {border: none;\n"         
"            background: rgb(255, 255, 255);\n"
"            width: 20px;\n"
"            margin: 26px 6px 26px 6px;}\n"
"QScrollBar::handle:vertical {background: lightgray; min-height: 26px;}\n"       
"QScrollBar::add-line:vertical {background: rgb(255, 255, 255);\n"      
"            height: 26px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;}\n"
"QScrollBar::sub-line:vertical {background: rgb(255, 255, 255);\n"         
"            height: 26px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;}\n"
"QScrollBar:up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"            width: 26px;\n"
"            height: 26px;\n"
            "background: rgb(255, 255, 255);}\n"
"QScrollBar::up-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowUp.png\");}\n"
"QScrollBar::down-arrow {\n"
"    image: url(\"c:/LMS_appVer2/icons/arrowDown.png\");}\n"
"")

        self.verticalLayout_6.addWidget(self.obTable)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 85))
        self.frame_2.setMaximumSize(QSize(16777215, 85))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(457, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 85))
        self.textEdit.setSizeIncrement(QSize(0, 85))

        self.horizontalLayout_3.addWidget(self.textEdit)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(250, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.updObBtn = QPushButton(self.frame_7, clicked = lambda: self.ovUpdate())  ###################### update observe values ################
        self.updObBtn.setObjectName(u"updObBtn")
        self.updObBtn.setGeometry(QRect(20, 50, 210, 30))
        self.updObBtn.setMinimumSize(QSize(210, 30))
        self.updObBtn.setMaximumSize(QSize(210, 16777215))
        self.updObBtn.setFont(font2)
        self.updObBtn.setStyleSheet(u"QPushButton:focus{\n"
"   color: rgb(0,0,0);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 5px;\n"
"}")
        self.fillTableBtn = QPushButton(self.frame_7, clicked = lambda: self.fillOVTable()) ############# Fill OV Table ##################
        self.fillTableBtn.setObjectName(u"fillTableBtn")
        self.fillTableBtn.setGeometry(QRect(20, 10, 101, 31))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(8)
        self.fillTableBtn.setFont(font8)
        self.fillTableBtn.setEnabled(False)
        self.fillTableBtn.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(67, 156, 250);\n"
"	background-color: rgb(67, 156, 250);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(67, 156, 250);\n"
" 	border-radius: 5px;\n"
"}\n"
"QPushButton:disabled{\n"
"background-color: rgb(200, 200, 200);\n"
"   color: rgb(255, 255, 255);\n"
"   border-radius: 5px;\n"
" border: 1px solid rgb(255, 255, 255);\n"
"}")
        self.fillCombo = QComboBox(self.frame_7)
        self.fillCombo.setObjectName(u"fillCombo")
        self.fillCombo.setGeometry(QRect(140, 10, 91, 31))
        font9 = QFont()
        font9.setFamily(u"Segoe UI Semibold")
        font9.setPointSize(9)
        font9.setBold(True)
        font9.setWeight(75)
        self.fillCombo.setFont(font9)
        self.fillCombo.setStyleSheet(u"QComboBox{\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(67, 156, 250);\n"
"}")
        self.fillCombo.addItems(["AO","SO","RO","NO"])
        self.horizontalLayout_3.addWidget(self.frame_7)


        self.verticalLayout_6.addWidget(self.frame_2)


        self.verticalLayout_4.addWidget(self.frame)


        self.verticalLayout_3.addWidget(self.ovFrame)

        self.label_8 = QLabel(self.rightFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 40))
        self.label_8.setMaximumSize(QSize(16777215, 40))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(255,255,255);\n"
"   border-radius: 10px;\n"
"	color: rgb(26, 194, 161);\n"
"   border: 1px solid rgb(26, 194, 161);\n"                                        
"}")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_8)

        self.attFrame = QFrame(self.rightFrame)
        self.attFrame.setObjectName(u"attFrame")
        self.attFrame.setMinimumSize(QSize(0, 0))
        self.attFrame.setMaximumSize(QSize(16777215, 230))
        self.attFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.attFrame.setFrameShape(QFrame.StyledPanel)
        self.attFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.attFrame)
        self.verticalLayout_5.setSpacing(12)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 0, 0)
        self.frame_6 = QFrame(self.attFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 45))
        self.frame_6.setMaximumSize(QSize(16777215, 60))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(125, 0))
        self.label_3.setMaximumSize(QSize(125, 16777215))
        font10 = QFont()
        font10.setFamily(u"Segoe UI")
        font10.setPointSize(9)
        font10.setBold(False)
        font10.setItalic(True)
        font10.setWeight(50)
        self.label_3.setFont(font10)

        self.horizontalLayout_4.addWidget(self.label_3)

        self.dateEdit = QDateEdit(self.frame_6)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(140, 30))
        self.dateEdit.setMaximumSize(QSize(180, 30))
        self.dateEdit.setFont(font7)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"border-radius: 5px;\n"
"border: 1px solid rgb(26, 191, 164);\n"
"\n"
"}")
        self.dateEdit.setCurrentSection(QDateTimeEdit.MonthSection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setDate(QDate(2022, 1, 1))

        self.horizontalLayout_4.addWidget(self.dateEdit)

        self.updMonthBtn = QPushButton(self.frame_6, clicked=lambda: self.updateMonth())  ############# updating month ####################
        self.updMonthBtn.setObjectName(u"updMonthBtn")
        self.updMonthBtn.setMinimumSize(QSize(100, 28))
        self.updMonthBtn.setMaximumSize(QSize(150, 16777215))
        font11 = QFont()
        font11.setFamily(u"Segoe UI")
        font11.setPointSize(9)
        self.updMonthBtn.setFont(font11)
        self.updMonthBtn.setStyleSheet(u"QPushButton{\n"
"color: rgb(255, 255, 255);\n"
"	border-radius: 5px;\n"
"	border: 1px solid rgb(26, 194, 161);\n"
"	background-color: rgb(26, 194, 161);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"	color: rgb(26, 194, 161);\n"
" 	border-radius: 5px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.updMonthBtn)

        self.startClassDate = QLabel(self.frame_6)
        self.startClassDate.setObjectName(u"startClassDate")
        font12 = QFont()
        font12.setFamily(u"Segoe UI Semibold")
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setItalic(False)
        font12.setWeight(75)
        self.startClassDate.setFont(font12)
        self.startClassDate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.startClassDate)

        self.updAttBtn = QPushButton(self.frame_6, clicked = lambda: self.attendanceUpd())  ################### update attendance ###################
        self.updAttBtn.setObjectName(u"updAttBtn")
        self.updAttBtn.setMinimumSize(QSize(170, 30))
        self.updAttBtn.setMaximumSize(QSize(170, 30))
        self.updAttBtn.setFont(font2)
        self.updAttBtn.setStyleSheet(u"QPushButton:focus{\n"
"   color: rgb(0,0,0);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(26, 194, 161);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(26, 194, 161);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 5px;\n"
"}")

        self.horizontalLayout_4.addWidget(self.updAttBtn)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.attTable = QTableWidget(self.attFrame)
        if (self.attTable.columnCount() < 13):
            self.attTable.setColumnCount(13)
        brush2 = QBrush(QColor(26, 194, 161, 255))
        brush2.setStyle(Qt.SolidPattern)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font2);
        __qtablewidgetitem21.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font2);
        __qtablewidgetitem22.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font2);
        __qtablewidgetitem23.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font2);
        __qtablewidgetitem24.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font2);
        __qtablewidgetitem25.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font2);
        __qtablewidgetitem26.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font2);
        __qtablewidgetitem27.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font2);
        __qtablewidgetitem28.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(7, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font2);
        __qtablewidgetitem29.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(8, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font2);
        __qtablewidgetitem30.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(9, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font2);
        __qtablewidgetitem31.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(10, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFont(font2);
        __qtablewidgetitem32.setForeground(brush2);
        self.attTable.setHorizontalHeaderItem(11, __qtablewidgetitem32)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font2);
        __qtablewidgetitem33.setForeground(brush3);
        self.attTable.setHorizontalHeaderItem(12, __qtablewidgetitem33)
        if (self.attTable.rowCount() < 3):
            self.attTable.setRowCount(3)
        font13 = QFont()
        font13.setFamily(u"Segoe UI")
        font13.setPointSize(9)
        font13.setBold(True)
        font13.setItalic(True)
        font13.setWeight(75)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font13);
        self.attTable.setVerticalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font13);
        self.attTable.setVerticalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font13);
        self.attTable.setVerticalHeaderItem(2, __qtablewidgetitem36)
        self.attTable.setObjectName(u"attTable")
        self.attTable.setStyleSheet(u"QTableView::item:selected  {color: rgb(255, 255, 255);\n"
"   background-color: rgb(26, 194, 161);}\n"
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
"    image: url(\"c:/LMS_appVer2/icons/arrowRight.png\");\n"
"}")
        self.obTable.setColumnWidth(1,60)  ###################################### Column width (OV table)#######################
        self.obTable.setColumnWidth(2,60)
        self.obTable.setColumnWidth(3,60)
        self.obTable.setColumnWidth(4,60)

        self.ovheader = self.obTable.horizontalHeader()
        self.ovheader.setSectionResizeMode(0,QHeaderView.Stretch)
        self.ovheader.setFixedHeight(60)
        self.ovheader.setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(222, 222, 222); }")

        self.obTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch);  
        self.obTable.verticalHeader().setStyleSheet("QHeaderView:section{background-color: rgb(255,255,255); \
                                                            border-bottom: 1px solid rgb(200,200,200); border-right: 1px solid rgb(200,200,200);}")

        self.attheader = self.attTable.horizontalHeader()  ###################################### Column header (att table)#######################
        self.attheader.setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(222, 222, 222); }")

        self.monthArray = {1:"JANUARY", 2:"FEBRUARY", 3:"MARCH", 4:"APRIL", 5:"MAY", 6:"JUNE", 7:"JULY", 8:"AUGUST",\
                           9:"SEPTEMBER", 10:"OCTOBER", 11:"NOVEMBER", 12:"DECEMBER"}

        self.studentAttObTable.cellClicked.connect(lambda: self.clickedAttOVTable())   ####### Signal for clicking cell in table widget ##################

        self.verticalLayout_5.addWidget(self.attTable)

        self.verticalLayout_3.addWidget(self.attFrame)

        self.horizontalLayout.addWidget(self.rightFrame)

        self.retranslateUi(attendanceOVFrame)

        QMetaObject.connectSlotsByName(attendanceOVFrame)
    # setupUi

    def fillOVTable(self):
        filltext = self.fillCombo.currentText()

        for ovrow in range(self.obTable.rowCount()):               ############# Display selected info to table ##################
            for ovcolumn in range(1,5):
                self.obTable.setItem(ovrow, ovcolumn, QTableWidgetItem(""))
                self.obTable.setItem(ovrow, ovcolumn, QTableWidgetItem(filltext))

    def clickedAttOVTable(self):
        global select_list
        global ovdata
        global attdata
        learner = profileDataBase.viewstudentData()
        ovdata = ovDataBase.view_values()
        attdata = attDataBase.view_att()
        self.fillTableBtn.setEnabled(True)

        if len(learner) != 0: 
            select_list = []
            self.lrn_AttOb.setText("")
            self.name_AttOb.setText("")

            for item in self.studentAttObTable.selectedItems():
                select_list.append(item.text())

            self.lrn_AttOb.setText(select_list[0])
            self.name_AttOb.setText(select_list[1])

            self.ovAttShowTable(select_list, ovdata, self.obTable, 1, 0, 1, 5)           ########### SHOWING OV DATA OF SELECTED LEARNER #############
            self.ovAttShowTable(select_list, attdata, self.attTable, 0, 1, 0, 13)        ########### SHOWING ATTENDANCE DATA OF SELECTED LEARNER #############

    def showAttOV_Info(self):   ############# Show Student Name and LRN to student table ########

        myClass = classDataBase.viewDataclass()           
        if len(myClass) != 0:

            learner = profileDataBase.viewstudentData()
            if len(learner) != 0:    
                self.studentAttObTable.setRowCount(0)
                for i, lrn_Name in enumerate(learner):
                    table_name = []  
                    table_name.append(lrn_Name[1])  ############# append LRN to temporary table name list ########

                    if lrn_Name[4] == "" or lrn_Name[4] == " ":
                        midname = "-"
                    else:
                        midname = lrn_Name[4].strip()

                    attOb_name = str(f"{lrn_Name[2]}, {lrn_Name[3]} {midname[0]}. {lrn_Name[5]}")
                    table_name.append(attOb_name) ############# append name to temporary table name list ########

                    self.rowcount = self.studentAttObTable.rowCount() 
                    self.studentAttObTable.insertRow(self.rowcount)    ########### Adding Row to table ############

                    for column, val in enumerate(tuple(table_name)):
                        self.studentAttObTable.setItem(i, column, QTableWidgetItem(val))
        else:
            print("No Attendance and Observe Values Data Available")

    def ovAttShowTable(self, itemSelect, database, table, c, r, startColumn, endColumn):
        for i in database:
            studentOV = list(i)
            if itemSelect[0] == studentOV[2]:
                break

        for ovrow in range(table.rowCount()):               ############# Display selected info to table ##################
            for ovcolumn in range(startColumn,endColumn):
                attOVItem = QTableWidgetItem(studentOV[((2+r)+ovcolumn) + ((endColumn-c)*(ovrow))])
                table.setItem(ovrow, ovcolumn, QTableWidgetItem(""))
                table.setItem(ovrow, ovcolumn, attOVItem)
                attOVItem.setTextAlignment(Qt.AlignCenter)

    def monthDisplay(self):         ########################### DISPLAYING MONTH IN TABLE ##########################

        myMonth = attDataBase.viewMonth()
        months = myMonth[0]

        if months[0] == 'Month1':
            pass
        else:
            msplit = months[0].split(",",2)
            listMonths = list(months)
            listMonths[0] = msplit[0] 

            monthNum = list(self.monthArray.keys())[list(self.monthArray.values()).index(msplit[0])]   ######## Convert Word Month to Number Month ########

            self.dateEdit.setDate(QDate(int(msplit[2]), monthNum, int(msplit[1])))

            self.attTable.setHorizontalHeaderLabels("")
            self.attTable.setHorizontalHeaderLabels(listMonths)

    def updateMonth(self):      ########################### UPDATING MONTH IN DATABASE ##########################
        month = self.dateEdit.date().month()
        tempMonth = []
        tempMonth.append(self.monthArray[month])

        for m in range(1,12):
            if (month+m) <= 12:
                tempMonth.append(self.monthArray[month + m])
            else:
                tempMonth.append(self.monthArray[(month + m)%12])

        monthData = {}      ################### actual month data (passing as argument to update month function)###########  

        for n in range(1,13):
            mString = (f'n_month{n}')
            if n == 1:
                d = self.dateEdit.date()
                f = f'{tempMonth[n-1]}, {d.day()}, {d.year()}'
                monthData[mString] = f
            else:
                monthData[mString] = tempMonth[n-1]

        monthData['oid'] = 1

        attDataBase.updMonthData(monthData)
        self.monthDisplay()
        self.showMessageChild("Update", "School Month Updated", QMessageBox.Information)

    def attendanceUpd(self):
        try:
            attListdays = []
            attListPres = []
            attListAbs = []
            for attrows in range(3):
                for attCol in range(12):
                    if attrows == 0: 
                        attDays = self.attTable.item(attrows, attCol)
                        attListdays.append(attDays.text())
                    elif attrows == 1:
                        attPres = self.attTable.item(attrows, attCol)
                        attListPres.append(attPres.text())
                    else:
                        attAbs = self.attTable.item(attrows, attCol)
                        attListAbs.append(attAbs.text())

            daysSum = self.totaldays(attListdays, 0)
            presSum = self.totaldays(attListPres, 1)
            absSum = self.totaldays(attListAbs, 2)

            for d in attdata:               
                studentinfoID = list(d)
                attDataBase.updNumDays(attListdays, str(daysSum), studentinfoID[0])     ################### UPDATING TOTAL NO. OF DAYS (ALL LEARNERS)#############      

                if select_list[0] ==  studentinfoID[2]:
                    attDataBase.updateAtt(attListPres, attListAbs, studentinfoID[0])  ################### UPDATING TOTAL NO. OF PRESENT & ABSENT (PER LEARNER) #############
                    attDataBase.updateTotal(str(presSum), str(absSum), studentinfoID[0])

            self.showMessageChild("Update", "Learner's Attendance has been updated Successfully", QMessageBox.Information)

        except:
            self.showMessageChild("Error", "Select learner from the table (Left Side)", QMessageBox.Warning)

    def totaldays(self, dayList, totalRow):

        totdays = 0
        if any(v for v in dayList):        ################ Check if all month have total number of days entries ########
            for days in dayList:
                if days != '' and days.isdigit():
                    totdays += int(days)
        else:
            totdays = ''
        
        self.attTable.setItem(totalRow, 12, QTableWidgetItem(""))
        self.attTable.setItem(totalRow, 12, QTableWidgetItem(str(totdays)))

        return totdays

    def ovUpdate(self):
        try:
            validOV = ["AO","ao","SO","so","RO","ro","NO","no",""," "]
            ovList = []
            for ovRow in range(7):
                for ovCol in range(1,5):
                    ovData = self.obTable.item(ovRow,ovCol)

                    ovValid = False             ##### iteration for valid OV #######
                    for v in validOV:
                        if ovData.text() == v:
                            ovValid = True

                    if ovValid:
                        ovList.append(ovData.text())
                    else:
                        self.showMessageChild("Error", f"{ovData.text()} is not a valid input\nChoose among (AO, SO, RO, NO) or (ao, so, ro, no)", QMessageBox.Warning)
                        self.obTable.setItem(ovRow, ovCol, QTableWidgetItem(""))
                        ovValid = False
                        break

            for o in ovdata:
                studentinfoOV = list(o)
                if select_list[0] == studentinfoOV[2]:
                    break

            if ovValid:
                ovDataBase.updOV(ovList, studentinfoOV[0])   ################### updating observe values on database ############
                self.showMessageChild("Update", "Observe Values has been updated Successfully", QMessageBox.Information)

        except:
            self.showMessageChild("Error", "Select learner from the table (Left Side)", QMessageBox.Warning)

    def clearEntry(self):
        for ovRow in range(7):              ############# Clear Entries OV table ###############
            for ovCol in range(1,5):
                self.obTable.setItem(ovRow, ovCol, QTableWidgetItem(""))
        for attrow in range(1,3):
            for attCol in range(13):
                self.attTable.setItem(attrow, attCol, QTableWidgetItem(""))
  
    def showMessageChild(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)   ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.exec_()

    def retranslateUi(self, attendanceOVFrame):
        attendanceOVFrame.setWindowTitle(QCoreApplication.translate("attendanceOVFrame", u"Frame", None))
        self.gradeSecAttOb.setText(QCoreApplication.translate("attendanceOVFrame", u"Grade and Section", None))
        self.advAttOb.setText(QCoreApplication.translate("attendanceOVFrame", u"Adviser: ", None))
        self.syAttOb.setText(QCoreApplication.translate("attendanceOVFrame", u"School Year", None))
        self.label.setText(QCoreApplication.translate("attendanceOVFrame", u"LRN:", None))
        self.label_2.setText(QCoreApplication.translate("attendanceOVFrame", u"Name:", None))
        self.lrn_AttOb.setText("")
        self.name_AttOb.setText("")
        self.label_6.setText(QCoreApplication.translate("attendanceOVFrame", u"  Select learner from the table", None))
        ___qtablewidgetitem = self.studentAttObTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("attendanceOVFrame", u"LRN", None));
        ___qtablewidgetitem1 = self.studentAttObTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("attendanceOVFrame", u"Name", None));
        self.delAllBtn.setText(QCoreApplication.translate("attendanceOVFrame", u"Clear Entries", None))
        self.label_7.setText(QCoreApplication.translate("attendanceOVFrame", u"REPORT ON LEARNER'S OBSERVED VALUES", None))
        ___qtablewidgetitem2 = self.obTable.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("attendanceOVFrame", u"BEHAVIOR STATEMENTS", None));
        ___qtablewidgetitem3 = self.obTable.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("attendanceOVFrame", u"Q1", None));
        ___qtablewidgetitem4 = self.obTable.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("attendanceOVFrame", u"Q2", None));
        ___qtablewidgetitem5 = self.obTable.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("attendanceOVFrame", u"Q3", None));
        ___qtablewidgetitem6 = self.obTable.horizontalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("attendanceOVFrame", u"Q4", None));
        ___qtablewidgetitem7 = self.obTable.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("attendanceOVFrame", u" 1. Maka-Diyos", None));
        ___qtablewidgetitem8 = self.obTable.verticalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("attendanceOVFrame", u" 2. Makatao", None));
        ___qtablewidgetitem9 = self.obTable.verticalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("attendanceOVFrame", u" 3. Makakalikasan", None));
        ___qtablewidgetitem10 = self.obTable.verticalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("attendanceOVFrame", u" 4. Makabansa", None));

        __sortingEnabled = self.obTable.isSortingEnabled()
        self.obTable.setSortingEnabled(False)
        ___qtablewidgetitem11 = self.obTable.item(0, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("attendanceOVFrame", u"Expresses ones spiritual beliefs while respecting the spiritual belief of others", None));
        ___qtablewidgetitem12 = self.obTable.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("attendanceOVFrame", u"Shows adherence to ethical principles by upholding truth", None));
        ___qtablewidgetitem13 = self.obTable.item(2, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("attendanceOVFrame", u"Is sensitive to individual, social, and cultural differences", None));
        ___qtablewidgetitem14 = self.obTable.item(3, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("attendanceOVFrame", u"Demonstrate the contributions toward solidarity", None));
        ___qtablewidgetitem15 = self.obTable.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("attendanceOVFrame", u"Cares for the environment and utilizes resources wisely, judiciously, and economically", None));
        ___qtablewidgetitem16 = self.obTable.item(5, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("attendanceOVFrame", u"Demonstrate pride in being a Filipino: exercise the rights and responsibilities of a Filipino citizen", None));
        ___qtablewidgetitem17 = self.obTable.item(6, 0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("attendanceOVFrame", u"Demonstrate appropriate behavior in carrying out activities in the school, community, and country", None));
        self.obTable.setSortingEnabled(__sortingEnabled)

        self.textEdit.setHtml(QCoreApplication.translate("attendanceOVFrame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">OBSERVED VALUES:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">AO</span><span style=\" font-size:9pt;\"> - Always Observed		</span><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">RO</span><span style=\" font-size:9pt;\"> - Rarely Observed</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-inde"
                        "nt:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">SO</span><span style=\" font-size:9pt;\"> - Sometimes Observed	</span><span style=\" font-size:9pt; font-weight:600; font-style:italic;\">NO</span><span style=\" font-size:9pt;\"> - Not Observed</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.updObBtn.setText(QCoreApplication.translate("attendanceOVFrame", u"Update Observed Values", None))
        self.fillTableBtn.setText(QCoreApplication.translate("attendanceOVFrame", u"Fill Table with", None))
        self.label_8.setText(QCoreApplication.translate("attendanceOVFrame", u"REPORT ON LEARNER'S ATTENDANCE", None))
        self.label_3.setText(QCoreApplication.translate("attendanceOVFrame", u"Start of Classes:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("attendanceOVFrame", u"MMM/dd/yyyy", None))
        self.updMonthBtn.setText(QCoreApplication.translate("attendanceOVFrame", u"Update Month", None))
        self.startClassDate.setText("")
        self.updAttBtn.setText(QCoreApplication.translate("attendanceOVFrame", u"Update Attendance", None))
        ___qtablewidgetitem18 = self.attTable.horizontalHeaderItem(0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 1", None));
        ___qtablewidgetitem19 = self.attTable.horizontalHeaderItem(1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 2", None));
        ___qtablewidgetitem20 = self.attTable.horizontalHeaderItem(2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 3", None));
        ___qtablewidgetitem21 = self.attTable.horizontalHeaderItem(3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 4", None));
        ___qtablewidgetitem22 = self.attTable.horizontalHeaderItem(4)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 5", None));
        ___qtablewidgetitem23 = self.attTable.horizontalHeaderItem(5)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 6", None));
        ___qtablewidgetitem24 = self.attTable.horizontalHeaderItem(6)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 7", None));
        ___qtablewidgetitem25 = self.attTable.horizontalHeaderItem(7)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 8", None));
        ___qtablewidgetitem26 = self.attTable.horizontalHeaderItem(8)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 9", None));
        ___qtablewidgetitem27 = self.attTable.horizontalHeaderItem(9)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 10", None));
        ___qtablewidgetitem28 = self.attTable.horizontalHeaderItem(10)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 11", None));
        ___qtablewidgetitem29 = self.attTable.horizontalHeaderItem(11)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("attendanceOVFrame", u"Month 12", None));
        ___qtablewidgetitem30 = self.attTable.horizontalHeaderItem(12)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("attendanceOVFrame", u"Total", None));
        ___qtablewidgetitem31 = self.attTable.verticalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("attendanceOVFrame", u"No. of School Days", None));
        ___qtablewidgetitem32 = self.attTable.verticalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("attendanceOVFrame", u"No. of Days Present", None));
        ___qtablewidgetitem33 = self.attTable.verticalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("attendanceOVFrame", u"No. of Days Absent", None));
    # retranslateUi

