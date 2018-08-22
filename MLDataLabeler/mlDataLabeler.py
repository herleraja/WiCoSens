# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\HackoMan\Google Drive\MasterThesis\Code\QtDesigner\Lable_Data.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import traceback
import os
import sys
import serial
import atexit
import colorSpaceUtil

ser = None
file = None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 719)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Icon/research4-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainTabObj = QtWidgets.QTabWidget(self.centralwidget)
        self.mainTabObj.setToolTip("")
        self.mainTabObj.setMovable(True)
        self.mainTabObj.setTabBarAutoHide(True)
        self.mainTabObj.setObjectName("mainTabObj")
        self.dataLabelingTab = QtWidgets.QWidget()
        self.dataLabelingTab.setObjectName("dataLabelingTab")
        self.formLayoutWidget = QtWidgets.QWidget(self.dataLabelingTab)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1287, 631))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.dataLabelingTabGridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.dataLabelingTabGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.dataLabelingTabGridLayout.setContentsMargins(0, 0, 0, 0)
        self.dataLabelingTabGridLayout.setObjectName("dataLabelingTabGridLayout")
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLineEdit, 0, 1, 1, 1)
        self.sensorButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.sensorButtonHorizontalLayout.setObjectName("sensorButtonHorizontalLayout")
        self.colSensorButton1 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton1.setAcceptDrops(False)
        self.colSensorButton1.setCheckable(True)
        self.colSensorButton1.setChecked(True)
        self.colSensorButton1.setObjectName("colSensorButton1")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton1)
        self.colSensorButton2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton2.setCheckable(True)
        self.colSensorButton2.setChecked(True)
        self.colSensorButton2.setObjectName("colSensorButton2")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton2)
        self.colSensorButton3 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton3.setCheckable(True)
        self.colSensorButton3.setChecked(True)
        self.colSensorButton3.setObjectName("colSensorButton3")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton3)
        self.colSensorButton4 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton4.setCheckable(True)
        self.colSensorButton4.setChecked(True)
        self.colSensorButton4.setObjectName("colSensorButton4")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton4)
        self.colSensorButton5 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton5.setCheckable(True)
        self.colSensorButton5.setChecked(True)
        self.colSensorButton5.setObjectName("colSensorButton5")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton5)
        self.colSensorButton6 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton6.setCheckable(True)
        self.colSensorButton6.setChecked(True)
        self.colSensorButton6.setObjectName("colSensorButton6")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton6)
        self.colSensorButton7 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton7.setCheckable(True)
        self.colSensorButton7.setChecked(True)
        self.colSensorButton7.setObjectName("colSensorButton7")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton7)
        self.colSensorButton8 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton8.setCheckable(True)
        self.colSensorButton8.setChecked(True)
        self.colSensorButton8.setObjectName("colSensorButton8")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton8)
        self.colSensorButton9 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton9.setCheckable(True)
        self.colSensorButton9.setChecked(True)
        self.colSensorButton9.setObjectName("colSensorButton9")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton9)
        self.colSensorButton10 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton10.setCheckable(True)
        self.colSensorButton10.setChecked(True)
        self.colSensorButton10.setObjectName("colSensorButton10")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton10)
        self.colSensorButton11 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton11.setCheckable(True)
        self.colSensorButton11.setChecked(True)
        self.colSensorButton11.setObjectName("colSensorButton11")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton11)
        self.colSensorButton12 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colSensorButton12.setCheckable(True)
        self.colSensorButton12.setChecked(True)
        self.colSensorButton12.setObjectName("colSensorButton12")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton12)
        self.dataLabelingTabGridLayout.addLayout(self.sensorButtonHorizontalLayout, 2, 1, 1, 1)
        self.classLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classLabelLabel.setObjectName("classLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLabel, 1, 0, 1, 1)
        self.sensorEnableDisableLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorEnableDisableLabel.setObjectName("sensorEnableDisableLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorEnableDisableLabel, 2, 0, 1, 1)
        self.captureLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.captureLabel.setObjectName("captureLabel")
        self.dataLabelingTabGridLayout.addWidget(self.captureLabel, 4, 0, 1, 1)
        self.closeResetHLayout = QtWidgets.QHBoxLayout()
        self.closeResetHLayout.setObjectName("closeResetHLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.closeResetHLayout.addItem(spacerItem)
        self.resetBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.resetBtn.setObjectName("resetBtn")
        self.closeResetHLayout.addWidget(self.resetBtn)
        self.closeBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.closeBtn.setObjectName("closeBtn")
        self.closeResetHLayout.addWidget(self.closeBtn)
        self.dataLabelingTabGridLayout.addLayout(self.closeResetHLayout, 9, 1, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLabel, 0, 0, 1, 1)
        self.capturSensorDataHLayout = QtWidgets.QHBoxLayout()
        self.capturSensorDataHLayout.setObjectName("capturSensorDataHLayout")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.capturSensorDataHLayout.addItem(spacerItem1)
        self.startCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.startCaptureBtn.setMouseTracking(False)
        self.startCaptureBtn.setObjectName("startCaptureBtn")
        self.capturSensorDataHLayout.addWidget(self.startCaptureBtn)
        self.stopCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.stopCaptureBtn.setEnabled(False)
        self.stopCaptureBtn.setObjectName("stopCaptureBtn")
        self.capturSensorDataHLayout.addWidget(self.stopCaptureBtn)
        self.dataLabelingTabGridLayout.addLayout(self.capturSensorDataHLayout, 4, 1, 1, 1)
        self.sensorTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sensorTextEdit.setUndoRedoEnabled(False)
        self.sensorTextEdit.setReadOnly(True)
        self.sensorTextEdit.setObjectName("sensorTextEdit")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextEdit, 5, 1, 1, 1)
        self.classLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.classLabelLineEdit.setObjectName("classLabelLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLineEdit, 1, 1, 1, 1)
        self.sensorTextLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorTextLabel.setObjectName("sensorTextLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextLabel, 5, 0, 1, 1)
        self.colorSpaceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.colorSpaceLabel.setObjectName("colorSpaceLabel")
        self.dataLabelingTabGridLayout.addWidget(self.colorSpaceLabel, 3, 0, 1, 1)
        self.colorSpaceButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.colorSpaceButtonsHorizontalLayout.setObjectName("colorSpaceButtonsHorizontalLayout")
        self.colorSpaceXYZButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colorSpaceXYZButton.setCheckable(True)
        self.colorSpaceXYZButton.setAutoExclusive(True)
        self.colorSpaceXYZButton.setObjectName("colorSpaceXYZButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceXYZButton)
        self.colorSpaceLabButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colorSpaceLabButton.setCheckable(True)
        self.colorSpaceLabButton.setAutoExclusive(True)
        self.colorSpaceLabButton.setObjectName("colorSpaceLabButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceLabButton)
        self.colorSpaceYCbCrButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colorSpaceYCbCrButton.setCheckable(True)
        self.colorSpaceYCbCrButton.setAutoExclusive(True)
        self.colorSpaceYCbCrButton.setObjectName("colorSpaceYCbCrButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceYCbCrButton)
        self.colorSpaceRGBButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colorSpaceRGBButton.setCheckable(True)
        self.colorSpaceRGBButton.setChecked(True)

        self.colorSpaceRGBButton.setAutoExclusive(True)
        self.colorSpaceRGBButton.setObjectName("colorSpaceRGBButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceRGBButton)
        self.colorSpaceHSVButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.colorSpaceHSVButton.setCheckable(True)
        #self.colorSpaceHSVButton.setChecked(True)
        self.colorSpaceHSVButton.setAutoExclusive(True)
        self.colorSpaceHSVButton.setObjectName("colorSpaceHSVButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceHSVButton)
        self.dataLabelingTabGridLayout.addLayout(self.colorSpaceButtonsHorizontalLayout, 3, 1, 1, 1)
        self.mainTabObj.addTab(self.dataLabelingTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.settingTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 10, 351, 131))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.settingTabMainGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.settingTabMainGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.settingTabMainGridLayout.setContentsMargins(0, 0, 0, 0)
        self.settingTabMainGridLayout.setObjectName("settingTabMainGridLayout")
        self.setialPortSettingsVerticalLayout = QtWidgets.QVBoxLayout()
        self.setialPortSettingsVerticalLayout.setObjectName("setialPortSettingsVerticalLayout")
        self.baudrateHorizontalLayout = QtWidgets.QHBoxLayout()
        self.baudrateHorizontalLayout.setObjectName("baudrateHorizontalLayout")
        self.baudrateLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.baudrateLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.baudrateLabel.setObjectName("baudrateLabel")
        self.baudrateHorizontalLayout.addWidget(self.baudrateLabel)
        self.baudrateComboBox = QtWidgets.QComboBox(self.gridLayoutWidget_2)
        self.baudrateComboBox.setMaxVisibleItems(20)
        self.baudrateComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.baudrateComboBox.setObjectName("baudrateComboBox")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateComboBox.addItem("")
        self.baudrateHorizontalLayout.addWidget(self.baudrateComboBox)
        self.setialPortSettingsVerticalLayout.addLayout(self.baudrateHorizontalLayout)
        self.portHorizontalLayout = QtWidgets.QHBoxLayout()
        self.portHorizontalLayout.setObjectName("portHorizontalLayout")
        self.portLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.portLabel.setObjectName("portLabel")
        self.portHorizontalLayout.addWidget(self.portLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHorizontalLayout.addItem(spacerItem2)
        self.portlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.portlineEdit.setObjectName("portlineEdit")
        self.portHorizontalLayout.addWidget(self.portlineEdit)
        self.setialPortSettingsVerticalLayout.addLayout(self.portHorizontalLayout)
        self.settingTabMainGridLayout.addLayout(self.setialPortSettingsVerticalLayout, 0, 1, 1, 1)
        self.serialPortSettingsLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serialPortSettingsLabel.setObjectName("serialPortSettingsLabel")
        self.settingTabMainGridLayout.addWidget(self.serialPortSettingsLabel, 0, 0, 1, 1)
        self.recordingFolderLocationhorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingFolderLocationhorizontalLayout.setObjectName("recordingFolderLocationhorizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingFolderLocationhorizontalLayout.addItem(spacerItem3)
        self.recordingFolderLocationLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.recordingFolderLocationLineEdit.setObjectName("recordingFolderLocationLineEdit")
        self.recordingFolderLocationhorizontalLayout.addWidget(self.recordingFolderLocationLineEdit)
        self.settingTabMainGridLayout.addLayout(self.recordingFolderLocationhorizontalLayout, 1, 1, 1, 1)
        self.recordingFolderLocationLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.recordingFolderLocationLabel.setObjectName("recordingFolderLocationLabel")
        self.settingTabMainGridLayout.addWidget(self.recordingFolderLocationLabel, 1, 0, 1, 1)
        self.mainTabObj.addTab(self.settingTab, "")
        self.classifierTab = QtWidgets.QWidget()
        self.classifierTab.setObjectName("classifierTab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.classifierTab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1321, 801))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.classifierTabGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.classifierTabGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.classifierTabGridLayout.setContentsMargins(0, 0, 0, 0)
        self.classifierTabGridLayout.setObjectName("classifierTabGridLayout")
        self.mainTabObj.addTab(self.classifierTab, "")
        self.gridLayout.addWidget(self.mainTabObj, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabObj.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #self.setUpSerialPort()
        self.addButtonOperations()
        self.addFiledsValidators()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Collection"))
        self.colSensorButton1.setText(_translate("MainWindow", "R5"))
        self.colSensorButton2.setText(_translate("MainWindow", "R4"))
        self.colSensorButton3.setText(_translate("MainWindow", "R3"))
        self.colSensorButton4.setText(_translate("MainWindow", "R2"))
        self.colSensorButton5.setText(_translate("MainWindow", "R1"))
        self.colSensorButton6.setText(_translate("MainWindow", "R0"))
        self.colSensorButton7.setText(_translate("MainWindow", "M"))
        self.colSensorButton8.setText(_translate("MainWindow", "L1"))
        self.colSensorButton9.setText(_translate("MainWindow", "L2"))
        self.colSensorButton10.setText(_translate("MainWindow", "L3"))
        self.colSensorButton11.setText(_translate("MainWindow", "L4"))
        self.colSensorButton12.setText(_translate("MainWindow", "L5"))
        self.classLabelLabel.setText(_translate("MainWindow", "ClassLabel"))
        self.sensorEnableDisableLabel.setText(_translate("MainWindow", "Enable / Disable Color Sensor"))
        self.captureLabel.setText(_translate("MainWindow", "Capture Sensor Data"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start"))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop"))
        self.sensorTextLabel.setText(_translate("MainWindow", "Captured Sensor Data"))
        self.colorSpaceLabel.setText(_translate("MainWindow", "Color Space"))
        self.colorSpaceXYZButton.setText(_translate("MainWindow", "XYZ"))
        self.colorSpaceLabButton.setText(_translate("MainWindow", "L*a*b*"))
        self.colorSpaceYCbCrButton.setText(_translate("MainWindow", "YCbCr"))
        self.colorSpaceRGBButton.setText(_translate("MainWindow", "RGB"))
        self.colorSpaceHSVButton.setText(_translate("MainWindow", "HSV"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.dataLabelingTab), _translate("MainWindow", "Data labeling"))
        self.baudrateLabel.setText(_translate("MainWindow", "Baudrate"))
        self.baudrateComboBox.setCurrentText(_translate("MainWindow", "115200"))
        self.baudrateComboBox.setItemText(0, _translate("MainWindow", "115200"))
        self.baudrateComboBox.setItemText(1, _translate("MainWindow", "57600"))
        self.baudrateComboBox.setItemText(2, _translate("MainWindow", "38400"))
        self.baudrateComboBox.setItemText(3, _translate("MainWindow", "28800"))
        self.baudrateComboBox.setItemText(4, _translate("MainWindow", "19200"))
        self.baudrateComboBox.setItemText(5, _translate("MainWindow", "14400"))
        self.baudrateComboBox.setItemText(6, _translate("MainWindow", "9600"))
        self.baudrateComboBox.setItemText(7, _translate("MainWindow", "4800"))
        self.baudrateComboBox.setItemText(8, _translate("MainWindow", "2400"))
        self.baudrateComboBox.setItemText(9, _translate("MainWindow", "1200"))
        self.baudrateComboBox.setItemText(10, _translate("MainWindow", "900"))
        self.baudrateComboBox.setItemText(11, _translate("MainWindow", "600"))
        self.baudrateComboBox.setItemText(12, _translate("MainWindow", "300"))
        self.portLabel.setText(_translate("MainWindow", "Port"))
        self.portlineEdit.setText(_translate("MainWindow", "COM3"))
        self.serialPortSettingsLabel.setText(_translate("MainWindow", "Serial Port Settings"))
        self.recordingFolderLocationLineEdit.setText(_translate("MainWindow", "recording_folder/"))
        self.recordingFolderLocationLabel.setText(_translate("MainWindow", "Recording Folder Location"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.settingTab), _translate("MainWindow", "Settings"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.classifierTab), _translate("MainWindow", "Classify"))



    def setUpSerialPort(self):
        baudrate = self.baudrateComboBox.currentText()
        port = self.portlineEdit.text()
        if hasattr(self, 'ser') and self.ser.isOpen():
            return
        self.ser = serial.Serial(port, int(baudrate), timeout=None)

    def addButtonOperations(self):
        self.closeBtn.clicked.connect(self.closeWindow)
        self.resetBtn.clicked.connect(self.resetFields)
        self.startCaptureBtn.clicked.connect(self.startCaptureBtnPressedEvent)
        self.stopCaptureBtn.clicked.connect(self.stopCaptureSensorData)

    def addFiledsValidators(self):

        regexp = QtCore.QRegExp('[a-zA-Z0-9_ -]+')
        validator = QtGui.QRegExpValidator(regexp)

        self.fileNameLineEdit.setValidator(validator)
        self.classLabelLineEdit.setValidator(validator)


    def captureSensorData(self):
        try:

            current_label = self.classLabelLineEdit.text()

            new_line = self.ser.readline().decode('utf-8').rstrip()
            #new_line = "test1, Test2, Test3"

            ## frame contains accel+ color data
            line_array = new_line.split(',')

            if line_array.__len__() == 54:

                new_line = line_array[0] + ',' + line_array[1] + ',' +line_array[2] + ',' +line_array[3]

                #for i in (6,10,14,18,22,26,30,34,38,42,46,50):
                #    new_line += self.rgb2hsv(float(line_array[i]), float(line_array[i+1]), float(line_array[i+2]),float(line_array[i+3]))


                if self.colSensorButton1.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[6]),float(line_array[7]),float(line_array[8]),float(line_array[9]))   # Right side(R5) sensor
                if self.colSensorButton2.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[10]), float(line_array[11]), float(line_array[12]),float(line_array[13]))  # Right side(R4) sensor
                if self.colSensorButton3.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[14]),float(line_array[15]),float(line_array[16]),float(line_array[17]))   # Right side(R3) sensor
                if self.colSensorButton4.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[18]), float(line_array[19]), float(line_array[20]),float(line_array[21]))  # Right side(R2) sensor
                if self.colSensorButton5.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[22]),float(line_array[23]),float(line_array[24]),float(line_array[25]))   # Right side(R1) sensor
                if self.colSensorButton6.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[26]), float(line_array[27]), float(line_array[28]),float(line_array[29]))  # Right side(R0) sensor
                if self.colSensorButton7.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[30]), float(line_array[31]), float(line_array[32]),float(line_array[33]))  # middle sensor
                if self.colSensorButton8.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[34]),float(line_array[35]),float(line_array[36]),float(line_array[37]))   # Left side(L1) sensor
                if self.colSensorButton9.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[38]), float(line_array[39]), float(line_array[40]),float(line_array[41]))  # Left side(L2) sensor
                if self.colSensorButton10.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[42]),float(line_array[43]),float(line_array[44]),float(line_array[45]))   # Left side(L3) sensor
                if self.colSensorButton11.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[46]), float(line_array[47]), float(line_array[48]),float(line_array[49]))  # Left side(L4) sensor
                if self.colSensorButton12.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[50]), float(line_array[51]), float(line_array[52]),float(line_array[53]))  # Left side(L5) sensor


                new_line = new_line + ',' + current_label + '\n'

                self.file.write(new_line)
                self.file.flush()

                self.sensorTextEdit.append(new_line)
                self.sensorTextEdit.repaint()

            if not self.startCaptureBtn.isEnabled():
                QtCore.QTimer.singleShot(1, self.captureSensorData)
            else:
                self.file.close()
        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def colorSpaceCoverstion(self, r, g, b, c):

        if self.colorSpaceHSVButton.isChecked():
            colorSpaceCoverstionFunction = colorSpaceUtil.switcher.get('HSV')
        elif self.colorSpaceYCbCrButton.isChecked():
            colorSpaceCoverstionFunction = colorSpaceUtil.switcher.get('YCbCr')
        elif self.colorSpaceLabButton.isChecked():
            colorSpaceCoverstionFunction = colorSpaceUtil.switcher.get('Lab')
        elif self.colorSpaceXYZButton.isChecked():
            colorSpaceCoverstionFunction = colorSpaceUtil.switcher.get('XYZ')
        elif self.colorSpaceRGBButton.isChecked():
            colorSpaceCoverstionFunction = colorSpaceUtil.switcher.get('RGB')

        color1, color2, color3 = colorSpaceCoverstionFunction(r, g, b, c)
        return ',' + str(color1) + ',' + str(color2) + ',' + str(color3)


    def startCaptureBtnPressedEvent(self):
        try:
            if(self.isValidFields()):
                print("Data stored in file: << {0} >> and file located in : << {1} >> ".format(self.fileNameLineEdit.text(),self.recordingFolderLocationLineEdit.text()))
                self.startCaptureBtn.setEnabled(False)
                self.stopCaptureBtn.setEnabled(True)

                self.startCaptureBtn.repaint()
                self.stopCaptureBtn.repaint()

                self.setUpSerialPort()
                self.openFileForWriting()  # Create/Open file for saving sensor data


                if not self.startCaptureBtn.isEnabled():
                    QtCore.QTimer.singleShot(1, self.captureSensorData)

            else:
                self.displayWarningPopUp("Please fill the required fields !!")

        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())


    def openFileForWriting(self):
        write_path = self.recordingFolderLocationLineEdit.text()
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        file_name = self.fileNameLineEdit.text()
        file_name  = write_path + file_name + ".csv"
        self.file = open(file_name, 'a')

    def stopCaptureSensorData(self):

        self.startCaptureBtn.setEnabled(True)
        self.stopCaptureBtn.setEnabled(False)

        self.startCaptureBtn.repaint()
        self.stopCaptureBtn.repaint()


    def isValidFields(self):
        return self.fileNameLineEdit.text().__len__()>0 and self.classLabelLineEdit.text().__len__()>0 and self.recordingFolderLocationLineEdit.text().__len__()>0

    def resetFields(self):
        if self.startCaptureBtn.isEnabled():
            self.fileNameLineEdit.clear()
            self.classLabelLineEdit.clear()
            self.sensorTextEdit.clear()
            self.colSensorButton1.setChecked(True)
            self.colSensorButton2.setChecked(True)
            self.colSensorButton3.setChecked(True)
            self.colSensorButton4.setChecked(True)
            self.colSensorButton5.setChecked(True)
            self.colSensorButton6.setChecked(True)
            self.colSensorButton7.setChecked(True)
            self.colSensorButton8.setChecked(True)
            self.colSensorButton9.setChecked(True)
            self.colSensorButton10.setChecked(True)
            self.colSensorButton11.setChecked(True)
            self.colSensorButton12.setChecked(True)
            self.colorSpaceHSVButton.setChecked(False)
            self.colorSpaceYCbCrButton.setChecked(False)
            self.colorSpaceLabButton.setChecked(False)
            self.colorSpaceXYZButton.setChecked(False)
            self.colorSpaceRGBButton.setChecked(True)

        else:
            self.displayWarningPopUp("Please stop capturing data before the reset")


    def displayWarningPopUp(self, warningText="Warning !!"):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText(warningText)
        msgBox.setWindowTitle("Warning !! ")
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.exec()

    def closeWindow(self):
        QtCore.QCoreApplication.instance().quit()


    def releaseResource(self):
        print("Releasing Resources.... ")
        if hasattr(self, 'ser') and self.ser.isOpen():
            self.ser.close()
        if hasattr(self, 'file') and not self.file.closed :
            self.file.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    atexit.register(ui.releaseResource)
    sys.exit(app.exec_())




