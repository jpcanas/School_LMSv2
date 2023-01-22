# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profileGeiqwB.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QIntValidator)                                             ############# Import QIntValidator ##############
from PySide2.QtWidgets import * 

import profileDataBase
import classDataBase
import gradesJHSDataBase
import gradesSHSDataBase1
import gradesSHSDataBase2
import ovDataBase
import attDataBase

class Ui_profileSection(object):

    def setupUi(self, profileSection):
        if profileSection.objectName():
            profileSection.setObjectName(u"profileSection")
        profileSection.resize(1152, 708)
        self.horizontalLayout = QHBoxLayout(profileSection)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.inputProfFrame = QFrame(profileSection)
        self.inputProfFrame.setObjectName(u"inputProfFrame")
        self.inputProfFrame.setMaximumSize(QSize(400, 16777215))
        self.inputProfFrame.setSizeIncrement(QSize(0, 0))
        self.inputProfFrame.setFrameShape(QFrame.StyledPanel)
        self.inputProfFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.inputProfFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.inputProfFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 25))
        self.frame.setMaximumSize(QSize(16777215, 30))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(11, 0, 0, 0)
        self.input_label = QLabel(self.frame)
        self.input_label.setObjectName(u"input_label")
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.input_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.input_label)

        self.hideSideBtn = QPushButton(self.frame, clicked = lambda: self.hideSide())
        self.hideSideBtn.setObjectName(u"hideSideBtn")
        self.hideSideBtn.setMaximumSize(QSize(30, 30))
        self.hideSideBtn.setStyleSheet(u"QPushButton{\n"
"border:none; background-color: rgb(235, 235, 235);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/togg.png", QSize(), QIcon.Normal, QIcon.Off)
        self.hideSideBtn.setIcon(icon)
        self.hideSideBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.hideSideBtn)


        self.verticalLayout.addWidget(self.frame)

        self.scrollArea = QScrollArea(self.inputProfFrame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(400, 0))
        self.scrollArea.setMaximumSize(QSize(400, 16777215))
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
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
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QFrame.Plain)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 1084))
        self.scrollAreaWidgetContents.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.scrollLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.scrollLayout.setSpacing(1)
        self.scrollLayout.setObjectName(u"scrollLayout")
        self.scrollLayout.setContentsMargins(2, 2, 2, 2)
        self.scroll_inputFrame = QFrame(self.scrollAreaWidgetContents)
        self.scroll_inputFrame.setObjectName(u"scroll_inputFrame")
        self.scroll_inputFrame.setMinimumSize(QSize(0, 1080))
        self.scroll_inputFrame.setMaximumSize(QSize(16777215, 1080))
        self.scroll_inputFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(67, 156, 250);\n"
"	border-radius: 5px;\n"
"}")
        self.scroll_inputFrame.setFrameShape(QFrame.NoFrame)
        self.scroll_inputFrame.setFrameShadow(QFrame.Plain)
        self.basicInfoFrame = QFrame(self.scroll_inputFrame)
        self.basicInfoFrame.setObjectName(u"basicInfoFrame")
        self.basicInfoFrame.setGeometry(QRect(0, 10, 374, 301))
        self.basicInfoFrame.setFrameShape(QFrame.StyledPanel)
        self.basicInfoFrame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.basicInfoFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setContentsMargins(-1, -1, 5, -1)
        self.lrn_label = QLabel(self.basicInfoFrame)
        self.lrn_label.setObjectName(u"lrn_label")
        font1 = QFont()
        font1.setFamily(u"Montserrat SemiBold")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.lrn_label.setFont(font1)
        self.lrn_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lrn_label)

        self.lrn_entry = QLineEdit(self.basicInfoFrame)
        self.lrn_entry.setObjectName(u"lrn_entry")
        font2 = QFont()
        font2.setFamily(u"Montserrat SemiBold")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.lrn_entry.setFont(font2)
        self.lrn_entry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lrn_entry)

        self.l_nameLabel = QLabel(self.basicInfoFrame)
        self.l_nameLabel.setObjectName(u"l_nameLabel")
        self.l_nameLabel.setFont(font1)
        self.l_nameLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.l_nameLabel)

        self.l_nameEntry = QLineEdit(self.basicInfoFrame)
        self.l_nameEntry.setObjectName(u"l_nameEntry")
        self.l_nameEntry.setFont(font2)
        self.l_nameEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.l_nameEntry)

        self.f_nameLabel = QLabel(self.basicInfoFrame)
        self.f_nameLabel.setObjectName(u"f_nameLabel")
        self.f_nameLabel.setFont(font1)
        self.f_nameLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.f_nameLabel)

        self.f_nameEntry = QLineEdit(self.basicInfoFrame)
        self.f_nameEntry.setObjectName(u"f_nameEntry")
        self.f_nameEntry.setFont(font2)
        self.f_nameEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.f_nameEntry)

        self.m_nameLabel = QLabel(self.basicInfoFrame)
        self.m_nameLabel.setObjectName(u"m_nameLabel")
        self.m_nameLabel.setFont(font1)
        self.m_nameLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.m_nameLabel)

        self.m_nameEntry = QLineEdit(self.basicInfoFrame)
        self.m_nameEntry.setObjectName(u"m_nameEntry")
        self.m_nameEntry.setFont(font2)
        self.m_nameEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.m_nameEntry)

        self.n_ExtLabel = QLabel(self.basicInfoFrame)
        self.n_ExtLabel.setObjectName(u"n_ExtLabel")
        self.n_ExtLabel.setFont(font1)
        self.n_ExtLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.n_ExtLabel)

        self.n_ExtEntry = QLineEdit(self.basicInfoFrame)
        self.n_ExtEntry.setObjectName(u"n_ExtEntry")
        self.n_ExtEntry.setFont(font2)
        self.n_ExtEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.n_ExtEntry)

        self.sexLabel = QLabel(self.basicInfoFrame)
        self.sexLabel.setObjectName(u"sexLabel")
        self.sexLabel.setFont(font1)
        self.sexLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.sexLabel)

        self.sexComboBox = QComboBox(self.basicInfoFrame)
        self.sexComboBox.setObjectName(u"sexComboBox")
        self.sexComboBox.setMaximumSize(QSize(150, 16777215))
        self.sexComboBox.setFont(font2)
        self.sexComboBox.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.sexComboBox.addItems(["MALE","FEMALE"])  ############################### ADD items sex combobox ###########################

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.sexComboBox)

        self.ageLabel = QLabel(self.basicInfoFrame)
        self.ageLabel.setObjectName(u"ageLabel")
        self.ageLabel.setFont(font1)
        self.ageLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.ageLabel)

        self.ageEntry = QLineEdit(self.basicInfoFrame)
        self.ageEntry.setObjectName(u"ageEntry")
        self.ageEntry.setMaximumSize(QSize(80, 16777215))
        self.ageEntry.setFont(font2)
        self.ageEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")
        self.ageEntry.setValidator(QIntValidator(10,99))   ########################### Age validator (int only between 10 - 99)####################

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ageEntry)

        self.addressContent = QFrame(self.scroll_inputFrame)
        self.addressContent.setObjectName(u"addressContent")
        self.addressContent.setGeometry(QRect(0, 340, 373, 131))
        self.addressContent.setMinimumSize(QSize(373, 0))
        self.addressContent.setMaximumSize(QSize(373, 16777215))
        self.addressContent.setFrameShape(QFrame.StyledPanel)
        self.addressContent.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.addressContent)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(15)
        self.formLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.brgyLabel = QLabel(self.addressContent)
        self.brgyLabel.setObjectName(u"brgyLabel")
        self.brgyLabel.setFont(font1)
        self.brgyLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.brgyLabel)

        self.brgyEntry = QLineEdit(self.addressContent)
        self.brgyEntry.setObjectName(u"brgyEntry")
        self.brgyEntry.setFont(font2)
        self.brgyEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.brgyEntry)

        self.munLabel = QLabel(self.addressContent)
        self.munLabel.setObjectName(u"munLabel")
        self.munLabel.setFont(font1)
        self.munLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.munLabel)

        self.munEntry = QLineEdit(self.addressContent)
        self.munEntry.setObjectName(u"munEntry")
        self.munEntry.setFont(font2)
        self.munEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.munEntry)

        self.provLabel = QLabel(self.addressContent)
        self.provLabel.setObjectName(u"provLabel")
        self.provLabel.setFont(font1)
        self.provLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.provLabel)

        self.provEntry = QLineEdit(self.addressContent)
        self.provEntry.setObjectName(u"provEntry")
        self.provEntry.setFont(font2)
        self.provEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.provEntry)

        self.addressLabel = QLabel(self.scroll_inputFrame)
        self.addressLabel.setObjectName(u"addressLabel")
        self.addressLabel.setGeometry(QRect(10, 315, 121, 21))
        font3 = QFont()
        font3.setFamily(u"Montserrat SemiBold")
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.addressLabel.setFont(font3)
        self.addressLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.dobLabel = QLabel(self.scroll_inputFrame)
        self.dobLabel.setObjectName(u"dobLabel")
        self.dobLabel.setGeometry(QRect(10, 480, 131, 21))
        self.dobLabel.setFont(font3)
        self.dobLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.dobFrame = QFrame(self.scroll_inputFrame)
        self.dobFrame.setObjectName(u"dobFrame")
        self.dobFrame.setGeometry(QRect(0, 510, 373, 131))
        self.dobFrame.setMinimumSize(QSize(373, 0))
        self.dobFrame.setMaximumSize(QSize(373, 16777215))
        self.dobFrame.setFrameShape(QFrame.StyledPanel)
        self.dobFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_3 = QFormLayout(self.dobFrame)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(12)
        self.formLayout_3.setVerticalSpacing(15)
        self.formLayout_3.setContentsMargins(-1, -1, 5, -1)
        self.monthLabel = QLabel(self.dobFrame)
        self.monthLabel.setObjectName(u"monthLabel")
        self.monthLabel.setFont(font1)
        self.monthLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.monthLabel)

        self.dateLabel = QLabel(self.dobFrame)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setFont(font1)
        self.dateLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.dateLabel)

        self.dateEntry = QLineEdit(self.dobFrame)
        self.dateEntry.setObjectName(u"dateEntry")
        self.dateEntry.setMinimumSize(QSize(150, 0))
        self.dateEntry.setMaximumSize(QSize(150, 16777215))
        self.dateEntry.setFont(font2)
        self.dateEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")
        self.dateEntry.setValidator(QIntValidator(1,31))   ########################### date validator (int only between 1 - 31)####################
        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.dateEntry)

        self.yearLabel = QLabel(self.dobFrame)
        self.yearLabel.setObjectName(u"yearLabel")
        self.yearLabel.setFont(font1)
        self.yearLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.yearLabel)

        self.yearEntry = QLineEdit(self.dobFrame)
        self.yearEntry.setObjectName(u"yearEntry")
        self.yearEntry.setMinimumSize(QSize(150, 0))
        self.yearEntry.setMaximumSize(QSize(150, 16777215))
        self.yearEntry.setFont(font2)
        self.yearEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")
        self.yearEntry.setValidator(QIntValidator(1800,3000))   ########################### yearEntry validator (int only between 1800-3000)####################
        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.yearEntry)

        self.monthCombo = QComboBox(self.dobFrame)
        self.monthCombo.setObjectName(u"monthCombo")
        self.monthCombo.setMaximumSize(QSize(300, 16777215))
        self.monthCombo.setFont(font2)
        self.monthCombo.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"\n"
"}")
         ################################### Combobox add Items (Month) ################ 
        self.monthCombo.addItems(["January","February","March","April","May","June","July","August","September","October","November","December"])  

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.monthCombo)

        self.parentFrame = QFrame(self.scroll_inputFrame)
        self.parentFrame.setObjectName(u"parentFrame")
        self.parentFrame.setGeometry(QRect(0, 650, 373, 211))
        self.parentFrame.setMinimumSize(QSize(373, 0))
        self.parentFrame.setMaximumSize(QSize(373, 16777215))
        self.parentFrame.setFrameShape(QFrame.StyledPanel)
        self.parentFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_4 = QFormLayout(self.parentFrame)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.motherLabel = QLabel(self.parentFrame)
        self.motherLabel.setObjectName(u"motherLabel")
        self.motherLabel.setFont(font1)
        self.motherLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.motherLabel)

        self.fatherLabel = QLabel(self.parentFrame)
        self.fatherLabel.setObjectName(u"fatherLabel")
        self.fatherLabel.setFont(font1)
        self.fatherLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_4.setWidget(2, QFormLayout.LabelRole, self.fatherLabel)

        self.fatherEntry = QLineEdit(self.parentFrame)
        self.fatherEntry.setObjectName(u"fatherEntry")
        self.fatherEntry.setMinimumSize(QSize(320, 0))
        self.fatherEntry.setMaximumSize(QSize(320, 16777215))
        self.fatherEntry.setFont(font2)
        self.fatherEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.fatherEntry)

        self.guardianLabel = QLabel(self.parentFrame)
        self.guardianLabel.setObjectName(u"guardianLabel")
        self.guardianLabel.setFont(font1)
        self.guardianLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.guardianLabel)

        self.guardianEntry = QLineEdit(self.parentFrame)
        self.guardianEntry.setObjectName(u"guardianEntry")
        self.guardianEntry.setMinimumSize(QSize(320, 0))
        self.guardianEntry.setMaximumSize(QSize(320, 16777215))
        self.guardianEntry.setFont(font2)
        self.guardianEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.guardianEntry)

        self.motherEntry = QLineEdit(self.parentFrame)
        self.motherEntry.setObjectName(u"motherEntry")
        self.motherEntry.setMinimumSize(QSize(320, 0))
        self.motherEntry.setMaximumSize(QSize(320, 16777215))
        self.motherEntry.setFont(font2)
        self.motherEntry.setStyleSheet(u"QLineEdit{\n"
"border-radius: 10px;\n"
"}")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.motherEntry)

        self.modalFrame = QFrame(self.scroll_inputFrame)
        self.modalFrame.setObjectName(u"modalFrame")
        self.modalFrame.setGeometry(QRect(0, 870, 373, 161))
        self.modalFrame.setMinimumSize(QSize(373, 0))
        self.modalFrame.setMaximumSize(QSize(373, 16777215))
        self.modalFrame.setFrameShape(QFrame.StyledPanel)
        self.modalFrame.setFrameShadow(QFrame.Raised)
        self.formLayout_5 = QFormLayout(self.modalFrame)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.modalLabel = QLabel(self.modalFrame)
        self.modalLabel.setObjectName(u"modalLabel")
        self.modalLabel.setFont(font1)
        self.modalLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.modalLabel)

        self.eligLabel = QLabel(self.modalFrame)
        self.eligLabel.setObjectName(u"eligLabel")
        self.eligLabel.setFont(font1)
        self.eligLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.eligLabel)

        self.modalCombo = QComboBox(self.modalFrame)
        self.modalCombo.setObjectName(u"modalCombo")
        self.modalCombo.setMaximumSize(QSize(300, 16777215))
        self.modalCombo.setFont(font2)
        self.modalCombo.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.modalCombo.addItems(["Modular","Face-to-Face","Online"])   ########################## modal combo items #################

        self.formLayout_5.setWidget(1, QFormLayout.SpanningRole, self.modalCombo)

        self.eligCombo = QComboBox(self.modalFrame)
        self.eligCombo.setObjectName(u"eligCombo")
        self.eligCombo.setMaximumSize(QSize(300, 16777215))
        self.eligCombo.setFont(font2)
        self.eligCombo.setStyleSheet(u"QComboBox{\n"
"border-radius: 10px;\n"
"\n"
"}")
        self.eligCombo.addItems(["Old-Students","Balik-Aral","Transferee","ALS"])   ####################### elig combo items ################

        self.formLayout_5.setWidget(3, QFormLayout.SpanningRole, self.eligCombo)


        self.scrollLayout.addWidget(self.scroll_inputFrame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.profFuncFrame = QFrame(self.inputProfFrame)
        self.profFuncFrame.setObjectName(u"profFuncFrame")
        self.profFuncFrame.setMinimumSize(QSize(0, 100))
        self.profFuncFrame.setMaximumSize(QSize(16777215, 100))
        self.profFuncFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.profFuncFrame.setFrameShape(QFrame.StyledPanel)
        self.profFuncFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.profFuncFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(16)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setContentsMargins(29, 2, 38, 2)
        self.saveBtn = QPushButton(self.profFuncFrame)
        self.saveBtn.setObjectName(u"saveBtn")
        self.saveBtn.setMinimumSize(QSize(0, 30))
        self.saveBtn.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"Montserrat SemiBold")
        font4.setPointSize(9)
        font4.setBold(True)
        font4.setItalic(False)
        font4.setWeight(75)
        self.saveBtn.setFont(font4)
        self.saveBtn.setStyleSheet(u"QPushButton{\n"
"	color: rgb(0,0,0);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(67, 156, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:focus{\n"
"background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}"
"QPushButton:disabled{\n"
"background-color: rgb(222, 222, 222);\n"
"color: rgb(255,255,255);\n"
"border: 2px solid rgb(222, 222, 222)\n"
"}")

        self.gridLayout.addWidget(self.saveBtn, 0, 0, 1, 1)

        self.updateBtn = QPushButton(self.profFuncFrame)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setMinimumSize(QSize(0, 30))
        self.updateBtn.setMaximumSize(QSize(16777215, 30))
        font5 = QFont()
        font5.setFamily(u"Montserrat SemiBold")
        font5.setPointSize(9)
        font5.setBold(True)
        font5.setWeight(75)
        self.updateBtn.setFont(font5)
        self.updateBtn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.updateBtn, 0, 1, 1, 1)

        self.delBtn = QPushButton(self.profFuncFrame)
        self.delBtn.setObjectName(u"delBtn")
        self.delBtn.setMinimumSize(QSize(0, 30))
        self.delBtn.setMaximumSize(QSize(16777215, 30))
        self.delBtn.setFont(font5)
        self.delBtn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.delBtn, 1, 0, 1, 1)

        self.clrEntryBtn = QPushButton(self.profFuncFrame)
        self.clrEntryBtn.setObjectName(u"clrEntryBtn")
        self.clrEntryBtn.setMinimumSize(QSize(0, 30))
        self.clrEntryBtn.setMaximumSize(QSize(16777215, 30))
        self.clrEntryBtn.setFont(font5)
        self.clrEntryBtn.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout.addWidget(self.clrEntryBtn, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.profFuncFrame)


        self.horizontalLayout.addWidget(self.inputProfFrame)

        self.sideFrame = QFrame(profileSection)
        self.sideFrame.setObjectName(u"sideFrame")
        self.sideFrame.setMaximumSize(QSize(0, 16777215))
        self.sideFrame.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(67, 156, 250);\n"
"}")
        self.sideFrame.setFrameShape(QFrame.StyledPanel)
        self.sideFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.sideFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.revealSideBtn = QPushButton(self.sideFrame, clicked = lambda: self.revealSide())
        self.revealSideBtn.setObjectName(u"revealSideBtn")
        self.revealSideBtn.setMaximumSize(QSize(30, 30))
        self.revealSideBtn.setStyleSheet(u"QPushButton{\n"
"border:none;background-color: rgb(67, 156, 250);\n"
"}")
        self.revealSideBtn.setIcon(icon)
        self.revealSideBtn.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.revealSideBtn)

        self.spacerFrame = QFrame(self.sideFrame)
        self.spacerFrame.setObjectName(u"spacerFrame")
        self.spacerFrame.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(67, 156, 250);\n"
"}")
        self.spacerFrame.setFrameShape(QFrame.StyledPanel)
        self.spacerFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.spacerFrame)


        self.horizontalLayout.addWidget(self.sideFrame)

        self.disProfFrame = QFrame(profileSection)
        self.disProfFrame.setObjectName(u"disProfFrame")
        self.disProfFrame.setMinimumSize(QSize(530, 450))
        self.disProfFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(235, 235, 235);\n"
"    border: solid;\n"
"	border-width: 2px 2px 2px 2px;\n"
"	border-color: rgb(26, 194, 161);\n"
"	border-radius: 10px\n"
"}")
        self.disProfFrame.setFrameShape(QFrame.StyledPanel)
        self.disProfFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.disProfFrame)
        self.verticalLayout_2.setSpacing(8)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.topLabelFrame = QFrame(self.disProfFrame)
        self.topLabelFrame.setObjectName(u"topLabelFrame")
        self.topLabelFrame.setStyleSheet(u"QFrame{\n"
"border: none;\n"
"}")
        self.topLabelFrame.setFrameShape(QFrame.StyledPanel)
        self.topLabelFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.topLabelFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.depLabel = QLabel(self.topLabelFrame)
        self.depLabel.setObjectName(u"depLabel")
        font6 = QFont()
        font6.setFamily(u"Montserrat SemiBold")
        font6.setPointSize(18)
        font6.setBold(True)
        font6.setWeight(75)
        self.depLabel.setFont(font6)
        self.depLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"border: none;\n"
"}")

        self.horizontalLayout_3.addWidget(self.depLabel)

        self.syLabel = QLabel(self.topLabelFrame)
        self.syLabel.setObjectName(u"syLabel")
        self.syLabel.setMinimumSize(QSize(160, 0))
        self.syLabel.setMaximumSize(QSize(160, 16777215))
        font7 = QFont()
        font7.setFamily(u"Montserrat")
        font7.setPointSize(11)
        font7.setItalic(True)
        self.syLabel.setFont(font7)
        self.syLabel.setLayoutDirection(Qt.LeftToRight)
        self.syLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.syLabel)


        self.verticalLayout_2.addWidget(self.topLabelFrame)

        self.gradeSectionFrame = QFrame(self.disProfFrame)
        self.gradeSectionFrame.setObjectName(u"gradeSectionFrame")
        self.gradeSectionFrame.setMinimumSize(QSize(0, 40))
        self.gradeSectionFrame.setMaximumSize(QSize(16777215, 40))
        self.gradeSectionFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.gradeSectionFrame.setFrameShape(QFrame.StyledPanel)
        self.gradeSectionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.gradeSectionFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, 0)
        self.gradeSectionLabel = QLabel(self.gradeSectionFrame)
        self.gradeSectionLabel.setObjectName(u"gradeSectionLabel")
        self.gradeSectionLabel.setMinimumSize(QSize(0, 40))
        self.gradeSectionLabel.setMaximumSize(QSize(16777215, 40))
        font8 = QFont()
        font8.setFamily(u"Kaleko 205 Round Bold Oblique")
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setItalic(False)
        font8.setWeight(75)
        self.gradeSectionLabel.setFont(font8)
        self.gradeSectionLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.gradeSectionLabel)

        self.strandLabel = QLabel(self.gradeSectionFrame)
        self.strandLabel.setObjectName(u"strandLabel")
        font9 = QFont()
        font9.setFamily(u"Verdana")
        font9.setPointSize(10)
        font9.setItalic(True)
        self.strandLabel.setFont(font9)

        self.horizontalLayout_4.addWidget(self.strandLabel)


        self.verticalLayout_2.addWidget(self.gradeSectionFrame)

        self.adviserFrame = QFrame(self.disProfFrame)
        self.adviserFrame.setObjectName(u"adviserFrame")
        self.adviserFrame.setMinimumSize(QSize(0, 30))
        self.adviserFrame.setMaximumSize(QSize(16777215, 30))
        self.adviserFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border: none;\n"
"}")
        self.adviserFrame.setFrameShape(QFrame.StyledPanel)
        self.adviserFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.adviserFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.adviserLabel = QLabel(self.adviserFrame)
        self.adviserLabel.setObjectName(u"adviserLabel")
        font10 = QFont()
        font10.setFamily(u"Montserrat")
        font10.setPointSize(11)
        self.adviserLabel.setFont(font10)

        self.horizontalLayout_5.addWidget(self.adviserLabel)

        self.semLabel = QLabel(self.adviserFrame)
        self.semLabel.setObjectName(u"semLabel")
        font11 = QFont()
        font11.setFamily(u"Montserrat")
        font11.setPointSize(11)
        font11.setBold(True)
        font11.setWeight(75)
        self.semLabel.setFont(font11)
        self.semLabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")

        self.horizontalLayout_5.addWidget(self.semLabel)


        self.verticalLayout_2.addWidget(self.adviserFrame)

        self.statFrame = QFrame(self.disProfFrame)
        self.statFrame.setObjectName(u"statFrame")
        self.statFrame.setMinimumSize(QSize(0, 30))
        self.statFrame.setMaximumSize(QSize(16777215, 30))
        self.statFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(26, 194, 161);\n"
"	border: none;\n"
"}")
        self.statFrame.setFrameShape(QFrame.StyledPanel)
        self.statFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.statFrame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(19, 0, 0, 0)
        self.maleLabel = QLabel(self.statFrame)
        self.maleLabel.setObjectName(u"maleLabel")
        font12 = QFont()
        font12.setFamily(u"Montserrat")
        font12.setPointSize(10)
        font12.setBold(True)
        font12.setWeight(75)
        self.maleLabel.setFont(font12)
        self.maleLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.maleLabel)

        self.femaleLabel = QLabel(self.statFrame)
        self.femaleLabel.setObjectName(u"femaleLabel")
        self.femaleLabel.setFont(font12)
        self.femaleLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.femaleLabel)

        self.totalLabel = QLabel(self.statFrame)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setFont(font12)
        self.totalLabel.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.horizontalLayout_6.addWidget(self.totalLabel)


        self.verticalLayout_2.addWidget(self.statFrame)

        self.tableWidget = QTableWidget(self.disProfFrame)
        if (self.tableWidget.columnCount() < 15):
            self.tableWidget.setColumnCount(15)
        brush = QBrush(QColor(0, 0, 2, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font2);
        __qtablewidgetitem.setForeground(brush);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        brush1 = QBrush(QColor(26, 194, 161, 255))
        brush1.setStyle(Qt.SolidPattern)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font12);
        __qtablewidgetitem1.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font12);
        __qtablewidgetitem2.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font12);
        __qtablewidgetitem3.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font12);
        __qtablewidgetitem4.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font12);
        __qtablewidgetitem5.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem6.setFont(font12);
        __qtablewidgetitem6.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem7.setFont(font12);
        __qtablewidgetitem7.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem8.setFont(font12);
        __qtablewidgetitem8.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem9.setFont(font12);
        __qtablewidgetitem9.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem10.setFont(font12);
        __qtablewidgetitem10.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem11.setFont(font12);
        __qtablewidgetitem11.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem12.setFont(font12);
        __qtablewidgetitem12.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem13.setFont(font12);
        __qtablewidgetitem13.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem14.setFont(font12);
        __qtablewidgetitem14.setForeground(brush1);
        self.tableWidget.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        self.tableWidget.setObjectName(u"tableWidget")
        font13 = QFont()
        font13.setFamily(u"Verdana")
        font13.setPointSize(9)
        self.tableWidget.setFont(font13)
        self.tableWidget.setStyleSheet(u"QTableWidget{border: none;\n"
"background-color: rgb(255, 255, 255);}\n"
"QFrame{background-color:  rgb(255, 255, 255);\n"	
"    border: none;}\n"
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
        self.tableWidget.setFrameShape(QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)

        ###########========================= SET SPECIFIC HEADER COLUMN WIDTH ======================================###############################

        self.tableWidget.setColumnWidth(0, 30)    ###### No.
        self.tableWidget.setColumnWidth(2, 220)    ###### Last Name
        self.tableWidget.setColumnWidth(3, 220)    ###### First Name
        self.tableWidget.setColumnWidth(4, 220)    ###### Middle Name
        self.tableWidget.setColumnWidth(5, 150)    #### Name Ext
        self.tableWidget.setColumnWidth(6, 100)
        self.tableWidget.setColumnWidth(7, 70)
        self.tableWidget.setColumnWidth(8, 300)
        self.tableWidget.setColumnWidth(9, 230)
        self.tableWidget.setColumnWidth(10, 260)
        self.tableWidget.setColumnWidth(11, 260)
        self.tableWidget.setColumnWidth(12, 260)
        self.tableWidget.setColumnWidth(13, 260)
        self.tableWidget.setColumnWidth(14, 260)

        ################ SET table Header Height ####################################
        self.header = self.tableWidget.horizontalHeader()
        self.header.setFixedHeight(60)
        self.header.setStyleSheet("QHeaderView{ border-bottom: 1px solid rgb(222, 222, 222); }")

        self.verticalLayout_2.addWidget(self.tableWidget)

        self.horizontalLayout.addWidget(self.disProfFrame)

        self.retranslateUi(profileSection)

        QMetaObject.connectSlotsByName(profileSection)
    # setupUi

        self.tableWidget.cellClicked.connect(lambda: self.clickedTable())   ####### Signal for clicking cell in table widget ##################

    def clickedTable(self):

        myClass = classDataBase.viewDataclass()
        global classData
        classData = myClass[0]
        try:
            learner = profileDataBase.viewstudentData()
            global select_list
            select_list = []
            for item in self.tableWidget.selectedItems():
                select_list.append(item.text())

            self.lrn_entry.setText(select_list[1])      ################### INSERTING SELECTED DATA FROM TABLE WIDGET TO ENTRIES ##################
            self.l_nameEntry.setText(select_list[2])
            self.f_nameEntry.setText(select_list[3])
            self.m_nameEntry.setText(select_list[4])
            self.n_ExtEntry.setText(select_list[5])
            self.sexComboBox.setCurrentText(select_list[6])
            self.ageEntry.setText(select_list[7])

            self.revAddress = select_list[8] 
            self.splitAddress = self.revAddress.rsplit(", ",2)   # ------------------------- splitting address into brgy., town and province ---------------------

            self.brgyEntry.setText(self.splitAddress[0])
            self.munEntry.setText(self.splitAddress[1])
            self.provEntry.setText(self.splitAddress[2])

            self.revdob_all = select_list[9]
            self.splitdob = self.revdob_all.rsplit(" ",2)  #------------------------------ splitting date of birth into Month, Date and Year --------------------
            self.add = self.splitdob[0]

            self.monthCombo.setCurrentText(self.add.capitalize())
            self.dateEntry.setText(self.splitdob[1])
            self.yearEntry.setText(self.splitdob[2])

            self.motherEntry.setText(select_list[10])
            self.fatherEntry.setText(select_list[11])
            self.guardianEntry.setText(select_list[12])
            self.modalCombo.setCurrentText(select_list[13])
            self.eligCombo.setCurrentText(select_list[14])

            self.saveBtn.setEnabled(False)

        except:
            print("No available List")

############################################### FUNCTIONS ###########################################################

    def hideSide(self):
        self.inputProfFrame.setMaximumSize(QSize(0, 16777215))  ############ toggle(hide) input Frame ###################
        self.sideFrame.setMaximumSize(QSize(33, 16777215))

    def revealSide(self):
        self.inputProfFrame.setMaximumSize(QSize(400, 16777215))  ############ toggle(reveal) input Frame ###################
        self.sideFrame.setMaximumSize(QSize(0, 16777215))

    def showLearner(self):

        myClass = classDataBase.viewDataclass()
        if len(myClass) != 0:
            learner = profileDataBase.viewstudentData()

            self.munEntry.setText("LIBMANAN")
            self.provEntry.setText("CAMARINES SUR")

            if len(learner) != 0:                   ######## Add database file to tableWidget if it is not empty #########
                self.tableWidget.setRowCount(0)       ############# erase tableWidget content ###################
                for i, row in enumerate(learner):
                    self.rowcount = self.tableWidget.rowCount() 
                    self.tableWidget.insertRow(self.rowcount)    ########### Adding Row to table ############

                    for column, val in enumerate(row):   
                        self.tableWidget.setItem(i, column, QTableWidgetItem(str(val)))  ########### Adding Learner's data to tableWidget row ############

            self.genderStat()
        else:
            print("No learner to show")

    def updateProfile(self, disJHS, disSHS, disAttOV, message, msgIcon):

        try:
            addressAll = self.brgyEntry.text() + ', ' + self.munEntry.text() + ', ' + self.provEntry.text()
            dob = self.monthCombo.currentText() + ' ' + self.dateEntry.text() + ' ' +  self.yearEntry.text()
            lastName = self.l_nameEntry.text()
            firstName = self.f_nameEntry.text()
            middleName = self.m_nameEntry.text()
            mother = self.motherEntry.text()
            father = self.fatherEntry.text()
            guardian = self.guardianEntry.text()

            if middleName == "":
                middleInitial = ""
            else:
                middleInitial = middleName[0].upper()

            name = str(f"{lastName.upper()}, {firstName.upper()} {middleInitial}. {self.n_ExtEntry.text()}")

            profileDataBase.updateStdRec(self.lrn_entry.text(),lastName.upper(),firstName.upper(),middleName.upper(),self.n_ExtEntry.text(),\
                    self.sexComboBox.currentText(), self.ageEntry.text(), addressAll.upper(),dob.upper(),mother.upper(),father.upper(),\
                    guardian.upper(), self.modalCombo.currentText(), self.eligCombo.currentText(), select_list[0])

            self.showLearner()

            if classData[1] == "JUNIOR HIGH SCHOOL":
                gradesJHSDataBase.updNameLRNjhs(name, self.lrn_entry.text(), self.sexComboBox.currentText(), self.ageEntry.text(), select_list[0])
                disJHS()
            else:
                gradesSHSDataBase1.updNameLRNsem1(name, self.lrn_entry.text(), self.sexComboBox.currentText(), self.ageEntry.text(), select_list[0])
                gradesSHSDataBase2.updNameLRNsem2(name, self.lrn_entry.text(), self.sexComboBox.currentText(), self.ageEntry.text(), select_list[0])
                disSHS()

            ovDataBase.updNameLRNAov(name, self.lrn_entry.text(), select_list[0])  ###### update observed values name and LRN ############
            attDataBase.updNameLRNAtt(name, self.lrn_entry.text(), select_list[0]) ###### update attendance name and LRN ############
            disAttOV()
            self.clearEntry()
            message("Update Info","Profile has been successfully updated", msgIcon)
            
        except:
            message("Info","No learner selected", msgIcon)

    def delProfile(self, disJHS, disSHS, disAttOV, message, msgIcon):
        try:
            profileDataBase.deleteStdRec(select_list[0])
            self.showLearner()

            if classData[1] == "JUNIOR HIGH SCHOOL":
                gradesJHSDataBase.deleteGradeJHS(select_list[0])
                disJHS()
            else:
                gradesSHSDataBase1.deleteGradesem1(select_list[0])
                gradesSHSDataBase2.deleteGradesem2(select_list[0])
                disSHS()

            ovDataBase.delete_values(select_list[0])
            attDataBase.delete_att(select_list[0])
            disAttOV()
            self.clearEntry()
            message("Delete learner","Learner has been deleted", msgIcon)
            
        except:
            message("Info","No learner selected", msgIcon)

    def genderStat(self):

        learner = profileDataBase.viewstudentData()
        self.maleCount = 0
        self.femaleCount = 0
        self.totalCount = 0
        for gender in learner:
            if gender[6] == "MALE":
                self.maleCount+=1
            elif gender[6] == "FEMALE":
                self.femaleCount+=1
            else:
                pass
        self.totalCount = self.maleCount + self.femaleCount
  
        self.maleLabel.setText(f'Male: {self.maleCount}')
        self.femaleLabel.setText(f'Female: {self.femaleCount}')
        self.totalLabel.setText(f'Total: {self.totalCount}')

    def clearEntry(self):               ########### Clear entries Function #######################
        global select_list
        self.lrn_entry.setText("")
        self.l_nameEntry.setText("")
        self.f_nameEntry.setText("")
        self.m_nameEntry.setText("")
        self.n_ExtEntry.setText("")
        self.ageEntry.setText("")
        self.provEntry.setText("")
        self.dateEntry.setText("")
        self.yearEntry.setText("")
        self.motherEntry.setText("")
        self.fatherEntry.setText("")
        self.guardianEntry.setText("")
        self.tableWidget.clearSelection()
        select_list = []
        self.saveBtn.setEnabled(True)

############################################################################################################################

    def retranslateUi(self, profileSection):
        profileSection.setWindowTitle(QCoreApplication.translate("profileSection", u"Frame", None))
        self.input_label.setText(QCoreApplication.translate("profileSection", u"Add/Edit Learner's Information here", None))
        self.hideSideBtn.setText("")
        self.lrn_label.setText(QCoreApplication.translate("profileSection", u"LRN:", None))
        self.l_nameLabel.setText(QCoreApplication.translate("profileSection", u"Last Name:", None))
        self.f_nameLabel.setText(QCoreApplication.translate("profileSection", u"First Name:", None))
        self.m_nameLabel.setText(QCoreApplication.translate("profileSection", u"Middle Name:", None))
        self.n_ExtLabel.setText(QCoreApplication.translate("profileSection", u"Name Ext.:", None))
        self.sexLabel.setText(QCoreApplication.translate("profileSection", u"Sex:", None))
        self.ageLabel.setText(QCoreApplication.translate("profileSection", u"Age:", None))
        self.brgyLabel.setText(QCoreApplication.translate("profileSection", u"Barangay:", None))
        self.munLabel.setText(QCoreApplication.translate("profileSection", u"Municipality:", None))
        self.provLabel.setText(QCoreApplication.translate("profileSection", u"Province:", None))
        self.addressLabel.setText(QCoreApplication.translate("profileSection", u"Address:", None))
        self.dobLabel.setText(QCoreApplication.translate("profileSection", u"Date of Birth:", None))
        self.monthLabel.setText(QCoreApplication.translate("profileSection", u"Month:", None))
        self.dateLabel.setText(QCoreApplication.translate("profileSection", u"Date:", None))
        self.yearLabel.setText(QCoreApplication.translate("profileSection", u"Year:", None))
        self.motherLabel.setText(QCoreApplication.translate("profileSection", u"Mother's Maiden Name:", None))
        self.fatherLabel.setText(QCoreApplication.translate("profileSection", u"Father's Name:", None))
        self.guardianLabel.setText(QCoreApplication.translate("profileSection", u"Name of Guardian:", None))
        self.modalLabel.setText(QCoreApplication.translate("profileSection", u"Learning Modality:", None))
        self.eligLabel.setText(QCoreApplication.translate("profileSection", u"Enrollment Eligibility:", None))
        self.saveBtn.setText(QCoreApplication.translate("profileSection", u"Add Learner", None))
        self.updateBtn.setText(QCoreApplication.translate("profileSection", u"Update Info", None))
        self.delBtn.setText(QCoreApplication.translate("profileSection", u"Delete Learner", None))
        self.clrEntryBtn.setText(QCoreApplication.translate("profileSection", u"Clear Entry", None))
        self.revealSideBtn.setText("")
        self.depLabel.setText(QCoreApplication.translate("profileSection", u"<DEPARTMENT>", None))
        self.syLabel.setText(QCoreApplication.translate("profileSection", u"School Year", None))
        self.gradeSectionLabel.setText(QCoreApplication.translate("profileSection", u" Grade & Section", None))
        self.strandLabel.setText(QCoreApplication.translate("profileSection", u"", None))
        self.adviserLabel.setText(QCoreApplication.translate("profileSection", u" Adviser", None))
        self.semLabel.setText(QCoreApplication.translate("profileSection", u"", None))
        self.maleLabel.setText(QCoreApplication.translate("profileSection", u"Male: 0", None))
        self.femaleLabel.setText(QCoreApplication.translate("profileSection", u"Female: 0", None))
        self.totalLabel.setText(QCoreApplication.translate("profileSection", u"Total: 0", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("profileSection", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("profileSection", u"LRN", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("profileSection", u"LAST NAME", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("profileSection", u"FIRST NAME", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("profileSection", u"MIDDLE NAME", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("profileSection", u"NAME EXT.", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("profileSection", u"SEX", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("profileSection", u"AGE", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("profileSection", u"ADDRESS", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("profileSection", u"DATE OF BIRTH", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("profileSection", u"MOTHER'S MAIDEN NAME", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("profileSection", u"FATHER'S NAME", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("profileSection", u"NAME OF GUARDIAN", None));
        ___qtablewidgetitem13 = self.tableWidget.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("profileSection", u"LEARNING MODALITY", None));
        ___qtablewidgetitem14 = self.tableWidget.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("profileSection", u"ENROLLMENT ELIGIBILITY", None));
    # retranslateUi

