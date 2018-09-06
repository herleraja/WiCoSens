# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\NUCER\Documents\git\WiCoSens\MLDataLabeler\mlDataLabeler_rack_container_box.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

import atexit
import csv
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
    currentState = lastState = 0
    container_dict = rack_container_box_dict = {}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1342, 715)
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
        self.closeResetHLayout = QtWidgets.QHBoxLayout()
        self.closeResetHLayout.setObjectName("closeResetHLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.closeResetHLayout.addItem(spacerItem)
        self.startCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.startCaptureBtn.setMouseTracking(False)
        self.startCaptureBtn.setObjectName("startCaptureBtn")
        self.closeResetHLayout.addWidget(self.startCaptureBtn)
        self.stopCaptureBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.stopCaptureBtn.setEnabled(False)
        self.stopCaptureBtn.setObjectName("stopCaptureBtn")
        self.closeResetHLayout.addWidget(self.stopCaptureBtn)
        self.clearPushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.clearPushButton.setObjectName("clearPushButton")
        self.closeResetHLayout.addWidget(self.clearPushButton)
        self.resetBtn = QtWidgets.QPushButton(self.formLayoutWidget)
        self.resetBtn.setObjectName("resetBtn")
        self.closeResetHLayout.addWidget(self.resetBtn)
        self.dataLabelingTabGridLayout.addLayout(self.closeResetHLayout, 14, 1, 1, 1)
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
        self.containerNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.containerNumberLabel.setObjectName("containerNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.containerNumberLabel, 1, 0, 1, 1)
        self.classLabelHorizontalLayout = QtWidgets.QHBoxLayout()
        self.classLabelHorizontalLayout.setObjectName("classLabelHorizontalLayout")
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
        self.boxLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.boxLabel.setObjectName("boxLabel")
        self.classLabelHorizontalLayout.addWidget(self.boxLabel)
        self.boxLabelLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.boxLabelLineEdit.setEnabled(False)
        self.boxLabelLineEdit.setObjectName("boxLabelLineEdit")
        self.classLabelHorizontalLayout.addWidget(self.boxLabelLineEdit)
        self.dataLabelingTabGridLayout.addLayout(self.classLabelHorizontalLayout, 2, 1, 1, 1)
        self.classLabelLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.classLabelLabel.setObjectName("classLabelLabel")
        self.dataLabelingTabGridLayout.addWidget(self.classLabelLabel, 2, 0, 1, 1)
        self.tagButtonGroupBox = QtWidgets.QGroupBox(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagButtonGroupBox.sizePolicy().hasHeightForWidth())
        self.tagButtonGroupBox.setSizePolicy(sizePolicy)
        self.tagButtonGroupBox.setObjectName("tagButtonGroupBox")
        self.emptyTagPushButton = QtWidgets.QPushButton(self.tagButtonGroupBox)
        self.emptyTagPushButton.setGeometry(QtCore.QRect(10, 20, 371, 23))
        self.emptyTagPushButton.setCheckable(True)
        self.emptyTagPushButton.setChecked(True)
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
        self.dataLabelingTabGridLayout.addWidget(self.tagButtonGroupBox, 3, 1, 1, 1)
        self.sensorTextLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.sensorTextLabel.setObjectName("sensorTextLabel")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextLabel, 12, 0, 1, 1)
        self.randomNumberHorizontalLayout = QtWidgets.QHBoxLayout()
        self.randomNumberHorizontalLayout.setObjectName("randomNumberHorizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem1)
        self.ranodmNumberEnableLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.ranodmNumberEnableLabel.setObjectName("ranodmNumberEnableLabel")
        self.randomNumberHorizontalLayout.addWidget(self.ranodmNumberEnableLabel)
        self.randomNumberCheckBox = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.randomNumberCheckBox.setText("")
        self.randomNumberCheckBox.setChecked(True)
        self.randomNumberCheckBox.setObjectName("randomNumberCheckBox")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberCheckBox)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem2)
        self.randomNumberUpperLimitLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberUpperLimitLabel.setObjectName("randomNumberUpperLimitLabel")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLabel)
        self.randomNumberUpperLimitLineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.randomNumberUpperLimitLineEdit.setObjectName("randomNumberUpperLimitLineEdit")
        self.randomNumberHorizontalLayout.addWidget(self.randomNumberUpperLimitLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.randomNumberHorizontalLayout.addItem(spacerItem3)
        self.dataLabelingTabGridLayout.addLayout(self.randomNumberHorizontalLayout, 7, 1, 1, 1)
        self.sensorTextEdit = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.sensorTextEdit.setReadOnly(True)
        self.sensorTextEdit.setObjectName("sensorTextEdit")
        self.dataLabelingTabGridLayout.addWidget(self.sensorTextEdit, 12, 1, 1, 1)
        self.stateLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.stateLabel.setText("")
        self.stateLabel.setObjectName("stateLabel")
        self.dataLabelingTabGridLayout.addWidget(self.stateLabel, 11, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem4, 9, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        self.randomNumberLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.randomNumberLabel.setObjectName("randomNumberLabel")
        self.dataLabelingTabGridLayout.addWidget(self.randomNumberLabel, 7, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem6, 10, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.dataLabelingTabGridLayout.addItem(spacerItem7, 8, 0, 1, 1)
        self.captureBtnsHorizontalLayout = QtWidgets.QHBoxLayout()
        self.captureBtnsHorizontalLayout.setObjectName("captureBtnsHorizontalLayout")
        self.stateChangePushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.stateChangePushButton.setObjectName("stateChangePushButton")
        self.captureBtnsHorizontalLayout.addWidget(self.stateChangePushButton)
        self.randomBoxNumberGeneratorPushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.randomBoxNumberGeneratorPushButton.setObjectName("randomBoxNumberGeneratorPushButton")
        self.captureBtnsHorizontalLayout.addWidget(self.randomBoxNumberGeneratorPushButton)
        self.saveDataManuallyPushButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.saveDataManuallyPushButton.setObjectName("saveDataManuallyPushButton")
        self.captureBtnsHorizontalLayout.addWidget(self.saveDataManuallyPushButton)
        self.dataLabelingTabGridLayout.addLayout(self.captureBtnsHorizontalLayout, 11, 1, 1, 1)
        self.mainTabObj.addTab(self.dataLabelingTab, "")
        self.settingTab = QtWidgets.QWidget()
        self.settingTab.setObjectName("settingTab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.settingTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(20, 10, 1116, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.settingTabMainGridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.settingTabMainGridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.settingTabMainGridLayout.setContentsMargins(0, 0, 0, 0)
        self.settingTabMainGridLayout.setObjectName("settingTabMainGridLayout")
        self.recordingFolderLocationLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.recordingFolderLocationLabel.setObjectName("recordingFolderLocationLabel")
        self.settingTabMainGridLayout.addWidget(self.recordingFolderLocationLabel, 1, 0, 1, 1)
        self.serialPortSettingsLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.serialPortSettingsLabel.setObjectName("serialPortSettingsLabel")
        self.settingTabMainGridLayout.addWidget(self.serialPortSettingsLabel, 0, 0, 1, 1)
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
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.portHorizontalLayout.addItem(spacerItem8)
        self.portlineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.portlineEdit.setObjectName("portlineEdit")
        self.portHorizontalLayout.addWidget(self.portlineEdit)
        self.setialPortSettingsVerticalLayout.addLayout(self.portHorizontalLayout)
        self.settingTabMainGridLayout.addLayout(self.setialPortSettingsVerticalLayout, 0, 1, 1, 1)
        self.fileNameLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.fileNameLineEdit.setEnabled(False)
        self.fileNameLineEdit.setObjectName("fileNameLineEdit")
        self.settingTabMainGridLayout.addWidget(self.fileNameLineEdit, 2, 1, 1, 1)
        self.recordingFolderLocationhorizontalLayout = QtWidgets.QHBoxLayout()
        self.recordingFolderLocationhorizontalLayout.setObjectName("recordingFolderLocationhorizontalLayout")
        self.recordingFolderLocationLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.recordingFolderLocationLineEdit.setObjectName("recordingFolderLocationLineEdit")
        self.recordingFolderLocationhorizontalLayout.addWidget(self.recordingFolderLocationLineEdit)
        self.settingTabMainGridLayout.addLayout(self.recordingFolderLocationhorizontalLayout, 1, 1, 1, 1)
        self.fileNameLabel = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.fileNameLabel.setEnabled(False)
        self.fileNameLabel.setObjectName("fileNameLabel")
        self.settingTabMainGridLayout.addWidget(self.fileNameLabel, 2, 0, 1, 1)
        self.sensorEnableDisableLabel_2 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.sensorEnableDisableLabel_2.setObjectName("sensorEnableDisableLabel_2")
        self.settingTabMainGridLayout.addWidget(self.sensorEnableDisableLabel_2, 3, 0, 1, 1)
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

        self.load_dictionary()

        if self.randomNumberCheckBox.isChecked():
            self.displayRandomBoxNumber()

        self.addButtonOperations()
        self.addFiledsValidators()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Collection"))
        self.startCaptureBtn.setToolTip(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setWhatsThis(_translate("MainWindow", "click to capture the sensor data"))
        self.startCaptureBtn.setText(_translate("MainWindow", "Start"))
        self.stopCaptureBtn.setText(_translate("MainWindow", "Stop"))
        self.clearPushButton.setText(_translate("MainWindow", "Clear"))
        self.resetBtn.setText(_translate("MainWindow", "Reset"))
        self.containerNumberLabelValueDisplay.setText(_translate("MainWindow", "999"))
        self.containerNumberLabel.setText(_translate("MainWindow", "Box  Number"))
        self.rackLabel.setText(_translate("MainWindow", "Rack Label"))
        self.containerLabel.setText(_translate("MainWindow", "Container Label"))
        self.boxLabel.setText(_translate("MainWindow", "Box Label"))
        self.classLabelLabel.setText(_translate("MainWindow", "Class Labels"))
        self.tagButtonGroupBox.setTitle(_translate("MainWindow", "States"))
        self.emptyTagPushButton.setText(_translate("MainWindow", "Empty Tag"))
        self.rackLabelCapturePushButton.setText(_translate("MainWindow", "Tag Rack Label"))
        self.containerLabelCapturePushButton.setText(_translate("MainWindow", "Tag Container Label"))
        self.sensorTextLabel.setText(_translate("MainWindow", "Captured Sensor Data"))
        self.ranodmNumberEnableLabel.setText(_translate("MainWindow", "Enable Randomness"))
        self.randomNumberUpperLimitLabel.setText(_translate("MainWindow", "Number of Boxes"))
        self.randomNumberUpperLimitLineEdit.setText(_translate("MainWindow", "24"))
        self.randomNumberLabel.setText(_translate("MainWindow", "Use random number generator "))
        self.stateChangePushButton.setText(_translate("MainWindow", "State Change"))
        self.randomBoxNumberGeneratorPushButton.setText(_translate("MainWindow", "Generate Random Box Number"))
        self.saveDataManuallyPushButton.setText(_translate("MainWindow", "Save Data Manually"))
        self.mainTabObj.setTabText(self.mainTabObj.indexOf(self.dataLabelingTab), _translate("MainWindow", "Data labeling"))
        self.recordingFolderLocationLabel.setText(_translate("MainWindow", "Recording Folder Location"))
        self.serialPortSettingsLabel.setText(_translate("MainWindow", "Serial Port Settings"))
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
        self.fileNameLineEdit.setText(_translate("MainWindow", "<< Future use >>"))
        self.recordingFolderLocationLineEdit.setText(_translate("MainWindow", "datarecording/"))
        self.fileNameLabel.setText(_translate("MainWindow", "FileName"))
        self.sensorEnableDisableLabel_2.setText(_translate("MainWindow", "Enable / Disable Color Sensor"))
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
        self.clearPushButton.clicked.connect(self.clearSensorData)
        self.resetBtn.clicked.connect(self.resetFields)
        self.startCaptureBtn.clicked.connect(self.startBtnPressedEvent)
        self.stopCaptureBtn.clicked.connect(self.stopCaptureBtnPressedEvent)
        self.randomNumberCheckBox.clicked.connect(self.randomNumberCheckBoxPressedEvent)
        self.randomNumberUpperLimitLineEdit.textChanged.connect(self.randomNumberUpperLimitLineEditTextChangeEvent)
        self.stateChangePushButton.clicked.connect(self.stateChangeBtnPressedEvent)
        self.randomBoxNumberGeneratorPushButton.clicked.connect(self.randomBoxNumberChangeBtnPressedEvent)
        self.saveDataManuallyPushButton.clicked.connect(self.saveDataManuallyBtnPressedEvent)

        self.stateChangePushButton.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Space))
        self.randomBoxNumberGeneratorPushButton.setShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return))

    def addFiledsValidators(self):

        regexp = QtCore.QRegExp('[a-zA-Z0-9_ -]+')
        validator = QtGui.QRegExpValidator(regexp)

        self.fileNameLineEdit.setValidator(validator)
        self.boxLabelLineEdit.setValidator(validator)

    def getClassLabels(self):
        rack_label = container_label = box_label = '0'

        if self.emptyTagPushButton.isChecked():
            rack_label = container_label = box_label = '0'
            self.currentState = 0

        elif self.rackLabelCapturePushButton.isChecked():
            rack_label = self.rackLabelLineEdit.text()
            box_label = self.boxLabelLineEdit.text()
            self.currentState = 1

        elif self.containerLabelCapturePushButton.isChecked():
            container_label = self.containerLabelLineEdit.text()
            box_label = self.boxLabelLineEdit.text()
            self.currentState = 2

        labels = ',' + str(self.currentState) + ',' + rack_label + ',' + container_label + ',' + box_label

        return labels

    def saveSensorData(self):
        try:
            self.openFileForWriting()
            self.file.write(self.sensorTextEdit.toPlainText())
            self.file.flush()
            self.file.close()

            self.sensorTextEdit.clear()
            self.sensorTextEdit.repaint()

            classlabel = int(self.boxLabelLineEdit.text())  # To add class label to dictionary

            if classlabel in self.container_dict:
                self.container_dict[classlabel] = self.container_dict[classlabel] + 1
            else:
                self.container_dict[classlabel] = 1

        except:
            traceback.print_exc()
            self.displayWarningPopUp(traceback.format_exc())

    def displaySensorData(self):
        try:
            new_line = self.ser.readline().decode('utf-8').rstrip()
            line_array = new_line.split(',')

            if line_array.__len__() == 54:

                new_line = line_array[0] + ',' + line_array[1] + ',' + line_array[2] + ',' + line_array[3]

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

                new_line = new_line + self.getClassLabels()

                self.sensorTextEdit.append(new_line)
                self.sensorTextEdit.repaint()

            if not self.startCaptureBtn.isEnabled():
                QtCore.QTimer.singleShot(1, self.displaySensorData)

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

    def startBtnPressedEvent(self):
        try:
            if self.isValidFields():
                self.startCaptureBtn.setEnabled(False)
                self.stopCaptureBtn.setEnabled(True)

                self.startCaptureBtn.repaint()
                self.stopCaptureBtn.repaint()

                self.setUpSerialPort()

                if not self.startCaptureBtn.isEnabled():
                    QtCore.QTimer.singleShot(1, self.displaySensorData)  # To save the sensor data.

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

    def randomNumberCheckBoxPressedEvent(self):
        if self.randomNumberCheckBox.isChecked():
            self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
            self.boxLabelLineEdit.setEnabled(False)
            self.rackLabelLineEdit.setEnabled(False)
            self.containerLabelLineEdit.setEnabled(False)
            self.randomNumberUpperLimitLineEdit.setEnabled(True)
        else:
            self.boxLabelLineEdit.setEnabled(True)
            self.rackLabelLineEdit.setEnabled(True)
            self.containerLabelLineEdit.setEnabled(True)
            self.randomNumberUpperLimitLineEdit.setEnabled(False)

    def randomNumberUpperLimitLineEditTextChangeEvent(self):
        self.container_dict = {}  # To reset the dictionary
        self.displayRandomBoxNumber()  # To reset the random number value

    def randomBoxNumberChangeBtnPressedEvent(self):
        if self.sensorTextEdit.toPlainText().__len__() > 0:
            self.saveSensorData()

            if self.randomNumberCheckBox.isChecked():
                self.displayRandomBoxNumber()

                self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
                self.boxLabelLineEdit.repaint()

                rack_container_values = self.rack_container_box_dict[self.boxLabelLineEdit.text()].split(',')
                self.rackLabelLineEdit.setText(rack_container_values[0])
                self.rackLabelLineEdit.repaint()
                self.containerLabelLineEdit.setText(rack_container_values[1])
                self.containerLabelLineEdit.repaint()

            self.emptyTagPushButton.setChecked(True)
            self.rackLabelCapturePushButton.setChecked(False)
            self.containerLabelCapturePushButton.setChecked(False)
        else:
            self.displayWarningPopUp("No data to save. Please Start the the serial port by pressing start button.")

    def stateChangeBtnPressedEvent(self):
        if self.emptyTagPushButton.isChecked():
            self.rackLabelCapturePushButton.setChecked(True)
            self.lastState = 0
        elif self.rackLabelCapturePushButton.isChecked() and self.lastState == 0:
            self.containerLabelCapturePushButton.setChecked(True)
            self.lastState = 1
        elif self.containerLabelCapturePushButton.isChecked():
            self.rackLabelCapturePushButton.setChecked(True)
            self.lastState = 2
        elif self.rackLabelCapturePushButton.isChecked() and self.lastState == 2:
            self.emptyTagPushButton.setChecked(True)
            self.lastState = 1

    def saveDataManuallyBtnPressedEvent(self):
        if self.sensorTextEdit.toPlainText().__len__() > 0:
            self.saveSensorData()
        else:
            self.displayWarningPopUp("No data to save. Please Start the the serial port by pressing start button.")


    def openFileForWriting(self):
        write_path = self.recordingFolderLocationLineEdit.text()
        os.makedirs(os.path.dirname(write_path), exist_ok=True)
        file_name = self.boxLabelLineEdit.text()
        file_name = write_path + file_name + ".csv"
        self.file = open(file_name, 'a')

    def displayRandomBoxNumber(self):
        totalContainers = int(self.randomNumberUpperLimitLineEdit.text())
        maxSamplesPerKeyCount = 1
        skip_container_numbers = [1, 6, 11, 16]

        if sum(self.container_dict.values()) == (
                totalContainers - skip_container_numbers.__len__() + 1) * maxSamplesPerKeyCount:
            print(
                "\n\nThe sample reached maximum size limit / all the container samples taken. "
                "To take more samples please change **maxSamplesPerKeyCount** variable.\n\n")
            exit()

        while True:
            random_box_number = random.randint(0, totalContainers)  # to display random number from 0 to 24

            if random_box_number in skip_container_numbers:  # skip the mentioned box numbers
                continue

            if random_box_number in self.container_dict:
                if self.container_dict[random_box_number] < maxSamplesPerKeyCount:
                    break
                else:
                    continue  # Try other value
            else:
                break

        self.containerNumberLabelValueDisplay.setText(str(random_box_number))
        self.boxLabelLineEdit.setText(self.containerNumberLabelValueDisplay.text())
        rack_container_values = self.rack_container_box_dict[self.boxLabelLineEdit.text()].split(',')
        self.rackLabelLineEdit.setText(rack_container_values[0])
        self.containerLabelLineEdit.setText(rack_container_values[1])

    def isValidFields(self):

        return_value = self.boxLabelLineEdit.text().__len__() > 0 and self.recordingFolderLocationLineEdit.text().__len__() > 0 \
                       and self.rackLabelCapturePushButton.text().__len__() > 0 and self.containerLabelCapturePushButton.text().__len__() > 0
        if not return_value:
            self.displayWarningPopUp("Please fill the required fields !!")
            return return_value

        return return_value

    def resetFields(self):
        if self.startCaptureBtn.isEnabled():
            self.emptyTagPushButton.setChecked(True)
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

    def clearSensorData(self):
        self.sensorTextEdit.clear()

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

    def load_dictionary(self):

        with open('box_rac_container_label_map_input.csv') as rack_container_box_dict_file:
            reader = csv.reader(rack_container_box_dict_file)
            for row in reader:
                self.rack_container_box_dict[row[0]] = row[1] + ',' + row[2]
        rack_container_box_dict_file.close()

        try:
            with open('container_dict.txt', "rb") as myFile:
                self.container_dict = pickle.load(myFile)
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
