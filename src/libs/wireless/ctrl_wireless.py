# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.wireless.diag_wireless import DiagWireless
from libs.wireless.compat_wireless import CompatWireless
from libs.wireless.gui_wireless import GUIWireless

class CtrlWireless(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificacao, compatibilidade, diagnostico e cria a tela de exibicao.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._diag = DiagWireless(self)
		self._compat = CompatWireless(self)

		self._guiClass = GUIWireless

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
	ctrl = CtrlWireless()
	ctrl.execute_lib()

