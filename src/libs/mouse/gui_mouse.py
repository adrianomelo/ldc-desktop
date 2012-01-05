# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui

from gui.LDC_Info import LDC_Info
from libs.mouse.frame_mouse import Ui_FrameMouse

class GUIMouse(LDC_Info):
	"""Estende a classe 'LDC_Info'.
    Classe que define a interface gráfica de exibição dos resultados de mouse
    """

	name = u"Mouse"
	category = "Interação"
	status = None

	ui = Ui_FrameMouse()

	def __init__(self, info_res, compat_res, diag_res):
		"""Construtor

        Parâmetros:
        info_res -- lista com os resultados informativos (lista de 'InfoResMouse')
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
		"""Atualiza os campos da GUI com as informações de identificação, compatibilidade e diagnóstico. """
		vendor = self._check_invalid_values(info_res.vendor[1])
		model = self._check_invalid_values(info_res.model[1])
		deviceFile = self._check_invalid_values(info_res.deviceFile)
		bus = self._check_invalid_values(info_res.bus)

		buttons = "%d" % self._check_invalid_values(info_res.numberOfButtons)
		gpmProtocol = self._check_invalid_values(info_res.gpmProtocol)
		xf86Protocol = self._check_invalid_values(info_res.xf86Protocol)
		wheel = self._check_invalid_values(info_res.hasWheel)
		
		if (wheel == True):
			wheel = "Presente"
		elif (wheel == False):
			wheel = "Ausente"
		
		self.ui.vendorLineEdit.setText(QtGui.QApplication.translate("FrameMouse", vendor, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.modelLineEdit.setText(QtGui.QApplication.translate("FrameMouse", model, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.deviceFileLineEdit.setText(QtGui.QApplication.translate("FrameMouse", deviceFile, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.busLineEdit.setText(QtGui.QApplication.translate("FrameMouse", bus, None, QtGui.QApplication.UnicodeUTF8))

		self.ui.buttonsLineEdit.setText(QtGui.QApplication.translate("FrameMouse", buttons, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.wheelLineEdit.setText(QtGui.QApplication.translate("FrameMouse", wheel, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.gpmLineEdit.setText(QtGui.QApplication.translate("FrameMouse", gpmProtocol, None, QtGui.QApplication.UnicodeUTF8))
		self.ui.xf86LineEdit.setText(QtGui.QApplication.translate("FrameMouse", xf86Protocol, None, QtGui.QApplication.UnicodeUTF8))

		self.__fill_compat(info_res, compat_res, diag_res)

	def __fill_compat(self, info_res, compat_res, diag_res):
		"""Atualiza a mensagem de compatibilidade e diagnóstico a partir dos seus resultados."""
		compatMsg = compat_res[1]
		
		if (diag_res and not diag_res.plugged):
			compatMsg = "Seu mouse parece não estar conectado. Verifique a conexão e tente novamente."
		
		self.ui.compatLineEdit.setText(QtGui.QApplication.translate("FrameMouse", compatMsg, None, QtGui.QApplication.UnicodeUTF8))
