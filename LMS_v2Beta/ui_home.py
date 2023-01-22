# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homerxsswv.ui'
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

from ui_dashBoard import Ui_dBFrame
import classDataBase
import os

class Ui_homeMainFrame(object):
    def setupUi(self, homeMainFrame):
        if homeMainFrame.objectName():
            homeMainFrame.setObjectName(u"homeMainFrame")
        homeMainFrame.resize(1155, 622)
        self.horizontalLayout = QHBoxLayout(homeMainFrame)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(7, 7, 7, 7)
        self.leftFrame = QFrame(homeMainFrame)
        self.leftFrame.setObjectName(u"leftFrame")
        self.leftFrame.setMaximumSize(QSize(420, 16777215))
        self.leftFrame.setFrameShape(QFrame.StyledPanel)
        self.leftFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.leftFrame)
        self.verticalLayout_9.setSpacing(3)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.leftFrame)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"Verdana")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout_9.addWidget(self.label)

        self.shadowTop = QGraphicsDropShadowEffect()       ######################## add shadow effect ############################################
        self.shadowTop.setBlurRadius(15)
        self.shadowTop.setOffset(6, 6)

        self.pageBtnframe = QFrame(self.leftFrame)
        self.pageBtnframe.setObjectName(u"pageBtnframe")
        self.pageBtnframe.setMinimumSize(QSize(0, 80))
        self.pageBtnframe.setMaximumSize(QSize(16777215, 120))
        self.pageBtnframe.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.pageBtnframe.setFrameShape(QFrame.StyledPanel)
        self.pageBtnframe.setFrameShadow(QFrame.Raised)
        self.pageBtnframe.setGraphicsEffect(self.shadowTop) ############################# adding shadow effect to frame ###############
        self.horizontalLayout_10 = QHBoxLayout(self.pageBtnframe)
        self.horizontalLayout_10.setSpacing(3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.profBtn0 = QPushButton(self.pageBtnframe)
        self.profBtn0.setObjectName(u"profBtn0")
        self.profBtn0.setMinimumSize(QSize(115, 30))
        self.profBtn0.setMaximumSize(QSize(115, 50))
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(9)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setWeight(75)
        self.profBtn0.setFont(font1)
        self.profBtn0.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"	background-color: rgb(26, 194, 161);\n"
"	\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(26, 194, 161);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(26, 194, 161)\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(222, 222, 222);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(222, 222, 222)\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/prof.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profBtn0.setIcon(icon)
        self.profBtn0.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.profBtn0)

        self.gradeBtn0 = QPushButton(self.pageBtnframe)
        self.gradeBtn0.setObjectName(u"gradeBtn0")
        self.gradeBtn0.setMinimumSize(QSize(115, 30))
        self.gradeBtn0.setMaximumSize(QSize(115, 50))
        self.gradeBtn0.setFont(font1)
        self.gradeBtn0.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"	background-color: rgb(26, 194, 161);\n"
"	\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(26, 194, 161);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(26, 194, 161)\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(222, 222, 222);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(222, 222, 222)\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/grade.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gradeBtn0.setIcon(icon1)
        self.gradeBtn0.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.gradeBtn0)

        self.attendBtn0 = QPushButton(self.pageBtnframe)
        self.attendBtn0.setObjectName(u"attendBtn0")
        self.attendBtn0.setMinimumSize(QSize(160, 30))
        self.attendBtn0.setMaximumSize(QSize(160, 50))
        self.attendBtn0.setFont(font1)
        self.attendBtn0.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"	background-color: rgb(26, 194, 161);\n"
"	\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(26, 194, 161);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(26, 194, 161)\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(222, 222, 222);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(222, 222, 222)\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/att.png", QSize(), QIcon.Normal, QIcon.Off)
        self.attendBtn0.setIcon(icon2)
        self.attendBtn0.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.attendBtn0)


        self.verticalLayout_9.addWidget(self.pageBtnframe)

        self.label_2 = QLabel(self.leftFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 30))
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"QLabel{background-color: none;}")

        self.verticalLayout_9.addWidget(self.label_2)

        self.entryClassFrame = QFrame(self.leftFrame)
        self.entryClassFrame.setObjectName(u"entryClassFrame")
        self.entryClassFrame.setMinimumSize(QSize(0, 330))
        self.entryClassFrame.setMaximumSize(QSize(16777215, 1000))
        self.entryClassFrame.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.entryClassFrame.setFrameShape(QFrame.NoFrame)
        self.entryClassFrame.setFrameShadow(QFrame.Plain)
        self.formLayout = QFormLayout(self.entryClassFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout.setVerticalSpacing(14)
        self.formLayout.setContentsMargins(-1, -1, -1, 9)
        self.depLabel = QLabel(self.entryClassFrame)
        self.depLabel.setObjectName(u"depLabel")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.depLabel.setFont(font2)
        self.depLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.depLabel)

        self.depCombo = QComboBox(self.entryClassFrame)
        self.depCombo.setObjectName(u"depCombo")
        self.depCombo.setMinimumSize(QSize(0, 28))
        self.depCombo.setMaximumSize(QSize(16777215, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.depCombo.setFont(font3)
        self.depCombo.setStyleSheet(u"QComboBox{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.depCombo.addItem("-- select --")
        self.depCombo.addItem('JUNIOR HIGH SCHOOL', ['7','8','9','10'])  ################################### department items ##########################
        self.depCombo.addItem("SENIOR HIGH SCHOOL", ['11','12'])
        self.depCombo.activated.connect(self.depGrade)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.depCombo)

        self.syLabel = QLabel(self.entryClassFrame)
        self.syLabel.setObjectName(u"syLabel")
        self.syLabel.setFont(font2)
        self.syLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.syLabel)

        self.syEntry = QLineEdit(self.entryClassFrame)
        self.syEntry.setObjectName(u"syEntry")
        self.syEntry.setMinimumSize(QSize(0, 28))
        self.syEntry.setMaximumSize(QSize(16777215, 28))
        self.syEntry.setFont(font3)
        self.syEntry.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.syEntry)

        self.shLabel = QLabel(self.entryClassFrame)
        self.shLabel.setObjectName(u"shLabel")
        self.shLabel.setFont(font2)
        self.shLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.shLabel)

        self.shEntry = QLineEdit(self.entryClassFrame)
        self.shEntry.setObjectName(u"shEntry")
        self.shEntry.setMinimumSize(QSize(0, 28))
        self.shEntry.setMaximumSize(QSize(16777215, 28))
        self.shEntry.setFont(font3)
        self.shEntry.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.shEntry)

        self.gradeLabel = QLabel(self.entryClassFrame)
        self.gradeLabel.setObjectName(u"gradeLabel")
        self.gradeLabel.setFont(font2)
        self.gradeLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.gradeLabel)

        self.gradeCombo = QComboBox(self.entryClassFrame)
        self.gradeCombo.setObjectName(u"gradeCombo")
        self.gradeCombo.setMinimumSize(QSize(0, 28))
        self.gradeCombo.setMaximumSize(QSize(16777215, 28))
        self.gradeCombo.setFont(font3)
        self.gradeCombo.setStyleSheet(u"QComboBox{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.gradeCombo)

        self.sectionLabel = QLabel(self.entryClassFrame)
        self.sectionLabel.setObjectName(u"sectionLabel")
        self.sectionLabel.setFont(font2)
        self.sectionLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.sectionLabel)

        self.sectionEntry = QLineEdit(self.entryClassFrame)
        self.sectionEntry.setObjectName(u"sectionEntry")
        self.sectionEntry.setMinimumSize(QSize(0, 28))
        self.sectionEntry.setMaximumSize(QSize(16777215, 28))
        self.sectionEntry.setFont(font3)
        self.sectionEntry.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.sectionEntry)

        self.strandLabel = QLabel(self.entryClassFrame)
        self.strandLabel.setObjectName(u"strandLabel")
        self.strandLabel.setFont(font2)
        self.strandLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.strandLabel)

        self.strandCombo = QComboBox(self.entryClassFrame)
        self.strandCombo.setObjectName(u"strandCombo")
        self.strandCombo.setMinimumSize(QSize(0, 28))
        self.strandCombo.setMaximumSize(QSize(16777215, 28))
        self.strandCombo.setFont(font3)
        self.strandCombo.setStyleSheet(u"QComboBox{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.strandCombo)

        self.advLabel = QLabel(self.entryClassFrame)
        self.advLabel.setObjectName(u"advLabel")
        self.advLabel.setFont(font2)
        self.advLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.advLabel)

        self.advEntry = QLineEdit(self.entryClassFrame)
        self.advEntry.setObjectName(u"advEntry")
        self.advEntry.setMinimumSize(QSize(0, 28))
        self.advEntry.setMaximumSize(QSize(16777215, 28))
        self.advEntry.setFont(font3)
        self.advEntry.setStyleSheet(u"QLineEdit{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.advEntry)

        self.semLabel = QLabel(self.entryClassFrame)
        self.semLabel.setObjectName(u"semLabel")
        self.semLabel.setFont(font2)
        self.semLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.semLabel)

        self.semCombo = QComboBox(self.entryClassFrame)
        self.semCombo.setObjectName(u"semCombo")
        self.semCombo.setMinimumSize(QSize(0, 28))
        self.semCombo.setMaximumSize(QSize(16777215, 28))
        self.semCombo.setFont(font3)
        self.semCombo.setStyleSheet(u"QComboBox{\n"
"border: 1px solid;\n"
"border-color: rgb(26, 191, 164);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.semCombo)


        self.verticalLayout_9.addWidget(self.entryClassFrame)

        self.frame = QFrame(self.leftFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 100))
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saveClassBtn = QPushButton(self.frame)
        self.saveClassBtn.setObjectName(u"saveClassBtn")
        self.saveClassBtn.setMinimumSize(QSize(0, 25))
        self.saveClassBtn.setMaximumSize(QSize(16777215, 50))
        self.saveClassBtn.setFont(font2)
        self.saveClassBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(26, 191, 164);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.saveClassBtn, 0, 0, 1, 1)

        self.upClassBtn = QPushButton(self.frame)
        self.upClassBtn.setObjectName(u"upClassBtn")
        self.upClassBtn.setMinimumSize(QSize(0, 25))
        self.upClassBtn.setMaximumSize(QSize(16777215, 50))
        self.upClassBtn.setFont(font2)
        self.upClassBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(26, 191, 164);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.upClassBtn, 0, 1, 1, 1)

        self.delAllBtn = QPushButton(self.frame)
        self.delAllBtn.setObjectName(u"delAllBtn")
        self.delAllBtn.setMinimumSize(QSize(0, 25))
        self.delAllBtn.setMaximumSize(QSize(16777215, 50))
        self.delAllBtn.setFont(font2)
        self.delAllBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(26, 191, 164);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.delAllBtn, 1, 0, 1, 1)

        self.helpBtn = QPushButton(self.frame)
        self.helpBtn.setObjectName(u"helpBtn")
        self.helpBtn.setMinimumSize(QSize(0, 25))
        self.helpBtn.setMaximumSize(QSize(16777215, 50))
        self.helpBtn.setFont(font2)
        self.helpBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0, 0, 0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(26, 191, 164);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(26, 191, 164);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}")

        self.gridLayout.addWidget(self.helpBtn, 1, 1, 1, 1)


        self.verticalLayout_9.addWidget(self.frame)


        self.horizontalLayout.addWidget(self.leftFrame)

        self.rightFrame = QFrame(homeMainFrame)
        self.rightFrame.setObjectName(u"rightFrame")
        self.rightFrame.setFrameShape(QFrame.StyledPanel)
        self.rightFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.rightFrame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.rightFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 330))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"background-color: rgb(67, 156, 250);\n"
"}\n"
"\n"
"	")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 80))
        self.frame_5.setMaximumSize(QSize(16777215, 80))
        self.frame_5.setSizeIncrement(QSize(0, 40))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(67, 156, 250);\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.logo = QLabel(self.frame_5)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(90, 80))
        self.logo.setMaximumSize(QSize(80, 80))
        self.logo.setPixmap(QPixmap(u"icons/logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.logo)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(67, 156, 250);\n"
"}\n"
"")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(16)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_13.setFont(font4)
        self.label_13.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background-color: rgb(67, 156, 250);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_13.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.label_14.setFont(font5)
        self.label_14.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"background-color: rgb(67, 156, 250);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.label_14.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.label_14)


        self.horizontalLayout_12.addWidget(self.frame_6)


        self.verticalLayout_11.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_3)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 160))
        self.frame_7.setMaximumSize(QSize(16777215, 220))
        self.frame_7.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.depDisplay = QLabel(self.frame_7)
        self.depDisplay.setObjectName(u"depDisplay")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setItalic(False)
        font6.setWeight(75)
        self.depDisplay.setFont(font6)
        self.depDisplay.setStyleSheet(u"QLabel{\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.verticalLayout_14.addWidget(self.depDisplay)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.shDisplay = QLabel(self.frame_8)
        self.shDisplay.setObjectName(u"shDisplay")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setWeight(75)
        self.shDisplay.setFont(font7)

        self.horizontalLayout_13.addWidget(self.shDisplay)

        self.syDisplay = QLabel(self.frame_8)
        self.syDisplay.setObjectName(u"syDisplay")
        font8 = QFont()
        font8.setFamily(u"Verdana")
        font8.setPointSize(11)
        self.syDisplay.setFont(font8)

        self.horizontalLayout_13.addWidget(self.syDisplay)


        self.verticalLayout_14.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.advDisplay = QLabel(self.frame_9)
        self.advDisplay.setObjectName(u"advDisplay")
        font9 = QFont()
        font9.setFamily(u"Segoe UI")
        font9.setPointSize(11)
        font9.setItalic(True)
        self.advDisplay.setFont(font9)

        self.horizontalLayout_14.addWidget(self.advDisplay)

        self.semDisplay = QLabel(self.frame_9)
        self.semDisplay.setObjectName(u"semDisplay")
        font10 = QFont()
        font10.setFamily(u"Verdana")
        font10.setPointSize(10)
        self.semDisplay.setFont(font10)

        self.horizontalLayout_14.addWidget(self.semDisplay)

        self.verticalLayout_14.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_7)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gradeSecDisplay = QLabel(self.frame_10)
        self.gradeSecDisplay.setObjectName(u"gradeSecDisplay")
        font11 = QFont()
        font11.setFamily(u"Segoe UI Semibold")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.gradeSecDisplay.setFont(font11)
        self.gradeSecDisplay.setStyleSheet(u"QLabel{\n"
"background:none;\n"
"}")
        self.shadow = QGraphicsDropShadowEffect()       ######################## add shadow effect ############################################
        self.shadow.setBlurRadius(15)
        self.shadow.setOffset(6, 6)

        self.horizontalLayout_15.addWidget(self.gradeSecDisplay)

        self.strandDisplay = QLabel(self.frame_10)
        self.strandDisplay.setObjectName(u"strandDisplay")
        self.strandDisplay.setFont(font10)

        self.horizontalLayout_15.addWidget(self.strandDisplay)

        self.verticalLayout_14.addWidget(self.frame_10)

        self.verticalLayout_11.addWidget(self.frame_7)

        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.rightFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 10, 10)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(280, 182))
        self.frame_11.setMaximumSize(QSize(280, 16777215))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_11)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 10)

        self.importFrame = QFrame(self.frame_11)
        self.importFrame.setObjectName(u"importFrame")
        self.importFrame.setMinimumSize(QSize(270, 0))
        self.importFrame.setMaximumSize(QSize(270, 16777215))
        self.importFrame.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(67, 156, 250);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.importFrame.setFrameShape(QFrame.StyledPanel)
        self.importFrame.setFrameShadow(QFrame.Raised)
        self.importFrame.setGraphicsEffect(self.shadow) ############################# adding shadow effect to frame ###############
        self.verticalLayout_7 = QVBoxLayout(self.importFrame)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_22 = QLabel(self.importFrame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMinimumSize(QSize(0, 29))
        self.label_22.setMaximumSize(QSize(16777215, 30))
        self.label_22.setFont(font7)
        self.label_22.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"color: rgb(67, 156, 250);\n"
"}")
        self.verticalLayout_7.addWidget(self.label_22)

        self.textBrowser_2 = QTextBrowser(self.importFrame)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setMinimumSize(QSize(0, 60))
        self.textBrowser_2.setMaximumSize(QSize(16777215, 60))
        font12 = QFont()
        font12.setFamily(u"Segoe UI")
        font12.setPointSize(9)
        font12.setItalic(True)
        self.textBrowser_2.setFont(font12)
        self.textBrowser_2.setStyleSheet(u"QTextBrowser{\n"
"border: none;\n"
"}")

        self.verticalLayout_7.addWidget(self.textBrowser_2)

#         self.reportCombo_2 = QComboBox(self.importFrame)      ########## combobox for open file ###############
#         self.reportCombo_2.setObjectName(u"reportCombo_2")
#         self.reportCombo_2.setMinimumSize(QSize(0, 30))
#         self.reportCombo_2.setMaximumSize(QSize(16777215, 30))
#         self.reportCombo_2.setFont(font10)
#         self.reportCombo_2.setStyleSheet(u"QComboBox{\n"
# "border: 1px solid;\n"
# "border-color: rgb(67, 156, 250);\n"
# "border-radius: 5px;\n"
# "background-color: rgb(255, 255, 255);\n"
# "}\n"
# "\n"
# "	")

#         self.verticalLayout_7.addWidget(self.reportCombo_2)

        self.openSF1Btn = QPushButton(self.importFrame)
        self.openSF1Btn.setObjectName(u"openSF1Btn")
        self.openSF1Btn.setMinimumSize(QSize(0, 30))
        self.openSF1Btn.setMaximumSize(QSize(16777215, 50))
        self.openSF1Btn.setFont(font2)
        self.openSF1Btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.verticalLayout_7.addWidget(self.openSF1Btn)

        self.verticalLayout_2.addWidget(self.importFrame)

        self.shadow1 = QGraphicsDropShadowEffect()       ######################## add shadow effect ############################################
        self.shadow1.setBlurRadius(15)
        self.shadow1.setOffset(6, 6)

        self.reportFrame = QFrame(self.frame_11)
        self.reportFrame.setObjectName(u"reportFrame")
        self.reportFrame.setMinimumSize(QSize(270, 0))
        self.reportFrame.setMaximumSize(QSize(270, 16777215))
        self.reportFrame.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(67, 156, 250);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.reportFrame.setFrameShape(QFrame.StyledPanel)
        self.reportFrame.setFrameShadow(QFrame.Raised)
        self.reportFrame.setGraphicsEffect(self.shadow1) ############################# adding shadow effect to frame ###############

        self.verticalLayout_6 = QVBoxLayout(self.reportFrame)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 9, 9, 9)
        self.label_21 = QLabel(self.reportFrame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(0, 29))
        self.label_21.setMaximumSize(QSize(16777215, 30))
        self.label_21.setFont(font7)
        self.label_21.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"color: rgb(67, 156, 250);\n"
"}")

        self.verticalLayout_6.addWidget(self.label_21)

        self.textBrowser = QTextBrowser(self.reportFrame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(0, 60))
        self.textBrowser.setMaximumSize(QSize(16777215, 60))
        self.textBrowser.setFont(font12)
        self.textBrowser.setStyleSheet(u"QTextBrowser{\n"
"border: none;\n"
"}")

        self.verticalLayout_6.addWidget(self.textBrowser)

#         self.reportCombo = QComboBox(self.reportFrame)
#         self.reportCombo.setObjectName(u"reportCombo")
#         self.reportCombo.setMinimumSize(QSize(0, 30))
#         self.reportCombo.setMaximumSize(QSize(16777215, 30))
#         self.reportCombo.setFont(font10)
#         self.reportCombo.setStyleSheet(u"QComboBox{\n"
# "border: 1px solid;\n"
# "border-color: rgb(67, 156, 250);\n"
# "border-radius: 5px;\n"
# "background-color: rgb(255, 255, 255);\n"
# "}\n"
# "\n"
# "	")

#         self.verticalLayout_6.addWidget(self.reportCombo)

        self.expBtn = QPushButton(self.reportFrame, clicked=lambda:self.export())
        self.expBtn.setObjectName(u"expBtn")
        self.expBtn.setMinimumSize(QSize(0, 30))
        self.expBtn.setMaximumSize(QSize(16777215, 50))
        self.expBtn.setFont(font2)
        self.expBtn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.verticalLayout_6.addWidget(self.expBtn)

        self.verticalLayout_2.addWidget(self.reportFrame)

        self.horizontalLayout_3.addWidget(self.frame_11)

        self.shadow2 = QGraphicsDropShadowEffect()       ######################## add shadow effect ############################################
        self.shadow2.setBlurRadius(15)
        self.shadow2.setOffset(6, 6)

        self.dashBoardFrame = QFrame(self.frame_4)
        self.dashBoardFrame.setObjectName(u"dashBoardFrame")
        self.dashBoardFrame.setStyleSheet(u"QFrame{\n"
"border: 1px solid;\n"
"border-color: rgb(67, 156, 250);\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"	")
        self.dashBoardFrame.setFrameShape(QFrame.StyledPanel)
        self.dashBoardFrame.setFrameShadow(QFrame.Raised)
        self.dashBoardFrame.setGraphicsEffect(self.shadow2) ############################# adding shadow effect to frame ###############
        self.verticalLayout = QVBoxLayout(self.dashBoardFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_13 = QFrame(self.dashBoardFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(0, 46))
        self.frame_13.setMaximumSize(QSize(16777215, 46))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dashLabel = QLabel(self.frame_13)
        self.dashLabel.setObjectName(u"dashLabel")
        self.dashLabel.setFont(font7)
        self.dashLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"color: rgb(67, 156, 250);\n"
"}")
        self.horizontalLayout_2.addWidget(self.dashLabel)

        self.refBtn = QPushButton(self.frame_13, clicked=lambda:self.refreshDB())
        self.refBtn.setObjectName(u"refBtn")
        self.refBtn.setMinimumSize(QSize(100, 25))
        self.refBtn.setMaximumSize(QSize(100, 25))
        font13 = QFont()
        font13.setFamily(u"Segoe UI Semibold")
        font13.setBold(True)
        font13.setWeight(75)
        self.refBtn.setFont(font13)
        self.refBtn.setStyleSheet(u"QPushButton{border: 2px solid rgb(67, 156, 250);border-radius: 5px;\n"
"color: rgb(255, 255, 255);background-color: rgb(67, 156, 250);}\n"
"QPushButton:focus{border: 2px solid rgb(67, 156, 250);border-radius: 5px;\n"
"color: rgb(0,0,0);background-color: rgb(255,255,255);}\n")

        self.horizontalLayout_2.addWidget(self.refBtn)

        self.dashPrevBtn = QPushButton(self.frame_13, clicked=lambda: self.dashPrev())
        self.dashPrevBtn.setObjectName(u"dashPrevBtn")
        self.dashPrevBtn.setMinimumSize(QSize(40, 25))
        self.dashPrevBtn.setMaximumSize(QSize(40, 16777215))
        self.dashPrevBtn.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_2.addWidget(self.dashPrevBtn)

        self.dashNextBtn = QPushButton(self.frame_13, clicked=lambda: self.dashNext())
        self.dashNextBtn.setObjectName(u"dashNextBtn")
        self.dashNextBtn.setMinimumSize(QSize(40, 25))
        self.dashNextBtn.setMaximumSize(QSize(40, 16777215))
        self.dashNextBtn.setStyleSheet(u"QPushButton{\n"
"border: 2px solid;\n"
"border-color: rgb(67, 156, 250);\n"
"border-radius: 5px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout_2.addWidget(self.dashNextBtn)

        self.verticalLayout.addWidget(self.frame_13)

        self.dbContainer = QFrame(self.dashBoardFrame)
        self.dbContainer.setObjectName(u"dbContainer")
        self.dbContainer.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 3px;\n"
"border: none;\n"
"}")
        self.dbContainer.setFrameShape(QFrame.StyledPanel)
        self.dbContainer.setFrameShadow(QFrame.Raised)

        self.dbContainer.setFrameShape(QFrame.StyledPanel)
        self.dbContainer.setFrameShadow(QFrame.Raised)

        self.dashBoard = Ui_dBFrame()                   ############## frame for dashboard ####################
        self.dashBoard.setupUi(self.dbContainer)

        self.verticalLayout.addWidget(self.dbContainer)

        self.horizontalLayout_3.addWidget(self.dashBoardFrame)

        self.verticalLayout_10.addWidget(self.frame_4)

        self.horizontalLayout.addWidget(self.rightFrame)

        self.retranslateUi(homeMainFrame)

        QMetaObject.connectSlotsByName(homeMainFrame)
    # setupUi

    def refreshDB(self):
        pass

    def dashPrev(self):
        currentPage = self.dashBoard.stackedWidget.currentIndex()
        if currentPage != 0:
            self.dashBoard.stackedWidget.setCurrentIndex(currentPage - 1)

    def dashNext(self):
        pageCount = self.dashBoard.stackedWidget.count() 
        currentPage = self.dashBoard.stackedWidget.currentIndex()
        if currentPage != (pageCount-1):
            self.dashBoard.stackedWidget.setCurrentIndex(currentPage + 1)

    def depGrade(self, index):  ################### event for selecting department grade ######################
        self.gradeCombo.clear()
        self.strandCombo.clear()
        self.semCombo.clear()
        dep = self.depCombo.itemData(index)

        if dep:
            self.gradeCombo.addItems(dep)

            if self.depCombo.currentIndex() == 2:
                self.strandCombo.addItems(["General Academic Strand","TVL - Bread and Pastry Production, Beauty and Nail care, Dressmaking"])
                self.semCombo.addItems(["1st Semester","2nd Semester"])
            else:
                self.strandCombo.clear()
                self.semCombo.clear()

    def updateClass(self, displayMyClass):

        myClass = classDataBase.viewDataclass()
        if myClass != 0:
            classDataBase.updateClassRec(self.shEntry.text().upper(), self.advEntry.text().upper(), self.semCombo.currentText(), 1)
            display = displayMyClass()
            return display

    def delAllRecords(self, classDisplay):

        def msgFunction(i):                           ######### Callback function for messagebox (Return OK or Cancel) ####
            if i.text() == "OK":
                dbPath = "C:\\LMS_appVer2\\database\\"
                for file_name in os.listdir(dbPath):
                    file = dbPath + file_name
                    if os.path.isfile(file):
                        if file_name == 'class.db':
                            classDataBase.deleteALLClass()
                            continue
                        print('Deleting file:', file)
                        os.remove(file)
                classDisplay()

        self.showMessage("Warning", "Do you want to delete all records?\n(Class data, Learner's Profile and Grades will be deleted)\nClick Ok to proceed", msgFunction, QMessageBox.Warning)
    
    def openUIwindow(self):
        from ui_OpenFile import Ui_openFileWindow
        self.openFileWin = QMainWindow()
        self.openFileUI = Ui_openFileWindow()
        self.openFileUI.setupUi(self.openFileWin)
        self.openFileWin.show()

    def openFile(self, delDatabases):
        import openSF1
        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            sf1_excel = QFileDialog.getOpenFileName(None, "Open File", "", "Excel 97-2003 Workbook (*.xls)")
            
            if (sf1_excel[0]) != '':
                self.openUIwindow()                                    ###### Open second Window #######
                self.openFileUI.copyBtn.clicked.connect(lambda: self.openFileUI.copyFunction(self.openFileWin.close, sf1_excel[0]))
                self.openFileUI.cancelBtn.clicked.connect(lambda: self.openFileWin.close())                              
                if self.openFileUI.sf1Checker(sf1_excel[0]) == "validJHS":  ########### checking supported excel file ##########  
                    self.openFileUI.showSF1JHS_Data(sf1_excel[0])  ####### Junior High ######
                    self.openFileUI.stackedWidget.setCurrentWidget(self.openFileUI.validFrame)

                elif self.openFileUI.sf1Checker(sf1_excel[0]) == "validSHS":
                    self.openFileUI.showSF1SHS_Data(sf1_excel[0])    ####### Senior High #####
                    self.openFileUI.stackedWidget.setCurrentWidget(self.openFileUI.validFrame)
                else:
                    print(self.openFileUI.sf1Checker(sf1_excel[0]))
                    self.openFileUI.stackedWidget.setCurrentIndex(0)
                    self.openFileUI.okBtn.clicked.connect(lambda: self.openFileWin.close())
            else:
                print('no file selected')
        else:
            self.showMessage("No class entry","Fill up first the class entry then click save class", None, QMessageBox.Information)
    
    def openExport(self):
        from ui_export import Ui_ExpWindow
        self.exportWin = QMainWindow()
        self.exportUI = Ui_ExpWindow()
        self.exportUI.setupUi(self.exportWin)
        self.exportWin.show()
    
    def export(self):
        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            self.openExport()
            self.exportUI.cancelBtn.clicked.connect(lambda:self.exportWin.close())    
        else:
            self.showMessage("No class entry","Fill up first the class entry then click save class", None, QMessageBox.Information)

    def showMessage(self, title,  message, callback, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)  ## icons (QMessageBox.Question, QMessageBox.Information, QMessageBox.Warning, QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.buttonClicked.connect(callback)
        msg.exec_()

    def retranslateUi(self, homeMainFrame):
        homeMainFrame.setWindowTitle(QCoreApplication.translate("homeMainFrame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("homeMainFrame", u"Quick Icons", None))
#if QT_CONFIG(tooltip)
        self.profBtn0.setToolTip(QCoreApplication.translate("homeMainFrame", u"Student's Profile", None))
#endif // QT_CONFIG(tooltip)
        self.profBtn0.setText(QCoreApplication.translate("homeMainFrame", u"PROFILE ", None))
#if QT_CONFIG(tooltip)
        self.gradeBtn0.setToolTip(QCoreApplication.translate("homeMainFrame", u"Student's Profile", None))
#endif // QT_CONFIG(tooltip)
        self.gradeBtn0.setText(QCoreApplication.translate("homeMainFrame", u"GRADES", None))
#if QT_CONFIG(tooltip)
        self.attendBtn0.setToolTip(QCoreApplication.translate("homeMainFrame", u"Student's Profile", None))
#endif // QT_CONFIG(tooltip)
        self.attendBtn0.setText(QCoreApplication.translate("homeMainFrame", u"ATTENDANCE", None))
        self.label_2.setText(QCoreApplication.translate("homeMainFrame", u"Class Entry", None))
        self.depLabel.setText(QCoreApplication.translate("homeMainFrame", u"Department:", None))
        self.syLabel.setText(QCoreApplication.translate("homeMainFrame", u"School Year:", None))
        self.shLabel.setText(QCoreApplication.translate("homeMainFrame", u"School Head:", None))
        self.gradeLabel.setText(QCoreApplication.translate("homeMainFrame", u"Grade:", None))
        self.sectionLabel.setText(QCoreApplication.translate("homeMainFrame", u"Section:", None))
        self.strandLabel.setText(QCoreApplication.translate("homeMainFrame", u"Strand:", None))
        self.advLabel.setText(QCoreApplication.translate("homeMainFrame", u"Adviser:", None))
        self.semLabel.setText(QCoreApplication.translate("homeMainFrame", u"Semester:", None))
        self.saveClassBtn.setText(QCoreApplication.translate("homeMainFrame", u"Save Class", None))
        self.upClassBtn.setText(QCoreApplication.translate("homeMainFrame", u"Update Class", None))
        self.delAllBtn.setText(QCoreApplication.translate("homeMainFrame", u"Delete All Records", None))
        self.helpBtn.setText(QCoreApplication.translate("homeMainFrame", u"Help", None))
        self.logo.setText("")
        self.label_13.setText(QCoreApplication.translate("homeMainFrame", u"MANTALISAY NATIONAL HIGH SCHOOL", None))
        self.label_14.setText(QCoreApplication.translate("homeMainFrame", u"Mantalisay Libmanan Camarines Sur", None))
        self.depDisplay.setText(QCoreApplication.translate("homeMainFrame", u"<DEPARTMENT>", None))
        self.shDisplay.setText(QCoreApplication.translate("homeMainFrame", u"School Head:   ", None))
        self.syDisplay.setText(QCoreApplication.translate("homeMainFrame", u"School Year: ", None))
        self.advDisplay.setText(QCoreApplication.translate("homeMainFrame", u"Adviser:   ", None))
        self.semDisplay.setText("")
        self.gradeSecDisplay.setText(QCoreApplication.translate("homeMainFrame", u"Grade & Section", None))
        self.strandDisplay.setText("")
        self.label_22.setText(QCoreApplication.translate("homeMainFrame", u"Import Learner's Data", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("homeMainFrame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt;\">(Copy learner's data from School Form 1 (SF1) )</span></p></body></html>", None))
        self.openSF1Btn.setText(QCoreApplication.translate("homeMainFrame", u"Open SF1 File", None))
        self.label_21.setText(QCoreApplication.translate("homeMainFrame", u"Reports", None))
        self.textBrowser.setHtml(QCoreApplication.translate("homeMainFrame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:italic;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt;\">( Generate School Report Card, Class List, Attendance Form, Grading sheet in excel format)</span></p></body></html>", None))
        self.expBtn.setText(QCoreApplication.translate("homeMainFrame", u"Export", None))
        self.dashLabel.setText(QCoreApplication.translate("homeMainFrame", u"Dashboard", None))
        self.refBtn.setText(QCoreApplication.translate("homeMainFrame", u"Refresh Data", None))
        self.dashPrevBtn.setText(QCoreApplication.translate("homeMainFrame", u"<<", None))
        self.dashNextBtn.setText(QCoreApplication.translate("homeMainFrame", u">>", None))
    # retranslateUi

