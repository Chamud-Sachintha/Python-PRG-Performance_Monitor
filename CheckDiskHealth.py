# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CheckDiskHealth.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DiskHealthWindow(object):
    def setupUi(self, DiskHealthWindow):
        if not DiskHealthWindow.objectName():
            DiskHealthWindow.setObjectName(u"DiskHealthWindow")
        DiskHealthWindow.resize(796, 600)
        self.centralwidget = QWidget(DiskHealthWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 381, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_14 = QLabel(self.centralwidget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 50, 191, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_14.setFont(font1)
        self.processor_txt = QLabel(self.centralwidget)
        self.processor_txt.setObjectName(u"processor_txt")
        self.processor_txt.setGeometry(QRect(110, 50, 251, 21))
        self.processor_txt.setFont(font1)
        self.checkhealth_btn = QPushButton(self.centralwidget)
        self.checkhealth_btn.setObjectName(u"checkhealth_btn")
        self.checkhealth_btn.setGeometry(QRect(440, 40, 171, 31))
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(630, 40, 151, 31))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 500, 821, 21))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 520, 371, 21))
        self.label_8.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 440, 661, 21))
        self.label_5.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 410, 561, 21))
        self.label_4.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 470, 661, 21))
        self.label_6.setFont(font1)
        self.diskhealth_line = QTextEdit(self.centralwidget)
        self.diskhealth_line.setObjectName(u"diskhealth_line")
        self.diskhealth_line.setGeometry(QRect(10, 80, 771, 321))
        DiskHealthWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DiskHealthWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 796, 21))
        DiskHealthWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DiskHealthWindow)
        self.statusbar.setObjectName(u"statusbar")
        DiskHealthWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DiskHealthWindow)

        QMetaObject.connectSlotsByName(DiskHealthWindow)
    # setupUi

    def retranslateUi(self, DiskHealthWindow):
        DiskHealthWindow.setWindowTitle(QCoreApplication.translate("DiskHealthWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("DiskHealthWindow", u"Check System Disk Health & Performance", None))
        self.label_14.setText(QCoreApplication.translate("DiskHealthWindow", u"Processor :- ", None))
        self.processor_txt.setText(QCoreApplication.translate("DiskHealthWindow", u"...", None))
        self.checkhealth_btn.setText(QCoreApplication.translate("DiskHealthWindow", u"Begin Checking Disk Health", None))
        self.exit_btn.setText(QCoreApplication.translate("DiskHealthWindow", u"Exit To main Window", None))
        self.label_7.setText(QCoreApplication.translate("DiskHealthWindow", u"<>This Tool Will Run Both 32 bit - and 64 bit workstations and sometimes result box will not apper while disk defragmentation but ,", None))
        self.label_8.setText(QCoreApplication.translate("DiskHealthWindow", u"after the defragmentation the results will show the Results Box.", None))
        self.label_5.setText(QCoreApplication.translate("DiskHealthWindow", u"<>Therefore Run This Tool Under Your Administrative Privillages By Right clicking the tool and run as Administrator.", None))
        self.label_4.setText(QCoreApplication.translate("DiskHealthWindow", u"<>This Defragmentation Process Is required By Full Administrative Privillages Of your Computer.", None))
        self.label_6.setText(QCoreApplication.translate("DiskHealthWindow", u"<>This Tool Use Windows Defragmentation Utility Through Powershell Sripts.", None))
    # retranslateUi

