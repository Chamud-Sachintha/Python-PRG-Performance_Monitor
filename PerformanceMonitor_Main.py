import subprocess
import sys,os
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from PySide2.QtCore import QCoreApplication, QPropertyAnimation, QDate, QDateTime,QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
import psutil
from pyqtgraph import PlotWidget
import pyqtgraph as pg
from pathlib import Path
import numpy as np
from collections import deque
import GetBasicVolumeInformations
from performance import *
from DiskDefragemntation import *
from CheckDiskHealth import *
from VolumeInformationWindow import *
from ProcessorInformationsWindow import *
from MainMemoryPerformanceWindow import *
from DiskCleanUpWindow import *
from AboutSoftwareWindow import *
from UsageWindow import *

class PerformanceMonitorMain(QMainWindow):
    def GetSelectedVolumeInformationsForWindow(self, GetCurrentDriveLetter):
        CompleteVolumeInfo = GetBasicVolumeInformations.GetSelectedVolumeInformations(self,GetCurrentDriveLetter)
        TotalSpaceOfVolume = (CompleteVolumeInfo[0][0] / (1024*1024*1024))
        TotalUsedSpaceOfVolume = (CompleteVolumeInfo[0][1] / (1024*1024*1024))
        TotalFreeSpaceOfVolume = (CompleteVolumeInfo[0][2] / (1024*1024*1024))

        VolumeAvailableFreeSpace = (TotalUsedSpaceOfVolume * 100/TotalSpaceOfVolume)
        self.diskvolume_ui.freespace_progress.setValue(VolumeAvailableFreeSpace)

        self.diskvolume_ui.selecteddrive_txt.setText(str(CompleteVolumeInfo[1]))
        self.diskvolume_ui.totalspace_txt.setText("{:.6}".format(str(TotalSpaceOfVolume)) + " " + "GB")
        self.diskvolume_ui.usedspace_txt.setText("{:.6}".format(str(TotalUsedSpaceOfVolume)) + " " + "GB")
        self.diskvolume_ui.freespace_txt.setText("{:.6}".format(str(TotalFreeSpaceOfVolume)) + " " + "GB")
        self.diskvolume_ui.volumetype_txt.setText(str(CompleteVolumeInfo[2]))

        os.chdir(GetCurrentDriveLetter)
        Directory_list = os.listdir()

        self.diskvolume_ui.file_list_edit.setText('')
        for main_dir in Directory_list:
            self.diskvolume_ui.file_list_edit.append(main_dir)

        self.diskvolume_ui.filecount_txt.setText(str(len(Directory_list)) + " " + "Items")

    def GetSelectedVolumeInformations(self, GetCurrentDriveLetter):
        CompleteVolumeInfo = GetBasicVolumeInformations.GetSelectedVolumeInformations(self,GetCurrentDriveLetter)
        TotalSpaceOfVolume = (CompleteVolumeInfo[0][0] / (1024*1024*1024))
        TotalUsedSpaceOfVolume = (CompleteVolumeInfo[0][1] / (1024*1024*1024))
        TotalFreeSpaceOfVolume = (CompleteVolumeInfo[0][2] / (1024*1024*1024))

        VolumeAvailableFreeSpace = (TotalUsedSpaceOfVolume * 100/TotalSpaceOfVolume)
        self.ui.freespace_progress.setValue(VolumeAvailableFreeSpace)

        self.ui.selecteddrive_txt.setText(str(CompleteVolumeInfo[1]))
        self.ui.totalspace_txt.setText("{:.6}".format(str(TotalSpaceOfVolume)) + " " + "GB")
        self.ui.usedspace_txt.setText("{:.6}".format(str(TotalUsedSpaceOfVolume)) + " " + "GB")
        self.ui.freespace_txt.setText("{:.6}".format(str(TotalFreeSpaceOfVolume)) + " " + "GB")
        self.ui.volumetype_txt.setText(str(CompleteVolumeInfo[2]))

    def GettingOperatingSystemInformations(self):
        OperatingSystemdetails = GetBasicVolumeInformations.GetOperatingSystemInformations(self)
        
        self.ui.sysname_txt.setText(OperatingSystemdetails[0])
        self.ui.nodename_txt.setText(OperatingSystemdetails[1])
        self.ui.release_txt.setText(OperatingSystemdetails[2])
        self.ui.version_txt.setText(OperatingSystemdetails[3])
        self.ui.machine_txt.setText(OperatingSystemdetails[4])
        self.ui.processor_txt.setText(OperatingSystemdetails[5])

        self.ui.nodename_txt2.setText(OperatingSystemdetails[1])

    def MonitorDashboardSysDiskInformations(self):
        GetSysDiskInfor = GetBasicVolumeInformations.GetCompleteDiskStorageInformationStatus()
        DiskTotalUsedSpace = (GetSysDiskInfor[1] + GetSysDiskInfor[2] + GetSysDiskInfor[3]) // (2**30)
        DiskTotalFreeSpace = ((GetSysDiskInfor[0] - (GetSysDiskInfor[1] + GetSysDiskInfor[2] + GetSysDiskInfor[3])) // (2**30))

        self.ui.disktotalspace_txt.setText(str(GetSysDiskInfor[0] // (2**30)) + " " + "GB")
        self.ui.diskusedspace_txt.setText(str(DiskTotalUsedSpace) + " " + "GB")
        self.ui.diskfreespace_txt.setText(str(DiskTotalFreeSpace) + " " + "GB")

        DiskPercentageForUsed = (100 * (DiskTotalUsedSpace / (GetSysDiskInfor[0] // (2**30))))
        DiskPercentageForFree = (100 * (DiskTotalFreeSpace / (GetSysDiskInfor[0] // (2**30))))
        self.ui.diskstorage_progress.rpb_setMaximum(100)
        self.ui.diskstorage_progress.rpb_setValue(DiskPercentageForUsed)
        self.ui.diskstorage_progress2.rpb_setValue(DiskPercentageForFree)
        self.ui.totlab_txt.setStyleSheet("background-color: #1E90FF")
        self.ui.usedspace_lab.setStyleSheet("background-color: lightgrey")

    def start_cpu_graph(self):
        # self.timeaxis = []
        # self.cpuaxis = []
        if self.current_timer_graph:
            self.current_timer_graph.stop()
            self.current_timer_graph.deleteLater()
            self.current_timer_graph = None
        self.current_timer_graph = QtCore.QTimer()
        self.current_timer_graph.timeout.connect(self.update_cpu)
        self.current_timer_graph.start(1000)

    def update_cpu(self):
        self.cpu_percent = psutil.cpu_percent()
        self.timestamp += 1

        self.deque_timestamp.append(self.timestamp)
        self.deque_cpu.append(self.cpu_percent)
        self.deque_ram.append(self.ram_percent)
        timeaxis_list = list(self.deque_timestamp)
        cpu_list = list(self.deque_cpu)

        if self.timestamp > self.graph_lim:
            self.graphwidget1.setRange(xRange=[self.timestamp-self.graph_lim+1, self.timestamp], yRange=[
                                       min(cpu_list[-self.graph_lim:]), max(cpu_list[-self.graph_lim:])])
        self.set_plotdata(name="cpu", data_x=timeaxis_list,
                          data_y=cpu_list)

    def set_plotdata(self, name, data_x, data_y):
        # print('set_data')
        if name in self.traces:
            self.traces[name].setData(data_x, data_y)
        else:
            if name == "cpu":
                self.traces[name] = self.graphwidget1.getPlotItem().plot(
                    pen=pg.mkPen((85, 170, 255), width=3))

    def OpenDifragmentationWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.difrag_ui = Ui_DefragWindow()
        self.difrag_ui.setupUi(self.window)
        self.window.setFixedSize(800,580)
        self.window.show()

        self.difrag_ui.textEdit.append("==============Press Start Disk Defragmentation Button To Start Defragmentation process==============")
        self.difrag_ui.textEdit.append("===========Windows Disk Defragmentation and Configuration management============")
        self.process = QtCore.QProcess(self)
        operatingsystem_details = GetBasicVolumeInformations.GetOperatingSystemInformations(self)

        self.difrag_ui.sysname_txt.setText(operatingsystem_details[0])
        self.difrag_ui.nodename_txt.setText(operatingsystem_details[1])
        self.difrag_ui.start_defrag_btn.clicked.connect(self.defrag_btn_clicked)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)
        self.difrag_ui.exit_btn.clicked.connect(self.exit_func)

    def exit_func(self):
        self.window.close()

    def defrag_btn_clicked(self):
        if self.difrag_ui.start_defrag_btn.text() == "Start Defragmentation":
            self.difrag_ui.start_defrag_btn.setText("Stop")
            self.difrag_ui.textEdit.clear()
            self.process.setArguments([self.difrag_ui.textEdit.setText('')])
            self.process.start("defrag", ['C:'])
            self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        elif self.difrag_ui.start_defrag_btn.text() == "Stop":
            self.process.kill()
            self.difrag_ui.textEdit.append("=======================Termineted Process=================")
            self.difrag_ui.start_defrag_btn.setText("Start Defragmentation")

    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.difrag_ui.textEdit.append(text)

    def on_finished(self):
        self.difrag_ui.start_defrag_btn.setText("Start Defragmentation")
    
    def OpenCheckDiskHealthWindow(self):
        self.Healthwindow = QtWidgets.QMainWindow()
        self.diskHealth_ui = Ui_DiskHealthWindow()
        self.diskHealth_ui.setupUi(self.Healthwindow)
        self.Healthwindow.setFixedSize(800,580)
        self.Healthwindow.show()

        self.process = QtCore.QProcess(self)
        operatingsystem_details = GetBasicVolumeInformations.GetOperatingSystemInformations(self)

        self.diskHealth_ui.processor_txt.setText(operatingsystem_details[0])
        self.diskHealth_ui.checkhealth_btn.clicked.connect(self.checkhealth_btn_clicked)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutputDiskHealth)
        self.process.finished.connect(self.on_finishedDiskHealth)
        self.diskHealth_ui.exit_btn.clicked.connect(self.exit_funcHealth)

    def exit_funcHealth(self):
        self.Healthwindow.close()

    def checkhealth_btn_clicked(self):
        if self.diskHealth_ui.checkhealth_btn.text() == "Begin Checking Disk Health":
            self.diskHealth_ui.checkhealth_btn.setText("Stop")
            self.diskHealth_ui.diskhealth_line.clear()
            self.process.setArguments([self.diskHealth_ui.diskhealth_line.setText('')])
            self.process.start("chkdsk", ['C:'])
            self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        elif self.diskHealth_ui.checkhealth_btn.text() == "Stop":
            self.process.kill()
            self.diskHealth_ui.diskhealth_line.append("=======================Termineted Process=================")
            self.diskHealth_ui.checkhealth_btn.setText("Begin Checking Disk Health")

    def on_readyReadStandardOutputDiskHealth(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.diskHealth_ui.diskhealth_line.append(text)

    def on_finishedDiskHealth(self):
        self.diskHealth_ui.checkhealth_btn.setText("Begin Checking Disk Health")
        
    def OpenVolumeInformationWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.diskvolume_ui = Ui_VolumeInformationWindow()
        self.diskvolume_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(850,580)
        self.volumewindow.show()

        drive_list = GetBasicVolumeInformations.GetBasicDriveInfo()
        for each_drive in drive_list:
            self.diskvolume_ui.drive_list_cmb.addItem(each_drive)

        OperatingSystemdetails = GetBasicVolumeInformations.GetOperatingSystemInformations(self)
        self.GetSelectedVolumeInformationsForWindow('C://')
        self.diskvolume_ui.drive_list_cmb.currentTextChanged.connect(self.GetSelectedVolumeInformationsForWindow)
        self.diskvolume_ui.processor_txt.setText(OperatingSystemdetails[5])

    def OpenCheckProcessorPerformanceWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.processor_ui = Ui_ProcessorInformationWindow()
        self.processor_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(830,550)
        self.volumewindow.show()

        self.processor_ui.totlab_txt.setStyleSheet("background-color: #1E90FF")
        self.processor_ui.usedspace_lab.setStyleSheet("background-color: lightgrey")
        OperatingSystemInformations = GetBasicVolumeInformations.GetOperatingSystemInformations(self)
        self.processor_ui.sysnodename_txt.setText("System Node Name :- " + " " + OperatingSystemInformations[1])

        self.current_timer_systemStat = QtCore.QTimer()
        self.current_timer_systemStat.timeout.connect(self.getsystemStatpercent)
        self.current_timer_systemStat.start(1000)

        cpu_frequency = psutil.cpu_freq()

        self.processor_ui.physicalName_txt.setText(str(OperatingSystemInformations[5]))
        self.processor_ui.machineName_txt.setText(str(OperatingSystemInformations[4]))
        self.processor_ui.physicalCores_txt.setText(str(psutil.cpu_count(logical=False)) + " " + "Physical Cores")
        self.processor_ui.totalCores_txt.setText(str(psutil.cpu_count(logical=True)) + " " + "Total Cores (Logical + Physical)")
        self.processor_ui.maxFrequency_txt.setText("{:.2}".format(str(cpu_frequency.max)) + " MHz")
        self.processor_ui.minFrequency_txt.setText("{:.2}".format(str(cpu_frequency.min)) + " MHz")
        self.processor_ui.currentFrequency_txt.setText("{:.2}".format(str(cpu_frequency.current)) + " MHz")

        self.layout = self.processor_ui.gridLayout
        for each_core,percentage in enumerate(psutil.cpu_percent(percpu=True ,interval=1)):
            self.core_lab = QLabel
            label_txt = "Core" + " " + str(each_core+1) + "           " + str(percentage) + "%"
            self.layout.addWidget(self.core_lab(str(label_txt)))
            self.setLayout(self.layout)

    def getsystemStatpercent(self):
        # gives a single float value
        self.cpu_percent = psutil.cpu_percent()
        self.processor_ui.cpu_usage_progress.rpb_setValue(self.cpu_percent)

    def getMemoryStatpercent(self):
        # gives a single float value
        self.ram_percent = psutil.virtual_memory().percent
        self.memory_ui.memory_usage_progress.rpb_setValue(self.ram_percent)

    def OpenCheckMainMemoryPerformanceWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.memory_ui = Ui_MainmemoryPerformanceWindow()
        self.memory_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(830,550)
        self.volumewindow.show()

        svmem = psutil.virtual_memory()

        self.current_timer_systemStat = QtCore.QTimer()
        self.current_timer_systemStat.timeout.connect(self.getMemoryStatpercent)
        self.current_timer_systemStat.start(1000)
        OperatingSystemInformations = GetBasicVolumeInformations.GetOperatingSystemInformations(self)

        self.memory_ui.totmem_txt.setText("{:.6}".format(str((svmem.total)/(1024*1024))) + " " + "GB")
        self.memory_ui.usedmem_txt.setText("{:.6}".format(str((svmem.used)/(1024*1024))) + " " + "GB")
        self.memory_ui.freespacemem_txt.setText("{:.6}".format(str((svmem.available)/(1024*1024))) + " " + "GB")
        self.memory_ui.percentagemem_txt.setText(str(svmem.percent) + " " + "%")

        swap_mem = psutil.swap_memory()

        self.memory_ui.swaptot_txt.setText("{:.6}".format(str((swap_mem.total)/(1024*1024))) + " " + "GB")
        self.memory_ui.swapused_txt.setText("{:.6}".format(str((swap_mem.used)/(1024*1024))) + " " + "GB")
        self.memory_ui.swapfree_txt.setText("{:.6}".format(str((swap_mem.free)/(1024*1024))) + " " + "GB")
        self.memory_ui.swappercentage_txt.setText(str(swap_mem.percent) + " " + "%")

        self.memory_ui.sysnodename_txt.setText("System Node Name :- " + str(OperatingSystemInformations[1]))

    def OpenDiskCleanUpWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.diskcleanup_ui = Ui_DiskCleanupWindow()
        self.diskcleanup_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(830,550)
        self.volumewindow.show()

        self.process = QtCore.QProcess(self)
        operatingsystem_details = GetBasicVolumeInformations.GetOperatingSystemInformations(self)

        self.diskcleanup_ui.diskcleanup_btn.clicked.connect(self.diskcleanup_btn_clicked)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutputDiskCleanUp)
        self.process.finished.connect(self.on_finishedDiskCleanUp)
        self.diskcleanup_ui.exit_btn.clicked.connect(self.exit_funcDiskCleanUp)

    def diskcleanup_btn_clicked(self):
        if self.diskcleanup_ui.diskcleanup_btn.text() == "Begin Disk Clean Up Process":
            self.diskcleanup_ui.diskcleanup_btn.setText("Stop")
            self.diskcleanup_ui.diskcleanup_edit.clear()
            self.process.setArguments([self.diskcleanup_ui.diskcleanup_edit.setText('')])
            self.process.start("cleanmgr" ,['/sageset: 1'])
            self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        elif self.diskcleanup_ui.diskcleanup_btn.text() == "Stop":
            self.process.kill()
            self.diskcleanup_ui.diskcleanup_edit.append("=======================Termineted Process=================")
            self.diskcleanup_ui.diskcleanup_btn.setText("Begin Disk Clean Up Process")

    def on_readyReadStandardOutputDiskCleanUp(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.diskcleanup_ui.diskcleanup_edit.append(text)

    def on_finishedDiskCleanUp(self):
        self.diskcleanup_ui.diskcleanup_btn.setText("Begin Disk Clean Up Process")

    def exit_funcDiskCleanUp(self):
        self.volumewindow.close()

    def OpenAboutSoftwareWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.aboutsoftware_ui = Ui_AboutSoftwareWindow()
        self.aboutsoftware_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(800,400)
        self.volumewindow.show()

    def OpenSoftwareUsageWindow(self):
        self.volumewindow = QtWidgets.QMainWindow()
        self.usage_ui = Ui_UsageWindow()
        self.usage_ui.setupUi(self.volumewindow)
        self.volumewindow.setFixedSize(800,550)
        self.volumewindow.show()

    def ExitTabPress(self):
        sys.exit()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.showMaximized()

        self.ui.actionStart_Disk_Defragmentation.triggered.connect(self.OpenDifragmentationWindow)
        self.ui.actionCheck_Disk_Health.triggered.connect(self.OpenCheckDiskHealthWindow)
        self.ui.actionGet_Volume_Informations.triggered.connect(self.OpenVolumeInformationWindow)
        self.ui.actionProcessor_Performance.triggered.connect(self.OpenCheckProcessorPerformanceWindow)
        self.ui.actionMemory_Performance.triggered.connect(self.OpenCheckMainMemoryPerformanceWindow)
        self.ui.actionClean_Disk_2.triggered.connect(self.OpenDiskCleanUpWindow)
        self.ui.actionAbout.triggered.connect(self.OpenAboutSoftwareWindow)
        self.ui.actionHow_To.triggered.connect(self.OpenSoftwareUsageWindow)
        self.ui.actionExit.triggered.connect(self.ExitTabPress)
        drive_list = GetBasicVolumeInformations.GetBasicDriveInfo()

        for each_drive in drive_list:
            self.ui.drive_list_cmb.addItem(each_drive)

        self.MonitorDashboardSysDiskInformations()
        self.GettingOperatingSystemInformations()
        self.GetSelectedVolumeInformations('C://')
        self.ui.drive_list_cmb.currentTextChanged.connect(self.GetSelectedVolumeInformations)

        self.cpu_percent = 0
        self.ram_percent = 0
        self.traces = dict()
        self.timestamp = 0
        self.timeaxis = []
        self.cpuaxis = []
        self.ramaxis = []

        self.current_timer_graph = None
        self.graph_lim = 15
        self.deque_timestamp = deque([], maxlen=self.graph_lim+20)
        self.deque_cpu = deque([], maxlen=self.graph_lim+20)
        self.deque_ram = deque([], maxlen=self.graph_lim+20)

        self.graphwidget1 = PlotWidget(title="CPU Performance Percentage Average")
        x1_axis = self.graphwidget1.getAxis('bottom')
        x1_axis.setLabel(text='Time since start (s)')
        y1_axis = self.graphwidget1.getAxis('left')
        y1_axis.setLabel(text='Percent')

        self.ui.gridLayout.addWidget(self.graphwidget1, 0, 0, 1, 3)
        self.start_cpu_graph()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    windows = PerformanceMonitorMain()
    sys.exit(app.exec_())