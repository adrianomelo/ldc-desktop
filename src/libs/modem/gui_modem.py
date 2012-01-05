# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.modem.frame_modem import Ui_FrameModem

class GUIModem(LDC_Info):
	"""Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica com os resultados para o teste de modem.
    """

	name = u"Fax-Modem"
	category = "Conectividade"
	status = None

	ui = Ui_FrameModem()

	def __init__(self, info_res, compat_res, diag_res):
		"""Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResModem')
        compat_res -- Lista com as tuples de resultados de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (lista de 'DiagResModem')
        """

		LDC_Info.__init__(self)
		self.setTitle(self.name)

		if info_res:
			self.status = compat_res[0]
			self.ui.setupUi(self.frame)
			self.__fill_frame(info_res, compat_res, diag_res)
		else:
			self.status = False
			self.__labelError(compat_res)

	def __fill_frame(self, info_res, compat_res, diag_res):
		"""Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """

		self.ui.modelLineEdit.setText(QtGui.QApplication.translate("FrameModem", self._check_invalid_values(info_res.model[1]), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.vendorLineEdit.setText(QtGui.QApplication.translate("FrameModem", self._check_invalid_values(info_res.vendor[1]), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("FrameModem", self._check_invalid_values(info_res.deviceFile), None, QtGui.QApplication.UnicodeUTF8))
		self.ui.driversLineEdit.setText(QtGui.QApplication.translate("FrameModem", ", ".join(diag_res.drivers), None, QtGui.QApplication.UnicodeUTF8))

		self.__fill_compat(info_res, compat_res, diag_res)

	def __fill_compat(self, info_res, compat_res, diag_res):
		"""Atualiza a mensagem de compatibilidade e diagnóstico a partir dos seus resultados."""
		compatMsg = compat_res[1]
		self.ui.compatLineEdit.setText(QtGui.QApplication.translate("FrameModem", compatMsg, None, QtGui.QApplication.UnicodeUTF8))

	def __labelError(self, compat_res):
		"""Insere uma mensagem indicando que não foi encontrado nenhum dispositivo de modem"""
		label = QtGui.QLabel(u"Não foi detectado nenhum modem.")
		label.setStyleSheet("background-image: url(:/ldc_white_bckg/ldc_white_bckg.png); \n color: rgb(0, 0, 0);")
		verticalLayout = QtGui.QVBoxLayout(self.frame)
		verticalLayout.addWidget(label)

