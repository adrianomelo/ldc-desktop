# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from libs.network.frame_network import Ui_networkFrame

from gui.LDC_Info import LDC_Info


class GUINetwork(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de rede.
    """
    
    name = "Rede"
    category = "Conectividade"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor
        
        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResNetwork)
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagn�stico (lista de 'DaigResNetwork')
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_networkFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)

    def __check_invalid_values(self, value):
        ret = ""        
        if (value):
            if (value != "Other" and value != "NULL" and value != "Unknown"):
                ret = value
        return ret
    
    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        model = self.__check_invalid_values(info_res.model[1])
        vendor = self.__check_invalid_values(info_res.vendor[1])
        devFile = self.__check_invalid_values(info_res.deviceFile)
        driver = self.__check_invalid_values(info_res.driver)
        speed = self.__check_invalid_values(info_res.speed)
        linkDetec = "Não"
        if (info_res.linkState):
            linkDetec = "Sim"
        linkStatus = "Não"
        if (diag_res.linkStatus):
            linkStatus = "Sim"
        mac = self.__check_invalid_values(diag_res.macAddress)
        ip = self.__check_invalid_values(diag_res.ipAddress)
        netmask = self.__check_invalid_values(diag_res.netmask)
        gw = self.__check_invalid_values(diag_res.gateway)
                
        if not model:
            model = "Desconhecido"
        ui.modelLineEdit.setText(QtGui.QApplication.translate("networkFrame", model, None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("networkFrame", vendor, None, QtGui.QApplication.UnicodeUTF8))
        ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("networkFrame", devFile, None, QtGui.QApplication.UnicodeUTF8))
        ui.driversLineEdit.setText(QtGui.QApplication.translate("networkFrame", driver, None, QtGui.QApplication.UnicodeUTF8))
        ui.speedLineEdit.setText(QtGui.QApplication.translate("networkFrame", speed, None, QtGui.QApplication.UnicodeUTF8))
        ui.linkDetecLineEdit.setText(QtGui.QApplication.translate("networkFrame", linkDetec, None, QtGui.QApplication.UnicodeUTF8))
        ui.linkUpLineEdit.setText(QtGui.QApplication.translate("networkFrame", linkStatus, None, QtGui.QApplication.UnicodeUTF8))        
        ui.macLineEdit.setText(QtGui.QApplication.translate("networkFrame", mac, None, QtGui.QApplication.UnicodeUTF8))
        ui.ipLineEdit.setText(QtGui.QApplication.translate("networkFrame", ip, None, QtGui.QApplication.UnicodeUTF8))
        ui.netmaskLineEdit.setText(QtGui.QApplication.translate("networkFrame", netmask, None, QtGui.QApplication.UnicodeUTF8))
        ui.gwLineEdit.setText(QtGui.QApplication.translate("networkFrame", gw, None, QtGui.QApplication.UnicodeUTF8))
        ui.dnsTextEdit.setHtml(QtGui.QApplication.translate("networkFrame", self._check_invalid_list(diag_res.dnsList, '<BR>'), None, QtGui.QApplication.UnicodeUTF8))

        #Dependendo do resultado de compatibilidade mostra as informações de diagnóstico
        if not compat_res[0]:
            ui.compatMsgLineEdit.setText(QtGui.QApplication.translate("networkFrame", "A placa de rede não foi identificada corretamente.", None, QtGui.QApplication.UnicodeUTF8))
            
       
       