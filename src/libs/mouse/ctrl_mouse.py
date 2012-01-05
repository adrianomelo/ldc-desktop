# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.mouse.diag_mouse import DiagMouse
from libs.mouse.compat_mouse import CompatMouse
from libs.mouse.gui_mouse import GUIMouse

class CtrlMouse(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificação, compatibilidade e cria a tela de exibição.
	"""
	
	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)
		
		self._diag = DiagMouse(self)
		self._compat = CompatMouse(self)
		self._guiClass = GUIMouse

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
	ctrl = CtrlMouse()
	ctrl.execute_lib()

