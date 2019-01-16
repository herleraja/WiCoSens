import atexit
import csv
import os
import pickle
import random
import sys
import traceback
from collections import Counter

import keras
import numpy as np
import serial
from PyQt5 import QtCore, QtGui, QtWidgets

sys.path.insert(1, os.path.join(sys.path[0], '..'))

import colorSpaceUtil


class Ui_MainWindow(object):
    ser = bottom_file = left_file = right_file =result_file = model_bottom = model_left = model_right = text_class_model = bottom_preprocessor = left_preprocessor = right_preprocessor = None
    container_dict = color_concept_dict = {}
    start_time = 100
    # maxSamplesPerKeyCount = 2
    # skip_container_numbers = [1, 6, 11, 16]
    skip_container_numbers = []

    bottom_color_list = [0]
    left_color_list = [0]
    right_color_list = [0]

    no_records = 100

    color_space = 'HSV'
    feature_type = 'RAW'  # RAW, PREPROCESSED
    config_save_load_dir_path = "./resources/Classifier/" + feature_type + "/" + color_space.lower() + "/"

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1338, 538)
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
        self.formLayoutWidget.setGeometry(QtCore.QRect(14, 10, 1291, 451))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.dataLabelingTabGridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.dataLabelingTabGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.dataLabelingTabGridLayout.setContentsMargins(0, 0, 0, 0)
        self.dataLabelingTabGridLayout.setObjectName("dataLabelingTabGridLayout")
        self.bottomClassLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.bottomClassLabelLineEdit.setEnabled(False)
        self.bottomClassLabelLineEdit.setObjectName("bottomClassLabelLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.bottomClassLabelLineEdit, 4, 1, 1, 1)
        self.rightClassLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rightClassLabelLineEdit.setEnabled(False)
        self.rightClassLabelLineEdit.setObjectName("rightClassLabelLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.rightClassLabelLineEdit, 3, 1, 1, 1)
        self.bottomClassLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.bottomClassLabelLabel.setObjectName("bottomClassLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.bottomClassLabelLabel, 4, 0, 1, 1)
        self.rightClassLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rightClassLabelLabel.setObjectName("rightClassLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.rightClassLabelLabel, 3, 0, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLabel, 8, 0, 1, 1)
        self.captureLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.captureLabel.setObjectName("captureLabel")
        self.dataLabelingTabGridLayout.addWidget(self.captureLabel, 5, 0, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fileNameLineEdit.setClearButtonEnabled(True)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLineEdit, 8, 1, 1, 1)
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
        self.containerNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabel.setObjectName("containerNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabel, 1, 0, 1, 1)
        self.captureTimeLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.captureTimeLabel.setObjectName("captureTimeLabel")
        self.dataLabelingTabGridLayout.addWidget(self.captureTimeLabel, 7, 0, 1, 1)
        self.remainingSamplesToCaptureLCDNumber = QtWidgets.QLCDNumber(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.remainingSamplesToCaptureLCDNumber.setFont(font)
        self.remainingSamplesToCaptureLCDNumber.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.remainingSamplesToCaptureLCDNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.remainingSamplesToCaptureLCDNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.remainingSamplesToCaptureLCDNumber.setDigitCount(6)
        self.remainingSamplesToCaptureLCDNumber.setMode(QtWidgets.QLCDNumber.Dec)
        self.remainingSamplesToCaptureLCDNumber.setObjectName("remainingSamplesToCaptureLCDNumber")
        self.dataLabelingTabGridLayout.addWidget(self.remainingSamplesToCaptureLCDNumber, 6, 1, 1, 1)
        self.leftClassLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.leftClassLabelLineEdit.setEnabled(False)
        self.leftClassLabelLineEdit.setObjectName("leftClassLabelLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.leftClassLabelLineEdit, 2, 1, 1, 1)
        self.leftClassLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.leftClassLabelLabel.setObjectName("leftClassLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.leftClassLabelLabel, 2, 0, 1, 1)
        self.sensorTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sensorTextEdit.setUndoRedoEnabled(False)
        self.sensorTextEdit.setReadOnly(True)
        self.sensorTextEdit.setObjectName("sensorTextEdit")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextEdit, 9, 1, 1, 1)
        self.remainingSamplesToCaptureLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.remainingSamplesToCaptureLabel.setObjectName("remainingSamplesToCaptureLabel")
        self.dataLabelingTabGridLayout.addWidget(self.remainingSamplesToCaptureLabel, 6, 0, 1, 1)
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
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.containerNumberLabelValueDisplay.setFont(font)
        self.containerNumberLabelValueDisplay.setAutoFillBackground(False)
        self.containerNumberLabelValueDisplay.setTextFormat(QtCore.Qt.PlainText)
        self.containerNumberLabelValueDisplay.setAlignment(QtCore.Qt.AlignCenter)
        self.containerNumberLabelValueDisplay.setObjectName("containerNumberLabelValueDisplay")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabelValueDisplay, 1, 1, 1, 1)
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
        self.dataLabelingTabGridLayout.addLayout(self.capturSensorDataHLayout, 5, 1, 1, 1)
        self.sensorTextLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorTextLabel.setObjectName("sensorTextLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextLabel, 9, 0, 1, 1)
        self.captureTimeProgressBar = QtWidgets.QProgressBar(self.formLayoutWidget)
        self.captureTimeProgressBar.setProperty("value", 0)
        self.captureTimeProgressBar.setObjectName("captureTimeProgressBar")
        self.dataLabelingTabGridLayout.addWidget(self.captureTimeProgressBar, 7, 1, 1, 1)
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
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingFolderLocationhorizontalLayout.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHorizontalLayout.addItem(spacerItem4)
        self.portlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.portlineEdit.setClearButtonEnabled(True)
        self.portlineEdit.setObjectName("portlineEdit")
        self.portHorizontalLayout.addWidget(self.portlineEdit)
        self.setialPortSettingsVerticalLayout.addLayout(self.portHorizontalLayout)
        self.settingTabMainGridLayout.addLayout(self.setialPortSettingsVerticalLayout, 0, 1, 1, 1)
        self.recordingTimerLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.recordingTimerLabel.setObjectName("recordingTimerLabel")
        self.settingTabMainGridLayout.addWidget(self.recordingTimerLabel, 1, 0, 1, 1)
        self.colorSpaceLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.colorSpaceLabel.setObjectName("colorSpaceLabel")
        self.settingTabMainGridLayout.addWidget(self.colorSpaceLabel, 4, 0, 1, 1)
        self.sensorEnableDisableLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.sensorEnableDisableLabel.setObjectName("sensorEnableDisableLabel")
        self.settingTabMainGridLayout.addWidget(self.sensorEnableDisableLabel, 3, 0, 1, 1)
        self.recordingTimerHorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingTimerHorizontalLayout.setObjectName("recordingTimerHorizontalLayout")
        self.enableTimerCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.enableTimerCheckBox.setChecked(True)
        self.enableTimerCheckBox.setObjectName("enableTimerCheckBox")
        self.recordingTimerHorizontalLayout.addWidget(self.enableTimerCheckBox)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingTimerHorizontalLayout.addItem(spacerItem5)
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
        self.colSensorButton1.setEnabled(False)
        self.colSensorButton1.setAcceptDrops(False)
        self.colSensorButton1.setCheckable(True)
        self.colSensorButton1.setChecked(True)
        self.colSensorButton1.setObjectName("colSensorButton1")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton1)
        self.colSensorButton2 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton2.setEnabled(False)
        self.colSensorButton2.setCheckable(True)
        self.colSensorButton2.setChecked(True)
        self.colSensorButton2.setObjectName("colSensorButton2")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton2)
        self.colSensorButton3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton3.setEnabled(False)
        self.colSensorButton3.setCheckable(True)
        self.colSensorButton3.setChecked(True)
        self.colSensorButton3.setObjectName("colSensorButton3")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton3)
        self.colSensorButton4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton4.setEnabled(False)
        self.colSensorButton4.setCheckable(True)
        self.colSensorButton4.setChecked(True)
        self.colSensorButton4.setObjectName("colSensorButton4")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton4)
        self.colSensorButton5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton5.setEnabled(False)
        self.colSensorButton5.setCheckable(True)
        self.colSensorButton5.setChecked(True)
        self.colSensorButton5.setObjectName("colSensorButton5")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton5)
        self.colSensorButton6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton6.setEnabled(False)
        self.colSensorButton6.setCheckable(True)
        self.colSensorButton6.setChecked(True)
        self.colSensorButton6.setObjectName("colSensorButton6")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton6)
        self.colSensorButton7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton7.setEnabled(False)
        self.colSensorButton7.setCheckable(True)
        self.colSensorButton7.setChecked(True)
        self.colSensorButton7.setObjectName("colSensorButton7")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton7)
        self.colSensorButton8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton8.setEnabled(False)
        self.colSensorButton8.setCheckable(True)
        self.colSensorButton8.setChecked(True)
        self.colSensorButton8.setObjectName("colSensorButton8")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton8)
        self.colSensorButton9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton9.setEnabled(False)
        self.colSensorButton9.setCheckable(True)
        self.colSensorButton9.setChecked(True)
        self.colSensorButton9.setObjectName("colSensorButton9")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton9)
        self.colSensorButton10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton10.setEnabled(False)
        self.colSensorButton10.setCheckable(True)
        self.colSensorButton10.setChecked(True)
        self.colSensorButton10.setObjectName("colSensorButton10")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton10)
        self.colSensorButton11 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton11.setEnabled(False)
        self.colSensorButton11.setCheckable(True)
        self.colSensorButton11.setChecked(True)
        self.colSensorButton11.setObjectName("colSensorButton11")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton11)
        self.colSensorButton12 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colSensorButton12.setEnabled(False)
        self.colSensorButton12.setCheckable(True)
        self.colSensorButton12.setChecked(True)
        self.colSensorButton12.setObjectName("colSensorButton12")
        self.sensorButtonHorizontalLayout.addWidget(self.colSensorButton12)
        self.settingTabMainGridLayout.addLayout(self.sensorButtonHorizontalLayout, 3, 1, 1, 1)
        self.colorSpaceButtonsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.colorSpaceButtonsHorizontalLayout.setObjectName("colorSpaceButtonsHorizontalLayout")
        self.colorSpaceXYZButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        # self.colorSpaceXYZButton.setEnabled(False)
        self.colorSpaceXYZButton.setCheckable(True)
        self.colorSpaceXYZButton.setAutoExclusive(True)
        self.colorSpaceXYZButton.setObjectName("colorSpaceXYZButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceXYZButton)
        self.colorSpaceLabButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceLabButton.setEnabled(False)
        self.colorSpaceLabButton.setCheckable(True)
        self.colorSpaceLabButton.setAutoExclusive(True)
        self.colorSpaceLabButton.setObjectName("colorSpaceLabButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceLabButton)
        self.colorSpaceYCbCrButton = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.colorSpaceYCbCrButton.setEnabled(False)
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
        # self.colorSpaceHSVButton.setEnabled(False)
        self.colorSpaceHSVButton.setCheckable(True)
        self.colorSpaceHSVButton.setChecked(False)
        self.colorSpaceHSVButton.setAutoExclusive(True)
        self.colorSpaceHSVButton.setObjectName("colorSpaceHSVButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceHSVButton)
        self.settingTabMainGridLayout.addLayout(self.colorSpaceButtonsHorizontalLayout, 4, 1, 1, 1)
        self.randomNumberLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.randomNumberLabel.setObjectName("randomNumberLabel")
        self.settingTabMainGridLayout.addWidget(self.randomNumberLabel, 5, 0, 1, 1)
        self.randomNumberHorizontalLayout = QtWidgets.QHBoxLayout()
        self.randomNumberHorizontalLayout.setObjectName("randomNumberHorizontalLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem6)
        self.ranodmNumberEnableLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.ranodmNumberEnableLabel.setObjectName("ranodmNumberEnableLabel")
        self.randomNumberHorizontalLayout.addWidget(self.ranodmNumberEnableLabel)
        self.randomNumberCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget_2)
        self.randomNumberCheckBox.setText("")
        self.randomNumberCheckBox.setChecked(True)
        self.randomNumberCheckBox.setObjectName("randomNumberCheckBox")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberCheckBox)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem7)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label.setObjectName("label")
        self.randomNumberHorizontalLayout.addWidget(self.label)
        self.samplesPerKeyCountLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.samplesPerKeyCountLineEdit.setClearButtonEnabled(True)
        self.samplesPerKeyCountLineEdit.setObjectName("samplesPerKeyCountLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.samplesPerKeyCountLineEdit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem8)
        self.randomNumberLowerLimitLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.randomNumberLowerLimitLabel.setObjectName("randomNumberLowerLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberLowerLimitLabel)
        self.randomNumberLowerLimitLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.randomNumberLowerLimitLineEdit.setClearButtonEnabled(True)
        self.randomNumberLowerLimitLineEdit.setObjectName("randomNumberLowerLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberLowerLimitLineEdit)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem9)
        self.randomNumberUpperLimitLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.randomNumberUpperLimitLabel.setObjectName("randomNumberUpperLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLabel)
        self.randomNumberUpperLimitLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.randomNumberUpperLimitLineEdit.setClearButtonEnabled(True)
        self.randomNumberUpperLimitLineEdit.setObjectName("randomNumberUpperLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLineEdit)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem10)
        self.settingTabMainGridLayout.addLayout(self.randomNumberHorizontalLayout, 5, 1, 1, 1)
        self.mainTabObj.addTab(self.settingTab, "")
        self.classifierTab = QtWidgets.QWidget()
        self.classifierTab.setObjectName("classifierTab")
        self.classifierOutputDisplyLCDNumber = QtWidgets.QLCDNumber(self.classifierTab)
        self.classifierOutputDisplyLCDNumber.setGeometry(QtCore.QRect(430, 220, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.classifierOutputDisplyLCDNumber.setFont(font)
        self.classifierOutputDisplyLCDNumber.setStyleSheet("")
        self.classifierOutputDisplyLCDNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.classifierOutputDisplyLCDNumber.setLineWidth(1)
        self.classifierOutputDisplyLCDNumber.setProperty("value", 0.0)
        self.classifierOutputDisplyLCDNumber.setProperty("intValue", 0)
        self.classifierOutputDisplyLCDNumber.setObjectName("classifierOutputDisplyLCDNumber")
        self.graphicsView = QtWidgets.QGraphicsView(self.classifierTab)
        self.graphicsView.setGeometry(QtCore.QRect(270, 30, 401, 351))
        self.graphicsView.setStyleSheet("background-image: url(Icon/container.jpg);")
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.startPredictBtn = QtWidgets.QPushButton(self.classifierTab)
        self.startPredictBtn.setGeometry(QtCore.QRect(1040, 420, 121, 41))
        self.startPredictBtn.setMouseTracking(False)
        self.startPredictBtn.setObjectName("startPredictBtn")
        self.stopPredictBtn = QtWidgets.QPushButton(self.classifierTab)
        self.stopPredictBtn.setEnabled(False)
        self.stopPredictBtn.setGeometry(QtCore.QRect(1170, 420, 121, 41))
        self.stopPredictBtn.setMouseTracking(False)
        self.stopPredictBtn.setObjectName("stopPredictBtn")
        self.graphicsView.raise_()
        self.classifierOutputDisplyLCDNumber.raise_()
        self.startPredictBtn.raise_()
        self.stopPredictBtn.raise_()
        self.mainTabObj.addTab(self.classifierTab, "")
        self.gridLayout.addWidget(self.mainTabObj, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.mainTabObj.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.timer = QtCore.QTimer()
        self.load_dictionary('container_dict.txt')

        if self.randomNumberCheckBox.isChecked():
            self.displayRandomContainerNumber()

            color_concept_values = self.color_concept_dict[self.containerNumberLabelValueDisplay.text()].split(',')

            self.bottomClassLabelLineEdit.setText(color_concept_values[0])
            self.leftClassLabelLineEdit.setText(color_concept_values[1])
            self.rightClassLabelLineEdit.setText(color_concept_values[2])

            self.bottomClassLabelLineEdit.repaint()
            self.leftClassLabelLineEdit.repaint()
            self.rightClassLabelLineEdit.repaint()

            # self.displayRemainingSamplesCount()
            # self.leftClassLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())

        self.addButtonOperations()
        self.addFiledsValidators()

        if self.feature_type == 'PREPROCESSED':
            self.bottom_preprocessor = pickle.load(open(self.config_save_load_dir_path + "bottom_preprocessor.p", "rb"))
            self.left_preprocessor = pickle.load(open(self.config_save_load_dir_path + "left_preprocessor.p", "rb"))
            self.right_preprocessor = pickle.load(open(self.config_save_load_dir_path + "right_preprocessor.p", "rb"))
        
        write_path = self.recordingFolderLocationLineEdit.text()
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        result_file_name = write_path + "result.csv"
        self.result_file = open(result_file_name, 'a')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Collection"))
        self.bottomClassLabelLabel.setText(_translate("MainWindow", "Bottom Class Label"))
        self.rightClassLabelLabel.setText(_translate("MainWindow", "Right Class Label"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.captureLabel.setText(_translate("MainWindow", "Capture Sensor Data"))
        self.fileNameLineEdit.setText(_translate("MainWindow", "train"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.containerNumberLabel.setText(_translate("MainWindow", "Container Number"))
        self.captureTimeLabel.setText(_translate("MainWindow", "Capture Time"))
        self.leftClassLabelLabel.setText(_translate("MainWindow", "Left Class Label"))
        self.remainingSamplesToCaptureLabel.setText(_translate("MainWindow", "Remaining # Samples"))
        self.containerNumberLabelValueDisplay.setText(_translate("MainWindow", "999"))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start"))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop"))
        self.sensorTextLabel.setText(_translate("MainWindow", "Captured Sensor Data"))
        self.captureTimeProgressBar.setFormat(_translate("MainWindow", "%p %"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.dataLabelingTab),
                                   _translate("MainWindow", "Data labeling"))
        self.recordingFolderLocationLabel.setText(_translate("MainWindow", "Recording Folder Location"))
        self.serialPortSettingsLabel.setText(_translate("MainWindow", "Serial Port Settings"))
        self.recordingFolderLocationLineEdit.setText(
            _translate("MainWindow", "datarecording_discrete/color_concept_new/rgb/"))
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
        self.portlineEdit.setText(_translate("MainWindow", "COM6"))
        self.recordingTimerLabel.setText(_translate("MainWindow", "Recording Timer"))
        self.colorSpaceLabel.setText(_translate("MainWindow", "Color Space"))
        self.sensorEnableDisableLabel.setText(_translate("MainWindow", "Enable / Disable Color Sensor"))
        self.enableTimerCheckBox.setText(_translate("MainWindow", "Enable Timer"))
        self.timerInSecondsLabel.setText(_translate("MainWindow", "Time(in seconds)"))
        self.timerInSecondsLineEdit.setText(_translate("MainWindow", "20"))
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
        self.colorSpaceXYZButton.setText(_translate("MainWindow", "XYZ"))
        self.colorSpaceLabButton.setText(_translate("MainWindow", "L*a*b*"))
        self.colorSpaceYCbCrButton.setText(_translate("MainWindow", "YCbCr"))
        self.colorSpaceRGBButton.setText(_translate("MainWindow", "RGB"))
        self.colorSpaceHSVButton.setText(_translate("MainWindow", "HSV"))
        self.randomNumberLabel.setText(_translate("MainWindow", "Random number setting"))
        self.ranodmNumberEnableLabel.setText(_translate("MainWindow", "Enable Randomness"))
        self.label.setText(_translate("MainWindow", "#Samples / Key"))
        self.samplesPerKeyCountLineEdit.setText(_translate("MainWindow", "1"))
        self.randomNumberLowerLimitLabel.setText(_translate("MainWindow", "Lower Limit"))
        self.randomNumberLowerLimitLineEdit.setText(_translate("MainWindow", "0"))
        self.randomNumberUpperLimitLabel.setText(_translate("MainWindow", "Upper Limit"))
        self.randomNumberUpperLimitLineEdit.setText(_translate("MainWindow", "24"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.settingTab), _translate("MainWindow", "Settings"))
        self.startPredictBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startPredictBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startPredictBtn.setText(_translate("MainWindow", "Start Predict"))
        self.stopPredictBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.stopPredictBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.stopPredictBtn.setText(_translate("MainWindow", "Stop Predict"))
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
        self.samplesPerKeyCountLineEdit.textChanged.connect(self.randomNumberUpperLowerLimitLineEditTextChangeEvent)
        self.timer.timeout.connect(self.updateProgressBar)
        self.startPredictBtn.clicked.connect(self.startPredictBtnPressedEvent)
        self.stopPredictBtn.clicked.connect(self.stopPredictBtnPressedEvent)
        self.startCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space))
        self.stopCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape))

    def addFiledsValidators(self):
        regexp = QtCore.QRegExp('[a-zA-Z0-9_ -]+')
        validator = QtGui.QRegExpValidator(regexp)
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(0, 96)
        self.fileNameLineEdit.setValidator(validator)
        self.leftClassLabelLineEdit.setValidator(validator)
        self.randomNumberLowerLimitLineEdit.setValidator(intValidator)
        self.randomNumberUpperLimitLineEdit.setValidator(intValidator)
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(0, 10)
        self.samplesPerKeyCountLineEdit.setValidator(intValidator)
        intValidator = QtGui.QIntValidator()
        intValidator.setRange(0, 100)
        self.timerInSecondsLineEdit.setValidator(intValidator)

    def convertSensorData(self, input, appendAccelerometerData=True):
        bottom_color = ""
        left_color = ""
        right_color = ""
        line_array = input.split(',')

        if appendAccelerometerData:
            new_line_accelerometer = line_array[0] + ',' + line_array[1] + ',' + line_array[2] + ',' + line_array[3]
            bottom_color = new_line_accelerometer
            left_color = new_line_accelerometer
            right_color = new_line_accelerometer

        r5sensor = [float(line_array[4]), float(line_array[5]), float(line_array[6]),
                    float(line_array[7])]  # Right side(R5) sensor
        r4sensor = [float(line_array[8]), float(line_array[9]),
                    float(line_array[10]),
                    float(line_array[11])]  # Right side(R4) sensor

        r3sensor = [float(line_array[12]), float(line_array[13]),
                    float(line_array[14]),
                    float(line_array[15])]  # Right side(R3) sensor
        r2sensor = [float(line_array[16]), float(line_array[17]),
                    float(line_array[18]),
                    float(line_array[19])]  # Right side(R2) sensor
        r1sensor = [float(line_array[20]), float(line_array[21]),
                    float(line_array[22]),
                    float(line_array[23])]  # Right side(R1) sensor
        r0sensor = [float(line_array[24]), float(line_array[25]),
                    float(line_array[26]),
                    float(line_array[
                              27])]  # Right side(R0) sensor
        msensor = [float(line_array[28]), float(line_array[29]),
                   float(line_array[30]), float(line_array[31])]  # middle sensor
        l1sensor = [float(line_array[32]), float(line_array[33]),
                    float(line_array[34]),
                    float(line_array[35])]  # Left side(L1) sensor
        l2sensor = [float(line_array[36]), float(line_array[37]),
                    float(line_array[38]),
                    float(line_array[39])]  # Left side(L2) sensor
        l3sensor = [float(line_array[40]), float(line_array[41]),
                    float(line_array[42]),
                    float(line_array[43])]  # Left side(L3) sensor
        l4sensor = [float(line_array[44]), float(line_array[45]),
                    float(line_array[46]),
                    float(line_array[47])]  # Left side(L4) sensor
        l5sensor = [float(line_array[48]), float(line_array[49]),
                    float(line_array[50]),
                    float(line_array[51])]  # Left side(L5) sensor
        '''
        bottom_color += self.colorSpaceCoverstion(r5sensor)  
        bottom_color += self.colorSpaceCoverstion(r4sensor)
        right_color += self.colorSpaceCoverstion(r3sensor)
        right_color += self.colorSpaceCoverstion(r2sensor)
        right_color += self.colorSpaceCoverstion(r1sensor)
        right_color += self.colorSpaceCoverstion(r1sensor)
        left_color += self.colorSpaceCoverstion(msensor)
        left_color += self.colorSpaceCoverstion(l1sensor)
        left_color += self.colorSpaceCoverstion(l2sensor)
        left_color += self.colorSpaceCoverstion(l3sensor)
        bottom_color += self.colorSpaceCoverstion(l4sensor)
        bottom_color += self.colorSpaceCoverstion(l5sensor)
        '''
        bottom_color += self.colorSpaceCoverstion(r5sensor)
        bottom_color += self.colorSpaceCoverstion(r4sensor)
        bottom_color += self.colorSpaceCoverstion(r3sensor)
        bottom_color += self.colorSpaceCoverstion(l5sensor)

        right_color += self.colorSpaceCoverstion(r1sensor)
        right_color += self.colorSpaceCoverstion(r2sensor)
        right_color += self.colorSpaceCoverstion(r3sensor)
        right_color += self.colorSpaceCoverstion(r4sensor)
        # right_color += self.colorSpaceCoverstion(r5sensor)
        left_color += self.colorSpaceCoverstion(l5sensor)
        left_color += self.colorSpaceCoverstion(l4sensor)
        left_color += self.colorSpaceCoverstion(l3sensor)
        left_color += self.colorSpaceCoverstion(l2sensor)
        return bottom_color, left_color, right_color

    def captureSensorData(self):
        try:

            bottom_label = self.bottomClassLabelLineEdit.text()
            left_label = self.leftClassLabelLineEdit.text()
            right_label = self.rightClassLabelLineEdit.text()

            new_line = self.ser.readline().decode('utf-8').rstrip()

            if new_line.__len__() == 52:
                bottom_color, left_color, right_color = self.convertSensorData(new_line)

                bottom_color = bottom_color + ',' + bottom_label + '\n'
                left_color = left_color + ',' + left_label + '\n'
                right_color = right_color + ',' + right_label + '\n'

                self.bottom_file.write(bottom_color)
                self.left_file.write(left_color)
                self.right_file.write(right_color)

                self.bottom_file.flush()
                self.left_file.flush()
                self.right_file.flush()

                self.sensorTextEdit.append(new_line)
                self.sensorTextEdit.repaint()

            if not self.startCaptureBtn.isEnabled():
                QtCore.QTimer.singleShot(1, self.captureSensorData)
            else:
                self.bottom_file.close()
                self.left_file.close()
                self.right_file.close()
        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def colorSpaceCoverstion(self, rgbc):

        r = rgbc[0]
        g = rgbc[1]
        b = rgbc[2]
        c = rgbc[3]

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

    def startPredictBtnPressedEvent(self):

        self.startPredictBtn.setEnabled(False)
        self.stopPredictBtn.setEnabled(True)
        self.startPredictBtn.repaint()
        self.stopPredictBtn.repaint()

        self.setUpSerialPort()

        self.model_bottom = keras.models.load_model(self.config_save_load_dir_path + 'model_bottom.h5')
        self.model_left = keras.models.load_model(self.config_save_load_dir_path + 'model_left.h5')
        self.model_right = keras.models.load_model(self.config_save_load_dir_path + 'model_right.h5')
        self.text_class_model = keras.models.load_model(self.config_save_load_dir_path + 'text_class_model.h5')

        QtCore.QTimer.singleShot(1, self.predictContainerNumber)

    def stopPredictBtnPressedEvent(self):
        self.startPredictBtn.setEnabled(True)
        self.stopPredictBtn.setEnabled(False)
        self.classifierOutputDisplyLCDNumber.display(0)
        self.startPredictBtn.repaint()
        self.stopPredictBtn.repaint()

    def predictContainerNumber(self):
        try:
            if self.no_records != 0:

                frame_raw = self.ser.readline().decode('utf-8').rstrip()

                ## frame contains accel+ color data
                dt = frame_raw.split(',')

                if dt.__len__() == 52:

                    colorSpaceConversionFunction = colorSpaceUtil.switcher.get(self.color_space)

                    frame = np.asarray([])
                    for i in np.arange(4, 52, 4):
                        frame = np.append(frame,
                                          colorSpaceConversionFunction(float(dt[i]), float(dt[i + 1]), float(dt[i + 2]),
                                                                       float(dt[i + 3])))

                    frame = frame.reshape(1, 36)

                    # frame_bottom = np.append(frame[:, 0:6], frame[:, 30:36]).reshape(1, 12)  # R4, R5 and L4, L5
                    # frame_left = frame[:, 18:30].reshape(1, 12)  # middle, L1, L2, L3
                    # frame_right = frame[:, 6:18].reshape(1, 12)  # R3, R2, R1, R0

                    # OR
                    # frame_bottom = frame[:, 12:24].reshape(1, 12)  # R1, R0, middle, L1
                    # frame_left = frame[:, 0:12].reshape(1, 12)  # R4, R5, R3, R2
                    # frame_right = frame[:, 24:36].reshape(1, 12)  # L2, L3,L4, L5

                    # OR
                    # frame_bottom = np.append(frame[:, 0:9], frame[:, 33:36]).reshape(1, 12)  # R5, R4 and R3, L5

                    # frame_left_1 = np.append(frame[:, 33:36], frame[:, 30:33])
                    # frame_left_2 = np.append( frame[:, 27:30], frame[:, 24:27])
                    # frame_left = np.append(frame_left_1, frame_left_2 ).reshape(1, 12)  # L5, L4, L3, L2

                    # frame_right_1 = np.append(frame[:, 12:15], frame[:, 9:12])
                    # frame_right_2 = np.append(frame[:, 6:9], frame[:, 3:6])
                    # frame_right = np.append(frame_right_1,frame_right_2 ).reshape(1, 12)  # R1, R2, R3, R4

                    # OR
                    # frame_bottom = frame[:, 0:3].reshape(1, 3)  # R5
                    # frame_left = frame[:, 30:33].reshape(1, 3)  # L4
                    # frame_right = frame[:, 9:12].reshape(1, 3)  # R2

                    # OR
                    frame_bottom = frame[:, 0:6].reshape(1, 6)  # R5, R4
                    frame_left = np.append(frame[:, 30:33], frame[:, 27:30]).reshape(1, 6)  # L4, L3
                    frame_right = np.append(frame[:, 9:12], frame[:, 6:9]).reshape(1, 6)  # R2, R3

                    if self.feature_type == 'PREPROCESSED':
                        frame_bottom = self.bottom_preprocessor.transform(frame_bottom)
                        frame_left = self.left_preprocessor.transform(frame_left)
                        frame_right = self.right_preprocessor.transform(frame_right)

                    result_bottom = self.model_bottom.predict(frame_bottom, batch_size=1)
                    result_left = self.model_left.predict(frame_left, batch_size=1)
                    result_right = self.model_right.predict(frame_right, batch_size=1)

                    result_bottom_predicted = result_bottom.argmax(axis=-1)[0]
                    result_left_predicted = result_left.argmax(axis=-1)[0]
                    result_right_predicted = result_right.argmax(axis=-1)[0]

                    # confidence greater than 50% then only append the data
                    if result_bottom_predicted != 0 and (result_bottom[0][result_bottom_predicted] * 100) > 70:
                        self.bottom_color_list.append(result_bottom_predicted)

                    if result_left_predicted != 0 and (result_left[0][result_left_predicted] * 100) > 70:
                        self.left_color_list.append(result_left_predicted)

                    if result_right_predicted != 0 and (result_right[0][result_right_predicted] * 100) > 70:
                        self.right_color_list.append(result_right_predicted)

                    self.no_records -= 1

            else:
                #  Majority voting
                bottom_color_list_vote = Counter(self.bottom_color_list)
                left_color_list_vote = Counter(self.left_color_list)
                right_color_list_vote = Counter(self.right_color_list)

                bottom_color = float(bottom_color_list_vote.most_common(1)[0][0])
                left_color = float(left_color_list_vote.most_common(1)[0][0])
                right_color = float(right_color_list_vote.most_common(1)[0][0])

                print("\nBottom Vote: ", bottom_color_list_vote)
                print("Left Vote: ", left_color_list_vote)
                print("Right Vote: ", right_color_list_vote)

                #  Text classification
                test_data = np.asarray([bottom_color, left_color, right_color]).reshape(1, 3)
                result_text_class = self.text_class_model.predict(test_data, batch_size=1)
                boxNumber = result_text_class.argmax(axis=-1)
                self.classifierOutputDisplyLCDNumber.display(str(boxNumber))

                print("Box Number: ", boxNumber)

                # Push the result into the file for verification purposes.
                prediction_details = str(int(bottom_color)) + ',' + str(int(left_color)) +',' +str(int(right_color)) + ',' + str(boxNumber[0]) + '\n'

                self.result_file.write(prediction_details)
                self.result_file.flush()

                #  Break the while loop and we repeat the step again.
                #  Reset the parameters
                self.no_records = 100
                self.bottom_color_list = [0]
                self.left_color_list = [0]
                self.right_color_list = [0]

            if not self.startPredictBtn.isEnabled():
                QtCore.QTimer.singleShot(1, self.predictContainerNumber)
                

        except:

            self.startPredictBtn.setEnabled(False)
            self.stopPredictBtn.setEnabled(True)
            self.startPredictBtn.repaint()
            self.stopPredictBtn.repaint()

            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

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
                    color_concept_values = self.color_concept_dict[self.containerNumberLabelValueDisplay.text()].split(
                        ',')

                    self.bottomClassLabelLineEdit.setText(color_concept_values[0])
                    self.leftClassLabelLineEdit.setText(color_concept_values[1])
                    self.rightClassLabelLineEdit.setText(color_concept_values[2])

                    self.bottomClassLabelLineEdit.repaint()
                    self.leftClassLabelLineEdit.repaint()
                    self.rightClassLabelLineEdit.repaint()

                classLabel = int(self.containerNumberLabelValueDisplay.text())  # To add class label to dictionary

                if not self.startCaptureBtn.isEnabled():

                    if classLabel in self.container_dict:
                        self.container_dict[classLabel] = self.container_dict[classLabel] + 1
                    else:
                        self.container_dict[classLabel] = 1

                    self.displayRemainingSamplesCount()
                    self.addTimerFunctionality()

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
            # self.leftClassLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())  # last record update issue
        if self.timer.isActive():
            self.timer.stop()
            self.captureTimeProgressBar.reset()

    def randomNumberCheckBoxPressedEvent(self):
        if self.randomNumberCheckBox.isChecked():
            # self.leftClassLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
            self.displayRandomContainerNumber()
            self.bottomClassLabelLineEdit.setEnabled(False)
            self.leftClassLabelLineEdit.setEnabled(False)
            self.rightClassLabelLineEdit.setEnabled(False)
            self.randomNumberLowerLimitLineEdit.setEnabled(True)
            self.randomNumberUpperLimitLineEdit.setEnabled(True)
        else:
            self.bottomClassLabelLineEdit.setEnabled(True)
            self.leftClassLabelLineEdit.setEnabled(True)
            self.rightClassLabelLineEdit.setEnabled(True)
            self.randomNumberLowerLimitLineEdit.setEnabled(False)
            self.randomNumberUpperLimitLineEdit.setEnabled(False)

    def randomNumberUpperLowerLimitLineEditTextChangeEvent(self):
        try:
            if self.randomNumberLowerLimitLineEdit.text().__len__() > 0 and self.randomNumberUpperLimitLineEdit.text().__len__() > 0 and self.samplesPerKeyCountLineEdit.text().__len__() > 0:
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

        bottom_file_name = write_path + file_name + "_bottom.csv"
        left_file_name = write_path + file_name + "_left.csv"
        right_file_name = write_path + file_name + "_right.csv"
        
        self.bottom_file = open(bottom_file_name, 'a')
        self.left_file = open(left_file_name, 'a')
        self.right_file = open(right_file_name, 'a')

    def displayRandomContainerNumber(self):
        randomNumberLowerLimit = int(self.randomNumberLowerLimitLineEdit.text())
        randomNumberUpperLimit = int(self.randomNumberUpperLimitLineEdit.text())
        maxSamplesPerKeyCount = int(self.samplesPerKeyCountLineEdit.text())

        if sum(self.container_dict.values()) == (
                randomNumberUpperLimit - randomNumberLowerLimit - self.skip_container_numbers.__len__() + 1) * maxSamplesPerKeyCount:
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
                if self.container_dict[random_box_number] < maxSamplesPerKeyCount:
                    break
                else:
                    continue  # Try other value
            else:
                break

        self.containerNumberLabelValueDisplay.setText(str(random_box_number))
        self.containerNumberLabelValueDisplay.repaint()

        self.displayRemainingSamplesCount()  # To reset the remaining sample count value

    def isValidFields(self):
        return_value = self.fileNameLineEdit.text().__len__() > 0 and self.leftClassLabelLineEdit.text().__len__() > 0 \
                       and self.recordingFolderLocationLineEdit.text().__len__() > 0
        if not return_value:
            self.displayWarningPopUp("Please fill the required fields !!")
            return return_value
        return return_value

    def resetFields(self):
        if self.startCaptureBtn.isEnabled():
            self.fileNameLineEdit.clear()
            self.leftClassLabelLineEdit.clear()
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
        maxSamplesPerKeyCount = int(self.samplesPerKeyCountLineEdit.text())
        maxNumberOfSamples = (
                                     randomNumberUpperLimit - randomNumberLowerLimit - self.skip_container_numbers.__len__() + 1) * maxSamplesPerKeyCount
        remainingNumberOfContainers = maxNumberOfSamples - dictionarySumOfValues
        self.remainingSamplesToCaptureLCDNumber.display(str(remainingNumberOfContainers))

    def addTimerFunctionality(self):
        if self.enableTimerCheckBox.isChecked():
            timerUpperLimit = int(self.timerInSecondsLineEdit.text())
            self.captureTimeProgressBar.setMaximum(timerUpperLimit)
            self.captureTimeProgressBar.repaint()
            self.start_time = 0
            self.timer.start(1000)
        elif self.timer.isActive():
            self.timer.stop()

    def updateProgressBar(self):
        self.start_time += 1
        timerUpperLimit = int(self.timerInSecondsLineEdit.text())
        if self.start_time <= timerUpperLimit:
            self.captureTimeProgressBar.setValue(self.start_time)
        elif self.timer.isActive():
            self.timer.stop()
            self.captureTimeProgressBar.reset()
            self.stopCaptureBtnPressedEvent()

    def closeWindow(self):
        QtCore.QCoreApplication.instance().quit()

    def releaseResource(self):
        print("Releasing Resources.... ")
        if self.ser is not None and self.ser.isOpen():
            self.ser.close()

        if self.bottom_file is not None and not self.bottom_file.closed:
            self.bottom_file.close()

        if self.left_file is not None and not self.left_file.closed:
            self.left_file.close()

        if self.right_file is not None and not self.right_file.closed:
            self.right_file.close()

        if self.result_file is not None and not self.result_file.closed:
            self.result_file.close()

        self.save_dictionary('container_dict.txt')

    def save_dictionary(self, file_name):
        print('Dictionary contents\n{}'.format(self.container_dict.items()))
        with open(file_name, "wb") as myFile:
            pickle.dump(self.container_dict, myFile)
            myFile.close()

    def load_dictionary(self, file_name):
        try:

            with open('resources/color_concept_map_input.csv') as color_concept_dict_file:
                reader = csv.reader(color_concept_dict_file)
                headers = next(reader)
                for row in reader:
                    self.color_concept_dict[row[0]] = row[1] + ',' + row[2] + ',' + row[3]
                color_concept_dict_file.close()

            with open(file_name, "rb") as myFile:
                self.container_dict = pickle.load(myFile)
                print('loaded dictionary. The dictionary contents are : \n{}'.format(self.container_dict.items()))
                myFile.close()
        except FileNotFoundError:
            self.container_dict = {}
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
