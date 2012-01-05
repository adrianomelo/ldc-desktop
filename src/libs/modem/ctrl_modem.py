# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.modem.diag_modem import DiagModem
from libs.modem.compat_modem import CompatModem
from libs.modem.gui_modem import GUIModem

class CtrlModem(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificacao, compatibilidade, diagnostico e cria a tela de exibicao.
	"""
	
	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._name = "Fax-Modem"
		self._category = "Conectividade"

		self._diag = DiagModem(self)
		self._compat = CompatModem(self)
		self._guiClass = GUIModem

	def execute_lib(self):
		"""Executa o info, compat e diag (dependendo do resultado do compatibilidade) e cria as telas de exibicao."""
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

	ctrl = CtrlModem(None)

	ctrl.execute_lib()
	ctrl.print_test()
	ctrl.gui_test()

	sys.exit(app.exec_())