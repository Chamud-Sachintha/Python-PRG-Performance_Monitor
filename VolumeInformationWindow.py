# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VolumeInformationWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VolumeInformationWindow(object):
    def setupUi(self, VolumeInformationWindow):
        if not VolumeInformationWindow.objectName():
            VolumeInformationWindow.setObjectName(u"VolumeInformationWindow")
        VolumeInformationWindow.resize(843, 600)
        self.centralwidget = QWidget(VolumeInformationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 311, 31))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 50, 331, 501))
        self.groupBox.setFont(font)
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 50, 181, 31))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_8.setFont(font1)
        self.drive_list_cmb = QComboBox(self.groupBox)
        self.drive_list_cmb.setObjectName(u"drive_list_cmb")
        self.drive_list_cmb.setGeometry(QRect(190, 51, 131, 31))
        self.drive_list_cmb.setFont(font1)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 100, 161, 21))
        self.label_9.setFont(font1)
        self.freespace_progress = QProgressBar(self.groupBox)
        self.freespace_progress.setObjectName(u"freespace_progress")
        self.freespace_progress.setGeometry(QRect(10, 130, 311, 41))
        self.freespace_progress.setValue(24)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 180, 141, 21))
        self.label_10.setFont(font1)
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 210, 161, 21))
        self.label_11.setFont(font1)
        self.label_12 = QLabel(self.groupBox)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 240, 191, 21))
        self.label_12.setFont(font1)
        self.label_13 = QLabel(self.groupBox)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 310, 191, 21))
        self.label_13.setFont(font1)
        self.line_2 = QFrame(self.groupBox)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(17, 280, 291, 20))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.selecteddrive_txt = QLabel(self.groupBox)
        self.selecteddrive_txt.setObjectName(u"selecteddrive_txt")
        self.selecteddrive_txt.setGeometry(QRect(170, 100, 131, 21))
        self.selecteddrive_txt.setFont(font1)
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 430, 301, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.pushButton.setFont(font2)
        self.totalspace_txt = QLabel(self.groupBox)
        self.totalspace_txt.setObjectName(u"totalspace_txt")
        self.totalspace_txt.setGeometry(QRect(210, 180, 91, 21))
        self.totalspace_txt.setFont(font1)
        self.usedspace_txt = QLabel(self.groupBox)
        self.usedspace_txt.setObjectName(u"usedspace_txt")
        self.usedspace_txt.setGeometry(QRect(210, 210, 81, 21))
        self.usedspace_txt.setFont(font1)
        self.freespace_txt = QLabel(self.groupBox)
        self.freespace_txt.setObjectName(u"freespace_txt")
        self.freespace_txt.setGeometry(QRect(210, 240, 91, 21))
        self.freespace_txt.setFont(font1)
        self.volumetype_txt = QLabel(self.groupBox)
        self.volumetype_txt.setObjectName(u"volumetype_txt")
        self.volumetype_txt.setGeometry(QRect(110, 310, 91, 21))
        self.volumetype_txt.setFont(font1)
        self.processor_txt = QLabel(self.groupBox)
        self.processor_txt.setObjectName(u"processor_txt")
        self.processor_txt.setGeometry(QRect(110, 340, 171, 21))
        self.processor_txt.setFont(font1)
        self.label_14 = QLabel(self.groupBox)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 340, 191, 21))
        self.label_14.setFont(font1)
        self.filecount_txt = QLabel(self.groupBox)
        self.filecount_txt.setObjectName(u"filecount_txt")
        self.filecount_txt.setGeometry(QRect(110, 390, 91, 21))
        self.filecount_txt.setFont(font1)
        self.label_16 = QLabel(self.groupBox)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(10, 390, 81, 21))
        self.label_16.setFont(font1)
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(350, 60, 20, 491))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.file_list_edit = QTextEdit(self.centralwidget)
        self.file_list_edit.setObjectName(u"file_list_edit")
        self.file_list_edit.setGeometry(QRect(380, 90, 451, 461))
        self.label_15 = QLabel(self.centralwidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(380, 60, 261, 21))
        self.label_15.setFont(font1)
        VolumeInformationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VolumeInformationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 21))
        VolumeInformationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VolumeInformationWindow)
        self.statusbar.setObjectName(u"statusbar")
        VolumeInformationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VolumeInformationWindow)

        QMetaObject.connectSlotsByName(VolumeInformationWindow)
    # setupUi

    def retranslateUi(self, VolumeInformationWindow):
        VolumeInformationWindow.setWindowTitle(QCoreApplication.translate("VolumeInformationWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("VolumeInformationWindow", u"System Volume Informations", None))
        self.groupBox.setTitle(QCoreApplication.translate("VolumeInformationWindow", u"Volume Informations", None))
        self.label_8.setText(QCoreApplication.translate("VolumeInformationWindow", u"Choose Your Volume Letter :- ", None))
        self.label_9.setText(QCoreApplication.translate("VolumeInformationWindow", u"Selected Volume Name :- ", None))
        self.label_10.setText(QCoreApplication.translate("VolumeInformationWindow", u"Total Volume Space :- ", None))
        self.label_11.setText(QCoreApplication.translate("VolumeInformationWindow", u"Total Used Volume Space :- ", None))
        self.label_12.setText(QCoreApplication.translate("VolumeInformationWindow", u"Total Available Volume Space :- ", None))
        self.label_13.setText(QCoreApplication.translate("VolumeInformationWindow", u"Volume Type :- ", None))
        self.selecteddrive_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.pushButton.setText(QCoreApplication.translate("VolumeInformationWindow", u"Refresh Volume List", None))
        self.totalspace_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.usedspace_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.freespace_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.volumetype_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.processor_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.label_14.setText(QCoreApplication.translate("VolumeInformationWindow", u"Processor :- ", None))
        self.filecount_txt.setText(QCoreApplication.translate("VolumeInformationWindow", u"...", None))
        self.label_16.setText(QCoreApplication.translate("VolumeInformationWindow", u"File Count :- ", None))
        self.label_15.setText(QCoreApplication.translate("VolumeInformationWindow", u"Selected Volume Directory & Files Structure", None))
    # retranslateUi

