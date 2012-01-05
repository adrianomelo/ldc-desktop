# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.usb.diag_usb import DiagUsb
from libs.usb.compat_usb import CompatUsb
from libs.usb.gui_usb import GUIUsb

class CtrlUsb(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificacao, compatibilidade, diagnostico e cria a tela de exibicao.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._diag = DiagUsb(self)
		self._compat = CompatUsb(self)

		self._guiClass = GUIUsb

	def execute_lib(self):
		"""Executa o info, compat e diag (dependendo do resultado do compatibilidade) e cria as telas de exibição."""
		# Information
		self._callInfo()

		# Compatibility
		self._callCompat()

		# Diagnostic
		self._callDiag()

# Testing...

if __name__ == "__main__":
	from PyQt4 import QtCore, QtGui
	import sys

	app = QtGui.QApplication(sys.argv)

	ctrl = CtrlUsb()

	ctrl.execute_lib()
	ctrl.print_test()
	ctrl.gui_test()

	sys.exit(app.exec_())