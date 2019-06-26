# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GPS_App.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
from PyQt5.Qwt import *

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 420)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setBaseSize(QtCore.QSize(480, 280))
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(10, 10))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("#centralwidget {\n"
"background: Navy;\n"
"}\n"
"#tab_map, #tab_gps, #tab_gauge{\n"
"background: lightSteelBlue;\n"
"}\n"
"#AltBox{\n"
"color: yellow;\n"
"padding: 1px;\n"
"background-color: black;\n"
"border-style: sunken;\n"
"border-width: 3px;\n"
"}\n"
"#degLbl{\n"
"color: darkgray;\n"
"}\n"
"\n"
"#PlotLbl_N, #PlotLbl_E, #PlotLbl_S, #PlotLbl_W  {\n"
"color: darkgray;\n"
"background-color: black;\n"
"}\n"
"\n"
"#SpeedLCD, #CompassLCD  {\n"
"background-color: black;\n"
"}\n"
"\n"
"#Zeroline {\n"
"foreground color: blue;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.TabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.TabWidget.setGeometry(QtCore.QRect(0, 0, 800, 404))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabWidget.sizePolicy().hasHeightForWidth())
        self.TabWidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.TabWidget.setFont(font)
        self.TabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.TabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.TabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.TabWidget.setIconSize(QtCore.QSize(12, 12))
        self.TabWidget.setUsesScrollButtons(True)
        self.TabWidget.setObjectName("TabWidget")
        self.tab_map = QtWidgets.QWidget()
        self.tab_map.setObjectName("tab_map")
        self.ShowMap_pushbtn = QtWidgets.QPushButton(self.tab_map)
        self.ShowMap_pushbtn.setGeometry(QtCore.QRect(13, 34, 72, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowMap_pushbtn.setFont(font)
        self.ShowMap_pushbtn.setObjectName("ShowMap_pushbtn")
        self.webView = QtWebKitWidgets.QWebView(self.tab_map)
        self.webView.setGeometry(QtCore.QRect(100, 2, 640, 400))
        self.webView.setMinimumSize(QtCore.QSize(200, 150))
        self.webView.setBaseSize(QtCore.QSize(200, 150))
        self.webView.setUrl(QtCore.QUrl("about:blank"))
        self.webView.setObjectName("webView")
        self.MapStyle_comboBox = QtWidgets.QComboBox(self.tab_map)
        self.MapStyle_comboBox.setGeometry(QtCore.QRect(13, 75, 72, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MapStyle_comboBox.setFont(font)
        self.MapStyle_comboBox.setMaxVisibleItems(5)
        self.MapStyle_comboBox.setMaxCount(5)
        self.MapStyle_comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.MapStyle_comboBox.setMinimumContentsLength(0)
        self.MapStyle_comboBox.setModelColumn(0)
        self.MapStyle_comboBox.setObjectName("MapStyle_comboBox")
        self.MapStyle_comboBox.addItem("")
        self.MapStyle_comboBox.addItem("")
        self.MapStyle_comboBox.addItem("")
        self.MapStyle_comboBox.addItem("")
        self.ZoomSlider = QtWidgets.QSlider(self.tab_map)
        self.ZoomSlider.setGeometry(QtCore.QRect(20, 116, 24, 116))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ZoomSlider.sizePolicy().hasHeightForWidth())
        self.ZoomSlider.setSizePolicy(sizePolicy)
        self.ZoomSlider.setMinimumSize(QtCore.QSize(0, 28))
        self.ZoomSlider.setBaseSize(QtCore.QSize(40, 40))
        self.ZoomSlider.setMinimum(0)
        self.ZoomSlider.setMaximum(22)
        self.ZoomSlider.setSliderPosition(11)
        self.ZoomSlider.setOrientation(QtCore.Qt.Vertical)
        self.ZoomSlider.setInvertedAppearance(True)
        self.ZoomSlider.setInvertedControls(True)
        self.ZoomSlider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.ZoomSlider.setTickInterval(2)
        self.ZoomSlider.setObjectName("ZoomSlider")
        self.MapTypeBtnlabel = QtWidgets.QLabel(self.tab_map)
        self.MapTypeBtnlabel.setGeometry(QtCore.QRect(20, 57, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.MapTypeBtnlabel.setFont(font)
        self.MapTypeBtnlabel.setObjectName("MapTypeBtnlabel")
        self.ZoomSliderlabel_1 = QtWidgets.QLabel(self.tab_map)
        self.ZoomSliderlabel_1.setGeometry(QtCore.QRect(20, 100, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZoomSliderlabel_1.setFont(font)
        self.ZoomSliderlabel_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ZoomSliderlabel_1.setLineWidth(2)
        self.ZoomSliderlabel_1.setTextFormat(QtCore.Qt.PlainText)
        self.ZoomSliderlabel_1.setObjectName("ZoomSliderlabel_1")
        self.ZoomSliderlabel_2 = QtWidgets.QLabel(self.tab_map)
        self.ZoomSliderlabel_2.setGeometry(QtCore.QRect(46, 208, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZoomSliderlabel_2.setFont(font)
        self.ZoomSliderlabel_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ZoomSliderlabel_2.setLineWidth(2)
        self.ZoomSliderlabel_2.setTextFormat(QtCore.Qt.PlainText)
        self.ZoomSliderlabel_2.setObjectName("ZoomSliderlabel_2")
        self.ZoomSliderlabel_3 = QtWidgets.QLabel(self.tab_map)
        self.ZoomSliderlabel_3.setGeometry(QtCore.QRect(47, 116, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ZoomSliderlabel_3.setFont(font)
        self.ZoomSliderlabel_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.ZoomSliderlabel_3.setLineWidth(2)
        self.ZoomSliderlabel_3.setTextFormat(QtCore.Qt.PlainText)
        self.ZoomSliderlabel_3.setObjectName("ZoomSliderlabel_3")
        self.ShowData_pushbtn = QtWidgets.QPushButton(self.tab_map)
        self.ShowData_pushbtn.setGeometry(QtCore.QRect(13, 4, 72, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ShowData_pushbtn.setFont(font)
        self.ShowData_pushbtn.setObjectName("ShowData_pushbtn")
        self.TabWidget.addTab(self.tab_map, "")
        self.tab_gps = QtWidgets.QWidget()
        self.tab_gps.setObjectName("tab_gps")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_gps)
        self.tableWidget.setGeometry(QtCore.QRect(5, 25, 141, 180))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Piboto Condensed")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        font.setKerning(False)
        self.tableWidget.setFont(font)
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setLineWidth(3)
        self.tableWidget.setMidLineWidth(3)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setAutoScrollMargin(0)
        self.tableWidget.setTabKeyNavigation(False)
        self.tableWidget.setProperty("showDropIndicator", False)
        self.tableWidget.setDragDropOverwriteMode(False)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(False)
        self.tableWidget.setCornerButtonEnabled(False)
        self.tableWidget.setRowCount(9)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(71)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(20)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(20)
        self.UpdateGPS_pushbtn = QtWidgets.QPushButton(self.tab_gps)
        self.UpdateGPS_pushbtn.setGeometry(QtCore.QRect(45, 220, 61, 23))
        self.UpdateGPS_pushbtn.setObjectName("UpdateGPS_pushbtn")
        self.polarplot = PlotWidget(self.tab_gps)
        self.polarplot.setGeometry(QtCore.QRect(152, 26, 350, 350))
        self.polarplot.setObjectName("polarplot")
        self.barplot = PlotWidget(self.tab_gps)
        self.barplot.setGeometry(QtCore.QRect(508, 26, 265, 350))
        self.barplot.setObjectName("barplot")
        self.degLbl = QtWidgets.QLabel(self.tab_gps)
        self.degLbl.setGeometry(QtCore.QRect(334, 199, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Piboto Condensed")
        font.setPointSize(10)
        font.setItalic(True)
        self.degLbl.setFont(font)
        self.degLbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.degLbl.setTextFormat(QtCore.Qt.PlainText)
        self.degLbl.setObjectName("degLbl")
        self.PlotLbl_N = QtWidgets.QLabel(self.tab_gps)
        self.PlotLbl_N.setGeometry(QtCore.QRect(322, 26, 15, 15))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.PlotLbl_N.setFont(font)
        self.PlotLbl_N.setObjectName("PlotLbl_N")
        self.PlotLbl_E = QtWidgets.QLabel(self.tab_gps)
        self.PlotLbl_E.setGeometry(QtCore.QRect(486, 193, 15, 16))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.PlotLbl_E.setFont(font)
        self.PlotLbl_E.setObjectName("PlotLbl_E")
        self.PlotLbl_S = QtWidgets.QLabel(self.tab_gps)
        self.PlotLbl_S.setGeometry(QtCore.QRect(322, 359, 13, 16))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.PlotLbl_S.setFont(font)
        self.PlotLbl_S.setObjectName("PlotLbl_S")
        self.PlotLbl_W = QtWidgets.QLabel(self.tab_gps)
        self.PlotLbl_W.setGeometry(QtCore.QRect(152, 193, 16, 16))
        font = QtGui.QFont()
        font.setFamily("FreeSerif")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.PlotLbl_W.setFont(font)
        self.PlotLbl_W.setObjectName("PlotLbl_W")
        self.gpsTableLabel_2 = QtWidgets.QLabel(self.tab_gps)
        self.gpsTableLabel_2.setGeometry(QtCore.QRect(487, 5, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gpsTableLabel_2.setFont(font)
        self.gpsTableLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.gpsTableLabel_2.setObjectName("gpsTableLabel_2")
        self.gpsTableLabel_3 = QtWidgets.QLabel(self.tab_gps)
        self.gpsTableLabel_3.setGeometry(QtCore.QRect(560, 5, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gpsTableLabel_3.setFont(font)
        self.gpsTableLabel_3.setAlignment(QtCore.Qt.AlignCenter)
        self.gpsTableLabel_3.setObjectName("gpsTableLabel_3")
        self.gpsTableLabel_4 = QtWidgets.QLabel(self.tab_gps)
        self.gpsTableLabel_4.setGeometry(QtCore.QRect(244, 5, 201, 21))
        self.gpsTableLabel_4.setBaseSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gpsTableLabel_4.setFont(font)
        self.gpsTableLabel_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gpsTableLabel_4.setAlignment(QtCore.Qt.AlignCenter)
        self.gpsTableLabel_4.setObjectName("gpsTableLabel_4")
        self.gpsTableLabel_5 = QtWidgets.QLabel(self.tab_gps)
        self.gpsTableLabel_5.setGeometry(QtCore.QRect(0, 5, 151, 21))
        self.gpsTableLabel_5.setBaseSize(QtCore.QSize(30, 0))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.gpsTableLabel_5.setFont(font)
        self.gpsTableLabel_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gpsTableLabel_5.setAlignment(QtCore.Qt.AlignCenter)
        self.gpsTableLabel_5.setObjectName("gpsTableLabel_5")
        self.polarplot.raise_()
        self.tableWidget.raise_()
        self.UpdateGPS_pushbtn.raise_()
        self.barplot.raise_()
        self.PlotLbl_N.raise_()
        self.PlotLbl_E.raise_()
        self.PlotLbl_S.raise_()
        self.PlotLbl_W.raise_()
        self.gpsTableLabel_2.raise_()
        self.gpsTableLabel_3.raise_()
        self.gpsTableLabel_4.raise_()
        self.degLbl.raise_()
        self.gpsTableLabel_5.raise_()
        self.TabWidget.addTab(self.tab_gps, "")
        self.tab_gauge = QtWidgets.QWidget()
        self.tab_gauge.setObjectName("tab_gauge")
        self.SpeedDial = QwtDial(self.tab_gauge)
        self.SpeedDial.setGeometry(QtCore.QRect(8, 24, 300, 300))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.SpeedDial.setFont(font)
        self.SpeedDial.setUpperBound(90.0)
        self.SpeedDial.setScaleStepSize(5.0)
        self.SpeedDial.setProperty("value", 0.0)
        self.SpeedDial.setLineWidth(6)
        self.SpeedDial.setMinScaleArc(20.0)
        self.SpeedDial.setMaxScaleArc(340.0)
        self.SpeedDial.setObjectName("SpeedDial")
        self.Compass = QwtCompass(self.tab_gauge)
        self.Compass.setGeometry(QtCore.QRect(459, 24, 300, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Compass.sizePolicy().hasHeightForWidth())
        self.Compass.setSizePolicy(sizePolicy)
        self.Compass.setBaseSize(QtCore.QSize(180, 180))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.Compass.setFont(font)
        self.Compass.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Compass.setAutoFillBackground(False)
        self.Compass.setScaleMaxMajor(30)
        self.Compass.setScaleStepSize(5.0)
        self.Compass.setProperty("value", 0.0)
        self.Compass.setInvertedControls(False)
        self.Compass.setLineWidth(6)
        self.Compass.setFrameShadow(QwtDial.Sunken)
        self.Compass.setMode(QwtDial.RotateScale)
        self.Compass.setOrigin(270.0)
        self.Compass.setObjectName("Compass")
        self.SpeedLCD = QtWidgets.QLCDNumber(self.tab_gauge)
        self.SpeedLCD.setGeometry(QtCore.QRect(109, 330, 60, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.SpeedLCD.setFont(font)
        self.SpeedLCD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SpeedLCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.SpeedLCD.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SpeedLCD.setLineWidth(1)
        self.SpeedLCD.setSmallDecimalPoint(True)
        self.SpeedLCD.setDigitCount(2)
        self.SpeedLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.SpeedLCD.setProperty("intValue", 0)
        self.SpeedLCD.setObjectName("SpeedLCD")
        self.CompassLCD = QtWidgets.QLCDNumber(self.tab_gauge)
        self.CompassLCD.setGeometry(QtCore.QRect(570, 330, 60, 32))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.CompassLCD.setFont(font)
        self.CompassLCD.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CompassLCD.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.CompassLCD.setLineWidth(1)
        self.CompassLCD.setSmallDecimalPoint(True)
        self.CompassLCD.setDigitCount(3)
        self.CompassLCD.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.CompassLCD.setProperty("intValue", 0)
        self.CompassLCD.setObjectName("CompassLCD")
        self.VertSpdThermo = QwtThermo(self.tab_gauge)
        self.VertSpdThermo.setGeometry(QtCore.QRect(340, 61, 60, 291))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.VertSpdThermo.setFont(font)
        self.VertSpdThermo.setToolTipDuration(-4)
        self.VertSpdThermo.setLowerBound(-8.0)
        self.VertSpdThermo.setUpperBound(8.0)
        self.VertSpdThermo.setScaleMaxMajor(10)
        self.VertSpdThermo.setScaleMaxMinor(1)
        self.VertSpdThermo.setScaleStepSize(1.0)
        self.VertSpdThermo.setOriginMode(QwtThermo.OriginCustom)
        self.VertSpdThermo.setOrigin(0.0)
        self.VertSpdThermo.setPipeWidth(10)
        self.VertSpdThermo.setObjectName("VertSpdThermo")
        self.AltBox = QtWidgets.QLabel(self.tab_gauge)
        self.AltBox.setGeometry(QtCore.QRect(334, 26, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.AltBox.setFont(font)
        self.AltBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AltBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.AltBox.setLineWidth(3)
        self.AltBox.setMidLineWidth(3)
        self.AltBox.setTextFormat(QtCore.Qt.PlainText)
        self.AltBox.setAlignment(QtCore.Qt.AlignCenter)
        self.AltBox.setIndent(5)
        self.AltBox.setObjectName("AltBox")
        self.label = QtWidgets.QLabel(self.tab_gauge)
        self.label.setGeometry(QtCore.QRect(307, 0, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_gauge)
        self.label_2.setGeometry(QtCore.QRect(280, 352, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.Zeroline = QtWidgets.QFrame(self.tab_gauge)
        self.Zeroline.setGeometry(QtCore.QRect(290, 204, 181, 6))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.Zeroline.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Zeroline.setFont(font)
        self.Zeroline.setMidLineWidth(3)
        self.Zeroline.setFrameShape(QtWidgets.QFrame.HLine)
        self.Zeroline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.Zeroline.setObjectName("Zeroline")
        self.label_3 = QtWidgets.QLabel(self.tab_gauge)
        self.label_3.setGeometry(QtCore.QRect(175, 335, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_gauge)
        self.label_4.setGeometry(QtCore.QRect(635, 335, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_gauge)
        self.label_5.setGeometry(QtCore.QRect(50, 0, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_gauge)
        self.label_6.setGeometry(QtCore.QRect(523, 0, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.SpeedLCD.raise_()
        self.CompassLCD.raise_()
        self.AltBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.Zeroline.raise_()
        self.Compass.raise_()
        self.SpeedDial.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.VertSpdThermo.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.TabWidget.addTab(self.tab_gauge, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setMinimumSize(QtCore.QSize(480, 16))
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.TabWidget.setCurrentIndex(0)
        self.MapStyle_comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vogelectric GPS"))
        self.ShowMap_pushbtn.setText(_translate("MainWindow", "Show Map"))
        self.MapStyle_comboBox.setCurrentText(_translate("MainWindow", "road"))
        self.MapStyle_comboBox.setItemText(0, _translate("MainWindow", "road"))
        self.MapStyle_comboBox.setItemText(1, _translate("MainWindow", "satellite"))
        self.MapStyle_comboBox.setItemText(2, _translate("MainWindow", "terrain"))
        self.MapStyle_comboBox.setItemText(3, _translate("MainWindow", "hybrid"))
        self.MapTypeBtnlabel.setText(_translate("MainWindow", "Map Type "))
        self.ZoomSliderlabel_1.setText(_translate("MainWindow", "Zoom"))
        self.ZoomSliderlabel_2.setText(_translate("MainWindow", "In"))
        self.ZoomSliderlabel_3.setText(_translate("MainWindow", "Out"))
        self.ShowData_pushbtn.setText(_translate("MainWindow", "Show Data"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_map), _translate("MainWindow", "Map"))
        self.UpdateGPS_pushbtn.setText(_translate("MainWindow", "Update"))
        self.degLbl.setText(_translate("MainWindow", "15  30   45  60   75   90"))
        self.PlotLbl_N.setText(_translate("MainWindow", "N"))
        self.PlotLbl_E.setText(_translate("MainWindow", "E"))
        self.PlotLbl_S.setText(_translate("MainWindow", "S"))
        self.PlotLbl_W.setText(_translate("MainWindow", "W"))
        self.gpsTableLabel_2.setText(_translate("MainWindow", "PRN"))
        self.gpsTableLabel_3.setText(_translate("MainWindow", "Signal Strength"))
        self.gpsTableLabel_4.setText(_translate("MainWindow", "Celestial Positions"))
        self.gpsTableLabel_5.setText(_translate("MainWindow", "GPS Readings"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_gps), _translate("MainWindow", "GPS"))
        self.AltBox.setText(_translate("MainWindow", "0100.0"))
        self.label.setText(_translate("MainWindow", "Altitude"))
        self.label_2.setText(_translate("MainWindow", "Vert Speed ft /sec"))
        self.label_3.setText(_translate("MainWindow", "mph"))
        self.label_4.setText(_translate("MainWindow", "deg"))
        self.label_5.setText(_translate("MainWindow", "Ground Speed"))
        self.label_6.setText(_translate("MainWindow", "Heading"))
        self.TabWidget.setTabText(self.TabWidget.indexOf(self.tab_gauge), _translate("MainWindow", "Gauge"))

from PyQt5 import QtWebKitWidgets
from pyqtgraph import PlotWidget