# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DiskDefragemntation.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DefragWindow(object):
    def setupUi(self, DefragWindow):
        if not DefragWindow.objectName():
            DefragWindow.setObjectName(u"DefragWindow")
        DefragWindow.resize(800, 600)
        self.centralwidget = QWidget(DefragWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 130, 761, 251))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 311, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.nodename_txt = QLabel(self.centralwidget)
        self.nodename_txt.setObjectName(u"nodename_txt")
        self.nodename_txt.setGeometry(QRect(120, 80, 151, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.nodename_txt.setFont(font1)
        self.sysname_txt = QLabel(self.centralwidget)
        self.sysname_txt.setObjectName(u"sysname_txt")
        self.sysname_txt.setGeometry(QRect(120, 50, 101, 21))
        self.sysname_txt.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 111, 21))
        self.label_3.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 101, 21))
        self.label_2.setFont(font1)
        self.start_defrag_btn = QPushButton(self.centralwidget)
        self.start_defrag_btn.setObjectName(u"start_defrag_btn")
        self.start_defrag_btn.setGeometry(QRect(570, 40, 211, 31))
        self.start_defrag_btn.setFont(font1)
        self.exit_btn = QPushButton(self.centralwidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setGeometry(QRect(570, 80, 211, 31))
        self.exit_btn.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 410, 561, 21))
        self.label_4.setFont(font1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 440, 661, 21))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 470, 661, 21))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 500, 821, 21))
        self.label_7.setFont(font1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 520, 371, 21))
        self.label_8.setFont(font1)
        DefragWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DefragWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        DefragWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DefragWindow)
        self.statusbar.setObjectName(u"statusbar")
        DefragWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DefragWindow)

        QMetaObject.connectSlotsByName(DefragWindow)
    # setupUi

    def retranslateUi(self, DefragWindow):
        DefragWindow.setWindowTitle(QCoreApplication.translate("DefragWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("DefragWindow", u"Start Disk Defragmentation Process", None))
        self.nodename_txt.setText(QCoreApplication.translate("DefragWindow", u"...", None))
        self.sysname_txt.setText(QCoreApplication.translate("DefragWindow", u"...", None))
        self.label_3.setText(QCoreApplication.translate("DefragWindow", u"Node Name :- ", None))
        self.label_2.setText(QCoreApplication.translate("DefragWindow", u"Sys name :- ", None))
        self.start_defrag_btn.setText(QCoreApplication.translate("DefragWindow", u"Start Defragmentation", None))
        self.exit_btn.setText(QCoreApplication.translate("DefragWindow", u"Exit To Main Window", None))
        self.label_4.setText(QCoreApplication.translate("DefragWindow", u"<>This Defragmentation Process Is required By Full Administrative Privillages Of your Computer.", None))
        self.label_5.setText(QCoreApplication.translate("DefragWindow", u"<>Therefore Run This Tool Under Your Administrative Privillages By Right clicking the tool and run as Administrator.", None))
        self.label_6.setText(QCoreApplication.translate("DefragWindow", u"<>This Tool Use Windows Defragmentation Utility Through Powershell Sripts.", None))
        self.label_7.setText(QCoreApplication.translate("DefragWindow", u"<>This Tool Will Run Both 32 bit - and 64 bit workstations and sometimes result box will not apper while disk defragmentation but ,", None))
        self.label_8.setText(QCoreApplication.translate("DefragWindow", u"after the defragmentation the results will show the Results Box.", None))
    # retranslateUi

