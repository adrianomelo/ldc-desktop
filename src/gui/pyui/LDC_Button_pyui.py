# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_Button.ui'
#
# Created: Wed Jul 29 21:31:42 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_Button(object):
    def setupUi(self, LDC_Button):
        LDC_Button.setObjectName("LDC_Button")
        LDC_Button.resize(180, 40)
        self.pushButton = QtGui.QPushButton(LDC_Button)
        self.pushButton.setGeometry(QtCore.QRect(-10, 0, 190, 40))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LDC_Button)
        QtCore.QMetaObject.connectSlotsByName(LDC_Button)

    def retranslateUi(self, LDC_Button):
        LDC_Button.setWindowTitle(QtGui.QApplication.translate("LDC_Button", "LDC_Button", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setStyleSheet(QtGui.QApplication.translate("LDC_Button", "background-image: url(:/ldc_button_bckg/ldc_button_bckg.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LDC_Button", "PushButton", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
