# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from libs.sound.frame_sound import Ui_soundFrame
from gui.LDC_Info import LDC_Info

class GUISound(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de som.
    """
    name = "Som"
    category = "Multimidia"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResSound)
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DaigResSound')
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_soundFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)


    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        ui.productLineEdit.setText(QtGui.QApplication.translate("soundFrame", self._check_invalid_values(info_res.product[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("soundFrame", self._check_invalid_values(info_res.vendor[1]), None, QtGui.QApplication.UnicodeUTF8))
        ui.modelLineEdit.setText(QtGui.QApplication.translate("soundFrame", self._check_invalid_values(info_res.model), None, QtGui.QApplication.UnicodeUTF8))
        ui.idDeviceLineEdit.setText(QtGui.QApplication.translate("soundFrame", self._check_invalid_values(info_res.deviceID), None, QtGui.QApplication.UnicodeUTF8))
        active = "Não"
        if info_res.driverActive:
            active = "Sim"
        ui.activeDriverLineEdit.setText(QtGui.QApplication.translate("soundFrame", active, None, QtGui.QApplication.UnicodeUTF8))
        ui.driverModulesLineEdit.setText(QtGui.QApplication.translate("soundFrame", self._check_invalid_values(info_res.drivers), None, QtGui.QApplication.UnicodeUTF8))

        #Não foi implementado o teste de compatibilidade ainda
        ui.compatGroupBox.setVisible(True)
        ui.compatMsgLineEdit.setVisible(True)
        ui.compatMsgLineEdit.setText(QtGui.QApplication.translate("soundFrame", compat_res[1], None, QtGui.QApplication.UnicodeUTF8))

        if compat_res[0]:
            ui.mutableLabel.setVisible(False)
            ui.mutableLineEdit.setVisible(False)
            ui.adjustableLabel.setVisible(False)
            ui.adjustableLineEdit.setVisible(False)
        else:
            if (diag_res.alsaMute):
                ui.mutableLineEdit.setText(QtGui.QApplication.translate("soundFrame", "alsa mute 1", None, QtGui.QApplication.UnicodeUTF8))
            else:
                ui.mutableLineEdit.setText(QtGui.QApplication.translate("soundFrame", "alsa mute 0", None, QtGui.QApplication.UnicodeUTF8))

            if (diag_res.alsaVolume):
                ui.adjustableLineEdit.setText(QtGui.QApplication.translate("soundFrame", "alsa volume 1", None, QtGui.QApplication.UnicodeUTF8))
            else:
                ui.adjustableLineEdit.setText(QtGui.QApplication.translate("soundFrame", "alsa volume 0", None, QtGui.QApplication.UnicodeUTF8))



