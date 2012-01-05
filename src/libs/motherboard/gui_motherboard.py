# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.motherboard.frame_motherboard import Ui_MotherboardFrame

class GUIMotherboard(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica de exibição dos resultados para a placa mãe
    """

    name = u"Placa Mãe"  #Atributo que define o nome da biblioteca
    category = "Sistema" #Atributo que define a categoria da biblioteca
    status = None        #Atributo que define o status atual do teste (True/False)

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResMotherboard')
        compat_res -- Lista com as tuples de resultado de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (nesse caso não existe teste de diagnóstico, recebe-se uma lista vazia)
        """

        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0]

        ui = Ui_MotherboardFrame() #UI que define os campos da GUI da placa mãe
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)

    def __fill_frame(self, ui, info_res, compat_res, diag_res):
         """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
         ui.modelLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.model), None, QtGui.QApplication.UnicodeUTF8))
         ui.vendorLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.vendor), None, QtGui.QApplication.UnicodeUTF8))
         serial = info_res.serial
         if "SERIAL" in serial.upper() or "UNKNOWN" in serial.upper() or 'MF.OUT' in serial.upper() or 'NOT' in serial.upper():
             serial = ""
         ui.serialLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", serial, None, QtGui.QApplication.UnicodeUTF8))
         ui.versionLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.version), None, QtGui.QApplication.UnicodeUTF8))
         ui.biosVendorLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.bios_vendor), None, QtGui.QApplication.UnicodeUTF8))
         ui.biosDateLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.bios_date), None, QtGui.QApplication.UnicodeUTF8))
         ui.biosVersionLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.bios_version), None, QtGui.QApplication.UnicodeUTF8))
         ui.chipsetModelLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.chipset_device.value), None, QtGui.QApplication.UnicodeUTF8))
         ui.chipsetModelLineEdit.setCursorPosition(0)
         ui.chipsetVendorLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.chipset_vendor.value), None, QtGui.QApplication.UnicodeUTF8))
         ui.chipsetDriverLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", self._check_invalid_values(info_res.chipset_driver_modules), None, QtGui.QApplication.UnicodeUTF8))

         if compat_res[0]: #Se a compatibilidade for True não vai exibir as mensagens de diagnóstico
             ui.sugestionLabel.setVisible(False)
             ui.SugestionLineEdit.setVisible(False)
         else:
            ui.compatLineEdit.setText(QtGui.QApplication.translate("MotherboardFrame", "Os dispositivos da placa mãe não foram identificados corretamente.", None, QtGui.QApplication.UnicodeUTF8))
