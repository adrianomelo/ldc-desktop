# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_Selection_Frame.ui'
#
# Created: Wed Sep  9 09:59:38 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_Selection_Frame(object):
    def setupUi(self, LDC_Selection_Frame):
        LDC_Selection_Frame.setObjectName("LDC_Selection_Frame")
        LDC_Selection_Frame.resize(800, 600)
        LDC_Selection_Frame.setMinimumSize(QtCore.QSize(800, 580))
        LDC_Selection_Frame.setMaximumSize(QtCore.QSize(800, 600))
        LDC_Selection_Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        LDC_Selection_Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2 = QtGui.QFrame(LDC_Selection_Frame)
        self.frame_2.setGeometry(QtCore.QRect(290, 170, 491, 251))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtGui.QFrame(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.frame.setFont(font)
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Plain)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(0)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 21))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.checkBox = QtGui.QCheckBox(self.frame)
        self.checkBox.setMaximumSize(QtCore.QSize(16777215, 21))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton = QtGui.QPushButton(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(180)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(183, 44))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(LDC_Selection_Frame)
        QtCore.QMetaObject.connectSlotsByName(LDC_Selection_Frame)

    def retranslateUi(self, LDC_Selection_Frame):
        LDC_Selection_Frame.setWindowTitle(QtGui.QApplication.translate("LDC_Selection_Frame", "Librix Diagnostics Center", None, QtGui.QApplication.UnicodeUTF8))
        LDC_Selection_Frame.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "background-image: url(:/ldc_selection_bckg/ldc_selection_bckg.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.frame_2.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "background-image: url(:/ldc_transparency/ldc_transparency.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.frame.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "background-image: url(:/ldc_white_bckg/ldc_white_bckg.png);\n"
"border-color: rgb(255, 0, 0);", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "color: rgb(57, 93, 118);", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("LDC_Selection_Frame", "Selecione os dispositivos:", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "color: rgb(15, 82, 2);", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("LDC_Selection_Frame", "Todos", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setStyleSheet(QtGui.QApplication.translate("LDC_Selection_Frame", "background-image: url(:/ldc_button_bckg/ldc_button.png);\n"
"border-color: rgb(184, 202, 217);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LDC_Selection_Frame", "Diagnosticar", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
