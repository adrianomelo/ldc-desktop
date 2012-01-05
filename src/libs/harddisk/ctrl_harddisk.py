# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.harddisk.diag_harddisk import DiagHarddisk
from libs.harddisk.compat_harddisk import CompatHarddisk
from libs.harddisk.gui_harddisk import GUIHarddisk

class CtrlHarddisk(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificação, compatibilidade, diagnóstico e cria a tela de exibição.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._name = "Disco Rigido"
		self._category = "Armazenamento"

		self._diag = DiagHarddisk(self)
		self._compat = CompatHarddisk(self)

		self._guiClass = GUIHarddisk

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

	ctrl = CtrlHarddisk(None)

	ctrl.execute_lib()
	ctrl.print_test()
	ctrl.gui_test()

	sys.exit(app.exec_())