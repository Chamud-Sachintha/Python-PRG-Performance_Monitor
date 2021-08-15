# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AboutSoftwareWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AboutSoftwareWindow(object):
    def setupUi(self, AboutSoftwareWindow):
        if not AboutSoftwareWindow.objectName():
            AboutSoftwareWindow.setObjectName(u"AboutSoftwareWindow")
        AboutSoftwareWindow.resize(800, 417)
        self.centralwidget = QWidget(AboutSoftwareWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 281, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 60, 261, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.centralwidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 90, 741, 21))
        self.label_13.setFont(font1)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(70, 110, 401, 21))
        self.label_14.setFont(font1)
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(50, 130, 741, 21))
        self.label_15.setFont(font1)
        self.label_16 = QLabel(self.centralwidget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(50, 150, 411, 21))
        self.label_16.setFont(font1)
        self.label_17 = QLabel(self.centralwidget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 170, 421, 21))
        self.label_17.setFont(font1)
        self.label_18 = QLabel(self.centralwidget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(50, 190, 421, 21))
        self.label_18.setFont(font1)
        self.label_19 = QLabel(self.centralwidget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 250, 421, 21))
        self.label_19.setFont(font1)
        self.label_20 = QLabel(self.centralwidget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(50, 210, 411, 21))
        self.label_20.setFont(font1)
        self.label_21 = QLabel(self.centralwidget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(50, 230, 421, 21))
        self.label_21.setFont(font1)
        self.label_22 = QLabel(self.centralwidget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(50, 290, 421, 21))
        self.label_22.setFont(font1)
        self.label_23 = QLabel(self.centralwidget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(50, 310, 421, 21))
        self.label_23.setFont(font1)
        self.label_24 = QLabel(self.centralwidget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(70, 270, 161, 21))
        self.label_24.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(500, 150, 271, 221))
        self.label_2.setPixmap(QPixmap(u"C:/Users/Sherlock/Downloads/131-1318667_performance-monitoring-application-performance-management-apm-logo-hd.png"))
        self.label_2.setScaledContents(True)
        self.label_25 = QLabel(self.centralwidget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(50, 350, 421, 21))
        self.label_25.setFont(font1)
        AboutSoftwareWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AboutSoftwareWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        AboutSoftwareWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AboutSoftwareWindow)
        self.statusbar.setObjectName(u"statusbar")
        AboutSoftwareWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutSoftwareWindow)

        QMetaObject.connectSlotsByName(AboutSoftwareWindow)
    # setupUi

    def retranslateUi(self, AboutSoftwareWindow):
        AboutSoftwareWindow.setWindowTitle(QCoreApplication.translate("AboutSoftwareWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AboutSoftwareWindow", u"About Software......", None))
        self.label_12.setText(QCoreApplication.translate("AboutSoftwareWindow", u"General Details About The Software System", None))
        self.label_13.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@.This is general purpose software application and developed by Python and QT Framework,and also this is used", None))
        self.label_14.setText(QCoreApplication.translate("AboutSoftwareWindow", u" Default system-ctl commands for perform various tasks.", None))
        self.label_15.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. This Application is open source application that helps to monitor CPU Performance and Disk usage.", None))
        self.label_16.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to Defrag Hard Disk and Check Disk health Greately.", None))
        self.label_17.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to Check Hard Disk Volume's status.", None))
        self.label_18.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to Make Some Decissions base in your disk health.", None))
        self.label_19.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to See Your main memoty and SWAP Memory in", None))
        self.label_20.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to Whole Disk Storage Status.", None))
        self.label_21.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. Also it can helps to See Your Processor Performance very effectively.", None))
        self.label_22.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. You can clean your disk drive without any interuption.", None))
        self.label_23.setText(QCoreApplication.translate("AboutSoftwareWindow", u"@. To See more details please visit our web site.", None))
        self.label_24.setText(QCoreApplication.translate("AboutSoftwareWindow", u"Details.", None))
        self.label_2.setText("")
        self.label_25.setText(QCoreApplication.translate("AboutSoftwareWindow", u"Developped By :- Chamud Sachintha (Sh3rl0k)", None))
    # retranslateUi

