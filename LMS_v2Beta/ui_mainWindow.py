# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainWindowwPellY.ui'
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

from ui_profile import Ui_profileSection
from ui_home import Ui_homeMainFrame
from ui_gradesJHS import Ui_gradesJHSsection
from ui_gradesSHS import Ui_gradesSHSsection
from ui_attendanceOb import Ui_attendanceOVFrame

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1064, 728)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.modernLayout = QVBoxLayout(self.centralwidget)
        self.modernLayout.setSpacing(0)
        self.modernLayout.setObjectName(u"modernLayout")
        self.modernLayout.setContentsMargins(10, 10, 10, 10)
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.mainFrame.setFrameShape(QFrame.NoFrame)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titleBar = QFrame(self.mainFrame)
        self.titleBar.setObjectName(u"titleBar")
        self.titleBar.setMaximumSize(QSize(16777215, 60))
        self.titleBar.setSizeIncrement(QSize(0, 0))
        self.titleBar.setStyleSheet(u"background-color: rgb(26, 194, 161);")
        self.titleBar.setFrameShape(QFrame.NoFrame)
        self.titleBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titleBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_InputFrame = QFrame(self.titleBar)
        self.title_InputFrame.setObjectName(u"title_InputFrame")
        self.title_InputFrame.setFrameShape(QFrame.StyledPanel)
        self.title_InputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.title_InputFrame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 0, 0, 0)
        self.app_label = QLabel(self.title_InputFrame)
        self.app_label.setObjectName(u"app_label")
        font = QFont()
        font.setFamily(u"Montserrat")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.app_label.setFont(font)
        self.app_label.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_2.addWidget(self.app_label)


        self.horizontalLayout.addWidget(self.title_InputFrame)

        self.frame_btns = QFrame(self.titleBar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(200, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minBtn = QPushButton(self.frame_btns)
        self.minBtn.setObjectName(u"minBtn")
        self.minBtn.setMaximumSize(QSize(50, 50))
        self.minBtn.setToolTipDuration(0)
        self.minBtn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u"icons/min.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minBtn.setIcon(icon)
        self.minBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minBtn)

        self.maxBtn = QPushButton(self.frame_btns)
        self.maxBtn.setObjectName(u"maxBtn")
        self.maxBtn.setMaximumSize(QSize(50, 50))
        self.maxBtn.setToolTipDuration(0)
        self.maxBtn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u"icons/max.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maxBtn.setIcon(icon1)
        self.maxBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maxBtn)

        self.closeBtn = QPushButton(self.frame_btns)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setMaximumSize(QSize(50, 50))
        self.closeBtn.setToolTipDuration(0)
        self.closeBtn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u"icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon2)
        self.closeBtn.setIconSize(QSize(20, 20))
        self.closeBtn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.closeBtn)


        self.horizontalLayout.addWidget(self.frame_btns)


        self.verticalLayout.addWidget(self.titleBar)

        self.contentFrame = QFrame(self.mainFrame)
        self.contentFrame.setObjectName(u"contentFrame")
        self.contentFrame.setStyleSheet(u"QFrame{\n"
"border-radius: 0px;\n"
"\n"
"}")
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.contentFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_8 = QVBoxLayout(self.home)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.homeTitleFrame = QFrame(self.home)
        self.homeTitleFrame.setObjectName(u"homeTitleFrame")
        self.homeTitleFrame.setMinimumSize(QSize(0, 60))
        self.homeTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.homeTitleFrame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 255, 225, 255), stop:1 rgba(213, 236, 255, 255));\n"
"}")
        self.homeTitleFrame.setFrameShape(QFrame.NoFrame)
        self.homeTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.homeTitleFrame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.hhomeicon = QLabel(self.homeTitleFrame)
        self.hhomeicon.setObjectName(u"hhomeicon")
        self.hhomeicon.setMaximumSize(QSize(60, 16777215))
        self.hhomeicon.setStyleSheet(u"QLabel{\n"
"	background-color: none;\n"
"}")
        self.hhomeicon.setPixmap(QPixmap(u"icons/homeGreen.png"))
        self.hhomeicon.setScaledContents(True)
        self.hhomeicon.setMargin(8)

        self.horizontalLayout_5.addWidget(self.hhomeicon)

        self.homelabel = QLabel(self.homeTitleFrame)
        self.homelabel.setObjectName(u"homelabel")
        font1 = QFont()
        font1.setFamily(u"Montserrat")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(75)
        self.homelabel.setFont(font1)
        self.homelabel.setAutoFillBackground(False)
        self.homelabel.setStyleSheet(u"QLabel{\n"
"color: rgb(26, 194, 161);\n"
"}")
        self.homelabel.setFrameShape(QFrame.NoFrame)
        self.homelabel.setFrameShadow(QFrame.Plain)
        self.homelabel.setLineWidth(0)

        self.horizontalLayout_5.addWidget(self.homelabel)


        self.verticalLayout_8.addWidget(self.homeTitleFrame)

        self.homeMainFrame = QFrame(self.home)
        self.homeMainFrame.setObjectName(u"homeMainFrame")
        self.homeMainFrame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(234, 234, 234);\n"
"}")
        self.homeMainFrame.setFrameShape(QFrame.StyledPanel)
        self.homeMainFrame.setFrameShadow(QFrame.Raised)

        self.homeSection = Ui_homeMainFrame()                   ############## Home Section UI ##################
        self.homeSection.setupUi(self.homeMainFrame)

        self.verticalLayout_8.addWidget(self.homeMainFrame)

        self.stackedWidget.addWidget(self.home)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_7 = QVBoxLayout(self.profilePage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.profTitleFrame = QFrame(self.profilePage)
        self.profTitleFrame.setObjectName(u"profTitleFrame")
        self.profTitleFrame.setMinimumSize(QSize(0, 60))
        self.profTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.profTitleFrame.setStyleSheet(u"QFrame{\n"
"border: solid;\n"
"border-width: 0px 0px 1px 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.profTitleFrame.setFrameShape(QFrame.NoFrame)
        self.profTitleFrame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_6 = QHBoxLayout(self.profTitleFrame)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 8, 0)
        self.profIcon = QLabel(self.profTitleFrame)
        self.profIcon.setObjectName(u"profIcon")
        self.profIcon.setMinimumSize(QSize(60, 0))
        self.profIcon.setMaximumSize(QSize(60, 16777215))
        self.profIcon.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}")
        self.profIcon.setLineWidth(0)
        self.profIcon.setPixmap(QPixmap(u"icons/profBlue.png"))
        self.profIcon.setScaledContents(True)
        self.profIcon.setMargin(7)

        self.horizontalLayout_6.addWidget(self.profIcon)

        self.profLabel = QLabel(self.profTitleFrame)
        self.profLabel.setObjectName(u"profLabel")
        font2 = QFont()
        font2.setFamily(u"Montserrat")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.profLabel.setFont(font2)
        self.profLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.horizontalLayout_6.addWidget(self.profLabel)

        self.homeBtnProf = QPushButton(self.profTitleFrame)
        self.homeBtnProf.setObjectName(u"homeBtnProf")
        self.homeBtnProf.setMaximumSize(QSize(120, 30))
        font3 = QFont()
        font3.setFamily(u"Montserrat")
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setWeight(75)
        self.homeBtnProf.setFont(font3)
        self.homeBtnProf.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u"icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtnProf.setIcon(icon3)
        self.homeBtnProf.setIconSize(QSize(22, 22))

        self.horizontalLayout_6.addWidget(self.homeBtnProf)

        self.gradesBtnProf = QPushButton(self.profTitleFrame)
        self.gradesBtnProf.setObjectName(u"gradesBtnProf")
        self.gradesBtnProf.setMaximumSize(QSize(130, 30))
        self.gradesBtnProf.setFont(font3)
        self.gradesBtnProf.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_6.addWidget(self.gradesBtnProf)


        self.verticalLayout_7.addWidget(self.profTitleFrame)

        self.profMainFrame = QFrame(self.profilePage)
        self.profMainFrame.setObjectName(u"profMainFrame")
        self.profMainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.profMainFrame.setFrameShape(QFrame.NoFrame)
        self.profMainFrame.setFrameShadow(QFrame.Sunken)
        self.profMainFrame.setLineWidth(1)
        self.profMainFrame.setMidLineWidth(0)

        self.profSection = Ui_profileSection()                   ############## Profile Section UI ##################
        self.profSection.setupUi(self.profMainFrame)

        self.verticalLayout_7.addWidget(self.profMainFrame)

        self.stackedWidget.addWidget(self.profilePage)
        self.gradeJHSPage = QWidget()
        self.gradeJHSPage.setObjectName(u"gradeJHSPage")
        self.verticalLayout_6 = QVBoxLayout(self.gradeJHSPage)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gJHSTitleFrame = QFrame(self.gradeJHSPage)
        self.gJHSTitleFrame.setObjectName(u"gJHSTitleFrame")
        self.gJHSTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.gJHSTitleFrame.setStyleSheet(u"QFrame{\n"
"border: solid;\n"
"border-width: 0px 0px 1px 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.gJHSTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.gJHSTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.gJHSTitleFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 8, 0)
        self.grdJHSIcon = QLabel(self.gJHSTitleFrame)
        self.grdJHSIcon.setObjectName(u"grdJHSIcon")
        self.grdJHSIcon.setMinimumSize(QSize(60, 0))
        self.grdJHSIcon.setMaximumSize(QSize(60, 16777215))
        self.grdJHSIcon.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}")
        self.grdJHSIcon.setPixmap(QPixmap(u"icons/gradesBlue.png"))
        self.grdJHSIcon.setScaledContents(True)
        self.grdJHSIcon.setMargin(9)

        self.horizontalLayout_7.addWidget(self.grdJHSIcon)

        self.gradesJHSLabel = QLabel(self.gJHSTitleFrame)
        self.gradesJHSLabel.setObjectName(u"gradesJHSLabel")
        self.gradesJHSLabel.setFont(font2)
        self.gradesJHSLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.horizontalLayout_7.addWidget(self.gradesJHSLabel)

        self.homeBtnJHS = QPushButton(self.gJHSTitleFrame)
        self.homeBtnJHS.setObjectName(u"homeBtnJHS")
        self.homeBtnJHS.setMaximumSize(QSize(120, 30))
        self.homeBtnJHS.setFont(font3)
        self.homeBtnJHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")
        self.homeBtnJHS.setIcon(icon3)
        self.homeBtnJHS.setIconSize(QSize(22, 22))

        self.horizontalLayout_7.addWidget(self.homeBtnJHS)

        self.prevBtnJHS = QPushButton(self.gJHSTitleFrame)
        self.prevBtnJHS.setObjectName(u"prevBtnJHS")
        self.prevBtnJHS.setMaximumSize(QSize(130, 30))
        self.prevBtnJHS.setFont(font3)
        self.prevBtnJHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_7.addWidget(self.prevBtnJHS)

        self.attendBtnJHS = QPushButton(self.gJHSTitleFrame)
        self.attendBtnJHS.setObjectName(u"attendBtnJHS")
        self.attendBtnJHS.setMaximumSize(QSize(130, 30))
        self.attendBtnJHS.setFont(font3)
        self.attendBtnJHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_7.addWidget(self.attendBtnJHS)


        self.verticalLayout_6.addWidget(self.gJHSTitleFrame)

        self.gJHSMainFrame = QFrame(self.gradeJHSPage)
        self.gJHSMainFrame.setObjectName(u"gJHSMainFrame")
        self.gJHSMainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.gJHSMainFrame.setFrameShape(QFrame.StyledPanel)
        self.gJHSMainFrame.setFrameShadow(QFrame.Raised)

        self.gJHSSection = Ui_gradesJHSsection()                   ############## grades JHS Section UI ##################
        self.gJHSSection.setupUi(self.gJHSMainFrame)

        self.verticalLayout_6.addWidget(self.gJHSMainFrame)

        self.stackedWidget.addWidget(self.gradeJHSPage)
        self.gradeSHSPage = QWidget()
        self.gradeSHSPage.setObjectName(u"gradeSHSPage")
        self.verticalLayout_5 = QVBoxLayout(self.gradeSHSPage)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gSHSTitleFrame = QFrame(self.gradeSHSPage)
        self.gSHSTitleFrame.setObjectName(u"gSHSTitleFrame")
        self.gSHSTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.gSHSTitleFrame.setStyleSheet(u"QFrame{\n"
"border: solid;\n"
"border-width: 0px 0px 1px 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.gSHSTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.gSHSTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.gSHSTitleFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 8, 0)
        self.grdSHSIcon = QLabel(self.gSHSTitleFrame)
        self.grdSHSIcon.setObjectName(u"grdSHSIcon")
        self.grdSHSIcon.setMinimumSize(QSize(60, 0))
        self.grdSHSIcon.setMaximumSize(QSize(60, 16777215))
        self.grdSHSIcon.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}")
        self.grdSHSIcon.setPixmap(QPixmap(u"icons/gradesBlue.png"))
        self.grdSHSIcon.setScaledContents(True)
        self.grdSHSIcon.setMargin(9)

        self.horizontalLayout_8.addWidget(self.grdSHSIcon)

        self.gradesSHSLabel = QLabel(self.gSHSTitleFrame)
        self.gradesSHSLabel.setObjectName(u"gradesSHSLabel")
        self.gradesSHSLabel.setFont(font2)
        self.gradesSHSLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.horizontalLayout_8.addWidget(self.gradesSHSLabel)

        self.homeBtnSHS = QPushButton(self.gSHSTitleFrame)
        self.homeBtnSHS.setObjectName(u"homeBtnSHS")
        self.homeBtnSHS.setMaximumSize(QSize(120, 30))
        self.homeBtnSHS.setFont(font3)
        self.homeBtnSHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")
        self.homeBtnSHS.setIcon(icon3)
        self.homeBtnSHS.setIconSize(QSize(22, 22))

        self.horizontalLayout_8.addWidget(self.homeBtnSHS)

        self.prevBtnSHS = QPushButton(self.gSHSTitleFrame)
        self.prevBtnSHS.setObjectName(u"prevBtnSHS")
        self.prevBtnSHS.setMaximumSize(QSize(130, 30))
        self.prevBtnSHS.setFont(font3)
        self.prevBtnSHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_8.addWidget(self.prevBtnSHS)

        self.attendBtnSHS = QPushButton(self.gSHSTitleFrame)
        self.attendBtnSHS.setObjectName(u"attendBtnSHS")
        self.attendBtnSHS.setMaximumSize(QSize(130, 30))
        self.attendBtnSHS.setFont(font3)
        self.attendBtnSHS.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_8.addWidget(self.attendBtnSHS)


        self.verticalLayout_5.addWidget(self.gSHSTitleFrame)

        self.gSHSMainFrame = QFrame(self.gradeSHSPage)
        self.gSHSMainFrame.setObjectName(u"gSHSMainFrame")
        self.gSHSMainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.gSHSSection = Ui_gradesSHSsection()                   ############## grades SHS Section UI ##################
        self.gSHSSection.setupUi(self.gSHSMainFrame)

        self.gSHSMainFrame.setFrameShape(QFrame.StyledPanel)
        self.gSHSMainFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.gSHSMainFrame)

        self.stackedWidget.addWidget(self.gradeSHSPage)
        self.attendPage = QWidget()
        self.attendPage.setObjectName(u"attendPage")
        self.verticalLayout_4 = QVBoxLayout(self.attendPage)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.attendTitleFrame = QFrame(self.attendPage)
        self.attendTitleFrame.setObjectName(u"attendTitleFrame")
        self.attendTitleFrame.setMaximumSize(QSize(16777215, 60))
        self.attendTitleFrame.setStyleSheet(u"QFrame{\n"
"border: solid;\n"
"border-width: 0px 0px 1px 0px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.attendTitleFrame.setFrameShape(QFrame.StyledPanel)
        self.attendTitleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.attendTitleFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 8, 0)
        self.attIcon = QLabel(self.attendTitleFrame)
        self.attIcon.setObjectName(u"attIcon")
        self.attIcon.setMinimumSize(QSize(60, 0))
        self.attIcon.setMaximumSize(QSize(60, 16777215))
        self.attIcon.setStyleSheet(u"QLabel{\n"
"background-color: rgb(255, 255, 255);\n"
"border: none;\n"
"}")
        self.attIcon.setPixmap(QPixmap(u"icons/attBlue.png"))
        self.attIcon.setScaledContents(True)
        self.attIcon.setMargin(9)

        self.horizontalLayout_9.addWidget(self.attIcon)

        self.attendLabel = QLabel(self.attendTitleFrame)
        self.attendLabel.setObjectName(u"attendLabel")
        self.attendLabel.setFont(font2)
        self.attendLabel.setStyleSheet(u"QLabel{\n"
"border: none;\n"
"	color: rgb(67, 156, 250);\n"
"}")

        self.horizontalLayout_9.addWidget(self.attendLabel)

        self.homeBtnAttend = QPushButton(self.attendTitleFrame)
        self.homeBtnAttend.setObjectName(u"homeBtnAttend")
        self.homeBtnAttend.setMaximumSize(QSize(120, 30))
        self.homeBtnAttend.setFont(font3)
        self.homeBtnAttend.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")
        self.homeBtnAttend.setIcon(icon3)
        self.homeBtnAttend.setIconSize(QSize(22, 22))

        self.horizontalLayout_9.addWidget(self.homeBtnAttend)

        self.prevBtnAttend = QPushButton(self.attendTitleFrame)
        self.prevBtnAttend.setObjectName(u"prevBtnAttend")
        self.prevBtnAttend.setMaximumSize(QSize(130, 30))
        self.prevBtnAttend.setFont(font3)
        self.prevBtnAttend.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(67, 156, 250);\n"
"	color: rgb(255, 255, 255);\n"
" 	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:focus{\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(67, 156, 250);\n"
"border-radius: 10px;\n"
"border: 2px solid rgb(67, 156, 250)\n"
"}")

        self.horizontalLayout_9.addWidget(self.prevBtnAttend)


        self.verticalLayout_4.addWidget(self.attendTitleFrame)

        self.attendMainFrame = QFrame(self.attendPage)
        self.attendMainFrame.setObjectName(u"attendMainFrame")
        self.attendMainFrame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(234, 234, 234);\n"
"}")
        self.attOVSection = Ui_attendanceOVFrame()                   ############## Attendance Observed Values UI ##################
        self.attOVSection.setupUi(self.attendMainFrame)

        self.attendMainFrame.setFrameShape(QFrame.StyledPanel)
        self.attendMainFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_4.addWidget(self.attendMainFrame)

        self.stackedWidget.addWidget(self.attendPage)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.creditFrame = QFrame(self.contentFrame)
        self.creditFrame.setObjectName(u"creditFrame")
        self.creditFrame.setMinimumSize(QSize(0, 25))
        self.creditFrame.setMaximumSize(QSize(16777215, 25))
        self.creditFrame.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(187, 255, 225, 255), stop:1 rgba(213, 236, 255, 255));\n"
"}")
        self.creditFrame.setFrameShape(QFrame.NoFrame)
        self.creditFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.creditFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 0)
        self.author = QLabel(self.creditFrame)
        self.author.setObjectName(u"author")
        font4 = QFont()
        font4.setFamily(u"Montserrat Medium")
        font4.setPointSize(7)
        font4.setItalic(True)
        self.author.setFont(font4)

        self.horizontalLayout_3.addWidget(self.author)

        self.version = QLabel(self.creditFrame)
        self.version.setObjectName(u"version")
        self.version.setFont(font4)

        self.horizontalLayout_3.addWidget(self.version)

        self.gripFrame = QFrame(self.creditFrame)
        self.gripFrame.setObjectName(u"gripFrame")
        self.gripFrame.setMinimumSize(QSize(25, 0))
        self.gripFrame.setMaximumSize(QSize(25, 16777215))
        self.gripFrame.setFrameShape(QFrame.NoFrame)
        self.gripFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.gripFrame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.gripFrame)


        self.verticalLayout_3.addWidget(self.creditFrame)


        self.verticalLayout.addWidget(self.contentFrame)


        self.modernLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_label.setText(QCoreApplication.translate("MainWindow", u"LEARNER MANAGEMENT SYSTEM ", None))
#if QT_CONFIG(tooltip)
        self.minBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maxBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.hhomeicon.setText("")
        self.homelabel.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profIcon.setText("")
        self.profLabel.setText(QCoreApplication.translate("MainWindow", u"Student's Profile", None))
#if QT_CONFIG(tooltip)
        self.homeBtnProf.setToolTip(QCoreApplication.translate("MainWindow", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtnProf.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.gradesBtnProf.setToolTip(QCoreApplication.translate("MainWindow", u"Grades", None))
#endif // QT_CONFIG(tooltip)
        self.gradesBtnProf.setText(QCoreApplication.translate("MainWindow", u"Grades >>", None))
        self.grdJHSIcon.setText("")
        self.gradesJHSLabel.setText(QCoreApplication.translate("MainWindow", u"Grades - Junior High School", None))
        self.homeBtnJHS.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.prevBtnJHS.setText(QCoreApplication.translate("MainWindow", u"<<Previous", None))
        self.attendBtnJHS.setText(QCoreApplication.translate("MainWindow", u"Attendance >>", None))
        self.grdSHSIcon.setText("")
        self.gradesSHSLabel.setText(QCoreApplication.translate("MainWindow", u"Grades - Senior High School", None))
        self.homeBtnSHS.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.prevBtnSHS.setText(QCoreApplication.translate("MainWindow", u"<<Previous", None))
        self.attendBtnSHS.setText(QCoreApplication.translate("MainWindow", u"Attendance >>", None))
        self.attIcon.setText("")
        self.attendLabel.setText(QCoreApplication.translate("MainWindow", u"Attendance & Observed Values", None))
        self.homeBtnAttend.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.prevBtnAttend.setText(QCoreApplication.translate("MainWindow", u"<<Previous", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"By: JPCa\u00f1as", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"version 1.2.0", None))
    # retranslateUi

