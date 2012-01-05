# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messagebox.ui'
#
# Created: Fri Jul 24 10:35:29 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_MessageBox(object):
    def setupUi(self, LDC_MessageBox):
        LDC_MessageBox.setObjectName("LDC_MessageBox")
        LDC_MessageBox.resize(500, 122)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LDC_MessageBox.sizePolicy().hasHeightForWidth())
        LDC_MessageBox.setSizePolicy(sizePolicy)
        LDC_MessageBox.setMaximumSize(QtCore.QSize(500, 16777215))
        self.verticalLayout = QtGui.QVBoxLayout(LDC_MessageBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.message = QtGui.QLabel(LDC_MessageBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.message.sizePolicy().hasHeightForWidth())
        self.message.setSizePolicy(sizePolicy)
        self.message.setScaledContents(True)
        self.message.setAlignment(QtCore.Qt.AlignCenter)
        self.message.setWordWrap(True)
        self.message.setMargin(10)
        self.message.setObjectName("message")
        self.verticalLayout.addWidget(self.message)
        self.buttonBox = QtGui.QDialogButtonBox(LDC_MessageBox)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LDC_MessageBox)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), LDC_MessageBox.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), LDC_MessageBox.reject)
        QtCore.QMetaObject.connectSlotsByName(LDC_MessageBox)

    def retranslateUi(self, LDC_MessageBox):
        LDC_MessageBox.setWindowTitle(QtGui.QApplication.translate("LDC_MessageBox", "Librix Diagnostics Center", None, QtGui.QApplication.UnicodeUTF8))
        self.message.setText(QtGui.QApplication.translate("LDC_MessageBox", "Aqui vai um questionamento do tipo Ok/Cancel, como, por exemplo: o próximo teste consome um pouco de tempo - você deseja continuar?", None, QtGui.QApplication.UnicodeUTF8))

