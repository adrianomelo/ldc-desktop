# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.motherboard.diag_motherboard import DiagMotherboard
from libs.motherboard.compat_motherboard import CompatMotherboard
from libs.motherboard.gui_motherboard import GUIMotherboard

class CtrlMotherboard(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificação, compatibilidade e cria a tela de exibição.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)
		
		self._category = "Sistema"
		self._name = u"Placa Mãe"

		self._diag = DiagMotherboard(self)
		self._compat = CompatMotherboard(self)

		self._guiClass = GUIMotherboard

	def execute_lib(self):
		"""Executa o info, compat e diag (dependendo do resultado do compatibilidade) e cria as telas de exibição."""
		# Information
		self._callInfo()

		# Compatibility
		self._callCompat()

		runDiag = False

		for i in self._compatRes:
			# Compatibility result 1st tuple element is the overall result
			# If any of them failed, runDiag
			runDiag = runDiag | (not i[0])

		# Diagnostic
		if (runDiag):
			self._callDiag()

# Testing...

if __name__ == "__main__":
	from PyQt4 import QtCore, QtGui
	import sys

	app = QtGui.QApplication(sys.argv)

	ctrl = CtrlMotherboard()

	ctrl.execute_lib()
	ctrl.print_test()
	ctrl.gui_test()

	sys.exit(app.exec_())
