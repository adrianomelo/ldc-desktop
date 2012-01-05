# -*- coding: utf-8 -*-

from libs.core.ctrl_dev import CtrlDev
from libs.webcam.diag_webcam import DiagWebcam
from libs.webcam.compat_webcam import CompatWebcam
from libs.webcam.gui_webcam import GUIWebcam

class CtrlWebcam(CtrlDev):
	"""Estende a classe 'CtrlDev'.
	Classe de controle que chama os testes de identificação, compatibilidade e cria a tela de exibição.
	"""

	def __init__(self, parent):
		"""Construtor que inicializa os atributos '_diag', '_compat' e '_guiClass' definidos na classe base 'CtrlDev'."""
		CtrlDev.__init__(self, parent)

		self._diag = DiagWebcam(self)
		self._compat = CompatWebcam(self)

		self._guiClass = GUIWebcam

	def execute_lib(self):
		"""Executa o info, compat e diag (dependendo do resultado do compatibilidade) e cria as telas de exibição."""
		try:
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
		except:
			self._infoRes = [None]
			self._compatRes = [None]
			self._diagRes = [None]


		# Output everything
		#self._print_test()

# Testing...

if __name__ == "__main__":
	ctrl = CtrlWebcam()
	ctrl.execute_lib()

