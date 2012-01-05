# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.keyboard.frame_keyboard import Ui_FrameKeyboard

class GUIKeyboard(LDC_Info):
	"""Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica de exibição dos resultados de teclado
    """

	name = u"Teclado"
	category = "Interação"
	status = None

	ui = Ui_FrameKeyboard()

	def __init__(self, info_res, compat_res, diag_res):
		"""Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResKeyboard')
        compat_res -- Lista com as tuples de resultado de compatibilidade [(True, msg)]
        diag_res -- Lista com os resultados do diagnóstico (nesse caso não existe teste de diagnóstico, recebe-se uma lista vazia)
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
		"""Atualiza os campos da GUI com as informa￧￵es de identificação, compatibilidade e diagnóstico. """
		vendor = self._check_invalid_values(info_res.vendor[1])
		model = self._check_invalid_values(info_res.model[1])
		deviceFile = self._check_invalid_values(info_res.deviceFile)
		bus = self._check_invalid_values(info_res.bus)

		xkbLayout = self._check_invalid_values(info_res.xkbLayout)
		xkbRules = self._check_invalid_values(info_res.xkbRules)
		xkbModel = self._check_invalid_values(info_res.xkbModel)

		self.ui.vendorLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", vendor, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.modelLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", model, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", deviceFile, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.busLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", bus, None, QtGui.QApplication.UnicodeUTF8))

		self.ui.xkbLayoutLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", xkbLayout, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.xkbRulesLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", xkbRules, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.xkbModelLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", xkbModel, None, QtGui.QApplication.UnicodeUTF8))
		
		self.__fill_compat(info_res, compat_res, diag_res)

	def __fill_compat(self, info_res, compat_res, diag_res):
		"""Atualiza a mensagem de compatibilidade e diagnóstico a partir dos seus resultados."""
		compatMsg = compat_res[1]
		
		if (diag_res and not diag_res.plugged):
			compatMsg = "Seu teclado parece não estar conectado. Verifique a conexão e tente novamente."
		
		self.ui.compatLineEdit.setText(QtGui.QApplication.translate("FrameKeyboard", compatMsg, None, QtGui.QApplication.UnicodeUTF8))
