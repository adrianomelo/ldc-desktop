# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from libs.wireless.frame_wireless import Ui_wirelessFrame

from gui.LDC_Info import LDC_Info


class GUIWireless(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de rede.
    """

    name = "Wireless"
    category = "Conectividade"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResWireless)
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagn�stico (lista de 'DaigResWireless')
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_wirelessFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)


    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        ui.modelLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(info_res.model[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(info_res.vendor[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(info_res.deviceFile), None, QtGui.QApplication.UnicodeUTF8))
        ui.driversLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(info_res.driver), None, QtGui.QApplication.UnicodeUTF8))
        linkStatus = "Não"
        if (diag_res.linkStatus):
            linkStatus = "Sim"
        ui.linkUpLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", linkStatus, None, QtGui.QApplication.UnicodeUTF8))
        ui.macLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(diag_res.macAddress), None, QtGui.QApplication.UnicodeUTF8))
        ui.ipLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(diag_res.ipAddress), None, QtGui.QApplication.UnicodeUTF8))
        ui.netmaskLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(diag_res.netmask), None, QtGui.QApplication.UnicodeUTF8))
        ui.gwLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_values(diag_res.gateway), None, QtGui.QApplication.UnicodeUTF8))
        ui.dnsTextEdit.setHtml(QtGui.QApplication.translate("wirelessFrame", self._check_invalid_list(diag_res.dnsList, '<BR>'), None, QtGui.QApplication.UnicodeUTF8))

        encryption_modes = info_res.encryption_modes.strip().split(' ')
        for mode in encryption_modes:
            #print "DEBUG:", mode
            ui.encryptionListWidget.addItem(mode)

        authentication_modes = info_res.authentication_modes.strip().split(' ')
        for mode in authentication_modes:
            #print "DEBUG:", mode
            ui.authenticationListWidget.addItem(mode)

        modes = info_res.wifimode
        modes.strip()
        modes.strip("802.11")
        if modes.count('a') > 0:
            ui.wifimodesListWidget.addItem("802.11a - 54 Mbps")
        if modes.count('b') > 0:
            ui.wifimodesListWidget.addItem("802.11b - 11 Mbps")
        if modes.count('g') > 0:
            ui.wifimodesListWidget.addItem("802.11g - 54 Mbps")
        if modes.count('n') > 0:
            ui.wifimodesListWidget.addItem("802.11n - 128 Mbps")

        ui.notFoundLineEdit.hide()

        if compat_res[0]:
            if compat_res[2] != []:
                for wlan in compat_res[2]:
                    if wlan != "":
                        ui.wlansFoundListWidget.addItem(wlan)
            else:
                ui.wlansFoundLabel.setText(QtGui.QApplication.translate("wirelessFrame", "Nenhuma rede foi identificada ao alcance do seu computador.", None, QtGui.QApplication.UnicodeUTF8))
                ui.wlansFoundListWidget.hide()

        else:
            ui.notFoundLineEdit.setText(QtGui.QApplication.translate("wirelessFrame", compat_res[1], None, QtGui.QApplication.UnicodeUTF8))
            ui.notFoundLineEdit.show()
            ui.compatGroupBox.hide()
            ui.wlansFoundLabel.hide()
            ui.wlansFoundListWidget.hide()
            ui.wifimodesGroupBox.hide()
            ui.encryptionGroupBox.hide()
            ui.authenticationGroupBox.hide()
            ui.dnsGroupBox.hide()
            ui.modelLabel.hide()
            ui.modelLineEdit.hide()
            ui.vendorLabel.hide()
            ui.vendorLineEdit.hide()
            ui.deviceFileLabel.hide()
            ui.deviceFileLineEdit.hide()
            ui.linkUpLabel.hide()
            ui.linkUpLineEdit.hide()
            ui.driversLabel.hide()
            ui.driversLineEdit.hide()
            ui.ipLabel.hide()
            ui.ipLineEdit.hide()
            ui.netmaskLabel.hide()
            ui.netmaskLineEdit.hide()
            ui.macLabel.hide()
            ui.macLineEdit.hide()
            ui.gwLabel.hide()
            ui.gwLineEdit.hide()


