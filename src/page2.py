# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1953, 1084)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(16, 16, 16))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_clock = QtWidgets.QLabel(self.centralwidget)
        self.label_clock.setGeometry(QtCore.QRect(0, 209, 920, 920))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 7, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 7, 10))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_clock.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(87)
        self.label_clock.setFont(font)
        self.label_clock.setStyleSheet("")
        self.label_clock.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_clock.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock.setObjectName("label_clock")
        self.label_clock_num = QtWidgets.QLabel(self.centralwidget)
        self.label_clock_num.setGeometry(QtCore.QRect(0, 0, 921, 201))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 208, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 208, 39))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_clock_num.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(116)
        self.label_clock_num.setFont(font)
        self.label_clock_num.setStyleSheet("")
        self.label_clock_num.setFrameShape(QtWidgets.QFrame.Box)
        self.label_clock_num.setAlignment(QtCore.Qt.AlignCenter)
        self.label_clock_num.setObjectName("label_clock_num")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(930, 10, 361, 311))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_1 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1.setObjectName("horizontalLayout_1")
        self.label_STR_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_STR_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_STR_1.setFont(font)
        self.label_STR_1.setStyleSheet("")
        self.label_STR_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_STR_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_STR_1.setObjectName("label_STR_1")
        self.horizontalLayout_1.addWidget(self.label_STR_1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_TNUM_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_TNUM_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_TNUM_1.setFont(font)
        self.label_TNUM_1.setStyleSheet("")
        self.label_TNUM_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_TNUM_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TNUM_1.setObjectName("label_TNUM_1")
        self.verticalLayout.addWidget(self.label_TNUM_1)
        self.label_HNUM_1 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_HNUM_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_HNUM_1.setFont(font)
        self.label_HNUM_1.setStyleSheet("")
        self.label_HNUM_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HNUM_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HNUM_1.setObjectName("label_HNUM_1")
        self.verticalLayout.addWidget(self.label_HNUM_1)
        self.horizontalLayout_1.addLayout(self.verticalLayout)
        self.horizontalLayout_1.setStretch(0, 2)
        self.horizontalLayout_1.setStretch(1, 4)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(930, 350, 361, 311))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_STR_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_STR_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_STR_2.setFont(font)
        self.label_STR_2.setStyleSheet("")
        self.label_STR_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_STR_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_STR_2.setObjectName("label_STR_2")
        self.horizontalLayout_3.addWidget(self.label_STR_2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_TNUM_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_TNUM_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_TNUM_2.setFont(font)
        self.label_TNUM_2.setStyleSheet("")
        self.label_TNUM_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_TNUM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TNUM_2.setObjectName("label_TNUM_2")
        self.verticalLayout_5.addWidget(self.label_TNUM_2)
        self.label_HNUM_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_HNUM_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_HNUM_2.setFont(font)
        self.label_HNUM_2.setStyleSheet("")
        self.label_HNUM_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HNUM_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HNUM_2.setObjectName("label_HNUM_2")
        self.verticalLayout_5.addWidget(self.label_HNUM_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 4)
        self.label_chartT_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartT_1.setGeometry(QtCore.QRect(1290, 12, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartT_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartT_1.setFont(font)
        self.label_chartT_1.setStyleSheet("")
        self.label_chartT_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartT_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartT_1.setObjectName("label_chartT_1")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(930, 690, 361, 311))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_STR3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(130, 130, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_STR3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_STR3.setFont(font)
        self.label_STR3.setStyleSheet("")
        self.label_STR3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_STR3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_STR3.setObjectName("label_STR3")
        self.horizontalLayout_4.addWidget(self.label_STR3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_TNUM_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(100, 230, 100))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_TNUM_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_TNUM_3.setFont(font)
        self.label_TNUM_3.setStyleSheet("")
        self.label_TNUM_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_TNUM_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TNUM_3.setObjectName("label_TNUM_3")
        self.verticalLayout_4.addWidget(self.label_TNUM_3)
        self.label_HNUM_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(65, 250, 250))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_HNUM_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(38)
        self.label_HNUM_3.setFont(font)
        self.label_HNUM_3.setStyleSheet("")
        self.label_HNUM_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_HNUM_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_HNUM_3.setObjectName("label_HNUM_3")
        self.verticalLayout_4.addWidget(self.label_HNUM_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4.setStretch(0, 2)
        self.horizontalLayout_4.setStretch(1, 4)
        self.label_chartH_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartH_1.setGeometry(QtCore.QRect(1290, 170, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartH_1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartH_1.setFont(font)
        self.label_chartH_1.setStyleSheet("")
        self.label_chartH_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartH_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartH_1.setObjectName("label_chartH_1")
        self.label_chartH_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartH_2.setGeometry(QtCore.QRect(1290, 508, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartH_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartH_2.setFont(font)
        self.label_chartH_2.setStyleSheet("")
        self.label_chartH_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartH_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartH_2.setObjectName("label_chartH_2")
        self.label_chartT_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartT_2.setGeometry(QtCore.QRect(1290, 350, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartT_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartT_2.setFont(font)
        self.label_chartT_2.setStyleSheet("")
        self.label_chartT_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartT_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartT_2.setObjectName("label_chartT_2")
        self.label_chartT_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartT_3.setGeometry(QtCore.QRect(1290, 690, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartT_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartT_3.setFont(font)
        self.label_chartT_3.setStyleSheet("")
        self.label_chartT_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartT_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartT_3.setObjectName("label_chartT_3")
        self.label_chartH_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_chartH_3.setGeometry(QtCore.QRect(1290, 850, 609, 150))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_chartH_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(27)
        self.label_chartH_3.setFont(font)
        self.label_chartH_3.setStyleSheet("")
        self.label_chartH_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_chartH_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_chartH_3.setObjectName("label_chartH_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1953, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_clock.setText(_translate("MainWindow", "圆形时钟"))
        self.label_clock_num.setText(_translate("MainWindow", "20:45"))
        self.label_STR_1.setText(_translate("MainWindow", "室外"))
        self.label_TNUM_1.setText(_translate("MainWindow", " 🌡22.2"))
        self.label_HNUM_1.setText(_translate("MainWindow", "💧66.6"))
        self.label_STR_2.setText(_translate("MainWindow", "卧室"))
        self.label_TNUM_2.setText(_translate("MainWindow", " 🌡22.2"))
        self.label_HNUM_2.setText(_translate("MainWindow", "💧66.6"))
        self.label_chartT_1.setText(_translate("MainWindow", "折线图_温度"))
        self.label_STR3.setText(_translate("MainWindow", "客厅"))
        self.label_TNUM_3.setText(_translate("MainWindow", " 🌡22.2"))
        self.label_HNUM_3.setText(_translate("MainWindow", "💧66.6"))
        self.label_chartH_1.setText(_translate("MainWindow", "折线图_湿度"))
        self.label_chartH_2.setText(_translate("MainWindow", "折线图_湿度"))
        self.label_chartT_2.setText(_translate("MainWindow", "折线图_温度"))
        self.label_chartT_3.setText(_translate("MainWindow", "折线图_温度"))
        self.label_chartH_3.setText(_translate("MainWindow", "折线图_湿度"))
