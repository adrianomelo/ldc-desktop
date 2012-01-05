# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inputdialog.ui'
#
# Created: Fri Jul 24 10:35:34 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_InputDialog(object):
    def setupUi(self, LDC_InputDialog):
        LDC_InputDialog.setObjectName("LDC_InputDialog")
        LDC_InputDialog.resize(500, 142)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LDC_InputDialog.sizePolicy().hasHeightForWidth())
        LDC_InputDialog.setSizePolicy(sizePolicy)
        LDC_InputDialog.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(LDC_InputDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtGui.QLabel(LDC_InputDialog)
        self.message.setScaledContents(True)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setMargin(10)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.inputBox = QtGui.QLineEdit(LDC_InputDialog)
        self.inputBox.setObjectName("inputBox")
        self.horizontalLayout.addWidget(self.inputBox)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(LDC_InputDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LDC_InputDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LDC_InputDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LDC_InputDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LDC_InputDialog)

    def retranslateUi(self, LDC_InputDialog):
        LDC_InputDialog.setWindowTitle(QtGui.QApplication.translate("LDC_InputDialog", "Librix Diagnostics Center", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("LDC_InputDialog", "Aqui vai um questionamento quantitativo, por exemplo: quantas portas USB seu computador possui?", None, QtGui.QApplication.UnicodeUTF8))

