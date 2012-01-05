# -*- coding: utf-8 -*-

"""
	RQF17.A : Identificar - Configuracao e tipo.
 	RQF17.C : Diagnostico - Verificar se o teclado esta plugado.
"""

from libs.core.diag_dev import DiagDev
from libs.keyboard.info_res_keyboard import InfoResKeyboard
from libs.keyboard.diag_res_keyboard import DiagResKeyboard
from libs.keyboard.diag_keyboard_gui import DiagKeyboardGUI

class DiagKeyboard(DiagDev):
	"""Classe de diagnóstico e informação de teclado"""

	def __init__(self, ctrl):
		"""Construtor que chama a classe base 'DiagDev' passando a nome da biblioteca do teclado."""
		DiagDev.__init__(self, "libldc_keyboard.so", ctrl, InfoResKeyboard, DiagResKeyboard)
		
	def diag(self, info):
		"""
		Redefine o método diag, definido previamente em DiagDev, uma vez que todo o
		diagnóstico de Keyboard é feito em python, não havendo biblioteca de diagnóstico
		de Keyboard em C.
		"""
		
		self._diag_tuple = (None, [])
		
		infos = self.getInfoResults()
		
		for info in infos:
			wizardRes = self._ctrl.showCustomDialog(DiagKeyboardGUI)
				
			if (wizardRes and wizardRes['code'] == 1):
				self._diag_tuple[1].append({'keyPressed': wizardRes['result']['keyPressed']})
			else: # Cancelado
				self._diag_tuple[1].append({'keyPressed': False})

def main(argv):
	test = DiagKeyboard()
	test.runTest()

import sys
if __name__ == "__main__":
	main(sys.argv)