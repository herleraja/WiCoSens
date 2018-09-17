# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NUCER\Documents\git\WiCoSens\MLDataLabeler\mlDataLabeler_container.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import atexit
import os
import pickle
import random
import sys
import traceback

import serial
from PyQt5 import QtCore, QtGui, QtWidgets

import colorSpaceUtil


class Ui_MainWindow(object):
    ser = file = None
    container_dict = {}
    maxSamplesPerKeyCount = 2
    # skip_container_numbers = [1, 6, 11, 16]
    skip_container_numbers = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1336, 719)
        MainWindow.setAcceptDrops(False)
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
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1295, 631))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.dataLabelingTabGridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.dataLabelingTabGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.dataLabelingTabGridLayout.setContentsMargins(0, 0, 0, 0)
        self.dataLabelingTabGridLayout.setObjectName("dataLabelingTabGridLayout")
        self.fileNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLabel, 7, 0, 1, 1)
        self.captureLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.captureLabel.setObjectName("captureLabel")
        self.dataLabelingTabGridLayout.addWidget(self.captureLabel, 4, 0, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fileNameLineEdit.setClearButtonEnabled(True)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLineEdit, 7, 1, 1, 1)
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
        self.dataLabelingTabGridLayout.addLayout(self.closeResetHLayout, 13, 1, 1, 1)
        self.classLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.classLabelLineEdit.setEnabled(False)
        self.classLabelLineEdit.setObjectName("classLabelLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLineEdit, 2, 1, 1, 1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.capturSensorDataHLayout.addItem(spacerItem2)
        self.dataLabelingTabGridLayout.addLayout(self.capturSensorDataHLayout, 4, 1, 1, 1)
        self.classLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classLabelLabel.setObjectName("classLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLabel, 2, 0, 1, 1)
        self.sensorTextLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorTextLabel.setObjectName("sensorTextLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextLabel, 9, 0, 1, 1)
        self.randomNumberHorizontalLayout = QtWidgets.QHBoxLayout()
        self.randomNumberHorizontalLayout.setObjectName("randomNumberHorizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem3)
        self.ranodmNumberEnableLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ranodmNumberEnableLabel.setObjectName("ranodmNumberEnableLabel")
        self.randomNumberHorizontalLayout.addWidget(self.ranodmNumberEnableLabel)
        self.randomNumberCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.randomNumberCheckBox.setText("")
        self.randomNumberCheckBox.setChecked(True)
        self.randomNumberCheckBox.setObjectName("randomNumberCheckBox")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberCheckBox)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem4)
        self.randomNumberLowerLimitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberLowerLimitLabel.setObjectName("randomNumberLowerLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberLowerLimitLabel)
        self.randomNumberLowerLimitLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.randomNumberLowerLimitLineEdit.setClearButtonEnabled(True)
        self.randomNumberLowerLimitLineEdit.setObjectName("randomNumberLowerLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberLowerLimitLineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem5)
        self.randomNumberUpperLimitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberUpperLimitLabel.setObjectName("randomNumberUpperLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLabel)
        self.randomNumberUpperLimitLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.randomNumberUpperLimitLineEdit.setClearButtonEnabled(True)
        self.randomNumberUpperLimitLineEdit.setObjectName("randomNumberUpperLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLineEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem6)
        self.dataLabelingTabGridLayout.addLayout(self.randomNumberHorizontalLayout, 8, 1, 1, 1)
        self.containerNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabel.setObjectName("containerNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabel, 1, 0, 1, 1)
        self.sensorTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sensorTextEdit.setUndoRedoEnabled(False)
        self.sensorTextEdit.setReadOnly(True)
        self.sensorTextEdit.setObjectName("sensorTextEdit")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextEdit, 9, 1, 1, 1)
        self.containerNumberLabelValueDisplay = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabelValueDisplay.setEnabled(True)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.containerNumberLabelValueDisplay.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.containerNumberLabelValueDisplay.setFont(font)
        self.containerNumberLabelValueDisplay.setAutoFillBackground(False)
        self.containerNumberLabelValueDisplay.setTextFormat(QtCore.Qt.PlainText)
        self.containerNumberLabelValueDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.containerNumberLabelValueDisplay.setObjectName("containerNumberLabelValueDisplay")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabelValueDisplay, 1, 1, 1, 1)
        self.randomNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberLabel.setObjectName("randomNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.randomNumberLabel, 8, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem7, 5, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.dataLabelingTabGridLayout.addWidget(self.progressBar, 6, 1, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.formLayoutWidget)
        self.lcdNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setObjectName("lcdNumber")
        self.dataLabelingTabGridLayout.addWidget(self.lcdNumber, 6, 0, 1, 1)
        self.mainTabObj.addTab(self.dataLabelingTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.settingTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 20, 1281, 251))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.settingTabMainGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.settingTabMainGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.settingTabMainGridLayout.setContentsMargins(0, 0, 0, 0)
        self.settingTabMainGridLayout.setObjectName("settingTabMainGridLayout")
        self.recordingFolderLocationLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.recordingFolderLocationLabel.setObjectName("recordingFolderLocationLabel")
        self.settingTabMainGridLayout.addWidget(self.recordingFolderLocationLabel, 2, 0, 1, 1)
        self.serialPortSettingsLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serialPortSettingsLabel.setObjectName("serialPortSettingsLabel")
        self.settingTabMainGridLayout.addWidget(self.serialPortSettingsLabel, 0, 0, 1, 1)
        self.recordingFolderLocationhorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingFolderLocationhorizontalLayout.setObjectName("recordingFolderLocationhorizontalLayout")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingFolderLocationhorizontalLayout.addItem(spacerItem8)
        self.recordingFolderLocationLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.recordingFolderLocationLineEdit.setClearButtonEnabled(True)
        self.recordingFolderLocationLineEdit.setObjectName("recordingFolderLocationLineEdit")
        self.recordingFolderLocationhorizontalLayout.addWidget(self.recordingFolderLocationLineEdit)
        self.settingTabMainGridLayout.addLayout(self.recordingFolderLocationhorizontalLayout, 2, 1, 1, 1)
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
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHorizontalLayout.addItem(spacerItem9)
        self.portlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.portlineEdit.setClearButtonEnabled(True)
        self.portlineEdit.setObjectName("portlineEdit")
        self.portHorizontalLayout.addWidget(self.portlineEdit)
        self.setialPortSettingsVerticalLayout.addLayout(self.portHorizontalLayout)
        self.settingTabMainGridLayout.addLayout(self.setialPortSettingsVerticalLayout, 0, 1, 1, 1)
        self.recordingTimerLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.recordingTimerLabel.setObjectName("recordingTimerLabel")
        self.settingTabMainGridLayout.addWidget(self.recordingTimerLabel, 1, 0, 1, 1)
        self.sensorEnableDisableLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.sensorEnableDisableLabel.setObjectName("sensorEnableDisableLabel")
        self.settingTabMainGridLayout.addWidget(self.sensorEnableDisableLabel, 3, 0, 1, 1)
        self.recordingTimerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingTimerHorizontalLayout.setObjectName("recordingTimerHorizontalLayout")
        self.enableTimerCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.enableTimerCheckBox.setChecked(True)
        self.enableTimerCheckBox.setObjectName("enableTimerCheckBox")
        self.recordingTimerHorizontalLayout.addWidget(self.enableTimerCheckBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingTimerHorizontalLayout.addItem(spacerItem10)
        self.timerInSecondsLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.timerInSecondsLabel.setObjectName("timerInSecondsLabel")
        self.recordingTimerHorizontalLayout.addWidget(self.timerInSecondsLabel)
        self.timerInSecondsLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.timerInSecondsLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.timerInSecondsLineEdit.setClearButtonEnabled(True)
        self.timerInSecondsLineEdit.setObjectName("timerInSecondsLineEdit")
        self.recordingTimerHorizontalLayout.addWidget(self.timerInSecondsLineEdit)
        self.settingTabMainGridLayout.addLayout(self.recordingTimerHorizontalLayout, 1, 1, 1, 1)
        self.sensorButtonHorizontalLayout = QtWidgets.QHBoxLayout()
        self.sensorButtonHorizontalLayout.setObjectName("sensorButtonHorizontalLayout")
        self.colSensorButton1 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton1.setAcceptDrops(False)
        self.colSensorButton1.setCheckable(True)
        self.colSensorButton1.setChecked(True)
        self.colSensorButton1.setObjectName("colSensorButton1")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton1)
        self.colSensorButton2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton2.setCheckable(True)
        self.colSensorButton2.setChecked(True)
        self.colSensorButton2.setObjectName("colSensorButton2")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton2)
        self.colSensorButton3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton3.setCheckable(True)
        self.colSensorButton3.setChecked(True)
        self.colSensorButton3.setObjectName("colSensorButton3")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton3)
        self.colSensorButton4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton4.setCheckable(True)
        self.colSensorButton4.setChecked(True)
        self.colSensorButton4.setObjectName("colSensorButton4")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton4)
        self.colSensorButton5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton5.setCheckable(True)
        self.colSensorButton5.setChecked(True)
        self.colSensorButton5.setObjectName("colSensorButton5")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton5)
        self.colSensorButton6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton6.setCheckable(True)
        self.colSensorButton6.setChecked(True)
        self.colSensorButton6.setObjectName("colSensorButton6")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton6)
        self.colSensorButton7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton7.setCheckable(True)
        self.colSensorButton7.setChecked(True)
        self.colSensorButton7.setObjectName("colSensorButton7")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton7)
        self.colSensorButton8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton8.setCheckable(True)
        self.colSensorButton8.setChecked(True)
        self.colSensorButton8.setObjectName("colSensorButton8")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton8)
        self.colSensorButton9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton9.setCheckable(True)
        self.colSensorButton9.setChecked(True)
        self.colSensorButton9.setObjectName("colSensorButton9")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton9)
        self.colSensorButton10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton10.setCheckable(True)
        self.colSensorButton10.setChecked(True)
        self.colSensorButton10.setObjectName("colSensorButton10")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton10)
        self.colSensorButton11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton11.setCheckable(True)
        self.colSensorButton11.setChecked(True)
        self.colSensorButton11.setObjectName("colSensorButton11")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton11)
        self.colSensorButton12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton12.setCheckable(True)
        self.colSensorButton12.setChecked(True)
        self.colSensorButton12.setObjectName("colSensorButton12")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton12)
        self.settingTabMainGridLayout.addLayout(self.sensorButtonHorizontalLayout, 3, 1, 1, 1)
        self.colorSpaceLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.colorSpaceLabel.setObjectName("colorSpaceLabel")
        self.settingTabMainGridLayout.addWidget(self.colorSpaceLabel, 4, 0, 1, 1)
        self.colorSpaceButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.colorSpaceButtonsHorizontalLayout.setObjectName("colorSpaceButtonsHorizontalLayout")
        self.colorSpaceXYZButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceXYZButton.setCheckable(True)
        self.colorSpaceXYZButton.setAutoExclusive(True)
        self.colorSpaceXYZButton.setObjectName("colorSpaceXYZButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceXYZButton)
        self.colorSpaceLabButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceLabButton.setCheckable(True)
        self.colorSpaceLabButton.setAutoExclusive(True)
        self.colorSpaceLabButton.setObjectName("colorSpaceLabButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceLabButton)
        self.colorSpaceYCbCrButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceYCbCrButton.setCheckable(True)
        self.colorSpaceYCbCrButton.setAutoExclusive(True)
        self.colorSpaceYCbCrButton.setObjectName("colorSpaceYCbCrButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceYCbCrButton)
        self.colorSpaceRGBButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceRGBButton.setCheckable(True)
        self.colorSpaceRGBButton.setChecked(True)
        self.colorSpaceRGBButton.setAutoExclusive(True)
        self.colorSpaceRGBButton.setObjectName("colorSpaceRGBButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceRGBButton)
        self.colorSpaceHSVButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceHSVButton.setCheckable(True)
        self.colorSpaceHSVButton.setChecked(False)
        self.colorSpaceHSVButton.setAutoExclusive(True)
        self.colorSpaceHSVButton.setObjectName("colorSpaceHSVButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceHSVButton)
        self.settingTabMainGridLayout.addLayout(self.colorSpaceButtonsHorizontalLayout, 4, 1, 1, 1)
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

        self.load_dictionary('container_dict.txt')

        if self.randomNumberCheckBox.isChecked():
            self.displayRandomContainerNumber()
            self.displayRemainingSamplesCount()
            self.classLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())

        self.addButtonOperations()
        self.addFiledsValidators()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Collection"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.captureLabel.setText(_translate("MainWindow", "Capture Sensor Data"))
        self.fileNameLineEdit.setText(_translate("MainWindow", "container_train"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start"))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop"))
        self.classLabelLabel.setText(_translate("MainWindow", "ClassLabel"))
        self.sensorTextLabel.setText(_translate("MainWindow", "Captured Sensor Data"))
        self.ranodmNumberEnableLabel.setText(_translate("MainWindow", "Enable Randomness"))
        self.randomNumberLowerLimitLabel.setText(_translate("MainWindow", "Lower Limit"))
        self.randomNumberLowerLimitLineEdit.setText(_translate("MainWindow", "0"))
        self.randomNumberUpperLimitLabel.setText(_translate("MainWindow", "Upper Limit"))
        self.randomNumberUpperLimitLineEdit.setText(_translate("MainWindow", "24"))
        self.containerNumberLabel.setText(_translate("MainWindow", "Container Number"))
        self.containerNumberLabelValueDisplay.setText(_translate("MainWindow", "999"))
        self.randomNumberLabel.setText(_translate("MainWindow", "Random number setting"))
        self.progressBar.setFormat(_translate("MainWindow", "%p"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.dataLabelingTab), _translate("MainWindow", "Data labeling"))
        self.recordingFolderLocationLabel.setText(_translate("MainWindow", "Recording Folder Location"))
        self.serialPortSettingsLabel.setText(_translate("MainWindow", "Serial Port Settings"))
        self.recordingFolderLocationLineEdit.setText(_translate("MainWindow", "datarecording_discrete/rgb/"))
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
        self.recordingTimerLabel.setText(_translate("MainWindow", "Recording Timer"))
        self.sensorEnableDisableLabel.setText(_translate("MainWindow", "Enable / Disable Color Sensor"))
        self.enableTimerCheckBox.setText(_translate("MainWindow", "Enable Timer"))
        self.timerInSecondsLabel.setText(_translate("MainWindow", "Time(in seconds)"))
        self.timerInSecondsLineEdit.setText(_translate("MainWindow", "40"))
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
        self.colorSpaceLabel.setText(_translate("MainWindow", "Color Space"))
        self.colorSpaceXYZButton.setText(_translate("MainWindow", "XYZ"))
        self.colorSpaceLabButton.setText(_translate("MainWindow", "L*a*b*"))
        self.colorSpaceYCbCrButton.setText(_translate("MainWindow", "YCbCr"))
        self.colorSpaceRGBButton.setText(_translate("MainWindow", "RGB"))
        self.colorSpaceHSVButton.setText(_translate("MainWindow", "HSV"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.settingTab), _translate("MainWindow", "Settings"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.classifierTab), _translate("MainWindow", "Classify"))



    def setUpSerialPort(self):
        baudrate = self.baudrateComboBox.currentText()
        port = self.portlineEdit.text()
        if self.ser is None:
            self.ser = serial.Serial(port, int(baudrate), timeout=None)
        else:
            return

    def addButtonOperations(self):
        self.closeBtn.clicked.connect(self.closeWindow)
        self.resetBtn.clicked.connect(self.resetFields)
        self.startCaptureBtn.clicked.connect(self.startCaptureBtnPressedEvent)
        self.stopCaptureBtn.clicked.connect(self.stopCaptureBtnPressedEvent)
        self.randomNumberCheckBox.clicked.connect(self.randomNumberCheckBoxPressedEvent)
        self.randomNumberUpperLimitLineEdit.textChanged.connect(self.randomNumberUpperLowerLimitLineEditTextChangeEvent)
        self.randomNumberLowerLimitLineEdit.textChanged.connect(self.randomNumberUpperLowerLimitLineEditTextChangeEvent)
        self.startCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space))
        self.stopCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape))

    def addFiledsValidators(self):

        regexp = QtCore.QRegExp('[a-zA-Z0-9_ -]+')
        validator = QtGui.QRegExpValidator(regexp)
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(0, 96)
        self.fileNameLineEdit.setValidator(validator)
        self.classLabelLineEdit.setValidator(validator)
        self.randomNumberLowerLimitLineEdit.setValidator(intValidator)
        self.randomNumberUpperLimitLineEdit.setValidator(intValidator)

    def captureSensorData(self):
        try:

            current_label = self.classLabelLineEdit.text()

            new_line = self.ser.readline().decode('utf-8').rstrip()

            line_array = new_line.split(',')

            if line_array.__len__() == 52:

                new_line = line_array[0] + ',' + line_array[1] + ',' + line_array[2] + ',' + line_array[3]

                if self.colSensorButton1.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[4]), float(line_array[5]),
                                                          float(line_array[6]),
                                                          float(line_array[7]))  # Right side(R5) sensor
                if self.colSensorButton2.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[8]), float(line_array[9]),
                                                          float(line_array[10]),
                                                          float(line_array[11]))  # Right side(R4) sensor
                if self.colSensorButton3.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[12]), float(line_array[13]),
                                                          float(line_array[14]),
                                                          float(line_array[15]))  # Right side(R3) sensor
                if self.colSensorButton4.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[16]), float(line_array[17]),
                                                          float(line_array[18]),
                                                          float(line_array[19]))  # Right side(R2) sensor
                if self.colSensorButton5.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[20]), float(line_array[21]),
                                                          float(line_array[22]),
                                                          float(line_array[23]))  # Right side(R1) sensor
                if self.colSensorButton6.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[24]), float(line_array[25]),
                                                          float(line_array[26]),
                                                          float(line_array[27]))  # Right side(R0) sensor
                if self.colSensorButton7.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[28]), float(line_array[29]),
                                                          float(line_array[30]), float(line_array[31]))  # middle sensor
                if self.colSensorButton8.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[32]), float(line_array[33]),
                                                          float(line_array[34]),
                                                          float(line_array[35]))  # Left side(L1) sensor
                if self.colSensorButton9.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[36]), float(line_array[37]),
                                                          float(line_array[38]),
                                                          float(line_array[39]))  # Left side(L2) sensor
                if self.colSensorButton10.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[40]), float(line_array[41]),
                                                          float(line_array[42]),
                                                          float(line_array[43]))  # Left side(L3) sensor
                if self.colSensorButton11.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[44]), float(line_array[45]),
                                                          float(line_array[46]),
                                                          float(line_array[47]))  # Left side(L4) sensor
                if self.colSensorButton12.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[48]), float(line_array[49]),
                                                          float(line_array[50]),
                                                          float(line_array[51]))  # Left side(L5) sensor

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
            if self.isValidFields():
                self.startCaptureBtn.setEnabled(False)
                self.stopCaptureBtn.setEnabled(True)

                self.startCaptureBtn.repaint()
                self.stopCaptureBtn.repaint()

                self.setUpSerialPort()
                self.openFileForWriting()  # Create/Open file for saving sensor data

                if self.randomNumberCheckBox.isChecked():
                    self.classLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
                    self.classLabelLineEdit.repaint()

                classLabel = int(self.classLabelLineEdit.text())  # To add class label to dictionary

                if not self.startCaptureBtn.isEnabled():

                    if classLabel in self.container_dict:
                        self.container_dict[classLabel] = self.container_dict[classLabel] + 1
                    else:
                        self.container_dict[classLabel] = 1




                    self.displayRemainingSamplesCount()

                    QtCore.QTimer.singleShot(1, self.captureSensorData)

        except:

            self.startCaptureBtn.setEnabled(False)
            self.stopCaptureBtn.setEnabled(True)

            self.startCaptureBtn.repaint()
            self.stopCaptureBtn.repaint()

            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def stopCaptureBtnPressedEvent(self):
        self.startCaptureBtn.setEnabled(True)
        self.startCaptureBtn.repaint()

        self.stopCaptureBtn.setEnabled(False)
        self.stopCaptureBtn.repaint()

        if self.randomNumberCheckBox.isChecked():
            self.displayRandomContainerNumber()
            # self.classLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())  # last record update issue

    def randomNumberCheckBoxPressedEvent(self):
        if self.randomNumberCheckBox.isChecked():
            self.classLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
            self.classLabelLineEdit.setEnabled(False)
            self.randomNumberLowerLimitLineEdit.setEnabled(True)
            self.randomNumberUpperLimitLineEdit.setEnabled(True)
        else:
            self.classLabelLineEdit.setEnabled(True)
            self.randomNumberLowerLimitLineEdit.setEnabled(False)
            self.randomNumberUpperLimitLineEdit.setEnabled(False)

    def randomNumberUpperLowerLimitLineEditTextChangeEvent(self):
        try:
            if self.randomNumberLowerLimitLineEdit.text().__len__() > 0 and self.randomNumberUpperLimitLineEdit.text().__len__() > 0:
                randomNumberLowerLimit = int(self.randomNumberLowerLimitLineEdit.text())
                randomNumberUpperLimit = int(self.randomNumberUpperLimitLineEdit.text())

                if randomNumberLowerLimit <= randomNumberUpperLimit:
                    self.container_dict = {}  # To reset the dictionary
                    self.displayRandomContainerNumber()  # To reset the random number value
                else:
                    return
            else:
                return

        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def openFileForWriting(self):
        write_path = self.recordingFolderLocationLineEdit.text()
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        file_name = self.fileNameLineEdit.text()
        file_name = write_path + file_name + ".csv"
        self.file = open(file_name, 'a')

    def displayRandomContainerNumber(self):
        randomNumberLowerLimit = int(self.randomNumberLowerLimitLineEdit.text())
        randomNumberUpperLimit = int(self.randomNumberUpperLimitLineEdit.text())

        if sum(self.container_dict.values()) == (
                randomNumberUpperLimit - randomNumberLowerLimit - self.skip_container_numbers.__len__() + 1) * self.maxSamplesPerKeyCount:
            print(
                "\n\nThe sample reached maximum size limit / all the container samples taken. "
                "To take more samples please change **maxSamplesPerKeyCount** variable.\n\n")
            exit()

        while True:
            random_box_number = random.randint(randomNumberLowerLimit,
                                               randomNumberUpperLimit)  # to display random number from 0 to 24

            if random_box_number in self.skip_container_numbers:  # skip the mentioned box numbers
                continue

            if random_box_number in self.container_dict:
                if self.container_dict[random_box_number] < self.maxSamplesPerKeyCount:
                    break
                else:
                    continue  # Try other value
            else:
                break

        self.containerNumberLabelValueDisplay.setText(str(random_box_number))
        self.containerNumberLabelValueDisplay.repaint()

    def isValidFields(self):

        return_value = self.fileNameLineEdit.text().__len__() > 0 and self.classLabelLineEdit.text().__len__() > 0 \
                       and self.recordingFolderLocationLineEdit.text().__len__() > 0
        if not return_value:
            self.displayWarningPopUp("Please fill the required fields !!")
            return return_value
        # if self.randomNumberCheckBox.isChecked() and self.classLabelLineEdit.text() != self.containerNumberLabelValueDisplay.text():
        # self.displayWarningPopUp("Class Label is not same as generated container number.")
        # return False
        return return_value

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
            self.randomNumberLowerLimitLineEdit.setText('0')
            self.randomNumberUpperLimitLineEdit.setText('24')

        else:
            self.displayWarningPopUp("Please stop capturing data before the reset")

    def displayWarningPopUp(self, warningText="Warning !!"):
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(warningText)
        msgbox.setWindowTitle("Warning !! ")
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.exec()

    def displayRemainingSamplesCount(self):
        dictionarySumOfValues = sum(self.container_dict.values())
        randomNumberLowerLimit = int(self.randomNumberLowerLimitLineEdit.text())
        randomNumberUpperLimit = int(self.randomNumberUpperLimitLineEdit.text())
        maxNumberOfSamples = (randomNumberUpperLimit - randomNumberLowerLimit - self.skip_container_numbers.__len__() + 1) * self.maxSamplesPerKeyCount
        remainingNumberOfContainers = maxNumberOfSamples - dictionarySumOfValues
        self.lcdNumber.display(str(remainingNumberOfContainers))


    def closeWindow(self):
        QtCore.QCoreApplication.instance().quit()

    def releaseResource(self):
        print("Releasing Resources.... ")
        if self.ser is not None and self.ser.isOpen():
            self.ser.close()
        if self.file is not None and not self.file.closed:
            self.file.close()
        self.save_dictionary('container_dict.txt')

    def save_dictionary(self, file_name):
        print('Dictionary contents\n{}'.format(self.container_dict.items()))
        with open(file_name, "wb") as myFile:
            pickle.dump(self.container_dict, myFile)
            myFile.close()

    def load_dictionary(self, file_name):
        try:
            with open(file_name, "rb") as myFile:
                self.container_dict = pickle.load(myFile)
                print('loaded dictionary. The dictionary contents are : \n{}'.format(self.container_dict.items()))
                myFile.close()
        except FileNotFoundError:
            print('\nDictionary file not found ! This occurs only in initial load'
                  ' of the program when there is no dictionary file available.\n')
            return


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    atexit.register(ui.releaseResource)
    sys.exit(app.exec_())
