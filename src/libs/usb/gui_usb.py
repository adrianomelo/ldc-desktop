# -*- coding: utf-8 -*-

import sys, string
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.usb.frame_usb import Ui_UsbFrame

class GUIUsb(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de portas USB.
    """
    name = u"Portas USB"
    category = "USB"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos
        compat_res -- Lista com as tuples de resultados de compatibilidade
        diag_res -- Lista com os resultados do diagnóstico
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)

        self.status = compat_res[0]

        ui = Ui_UsbFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)

    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        ui.usbTotalLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.usb_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.lowSpeedLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.low_speed_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.fullSpeedLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.full_speed_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.highSpeedLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.high_speed_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.ohciLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.ohci_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.uhciLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.uhci_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))
        ui.ehciLineEdit.setText(QtGui.QApplication.translate("UsbFrame", info_res.ehci_total.__str__(), None, QtGui.QApplication.UnicodeUTF8))

        devicesList = diag_res.pluggedDevices
        devices = string.split(devicesList, ";")

        #print "DEBUG:", devicesList
        #print "DEBUG:", devices

        ui.diagListWidget.clear()
        for device in devices:
            if device != "NULL":
                ui.diagListWidget.addItem(device)


        compatMsg = None
        if (compat_res[0]):
            compatMsg = compat_res[1]
        else:
            compatMsg = compat_res[1]

        ui.compatTextEdit.setPlainText(QtGui.QApplication.translate("UsbFrame", compatMsg, None, QtGui.QApplication.UnicodeUTF8))
        ui.compatTextEdit.setReadOnly(True)

