# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/ui/LDC_Result_Frame.ui'
#
# Created: Wed Sep  9 09:50:13 2009
#      by: PyQt4 UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_LDC_Result_Frame(object):
    def setupUi(self, LDC_Result_Frame):
        LDC_Result_Frame.setObjectName("LDC_Result_Frame")
        LDC_Result_Frame.resize(800, 600)
        LDC_Result_Frame.setMinimumSize(QtCore.QSize(800, 600))
        LDC_Result_Frame.setMaximumSize(QtCore.QSize(800, 600))
        self.verticalLayout_4 = QtGui.QVBoxLayout(LDC_Result_Frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtGui.QSpacerItem(20, 35, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtGui.QWidget(LDC_Result_Frame)
        self.widget.setMinimumSize(QtCore.QSize(200, 600))
        self.widget.setMaximumSize(QtCore.QSize(200, 600))
        self.widget.setAutoFillBackground(False)
        self.widget.setObjectName("widget")
        self.verticalLayoutWidget = QtGui.QWidget(self.widget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 200, 600))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtGui.QStackedWidget(LDC_Result_Frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(590, 485))
        self.stackedWidget.setMaximumSize(QtCore.QSize(590, 485))
        palette = QtGui.QPalette()
        self.stackedWidget.setPalette(palette)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedPage = QtGui.QWidget()
        self.stackedPage.setObjectName("stackedPage")
        self.stackedWidget.addWidget(self.stackedPage)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton_2 = QtGui.QPushButton(LDC_Result_Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(183)
        sizePolicy.setVerticalStretch(44)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(183, 44))
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton = QtGui.QPushButton(LDC_Result_Frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(183)
        sizePolicy.setVerticalStretch(44)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(183, 44))
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.retranslateUi(LDC_Result_Frame)
        QtCore.QMetaObject.connectSlotsByName(LDC_Result_Frame)

    def retranslateUi(self, LDC_Result_Frame):
        LDC_Result_Frame.setWindowTitle(QtGui.QApplication.translate("LDC_Result_Frame", "LDC Result Frame", None, QtGui.QApplication.UnicodeUTF8))
        LDC_Result_Frame.setStyleSheet(QtGui.QApplication.translate("LDC_Result_Frame", "background-image: url(:/ldc_result_bckg/ldc_result_bckg.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.widget.setStyleSheet(QtGui.QApplication.translate("LDC_Result_Frame", "background-image: url(:/ldc_transparency/ldc_transparency.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.stackedWidget.setStyleSheet(QtGui.QApplication.translate("LDC_Result_Frame", "background-image: url(:/ldc_transparency/ldc_transparency.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setStyleSheet(QtGui.QApplication.translate("LDC_Result_Frame", "background-image: url(:/ldc_button_bckg/ldc_button.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("LDC_Result_Frame", "Voltar ao início", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setStyleSheet(QtGui.QApplication.translate("LDC_Result_Frame", "background-image: url(:/ldc_button_bckg/ldc_button.png);", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("LDC_Result_Frame", "Gerar relatório", None, QtGui.QApplication.UnicodeUTF8))

import ldc_resources_rc
