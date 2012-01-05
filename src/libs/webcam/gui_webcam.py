# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from libs.webcam.frame_webcam import Ui_WebcamFrame

from gui.LDC_Info import LDC_Info


class GUIWebcam(LDC_Info):
    """Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de rede.
    """

    name = "Webcam"
    category = u"Multimídia"
    status = None

    def __init__(self, info_res, compat_res, diag_res):
        """Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResWebcam)
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagn�stico (lista de 'DaigResWebcam')
        """
        LDC_Info.__init__(self)
        self.setTitle(self.name)
        self.status = compat_res[0] #compat result

        ui = Ui_WebcamFrame()
        ui.setupUi(self.frame)
        self.__fill_frame(ui, info_res, compat_res, diag_res)


    def __fill_frame(self, ui, info_res, compat_res, diag_res):
        """Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
        ui.productLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", info_res.product, None, QtGui.QApplication.UnicodeUTF8))
        ui.vendorLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", info_res.vendor, None, QtGui.QApplication.UnicodeUTF8))
        ui.modelLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", info_res.model, None, QtGui.QApplication.UnicodeUTF8))
        ui.deviceLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", info_res.deviceFile, None, QtGui.QApplication.UnicodeUTF8))
        ui.driverLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", info_res.driver, None, QtGui.QApplication.UnicodeUTF8))

        if compat_res[0]:
            ui.loadedGroupBox.setVisible(False)
            ui.compatLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", compat_res[1], None, QtGui.QApplication.UnicodeUTF8))
        else:
            for driver in diag_res.drivers:
                ui.loadedListWidget.addItem(driver)
            ui.compatLineEdit.setText(QtGui.QApplication.translate("WebcamFrame", compat_res[1], None, QtGui.QApplication.UnicodeUTF8))
