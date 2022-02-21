# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plasmamKHoVA.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class UI_MainWindow(object):

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 600)
        MainWindow.setMinimumSize(QSize(1024, 600))
        MainWindow.setMaximumSize(QSize(1024, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"padding: 10px;\n"
                                         "background-color:#131220;\n"
                                         "font: 28pt \"Hero\";\n"
                                         "color:#4BB3C3;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.centralwidget)
        self.menu.setObjectName(u"menu")
        self.verticalLayout_5 = QVBoxLayout(self.menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, -1, 6, -1)
        self.button_home = QPushButton(self.menu)
        self.button_home.setObjectName(u"button_home")
        self.button_home.setStyleSheet(u"border:none;")
        icon = QIcon()
        icon.addFile(u"assets/home-act.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_home.setIcon(icon)
        self.button_home.setIconSize(QSize(90, 90))

        self.verticalLayout_5.addWidget(self.button_home)

        self.button_user = QPushButton(self.menu)
        self.button_user.setObjectName(u"button_user")
        self.button_user.setStyleSheet(u"border:none;")
        icon1 = QIcon()
        icon1.addFile(u"assets/user-reg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_user.setIcon(icon1)
        self.button_user.setIconSize(QSize(90, 90))

        self.verticalLayout_5.addWidget(self.button_user)

        self.button_settings = QPushButton(self.menu)
        self.button_settings.setObjectName(u"button_settings")
        self.button_settings.setStyleSheet(u"border:none;")
        icon2 = QIcon()
        icon2.addFile(u"assets/settings-reg.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.button_settings.setIcon(icon2)
        self.button_settings.setIconSize(QSize(90, 90))

        self.verticalLayout_5.addWidget(self.button_settings)

        self.horizontalLayout.addWidget(self.menu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.stackedWidget.setStyleSheet(u"color:#131220;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.horizontalLayout_2 = QHBoxLayout(self.home)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.timer_box = QWidget(self.home)
        self.timer_box.setObjectName(u"timer_box")
        self.timer_box.setMaximumSize(QSize(600, 16777215))
        self.timer_box.setStyleSheet(u"margin:0;")
        self.horizontalLayout_3 = QHBoxLayout(self.timer_box)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.l_timer_box = QWidget(self.timer_box)
        self.l_timer_box.setObjectName(u"l_timer_box")
        self.l_timer_box.setStyleSheet(u"margin:0;")
        self.verticalLayout_2 = QVBoxLayout(self.l_timer_box)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.l_up_arrow = QWidget(self.l_timer_box)
        self.l_up_arrow.setObjectName(u"l_up_arrow")
        self.gridLayout_3 = QGridLayout(self.l_up_arrow)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.l_up_button = QPushButton(self.l_up_arrow)
        self.l_up_button.setObjectName(u"l_up_button")
        self.l_up_button.setMinimumSize(QSize(182, 0))
        self.l_up_button.setTabletTracking(True)
        self.l_up_button.setStyleSheet(u"margin-right:23px;")
        icon3 = QIcon()
        icon3.addFile(u"assets/arrowUp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.l_up_button.setIcon(icon3)
        self.l_up_button.setIconSize(QSize(100, 100))
        self.l_up_button.setFlat(True)

        self.gridLayout_3.addWidget(self.l_up_button, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.l_up_arrow)

        self.l_timer = QWidget(self.l_timer_box)
        self.l_timer.setObjectName(u"l_timer")
        self.l_timer.setStyleSheet(u"padding:0;\n"
                                   "margin:0;")
        self.horizontalLayout_6 = QHBoxLayout(self.l_timer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.digit_1 = QLabel(self.l_timer)
        self.digit_1.setObjectName(u"digit_1")
        self.digit_1.setMaximumSize(QSize(16777215, 265))
        self.digit_1.setTabletTracking(True)
        self.digit_1.setLayoutDirection(Qt.LeftToRight)
        self.digit_1.setStyleSheet(u"font: 190pt \"Digital Play St\";\n"
                                   "color:#5BC7CA;\n"
                                   "")
        self.digit_1.setTextFormat(Qt.AutoText)
        self.digit_1.setScaledContents(False)
        self.digit_1.setAlignment(Qt.AlignCenter)
        self.digit_1.setWordWrap(False)
        self.digit_1.setMargin(0)
        self.digit_1.setIndent(0)

        self.horizontalLayout_6.addWidget(self.digit_1)

        self.verticalLayout_2.addWidget(self.l_timer)

        self.l_down_arrow = QWidget(self.l_timer_box)
        self.l_down_arrow.setObjectName(u"l_down_arrow")
        self.gridLayout_6 = QGridLayout(self.l_down_arrow)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.l_down_button = QPushButton(self.l_down_arrow)
        self.l_down_button.setObjectName(u"l_down_button")
        self.l_down_button.setMinimumSize(QSize(182, 0))
        self.l_down_button.setTabletTracking(True)
        self.l_down_button.setStyleSheet(u"margin-right:23px;")
        icon4 = QIcon()
        icon4.addFile(u"assets/arrowDown.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.l_down_button.setIcon(icon4)
        self.l_down_button.setIconSize(QSize(100, 100))
        self.l_down_button.setFlat(True)

        self.gridLayout_6.addWidget(self.l_down_button, 0, 0, 1, 1)

        self.verticalLayout_2.addWidget(self.l_down_arrow)

        self.horizontalLayout_3.addWidget(self.l_timer_box)

        self.c_timer_box = QWidget(self.timer_box)
        self.c_timer_box.setObjectName(u"c_timer_box")
        self.c_timer_box.setStyleSheet(u"margin:0;")
        self.verticalLayout_3 = QVBoxLayout(self.c_timer_box)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.c_up_arrow = QWidget(self.c_timer_box)
        self.c_up_arrow.setObjectName(u"c_up_arrow")
        self.c_up_arrow.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.c_up_arrow)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.c_up_button = QPushButton(self.c_up_arrow)
        self.c_up_button.setObjectName(u"c_up_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.c_up_button.sizePolicy().hasHeightForWidth())
        self.c_up_button.setSizePolicy(sizePolicy)
        self.c_up_button.setMinimumSize(QSize(160, 0))
        self.c_up_button.setMaximumSize(QSize(182, 122))
        self.c_up_button.setTabletTracking(True)
        self.c_up_button.setStyleSheet(u"margin-right:23px;")
        self.c_up_button.setIcon(icon3)
        self.c_up_button.setIconSize(QSize(100, 100))
        self.c_up_button.setFlat(True)

        self.gridLayout_4.addWidget(self.c_up_button, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.c_up_arrow)

        self.c_timer = QWidget(self.c_timer_box)
        self.c_timer.setObjectName(u"c_timer")
        self.c_timer.setStyleSheet(u"padding:0;")
        self.horizontalLayout_4 = QHBoxLayout(self.c_timer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.digit_2 = QLabel(self.c_timer)
        self.digit_2.setObjectName(u"digit_2")
        self.digit_2.setMaximumSize(QSize(16777215, 265))
        self.digit_2.setStyleSheet(u"font: 190pt \"Digital Play St\";\n"
                                   "color:#5BC7CA;\n"
                                   "")
        self.digit_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.digit_2)

        self.verticalLayout_3.addWidget(self.c_timer)

        self.c_down_arrow = QWidget(self.c_timer_box)
        self.c_down_arrow.setObjectName(u"c_down_arrow")
        self.gridLayout_7 = QGridLayout(self.c_down_arrow)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.c_down_nutton = QPushButton(self.c_down_arrow)
        self.c_down_nutton.setObjectName(u"c_down_nutton")
        self.c_down_nutton.setMinimumSize(QSize(182, 0))
        self.c_down_nutton.setTabletTracking(True)
        self.c_down_nutton.setStyleSheet(u"margin-right:23px;")
        self.c_down_nutton.setIcon(icon4)
        self.c_down_nutton.setIconSize(QSize(100, 100))
        self.c_down_nutton.setFlat(True)

        self.gridLayout_7.addWidget(self.c_down_nutton, 0, 0, 1, 1)

        self.verticalLayout_3.addWidget(self.c_down_arrow)

        self.horizontalLayout_3.addWidget(self.c_timer_box)

        self.r_timer_box = QWidget(self.timer_box)
        self.r_timer_box.setObjectName(u"r_timer_box")
        self.r_timer_box.setStyleSheet(u"margin:0;")
        self.verticalLayout_4 = QVBoxLayout(self.r_timer_box)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, 0, -1)
        self.r_up_arrow = QWidget(self.r_timer_box)
        self.r_up_arrow.setObjectName(u"r_up_arrow")
        self.gridLayout_5 = QGridLayout(self.r_up_arrow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.r_up_button = QPushButton(self.r_up_arrow)
        self.r_up_button.setObjectName(u"r_up_button")
        self.r_up_button.setMinimumSize(QSize(182, 0))
        self.r_up_button.setTabletTracking(True)
        self.r_up_button.setStyleSheet(u"margin-right:23px;")
        self.r_up_button.setIcon(icon3)
        self.r_up_button.setIconSize(QSize(100, 100))
        self.r_up_button.setFlat(True)

        self.gridLayout_5.addWidget(self.r_up_button, 0, 0, 1, 1)

        self.verticalLayout_4.addWidget(self.r_up_arrow)

        self.r_timer = QWidget(self.r_timer_box)
        self.r_timer.setObjectName(u"r_timer")
        self.r_timer.setStyleSheet(u"padding:0;")
        self.horizontalLayout_5 = QHBoxLayout(self.r_timer)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.digit_3 = QLabel(self.r_timer)
        self.digit_3.setObjectName(u"digit_3")
        self.digit_3.setMaximumSize(QSize(16777215, 265))
        self.digit_3.setStyleSheet(u"font: 190pt \"Digital Play St\";\n"
                                   "color:#5BC7CA;\n"
                                   "")
        self.digit_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.digit_3)

        self.verticalLayout_4.addWidget(self.r_timer)

        self.r_down_arrow = QWidget(self.r_timer_box)
        self.r_down_arrow.setObjectName(u"r_down_arrow")
        self.gridLayout_8 = QGridLayout(self.r_down_arrow)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.r_down_button = QPushButton(self.r_down_arrow)
        self.r_down_button.setObjectName(u"r_down_button")
        self.r_down_button.setMinimumSize(QSize(182, 0))
        self.r_down_button.setTabletTracking(True)
        self.r_down_button.setStyleSheet(u"margin-right:23px;")
        self.r_down_button.setIcon(icon4)
        self.r_down_button.setIconSize(QSize(100, 100))
        self.r_down_button.setFlat(True)

        self.gridLayout_8.addWidget(self.r_down_button, 0, 0, 1, 1)

        self.verticalLayout_4.addWidget(self.r_down_arrow)

        self.horizontalLayout_3.addWidget(self.r_timer_box)

        self.horizontalLayout_2.addWidget(self.timer_box)

        self.indicators_box = QWidget(self.home)
        self.indicators_box.setObjectName(u"indicators_box")
        self.indicators_box.setMaximumSize(QSize(260, 16777215))
        self.indicators_box.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.indicators_box)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 6, 0)
        self.indicator_box = QWidget(self.indicators_box)
        self.indicator_box.setObjectName(u"indicator_box")
        self.indicator_box.setMaximumSize(QSize(250, 250))
        self.gridLayout = QGridLayout(self.indicator_box)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.indicator_box)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u"assets/SVG/pb.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(230, 230))
        self.pushButton_2.setFlat(True)

        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.indicator_box)

        self.start_button_box = QWidget(self.indicators_box)
        self.start_button_box.setObjectName(u"start_button_box")
        self.start_button_box.setMaximumSize(QSize(260, 260))
        self.gridLayout_2 = QGridLayout(self.start_button_box)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pushButton = QPushButton(self.start_button_box)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(240, 240))
        self.pushButton.setTabletTracking(True)
        icon6 = QIcon()
        icon6.addFile(u"assets/startBtn.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u"assets/stopBtn.svg", QSize(), QIcon.Disabled, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(230, 230))

        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)

        self.verticalLayout.addWidget(self.start_button_box)

        self.horizontalLayout_2.addWidget(self.indicators_box)

        self.stackedWidget.addWidget(self.home)
        self.user = QWidget()
        self.user.setObjectName(u"user")
        self.stackedWidget.addWidget(self.user)

        self.horizontalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.button_home.setText("")
        self.button_user.setText("")
        self.button_settings.setText("")
        self.l_up_button.setText("")
        self.digit_1.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.l_down_button.setText("")
        self.c_up_button.setText("")
        self.digit_2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.c_down_nutton.setText("")
        self.r_up_button.setText("")
        self.digit_3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.r_down_button.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
    # retranslateUi
