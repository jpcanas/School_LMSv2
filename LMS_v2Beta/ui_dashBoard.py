# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dashBoardrVyvfh.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt, QMargins)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from PySide2.QtCharts import QtCharts

class Ui_dBFrame(object):
    def setupUi(self, dBFrame):
        if dBFrame.objectName():
            dBFrame.setObjectName(u"dBFrame")
        dBFrame.resize(461, 307)
        self.verticalLayout = QVBoxLayout(dBFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(dBFrame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.page1Layout = QHBoxLayout(self.page1)
        self.page1Layout.setSpacing(0)
        self.page1Layout.setObjectName(u"page1Layout")
        self.page1Layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.page2Layout = QHBoxLayout(self.page2)
        self.page2Layout.setSpacing(0)
        self.page2Layout.setObjectName(u"page2Layout")
        self.page2Layout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget.addWidget(self.page2)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(dBFrame)

        self.stackedWidget.setCurrentIndex(0)

        self.labelbrush = QBrush(QColor(255, 255, 255, 255))
        self.labelbrush.setStyle(Qt.SolidPattern)
        self.chartfont = QFont()
        self.chartfont.setFamily(u"Segoe UI")
        self.chartfont.setPointSize(12)
        self.chartfont.setBold(True)
        self.chartfont.setWeight(75)

        self.pieSliceFont = QFont()
        self.pieSliceFont.setFamily(u"Segoe UI")
        self.pieSliceFont.setPointSize(9)
        self.pieSliceFont.setBold(True)

        QMetaObject.connectSlotsByName(dBFrame)
    # setupUi
        self.pieChart()
        self.barGraph()

    def pieChart(self):                     ############# CLass distribution by gender ###########
        series = QtCharts.QPieSeries()
        series.append("Male", 16)
        series.append("Female", 20)
        series.setLabelsPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
        
        maleslice = series.slices()[0]
        maleslice.setExploded()
        maleslice.setLabelVisible()
        maleslice.setLabelFont(self.pieSliceFont)
        maleslice.setLabelBrush(self.labelbrush)

        femaleslice = series.slices()[1]
        femaleslice.setLabelVisible()
        femaleslice.setLabelFont(self.pieSliceFont)
        femaleslice.setLabelBrush(self.labelbrush)

        for myslice in series.slices():
            myslice.setLabel("{:.2f}%".format(100 * myslice.percentage()))

        chartMargin = QMargins()
        chartMargin.setLeft(1)
        chartMargin.setRight(1)
        chartMargin.setTop(1)
        chartMargin.setBottom(1)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setAnimationDuration(2500)
        chart.setTitle("Class Distribution")

        chart.setTitleFont(self.chartfont)
        chart.setMargins(chartMargin)
 
        chart.legend().markers(series)[0].setLabel("Male")
        chart.legend().markers(series)[1].setLabel("Female")
        chart.legend().setAlignment(Qt.AlignLeft)
        chart.legend().setFont(self.pieSliceFont)
        
        chartview = QtCharts.QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.page1Layout.addWidget(chartview)

    def barGraph(self):             ############## Student absences per Month #################
        set1 = QtCharts.QBarSet("August")
        set2 = QtCharts.QBarSet("September")
        set3 = QtCharts.QBarSet("October")
        set4 = QtCharts.QBarSet("November")
        set5 = QtCharts.QBarSet("December")
        set6 = QtCharts.QBarSet("January")
        set7 = QtCharts.QBarSet("February")
        set8 = QtCharts.QBarSet("March")
        set9 = QtCharts.QBarSet("April")
        set10 = QtCharts.QBarSet("May")

        set1.append(17)
        set2.append(12)
        set3.append(10)
        set4.append(6)
        set5.append(18)
        set6.append(8)
        set7.append(11)
        set8.append(16)
        set9.append(20)
        set10.append(15)

        barSeries = QtCharts.QBarSeries()
        barSeries.append(set1)
        barSeries.append(set2)
        barSeries.append(set3)
        barSeries.append(set4)
        barSeries.append(set5)
        barSeries.append(set6)
        barSeries.append(set7)
        barSeries.append(set8)
        barSeries.append(set9)
        barSeries.append(set10)

        barchart = QtCharts.QChart()
        barchart.addSeries(barSeries)
        barchart.setTitle("Class Absences")
        barchart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        barchart.legend().setAlignment(Qt.AlignLeft)

        chartview = QtCharts.QChartView(barchart)
        chartview.setRenderHint(QPainter.Antialiasing)
        self.page2Layout.addWidget(chartview)

    def retranslateUi(self, dBFrame):
        dBFrame.setWindowTitle(QCoreApplication.translate("dBFrame", u"Frame", None))
    # retranslateUi

# help(QtCharts.QBarSet)

# chart.setTheme(QtCharts.QChart.ChartTheme.ChartThemeHighContrast)
# ChartThemeBlueCerulean
# ChartThemeBlueIcy
# ChartThemeBlueNcs
# ChartThemeBrownSand
# ChartThemeDark
# ChartThemeHighContrast
# ChartThemeLight
# chart.setTitleBrush(self.titlebrush)