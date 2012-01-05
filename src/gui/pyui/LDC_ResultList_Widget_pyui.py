# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_ResultList_Widget.ui'
#
# Created: Thu Jul 30 13:02:13 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_ResultList_Widget(object):
    def setupUi(self, LDC_ResultList_Widget):
        LDC_ResultList_Widget.setObjectName("LDC_ResultList_Widget")
        LDC_ResultList_Widget.resize(580, 465)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(228, 224, 216, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        LDC_ResultList_Widget.setPalette(palette)
        self.scrollArea = QtGui.QScrollArea(LDC_ResultList_Widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 580, 475))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 580, 475))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(LDC_ResultList_Widget)
        QtCore.QMetaObject.connectSlotsByName(LDC_ResultList_Widget)

    def retranslateUi(self, LDC_ResultList_Widget):
        LDC_ResultList_Widget.setWindowTitle(QtGui.QApplication.translate("LDC_ResultList_Widget", "LDC_ResultList_Widget", None, QtGui.QApplication.UnicodeUTF8))
        LDC_ResultList_Widget.setStyleSheet(QtGui.QApplication.translate("LDC_ResultList_Widget", "background-image: url(:/ldc_transparency/ldc_transparency.png);\n"
"background-color: rgba(255, 255, 255, 0);", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
