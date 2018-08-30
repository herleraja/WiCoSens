# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NUCER\Documents\git\WiCoSens\MLDataLabeler\mlDataLabeler_rack_container_box.ui'
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

ser = None
file = None
container_dict = None
#random_container_number = None

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
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 1295, 631))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.dataLabelingTabGridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.dataLabelingTabGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.dataLabelingTabGridLayout.setContentsMargins(0, 0, 0, 0)
        self.dataLabelingTabGridLayout.setObjectName("dataLabelingTabGridLayout")
        self.classLabelHorizontalLayout = QtWidgets.QHBoxLayout()
        self.classLabelHorizontalLayout.setObjectName("classLabelHorizontalLayout")
        self.boxLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.boxLabel.setObjectName("boxLabel")
        self.classLabelHorizontalLayout.addWidget(self.boxLabel)
        self.boxLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.boxLabelLineEdit.setEnabled(False)
        self.boxLabelLineEdit.setObjectName("boxLabelLineEdit")
        self.classLabelHorizontalLayout.addWidget(self.boxLabelLineEdit)
        self.rackLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.rackLabel.setObjectName("rackLabel")
        self.classLabelHorizontalLayout.addWidget(self.rackLabel)
        self.rackLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rackLabelLineEdit.setEnabled(False)
        self.rackLabelLineEdit.setObjectName("rackLabelLineEdit")
        self.classLabelHorizontalLayout.addWidget(self.rackLabelLineEdit)
        self.containerLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerLabel.setObjectName("containerLabel")
        self.classLabelHorizontalLayout.addWidget(self.containerLabel)
        self.containerLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.containerLabelLineEdit.setEnabled(False)
        self.containerLabelLineEdit.setObjectName("containerLabelLineEdit")
        self.classLabelHorizontalLayout.addWidget(self.containerLabelLineEdit)
        self.dataLabelingTabGridLayout.addLayout(self.classLabelHorizontalLayout, 2, 1, 1, 1)
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
        self.dataLabelingTabGridLayout.addLayout(self.sensorButtonHorizontalLayout, 8, 1, 1, 1)
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
        self.colorSpaceHSVButton.setChecked(False)
        self.colorSpaceHSVButton.setAutoExclusive(True)
        self.colorSpaceHSVButton.setObjectName("colorSpaceHSVButton")
        self.colorSpaceButtonsHorizontalLayout.addWidget(self.colorSpaceHSVButton)
        self.dataLabelingTabGridLayout.addLayout(self.colorSpaceButtonsHorizontalLayout, 9, 1, 1, 1)
        self.sensorEnableDisableLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorEnableDisableLabel.setObjectName("sensorEnableDisableLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorEnableDisableLabel, 8, 0, 1, 1)
        self.containerNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabel.setObjectName("containerNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabel, 1, 0, 1, 1)
        self.capturSensorDataHLayout = QtWidgets.QHBoxLayout()
        self.capturSensorDataHLayout.setObjectName("capturSensorDataHLayout")
        self.startCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.startCaptureBtn.setMouseTracking(False)
        self.startCaptureBtn.setObjectName("startCaptureBtn")
        self.capturSensorDataHLayout.addWidget(self.startCaptureBtn)
        self.stopCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.stopCaptureBtn.setEnabled(False)
        self.stopCaptureBtn.setObjectName("stopCaptureBtn")
        self.capturSensorDataHLayout.addWidget(self.stopCaptureBtn)
        self.dataLabelingTabGridLayout.addLayout(self.capturSensorDataHLayout, 3, 1, 1, 1)
        self.colorSpaceLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.colorSpaceLabel.setObjectName("colorSpaceLabel")
        self.dataLabelingTabGridLayout.addWidget(self.colorSpaceLabel, 9, 0, 1, 1)
        self.captureLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.captureLabel.setObjectName("captureLabel")
        self.dataLabelingTabGridLayout.addWidget(self.captureLabel, 3, 0, 1, 1)
        self.randomNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberLabel.setObjectName("randomNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.randomNumberLabel, 10, 0, 1, 1)
        self.sensorTextLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorTextLabel.setObjectName("sensorTextLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextLabel, 11, 0, 1, 1)
        self.sensorTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sensorTextEdit.setUndoRedoEnabled(False)
        self.sensorTextEdit.setReadOnly(True)
        self.sensorTextEdit.setObjectName("sensorTextEdit")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextEdit, 11, 1, 1, 1)
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
        self.dataLabelingTabGridLayout.addLayout(self.closeResetHLayout, 15, 1, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLabel, 7, 0, 1, 1)
        self.containerNumberLabelValueDisplay = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabelValueDisplay.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 170, 0))
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
        self.randomNumberHorizontalLayout = QtWidgets.QHBoxLayout()
        self.randomNumberHorizontalLayout.setObjectName("randomNumberHorizontalLayout")
        self.ranodmNumberEnableLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ranodmNumberEnableLabel.setObjectName("ranodmNumberEnableLabel")
        self.randomNumberHorizontalLayout.addWidget(self.ranodmNumberEnableLabel)
        self.randomNumberCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.randomNumberCheckBox.setText("")
        self.randomNumberCheckBox.setChecked(True)
        self.randomNumberCheckBox.setObjectName("randomNumberCheckBox")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberCheckBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem1)
        self.randomNumberUpperLimitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberUpperLimitLabel.setObjectName("randomNumberUpperLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLabel)
        self.randomNumberUpperLimitLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.randomNumberUpperLimitLineEdit.setObjectName("randomNumberUpperLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem5)
        self.dataLabelingTabGridLayout.addLayout(self.randomNumberHorizontalLayout, 10, 1, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.dataLabelingTabGridLayout.addWidget(self.fileNameLineEdit, 7, 1, 1, 1)
        self.classLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classLabelLabel.setObjectName("classLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLabel, 2, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem7, 4, 0, 1, 1)
        self.tagButtonGroupBox = QtWidgets.QGroupBox(self.formLayoutWidget)
        self.tagButtonGroupBox.setObjectName("tagButtonGroupBox")
        self.emptyTagPushButton = QtWidgets.QPushButton(self.tagButtonGroupBox)
        self.emptyTagPushButton.setGeometry(QtCore.QRect(10, 20, 371, 23))
        self.emptyTagPushButton.setCheckable(True)
        self.emptyTagPushButton.setChecked(False)
        self.emptyTagPushButton.setAutoExclusive(True)
        self.emptyTagPushButton.setAutoDefault(True)
        self.emptyTagPushButton.setDefault(False)
        self.emptyTagPushButton.setFlat(False)
        self.emptyTagPushButton.setObjectName("emptyTagPushButton")
        self.rackLabelCapturePushButton = QtWidgets.QPushButton(self.tagButtonGroupBox)
        self.rackLabelCapturePushButton.setGeometry(QtCore.QRect(380, 20, 371, 23))
        self.rackLabelCapturePushButton.setCheckable(True)
        self.rackLabelCapturePushButton.setAutoExclusive(True)
        self.rackLabelCapturePushButton.setObjectName("rackLabelCapturePushButton")
        self.containerLabelCapturePushButton = QtWidgets.QPushButton(self.tagButtonGroupBox)
        self.containerLabelCapturePushButton.setGeometry(QtCore.QRect(750, 20, 371, 23))
        self.containerLabelCapturePushButton.setCheckable(True)
        self.containerLabelCapturePushButton.setAutoExclusive(True)
        self.containerLabelCapturePushButton.setObjectName("containerLabelCapturePushButton")
        self.dataLabelingTabGridLayout.addWidget(self.tagButtonGroupBox, 4, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem8, 5, 0, 1, 1)
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
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHorizontalLayout.addItem(spacerItem9)
        self.portlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.portlineEdit.setObjectName("portlineEdit")
        self.portHorizontalLayout.addWidget(self.portlineEdit)
        self.setialPortSettingsVerticalLayout.addLayout(self.portHorizontalLayout)
        self.settingTabMainGridLayout.addLayout(self.setialPortSettingsVerticalLayout, 0, 1, 1, 1)
        self.recordingFolderLocationhorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingFolderLocationhorizontalLayout.setObjectName("recordingFolderLocationhorizontalLayout")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.recordingFolderLocationhorizontalLayout.addItem(spacerItem10)
        self.recordingFolderLocationLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.recordingFolderLocationLineEdit.setObjectName("recordingFolderLocationLineEdit")
        self.recordingFolderLocationhorizontalLayout.addWidget(self.recordingFolderLocationLineEdit)
        self.settingTabMainGridLayout.addLayout(self.recordingFolderLocationhorizontalLayout, 1, 1, 1, 1)
        self.serialPortSettingsLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serialPortSettingsLabel.setObjectName("serialPortSettingsLabel")
        self.settingTabMainGridLayout.addWidget(self.serialPortSettingsLabel, 0, 0, 1, 1)
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

        self.load_dictionary('container_dict.txt')

        if self.randomNumberCheckBox.isChecked():
            self.displayRandomContainerNumber()
            self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())

        self.addButtonOperations()
        self.addFiledsValidators()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Collection"))
        self.boxLabel.setText(_translate("MainWindow", "Box Label"))
        self.rackLabel.setText(_translate("MainWindow", "Rack Label"))
        self.containerLabel.setText(_translate("MainWindow", "Container Label"))
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
        self.sensorEnableDisableLabel.setText(_translate("MainWindow", "Enable / Disable Color Sensor"))
        self.containerNumberLabel.setText(_translate("MainWindow", "Container Number"))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start"))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop"))
        self.colorSpaceLabel.setText(_translate("MainWindow", "Color Space"))
        self.captureLabel.setText(_translate("MainWindow", "Capture Sensor Data"))
        self.randomNumberLabel.setText(_translate("MainWindow", "Use random number generator "))
        self.sensorTextLabel.setText(_translate("MainWindow", "Captured Sensor Data"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.closeBtn.setText(_translate("MainWindow", "Close"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.containerNumberLabelValueDisplay.setText(_translate("MainWindow", "999"))
        self.ranodmNumberEnableLabel.setText(_translate("MainWindow", "Enable Randomness"))
        self.randomNumberUpperLimitLabel.setText(_translate("MainWindow", "Random Number Upper Limit"))
        self.randomNumberUpperLimitLineEdit.setText(_translate("MainWindow", "24"))
        self.fileNameLineEdit.setText(_translate("MainWindow", "rack1"))
        self.classLabelLabel.setText(_translate("MainWindow", "Class Labels"))
        self.tagButtonGroupBox.setTitle(_translate("MainWindow", "Tag Button"))
        self.emptyTagPushButton.setText(_translate("MainWindow", "Empty Tag"))
        self.rackLabelCapturePushButton.setText(_translate("MainWindow", "Tag Rack Label"))
        self.containerLabelCapturePushButton.setText(_translate("MainWindow", "Tag Container Label"))
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
        self.recordingFolderLocationLineEdit.setText(_translate("MainWindow", "recording_folder/"))
        self.serialPortSettingsLabel.setText(_translate("MainWindow", "Serial Port Settings"))
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
        self.stopCaptureBtn.clicked.connect(self.stopCaptureBtnPressedEvent)
        self.randomNumberCheckBox.clicked.connect(self.randomNumberCheckBoxPressedEvent)
        self.randomNumberUpperLimitLineEdit.textChanged.connect(self.randomNumberUpperLimitLineEditTextChangeEvent)
        self.startCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space))
        self.stopCaptureBtn.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Escape))

    def addFiledsValidators(self):

        regexp = QtCore.QRegExp('[a-zA-Z0-9_ -]+')
        validator = QtGui.QRegExpValidator(regexp)

        self.fileNameLineEdit.setValidator(validator)
        self.boxLabelLineEdit.setValidator(validator)

    def getClassLabels(self):
        rack_label = container_label = box_label = '0'

        if self.emptyTagPushButton.isChecked():
            rack_label = container_label = box_label = '0'

        elif self.rackLabelCapturePushButton.isChecked():
            rack_label = self.rackLabelLineEdit.text()
            box_label = self.boxLabelLineEdit.text()

        elif self.containerLabelCapturePushButton.isChecked():
            container_label = self.containerLabelLineEdit.text()
            box_label = self.boxLabelLineEdit.text()

        labels = ',' + rack_label + ',' + container_label + ',' + box_label

        return labels

    def captureSensorData(self):
        try:

            new_line = self.ser.readline().decode('utf-8').rstrip()
            # new_line = "test1, Test2, Test3"

            ## frame contains accel+ color data
            line_array = new_line.split(',')

            if line_array.__len__() == 54:

                new_line = line_array[0] + ',' + line_array[1] + ',' + line_array[2] + ',' + line_array[3]

                # for i in (6,10,14,18,22,26,30,34,38,42,46,50):
                #    new_line += self.rgb2hsv(float(line_array[i]), float(line_array[i+1]), float(line_array[i+2]),float(line_array[i+3]))

                if self.colSensorButton1.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[6]), float(line_array[7]),
                                                          float(line_array[8]),
                                                          float(line_array[9]))  # Right side(R5) sensor
                if self.colSensorButton2.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[10]), float(line_array[11]),
                                                          float(line_array[12]),
                                                          float(line_array[13]))  # Right side(R4) sensor
                if self.colSensorButton3.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[14]), float(line_array[15]),
                                                          float(line_array[16]),
                                                          float(line_array[17]))  # Right side(R3) sensor
                if self.colSensorButton4.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[18]), float(line_array[19]),
                                                          float(line_array[20]),
                                                          float(line_array[21]))  # Right side(R2) sensor
                if self.colSensorButton5.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[22]), float(line_array[23]),
                                                          float(line_array[24]),
                                                          float(line_array[25]))  # Right side(R1) sensor
                if self.colSensorButton6.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[26]), float(line_array[27]),
                                                          float(line_array[28]),
                                                          float(line_array[29]))  # Right side(R0) sensor
                if self.colSensorButton7.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[30]), float(line_array[31]),
                                                          float(line_array[32]), float(line_array[33]))  # middle sensor
                if self.colSensorButton8.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[34]), float(line_array[35]),
                                                          float(line_array[36]),
                                                          float(line_array[37]))  # Left side(L1) sensor
                if self.colSensorButton9.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[38]), float(line_array[39]),
                                                          float(line_array[40]),
                                                          float(line_array[41]))  # Left side(L2) sensor
                if self.colSensorButton10.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[42]), float(line_array[43]),
                                                          float(line_array[44]),
                                                          float(line_array[45]))  # Left side(L3) sensor
                if self.colSensorButton11.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[46]), float(line_array[47]),
                                                          float(line_array[48]),
                                                          float(line_array[49]))  # Left side(L4) sensor
                if self.colSensorButton12.isChecked():
                    new_line += self.colorSpaceCoverstion(float(line_array[50]), float(line_array[51]),
                                                          float(line_array[52]),
                                                          float(line_array[53]))  # Left side(L5) sensor

                new_line = new_line + self.getClassLabels() + '\n'

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
                    self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
                    self.boxLabelLineEdit.repaint()

                classLabel = int(self.boxLabelLineEdit.text())  # To add class label to dictionary

                if not self.startCaptureBtn.isEnabled():

                    if classLabel in self.container_dict:
                        self.container_dict[classLabel] = self.container_dict[classLabel] + 1
                    else:
                        self.container_dict[classLabel] = 1

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
            # self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())  # last record update issue

    def randomNumberCheckBoxPressedEvent(self):
        if self.randomNumberCheckBox.isChecked():
            self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
            self.boxLabelLineEdit.setEnabled(False)
            self.randomNumberUpperLimitLineEdit.setEnabled(True)
        else:
            self.boxLabelLineEdit.setEnabled(True)
            self.randomNumberUpperLimitLineEdit.setEnabled(False)

    def randomNumberUpperLimitLineEditTextChangeEvent(self):
        self.container_dict = {}  # To reset the dictionary
        self.displayRandomContainerNumber()  # To reset the random number value

    def openFileForWriting(self):
        write_path = self.recordingFolderLocationLineEdit.text()
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        file_name = self.fileNameLineEdit.text()
        file_name = write_path + file_name + ".csv"
        self.file = open(file_name, 'a')

    def displayRandomContainerNumber(self):
        totalContainers = int(self.randomNumberUpperLimitLineEdit.text())
        maxSamplesPerKeyCount = 1
        skip_container_numbers = [1, 6, 11, 16]
        # skip_container_numbers = [1]

        if not hasattr(self, 'container_dict'):
            self.container_dict = {}

        if sum(self.container_dict.values()) == (
                totalContainers - skip_container_numbers.__len__() + 1) * maxSamplesPerKeyCount:
            print(
                "\n\nThe sample reached maximum size limit / all the container samples taken. "
                "To take more samples please change **maxSamplesPerKeyCount** variable.\n\n")
            exit()

        while True:
            random_container_number = random.randint(0, totalContainers)  # to display random number from 0 to 24

            if random_container_number in skip_container_numbers:  # skip the mentioned box numbers
                continue

            if random_container_number in self.container_dict:
                if self.container_dict[random_container_number] < maxSamplesPerKeyCount:
                    # self.container_dict[random_container_number] = self.container_dict[random_container_number] + 1
                    break
                else:
                    continue  # Try other value
            else:
                # self.container_dict[random_container_number] = 1
                break

        self.containerNumberLabelValueDisplay.setText(str(random_container_number))
        self.containerNumberLabelValueDisplay.repaint()



    def isValidFields(self):

        return_value = self.fileNameLineEdit.text().__len__() > 0 and self.boxLabelLineEdit.text().__len__() > 0 \
                       and self.recordingFolderLocationLineEdit.text().__len__() > 0
        if not return_value:
            self.displayWarningPopUp("Please fill the required fields !!")
            return return_value
        # if self.randomNumberCheckBox.isChecked() and self.boxLabelLineEdit.text() != self.containerNumberLabelValueDisplay.text():
        # self.displayWarningPopUp("Class Label is not same as generated container number.")
        # return False
        return return_value

    def resetFields(self):
        if self.startCaptureBtn.isEnabled():
            self.fileNameLineEdit.clear()
            self.boxLabelLineEdit.clear()
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
        msgbox = QtWidgets.QMessageBox()
        msgbox.setText(warningText)
        msgbox.setWindowTitle("Warning !! ")
        msgbox.setIcon(QtWidgets.QMessageBox.Warning)
        msgbox.exec()

    def closeWindow(self):
        QtCore.QCoreApplication.instance().quit()

    def releaseResource(self):
        print("Releasing Resources.... ")
        if hasattr(self, 'ser') and self.ser.isOpen():
            self.ser.close()
        if hasattr(self, 'file') and not self.file.closed:
            self.file.close()
        if hasattr(self, 'container_dict'):
            self.save_dictionary('container_dict.txt')

    def save_dictionary(self, file_name):
        print('Dictionary contents\n{}'.format(self.container_dict.items()))
        with open(file_name, "wb") as myFile:
            pickle.dump(self.container_dict, myFile)
            myFile.close()

    def load_dictionary(self, file_name):
        try:
            with open(file_name, "rb") as myFile:
                container_dict = pickle.load(myFile)
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
