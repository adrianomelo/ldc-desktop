# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_Info.ui'
#
# Created: Thu Jul 30 09:41:52 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_Info(object):
    def setupUi(self, LDC_Info):
        LDC_Info.setObjectName("LDC_Info")
        LDC_Info.resize(532, 285)
        LDC_Info.setCheckable(False)
        self.verticalLayout = QtGui.QVBoxLayout(LDC_Info)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtGui.QFrame(LDC_Info)
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(LDC_Info)
        QtCore.QMetaObject.connectSlotsByName(LDC_Info)

    def retranslateUi(self, LDC_Info):
        LDC_Info.setWindowTitle(QtGui.QApplication.translate("LDC_Info", "LDC_Info", None, QtGui.QApplication.UnicodeUTF8))
        LDC_Info.setStyleSheet(QtGui.QApplication.translate("LDC_Info", "color: rgb(15, 82, 2);", None, QtGui.QApplication.UnicodeUTF8))
        LDC_Info.setTitle(QtGui.QApplication.translate("LDC_Info", "Device", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("LDC_Info", "color: rgb(57, 93, 118);", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
