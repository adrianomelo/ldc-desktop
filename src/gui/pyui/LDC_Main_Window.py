# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_Main_Window.ui'
#
# Created: Wed Jul 29 20:51:00 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_Main_Window(object):
    def setupUi(self, LDC_Main_Window):
        LDC_Main_Window.setObjectName("LDC_Main_Window")
        LDC_Main_Window.resize(800, 600)
        LDC_Main_Window.setMinimumSize(QtCore.QSize(800, 600))
        LDC_Main_Window.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ldc_icon/ldc_mainwindow_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LDC_Main_Window.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(LDC_Main_Window)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 580))
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget.setObjectName("centralwidget")
        LDC_Main_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(LDC_Main_Window)
        QtCore.QMetaObject.connectSlotsByName(LDC_Main_Window)

    def retranslateUi(self, LDC_Main_Window):
        LDC_Main_Window.setWindowTitle(QtGui.QApplication.translate("LDC_Main_Window", "Librix Diagnostics Center", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
