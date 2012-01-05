# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.memory.compat_memory import CompatMemory
from libs.memory.diag_memory import DiagMemory
from libs.memory.gui_memory import GUIMemory

class CtrlMemory(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificação, compatibilidade, diagnóstico e cria a tela de exibição.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._name = u"Memória"
		self._category = "Sistema"

		self._diag = DiagMemory(self)
		self._compat = CompatMemory(self)
		self._guiClass = GUIMemory

	def execute_lib(self):
		"""Executa o info, compat, diag e cria as telas de exibição."""
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

	ctrl = CtrlMemory()

	ctrl.execute_lib()
	ctrl.print_test()
	ctrl.gui_test()

	sys.exit(app.exec_())